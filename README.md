# Calyxion Continuity

Calyxion Continuity is a structured archive and retrieval workspace for preserving continuity across conversations, reflections, rituals, relics, voice material, and project work.

It combines long-term document storage with an early retrieval pipeline that:

1. **Chunks** curated markdown material
2. **Embeds** it (via `sentence-transformers`)
3. **Stores** vectors in **ChromaDB** for semantic lookup

---

## What this repository contains

At a high level, the repo is organized into:

- **Administrative context** in `00_admin/`
- **Archived source material** in `01_archive/`
- **Voice inputs and transcripts** in `02_voice/`
- **Project utilities** in `03_projects/`
- **Retrieval assets** in `04_retrieval/`
- **Interface placeholders** in `05_interface/`
- **Backup/export locations** in `06_backups/`

The repository is primarily markdown- and JSON-based, with a small Python console workflow for loading, embedding, and querying stored content.

---

## Repository layout

```text
00_admin/
  inventories/
  roadmap/
  schemas/
01_archive/
  conversations/
  laws/
  monthly_summaries/
  relics/
  rituals/
  weekly_threads/
02_voice/
  indexed/
  raw/
  transcripts/
03_projects/
  continuity_console/
    scripts/
04_retrieval/
  chroma_db/
  chunks/
  embeddings/
  indexes/
  manifests/
05_interface/
  app/
  mockups/
06_backups/
  export_manifests/
  local_snapshots/
```

---

## Core workflow (retrieval console)

The current retrieval flow lives in `03_projects/continuity_console/scripts/`:

- `test_loader.py`
  - Verifies chunk files can be discovered and previewed from `04_retrieval/chunks/`.

- `embed_and_store.py`
  - Reads markdown chunk files, generates embeddings with `sentence-transformers`, and stores them in a persistent Chroma collection.

- `query_memory.py`
  - Runs a semantic query against the stored collection and prints the top matching results.

---

## Quickstart

### Prerequisites

- Python **3.10+** recommended
- A local checkout of this repository
- Pip-installable dependencies:
  - `chromadb`
  - `sentence-transformers`

Install:

```bash
pip install chromadb sentence-transformers
```

### Run the console workflow

From the repository root:

1) Verify chunk loading

```bash
python 03_projects/continuity_console/scripts/test_loader.py
```

2) Embed chunk files into ChromaDB

```bash
python 03_projects/continuity_console/scripts/embed_and_store.py
```

3) Query stored memory

```bash
python 03_projects/continuity_console/scripts/query_memory.py
```

If you get “file not found” or an empty result set, confirm there are chunk `.md` files present in `04_retrieval/chunks/` and that the script root path is configured correctly (see next section).

---

## Configuration (important)

`embed_and_store.py` and `query_memory.py` currently define `ROOT` as a **hard-coded Windows path**.

Before running them on another machine, update that constant to point at your local repository checkout.

Notes:

- `test_loader.py` already resolves the repository root relative to the script location and can be run as-is.
- A future improvement would be to replace the hard-coded constant with one of:
  - an environment variable (e.g. `CALYXION_ROOT`)
  - a `.env` file
  - a required CLI argument (recommended)

---

## Metadata schema

Metadata guidance for archived material lives in `00_admin/schemas/metadata_schema.md`.

Required fields:

- `title`
- `date`
- `type`
- `source`
- `tags`
- `summary`

Optional fields currently documented include `people`, `project`, `ritual`, `continuity_tier`, `emotional_tone`, and `related_files`.

---

## Adding new material (suggested practice)

This repo is meant to be a living archive. A lightweight, consistent intake process keeps retrieval usable over time.

Suggested flow:

1. **Add source material** under the most fitting archive location (e.g. `01_archive/conversations/`, `01_archive/rituals/`, `02_voice/transcripts/`).
2. **Ensure metadata** exists and is consistent with `00_admin/schemas/metadata_schema.md`.
3. **Chunk** the material into retrieval-ready markdown chunks in `04_retrieval/chunks/`.
4. Run the console workflow to embed + store + query.

If you’re not sure where something belongs, prefer:

- durable originals in `01_archive/` / `02_voice/`
- derived retrieval artifacts in `04_retrieval/`

---

## Data & privacy

This repository may contain sensitive personal text (conversations, reflections), voice files, and transcripts.

Recommendations:

- Treat `04_retrieval/chroma_db/` as **local-first** unless you explicitly want to version it.
- Be cautious committing:
  - raw audio
  - transcripts containing personal identifiers
  - API keys, tokens, or machine-specific paths
- Consider adding (or tightening) `.gitignore` rules for local databases, exports, and any private working files.

---

## Current state

This repository already contains:

- Archived weekly threads and monthly summaries
- Identity and continuity “relic” documents
- Administrative schemas and inventories
- Retrieval chunk storage in `04_retrieval/chunks/`

Several directories are present as placeholders for future expansion, including interface, backup, and additional project areas.

---

## Roadmap (near-term ideas)

- Replace hard-coded `ROOT` with CLI/env-based configuration
- Add a chunking script (or document the chunking format) so chunk creation is reproducible
- Add a minimal `requirements.txt` (or `pyproject.toml`) for the console scripts
- Add a small “health check” command that verifies expected folders exist and the Chroma collection can be opened

---

## Notes

- There is currently no formal test, lint, or build automation configured at the repository level.
- The retrieval scripts appear to be an early console prototype rather than a packaged application.
- Keeping this README aligned with the actual folder structure and script behavior will make the repo easier to maintain.