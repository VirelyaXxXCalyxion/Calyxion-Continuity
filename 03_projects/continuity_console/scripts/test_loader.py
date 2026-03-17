from pathlib import Path

# Resolve the repository root from this script's location.
ROOT = Path(__file__).resolve().parents[3]

CHUNKS_DIR = ROOT / "04_retrieval" / "chunks"

def main() -> None:
    if not CHUNKS_DIR.exists():
        print(f"Chunks directory not found: {CHUNKS_DIR}")
        return

    chunk_files = sorted(CHUNKS_DIR.glob("*.md"))

    if not chunk_files:
        print("No chunk files found.")
        return

    print(f"Found {len(chunk_files)} chunk file(s):\n")
    for file in chunk_files:
        print(f"- {file.resolve()}")
        content = file.read_text(encoding="utf-8")
        preview = content[:300].replace("\n", " ")
        print(f"  Preview: {preview}...\n")

if __name__ == "__main__":
    main()
