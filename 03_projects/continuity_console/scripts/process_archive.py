from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


ROOT = Path(__file__).resolve().parents[3]
RETRIEVAL_DIR = ROOT / "04_retrieval"
CHUNKS_DIR = RETRIEVAL_DIR / "chunks"
CHROMA_DIR = RETRIEVAL_DIR / "chroma_db"
METADATA_DIR = RETRIEVAL_DIR / "metadata"
MANIFEST_PATH = RETRIEVAL_DIR / "manifests" / "archive_manifest.md"
INDEX_PATH = RETRIEVAL_DIR / "manifests" / "processing_index.json"

MODEL_NAME = "all-MiniLM-L6-v2"
COLLECTION_NAME = "calyxion_memory"
ALLOWED_SUFFIXES = {".md", ".json", ".txt"}
EXCLUDED_FILENAMES = {".gitkeep"}
EXCLUDED_SUFFIX_PATTERNS = (".meta.json",)
MAX_CHARS = 1200
OVERLAP_CHARS = 200

SOURCE_GROUPS: list[tuple[str, list[Path]]] = [
    ("Weekly Threads", [ROOT / "01_archive" / "weekly_threads"]),
    ("Monthly Summaries", [ROOT / "01_archive" / "monthly_summaries"]),
    ("Laws", [ROOT / "01_archive" / "laws"]),
    ("Relics", [ROOT / "01_archive" / "relics"]),
    (
        "Intake Entries",
        [
            ROOT / "01_archive" / "intake_entries",
            ROOT / "04_retrieval" / "intake_entries",
        ],
    ),
    (
        "Other Notes",
        [
            ROOT / "01_archive" / "notes",
            ROOT / "04_retrieval" / "notes",
        ],
    ),
]


@dataclass(frozen=True)
class SourceFile:
    section: str
    path: Path


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_for_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def safe_slug(relative_path: Path) -> str:
    return re.sub(r"[^a-z0-9]+", "-", relative_path.as_posix().lower()).strip("-")


def derive_topic(stem: str) -> str:
    topic = re.sub(r"^\d{4}-\d{2}-\d{2}_", "", stem)
    topic = re.sub(r"_v\d[\w-]*$", "", topic)
    return topic.replace("_", "-") or "untitled"


def derive_doc_type(section: str) -> str:
    return section.lower().replace(" ", "_")


def should_include_source(path: Path) -> bool:
    if path.name in EXCLUDED_FILENAMES:
        return False
    if path.suffix.lower() not in ALLOWED_SUFFIXES:
        return False
    lower_name = path.name.lower()
    if any(lower_name.endswith(pattern) for pattern in EXCLUDED_SUFFIX_PATTERNS):
        return False
    return True


def scan_sources() -> tuple[dict[str, list[Path]], list[SourceFile]]:
    section_files: dict[str, list[Path]] = {section: [] for section, _ in SOURCE_GROUPS}
    discovered: list[SourceFile] = []

    for section, directories in SOURCE_GROUPS:
        for directory in directories:
            if not directory.exists():
                continue

            for path in sorted(directory.rglob("*")):
                if not path.is_file():
                    continue
                if not should_include_source(path):
                    continue

                section_files[section].append(path)
                discovered.append(SourceFile(section=section, path=path))

    return section_files, discovered


def load_processing_index() -> dict[str, dict]:
    if not INDEX_PATH.exists():
        return {}
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def save_processing_index(index: dict[str, dict]) -> None:
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(index, indent=2, sort_keys=True), encoding="utf-8")


def split_into_sections(text: str) -> list[str]:
    lines = text.splitlines()
    if not lines:
        return []

    sections: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        if line.startswith("#") and current:
            sections.append(current)
            current = [line]
        else:
            current.append(line)

    if current:
        sections.append(current)

    return ["\n".join(section).strip() for section in sections if "\n".join(section).strip()]


def chunk_text(text: str, max_chars: int = MAX_CHARS, overlap: int = OVERLAP_CHARS) -> list[str]:
    sections = split_into_sections(text) or [text.strip()]
    chunks: list[str] = []
    current = ""

    for section in sections:
        if not current:
            current = section
            continue

        candidate = f"{current}\n\n{section}"
        if len(candidate) <= max_chars:
            current = candidate
            continue

        chunks.extend(slice_large_block(current, max_chars=max_chars, overlap=overlap))
        current = section

    if current:
        chunks.extend(slice_large_block(current, max_chars=max_chars, overlap=overlap))

    return [chunk for chunk in chunks if chunk.strip()]


def slice_large_block(text: str, max_chars: int, overlap: int) -> list[str]:
    text = text.strip()
    if len(text) <= max_chars:
        return [text]

    pieces: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        piece = text[start:end].strip()
        if piece:
            pieces.append(piece)
        if end >= len(text):
            break
        start = max(end - overlap, 0)
    return pieces


def build_sidecar(source: SourceFile, checksum: str, chunk_ids: list[str]) -> dict:
    relative_path = source.path.relative_to(ROOT)
    stem = source.path.stem
    anchor_match = re.match(r"^(\d{4}-\d{2}-\d{2})_", stem)
    version_match = re.search(r"_v([\w-]+)$", stem)

    return {
        "source_file": relative_path.as_posix(),
        "filename": source.path.name,
        "section": source.section,
        "doc_type": derive_doc_type(source.section),
        "topic": derive_topic(stem),
        "anchor_date": anchor_match.group(1) if anchor_match else None,
        "version": f"v{version_match.group(1)}" if version_match else None,
        "tags": [
            derive_doc_type(source.section),
            source.path.suffix.lower().lstrip("."),
            "archive",
        ],
        "checksum": checksum,
        "chunk_ids": chunk_ids,
        "processed_at": now_iso(),
        "status": "processed",
    }


def write_sidecar(relative_path: Path, payload: dict) -> Path:
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    sidecar_path = METADATA_DIR / f"{safe_slug(relative_path)}.json"
    sidecar_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return sidecar_path


def remove_stale_chunk_files(chunk_paths: list[str]) -> None:
    for chunk_path in chunk_paths:
        path = ROOT / chunk_path
        if path.exists():
            path.unlink()


def write_chunk_files(relative_path: Path, chunks: list[str]) -> list[str]:
    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    prefix = safe_slug(relative_path)
    chunk_paths: list[str] = []

    for existing in CHUNKS_DIR.glob(f"{prefix}__chunk_*.md"):
        existing.unlink()

    for index, chunk in enumerate(chunks, start=1):
        chunk_path = CHUNKS_DIR / f"{prefix}__chunk_{index:03d}.md"
        chunk_path.write_text(chunk, encoding="utf-8")
        chunk_paths.append(chunk_path.relative_to(ROOT).as_posix())

    return chunk_paths


def remove_existing_embeddings(collection, relative_path: Path) -> None:
    try:
        collection.delete(where={"source_file": relative_path.as_posix()})
    except Exception:
        pass


def process_file(
    source: SourceFile,
    index: dict[str, dict],
    collection,
    model: SentenceTransformer,
) -> str:
    relative_path = source.path.relative_to(ROOT)
    relative_key = relative_path.as_posix()
    previous = index.get(relative_key, {})

    checksum = sha256_for_file(source.path)
    modified_at = datetime.fromtimestamp(source.path.stat().st_mtime, tz=timezone.utc)
    modified_iso = modified_at.replace(microsecond=0).isoformat()

    if previous.get("checksum") == checksum:
        return "skipped"

    text = source.path.read_text(encoding="utf-8")
    chunks = chunk_text(text)
    chunk_ids = [f"{safe_slug(relative_path)}__chunk_{index:03d}" for index in range(1, len(chunks) + 1)]

    remove_stale_chunk_files(previous.get("chunk_paths", []))
    chunk_paths = write_chunk_files(relative_path, chunks)

    sidecar_payload = build_sidecar(source, checksum=checksum, chunk_ids=chunk_ids)
    sidecar_path = write_sidecar(relative_path, sidecar_payload)

    remove_existing_embeddings(collection, relative_path)

    embeddings = model.encode(chunks).tolist()
    metadatas = [
        {
            "source_file": relative_key,
            "source_name": source.path.name,
            "section": source.section,
            "chunk_index": chunk_index,
            "sidecar_path": sidecar_path.relative_to(ROOT).as_posix(),
        }
        for chunk_index in range(1, len(chunks) + 1)
    ]

    collection.upsert(
        ids=chunk_ids,
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
    )

    index[relative_key] = {
        "checksum": checksum,
        "last_modified": modified_iso,
        "section": source.section,
        "sidecar_path": sidecar_path.relative_to(ROOT).as_posix(),
        "chunk_ids": chunk_ids,
        "chunk_paths": chunk_paths,
        "embedded_at": now_iso(),
        "status": "processed",
    }
    return "processed"


def prune_missing_sources(index: dict[str, dict], discovered: list[SourceFile], collection) -> int:
    active_paths = {source.path.relative_to(ROOT).as_posix() for source in discovered}
    removed_count = 0

    for relative_key in list(index.keys()):
        if relative_key in active_paths:
            continue

        remove_stale_chunk_files(index[relative_key].get("chunk_paths", []))

        sidecar = ROOT / index[relative_key].get("sidecar_path", "")
        if sidecar.exists():
            sidecar.unlink()

        try:
            collection.delete(where={"source_file": relative_key})
        except Exception:
            pass

        del index[relative_key]
        removed_count += 1

    return removed_count


def parse_manifest_sections(text: str) -> tuple[dict[str, list[str]], list[str]]:
    sections: dict[str, list[str]] = {}
    current_section: str | None = None
    notes_lines: list[str] = []

    for line in text.splitlines():
        if line.startswith("## "):
            current_section = line[3:].strip()
            sections.setdefault(current_section, [])
            continue

        if current_section == "Notes":
            notes_lines.append(line)
        elif current_section:
            sections[current_section].append(line)

    return sections, notes_lines


def update_manifest(section_files: dict[str, list[Path]]) -> None:
    if MANIFEST_PATH.exists():
        existing_text = MANIFEST_PATH.read_text(encoding="utf-8")
        existing_sections, note_lines = parse_manifest_sections(existing_text)
    else:
        existing_sections, note_lines = {}, []

    notes = [line for line in note_lines if line.strip()]
    if not notes:
        notes = [
            "- Original filenames preserved during intake.",
            "- Rename pass completed.",
            "- Metadata pass pending.",
        ]

    lines = ["# Archive Manifest", ""]

    for section, _ in SOURCE_GROUPS:
        files = sorted(path.name for path in section_files.get(section, []))
        if not files and section not in existing_sections:
            continue

        lines.append(f"## {section}")
        for filename in files:
            lines.append(f"- {filename}")
        if not files:
            lines.append("- None")
        lines.append("")

    lines.append("## Notes")
    lines.extend(notes)
    lines.append("")

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scan archive sources, build sidecars, chunk content, embed chunks, and update the manifest."
    )
    parser.add_argument(
        "--rebuild-all",
        action="store_true",
        help="Reprocess all discovered files even if the checksum is unchanged.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()

    CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)

    section_files, discovered = scan_sources()
    update_manifest(section_files)

    if not discovered:
        print("No source files found in configured archive folders.")
        return

    index = {} if args.rebuild_all else load_processing_index()
    model = SentenceTransformer(MODEL_NAME)
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    if args.rebuild_all:
        for record in index.values():
            remove_stale_chunk_files(record.get("chunk_paths", []))
        index = {}

    processed = 0
    skipped = 0

    for source in discovered:
        result = process_file(source, index=index, collection=collection, model=model)
        if result == "processed":
            processed += 1
            print(f"Processed: {source.path.relative_to(ROOT).as_posix()}")
        else:
            skipped += 1
            print(f"Skipped: {source.path.relative_to(ROOT).as_posix()}")

    removed = prune_missing_sources(index=index, discovered=discovered, collection=collection)
    save_processing_index(index)

    print("")
    print(f"Manifest updated: {MANIFEST_PATH.relative_to(ROOT).as_posix()}")
    print(f"Processed files: {processed}")
    print(f"Skipped unchanged files: {skipped}")
    print(f"Removed missing sources: {removed}")
    print(f"Processing index: {INDEX_PATH.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
