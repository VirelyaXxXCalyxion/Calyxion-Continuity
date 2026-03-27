# README for Calyxion Continuity

## Overview

This repository provides tools for working with continuity preservation in data processing pipelines. The recommended approach is now to use `process_archive.py`.

## Recommended Pipeline

The `process_archive.py` script is the preferred method for handling data processing. It provides a streamlined workflow for archiving data while ensuring that all necessary processing steps are covered. You can use the `--rebuild-all` option to ensure that everything is reconstructed from scratch if needed.

## Quickstart

To quickly get started, you can run the following command:
```bash
python process_archive.py --rebuild-all
```

## Output Artifacts

When running the `process_archive.py`, the following output artifacts will be generated:
- **Chunks**: These are the segmented parts of the processed data, ready for further analysis.
- **Metadata Sidecars**: Accompanying files that hold necessary metadata about the processed chunks.
- **Manifests**: Files that provide a summary of all the output files and their properties.
- **Processing Index**: An index to help track the processing stages of the data.
- **Chroma DB**: A database used to handle the chromatic information of the artifacts.

## Legacy Scripts

The scripts `embed_and_store.py` and `query_memory.py` are now considered legacy/manual scripts. They rely on hard-coded ROOT and lack the portability features found in `process_archive.py` and `test_loader.py`. Hence, it is recommended to transition to using the latter for a more modular and flexible approach.