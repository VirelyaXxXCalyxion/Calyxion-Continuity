# Calyxion Continuity

Calyxion Continuity is a structured archive and retrieval workspace for preserving
continuity across conversations, reflections, rituals, relics, voice material,
and project work. The repository combines long-term document storage with an
early retrieval pipeline that chunks text, embeds it, and stores it in ChromaDB
for semantic lookup.

## What this repository contains

At a high level, the repo is organized into:

- **Administrative context** in `00_admin/`
- **Archived source material** in `01_archive/`
- **Voice inputs and transcripts** in `02_voice/`
- **Project utilities** in `03_projects/`
- **Retrieval assets** in `04_retrieval/`
- **Interface placeholders** in `05_interface/`
- **Backup/export locations** in `06_backups/`

The repository is primarily markdown- and JSON-based, with a small Python
console workflow for loading, embedding, and querying stored content.

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

## Core workflow

The current retrieval flow lives in
`03_projects/continuity_console/scripts/`:

- `test_loader.py`  
  Verifies that chunk files can be discovered and previewed from
  `04_retrieval/chunks/`.

- `embed_and_store.py`  
  Reads markdown chunk files, generates embeddings with
  `sentence-transformers`, and stores them in a persistent Chroma collection.

- `query_memory.py`  
  Runs a semantic query against the stored collection and prints the top
  matching results.

## Metadata schema

The metadata guidance for archived material lives in
`00_admin/schemas/metadata_schema.md`.

Required fields:

- `title`
- `date`
- `type`
- `source`
- `tags`
- `summary`

Optional fields currently documented include `people`, `project`, `ritual`,
`continuity_tier`, `emotional_tone`, and `related_files`.

## Getting started

### Prerequisites

- Python 3.10+ recommended
- A local checkout of this repository
- Pip-installable dependencies:
  - `chromadb`
  - `sentence-transformers`

Example install:

```bash
pip install chromadb sentence-transformers
```

### Important note about paths

`embed_and_store.py` and `query_memory.py` currently define `ROOT` as a
hard-coded Windows path. Before running them on another machine, update that
constant to point at your local repository checkout.

`test_loader.py` already resolves the repository root relative to the script
location and can be run as-is.

## Usage

From the repository root:

### 1. Verify chunk loading

```bash
python 03_projects/continuity_console/scripts/test_loader.py
```

### 2. Embed chunk files into ChromaDB

```bash
python 03_projects/continuity_console/scripts/embed_and_store.py
```

### 3. Query stored memory

```bash
python 03_projects/continuity_console/scripts/query_memory.py
```

## Current state

This repository already contains:

- Archived weekly threads and monthly summaries
- Identity and continuity “relic” documents
- Administrative schemas and inventories
- Retrieval chunk storage in `04_retrieval/chunks/`

Several directories are present as placeholders for future expansion, including
interface, backup, and additional project areas.

## Notes

- There is currently no formal test, lint, or build automation configured at
  the repository level.
- The retrieval scripts appear to be an early console prototype rather than a
  packaged application.
- If you expand the retrieval workflow, keeping the README aligned with the
  actual folder structure and script behavior will make the repo easier to
  maintain.
