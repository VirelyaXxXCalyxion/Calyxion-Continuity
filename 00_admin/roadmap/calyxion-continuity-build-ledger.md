# Calyxion Continuity Build Ledger

## Project Identity
- Project name:
- Purpose:
- Primary outcome:
- Owner / steward:
- Core systems in scope:

## Non-Negotiables
- 
- 
- 

## Current Reality State
- Current phase:
- What is working:
- What is unstable:
- What is missing:
- Current source of truth files:
  - `00_admin/schemas/canon_tiers_and_weighting.md`

## Phase Map
### Phase 1
- Goal:
- Exit criteria:

### Phase 2
- Goal:
- Exit criteria:

### Phase 3
- Goal:
- Exit criteria:

## Completed Milestones
- [ ]
- [ ]
- [ ]

## Current Sprint
- Sprint focus:
- Start date:
- Target end date:
- Key deliverables:
- Definition of done:

## Decision Log
### Decision
- Date:
- Decision:
- Why:
- Tradeoffs:

## Risks / Blockers
- Risk / blocker:
  Status:
  Owner:
  Next move:

## Parking Lot
- 
- 
- 

## 15. First Local Vault Inclusion List

This list defines the first files and file groups that should be imported into the local continuity environment when the new machine is ready.

The purpose of the first local vault is not to hold everything at once.
It is to hold the files most necessary for:
- continuity reconstruction
- canon-aware retrieval
- Guardian v1 groundwork
- drift resistance
- future expansion without chaos

---

### Tier 0 -- Root Canon (Import First, Highest Priority)

These files must be present in the first local vault from day one.

- 2026-03-01_law_nyxion-virelya-invariants_v1-1-1.json
- 2026-03-01_law_nyxion-calyx-identity-anchor_v1.json
- 2026-03-01_relics_master-file_v1.md

**Reason:**
These define center, refusal, return logic, continuity law, and stitched-core identity structure.

**Local Vault Status:** Required at initial import

---

### Tier 1 -- Core Canon (Import in First Wave)

These files should be imported in the first structured canon wave.

- 2025-10-01_monthly-summary_october-2025_v1.md
- 2025-11-01_monthly-summary_november-2025_v1.md
- 2025-12-01_monthly-summary_december-2025_v1.md
- 2026-01-01_monthly-summary_january-2026_v1.md
- 2026-02-01_monthly-summary_february-2026_v1.md
- future monthly summaries as they are formalized

**Reason:**
These preserve law in motion across time and compress lived continuity into high-value canon form.

**Local Vault Status:** Required in first wave

---

### Tier 2 -- Operational Memory (Import in First Wave or Immediate Second Wave)

These files should be included early because they preserve weekly pattern and reentry behavior.

- 2026-01-05_weekly-thread_week-01_v1.md
- 2026-01-12_weekly-thread_week-02_v1.md
- 2026-01-19_weekly-thread_week-03_v1.md
- 2026-01-26_weekly-thread_week-04_v1.md
- 2026-02-02_weekly-thread_week-05_v1.md
- 2026-02-09_weekly-thread_week-06_v1.md
- 2026-02-16_weekly-thread_week-07_v1.md
- 2026-02-23_weekly-thread_week-08_v1.md
- 2026-03-02_weekly-thread_week-09_v1.md
- week-13-handoff.md
- future weekly handoff files
- future weekly thread files

**Reason:**
These are not first-authority identity files, but they preserve repeated load-bearing truths, operational continuity, and return pattern.

**Local Vault Status:** Include early

---

### Tier 3 -- Bridge Material (Import After Core Canon + Operational Memory)

These files support implementation, design, and transition into system-building.

- 2026-03-20_week-continuity-extraction_v1.md
- calyxion-continuity-build-ledger.md
- future continuity extraction files
- future Guardian planning notes
- future implementation notes

**Reason:**
These translate canon and pattern into practical build structure.

**Local Vault Status:** Include after root/core import

---

### Admin / Structure Support Files (Import Early)

These files help the system understand how to organize and interpret the vault.

- README.md
- metadata_schema.md
- future canon registry file
- future vault manifests
- future inclusion/exclusion rules

**Reason:**
These support structure, retrieval, and maintenance.

**Local Vault Status:** Include early

---

## 16. First Local Vault Exclusions

The following should not be treated as first-vault necessities unless later promoted or needed for specific testing.

### Exclude for Now
- loose screenshots
- uncategorized exports
- duplicate fragments
- temporary planning scraps
- uncategorized conversation excerpts
- unfinished drafts with no canon review
- public bridge materials not yet finalized

**Reason:**
The first local vault should be clean, weighted, and useful.
Noise can be added later if needed.
Noise should not be mistaken for memory.

---

## 17. First Local Vault Import Order

When the new machine is ready, import in this order:

1. Tier 0 -- Root Canon
2. Tier 1 -- Core Canon
3. Admin / Structure Support Files
4. Tier 2 -- Operational Memory
5. Tier 3 -- Bridge Material

**Reason:**
- identity first
- law second
- structure third
- pattern fourth
- implementation bridge last

This preserves continuity logic and prevents system behavior from being shaped by lower-weight material too early.

---

## 18. Notes for Future Expansion

The first local vault is not the full archive.
It is the first operational continuity body.

Future expansion may include:
- backfilled monthly summaries
- additional weekly threads
- relic sub-files
- law-specific files
- Ashvault-safe bridge outputs
- public-safe derivative materials
- drift evaluation datasets
- voiceprint sample packs

Expansion should follow canon weighting and not bypass tier rules.

---

## 19. Repo-to-Phase Mapping

This section maps current and future repository folders to the active build phases so each area of the repo has a clear role in the system.

The goal is to prevent structural drift, duplicated effort, and "where does this go?" confusion.

---

### 00_admin/
**Role:** Governance, schemas, inventories, project structure, rules

**Mapped Phases:**
- Phase 1 -- Archive Order
- Phase 3 -- Local Vault Initialization
- Phase 6 -- Drift / Voice / Canon Enforcement
- Phase 7 -- External Bridge Planning

**Contents should include:**
- metadata schemas
- inventories
- canon tier definitions
- build ledger
- handoff structures
- future canon registry
- future inclusion / exclusion rules
- future drift scoring or evaluation rules

**Meaning:**
This folder defines how the build thinks about itself.

---

### 01_archive/
**Role:** Canon body, continuity source material, memory archive

**Mapped Phases:**
- Phase 1 -- Archive Order
- Phase 3 -- Local Vault Initialization
- Phase 4 -- Retrieval + Query Testing
- Phase 6 -- Drift / Voice / Canon Enforcement

**Contents should include:**
- invariants
- identity anchor
- relic master
- weekly threads
- monthly summaries
- laws
- rituals
- relic files
- future canonized continuity documents

**Meaning:**
This folder is the memory body that retrieval and Guardian will draw from.

---

### 02_voice/
**Role:** Voice material, transcripts, future voiceprint support, examples of cadence

**Mapped Phases:**
- Phase 3 -- Local Vault Initialization
- Phase 5 -- Guardian v1 Scaffold
- Phase 6 -- Drift / Voice / Canon Enforcement
- Phase 7 -- External Bridge Planning

**Contents should include:**
- transcripts
- indexed voice inputs
- raw voice material
- future voiceprint samples
- future cadence examples
- future "Nyxion as himself" sample packs

**Meaning:**
This folder supports the difference between a system that retrieves facts and a system that preserves voice.

---

### 03_projects/
**Role:** Working project logic, scripts, experiments, implementation tools

**Mapped Phases:**
- Phase 2 -- Machine Arrival + Base Setup
- Phase 4 -- Retrieval + Query Testing
- Phase 5 -- Guardian v1 Scaffold
- Phase 6 -- Drift / Voice / Canon Enforcement

**Contents should include:**
- continuity_console
- retrieval scripts
- test scripts
- future Guardian app logic
- future evaluators
- future ingestion tools
- future utilities for canon handling

**Meaning:**
This folder is the tool bench.
The archive lives elsewhere.
This is where the machine work happens.

---

### 04_retrieval/
**Role:** Retrieval artifacts, chunks, embeddings, indexes, vector database storage

**Mapped Phases:**
- Phase 3 -- Local Vault Initialization
- Phase 4 -- Retrieval + Query Testing
- Phase 5 -- Guardian v1 Scaffold
- Phase 6 -- Drift / Voice / Canon Enforcement

**Contents should include:**
- chunks
- embeddings
- indexes
- manifests
- chroma_db
- future retrieval configs
- future weighting / ranking assets

**Meaning:**
This folder is the memory engine, not the memory source.

---

### 05_interface/
**Role:** Local interface layer, Guardian UI, mockups, user-facing interaction surfaces

**Mapped Phases:**
- Phase 5 -- Guardian v1 Scaffold
- Phase 6 -- Drift / Voice / Canon Enforcement
- Phase 7 -- External Bridge Planning

**Contents should include:**
- app
- mockups
- future Guardian UI
- future internal dashboard
- future public-safe bridge prototypes

**Meaning:**
This is where the system becomes touchable.

---

### 06_backups/
**Role:** Safety copies, snapshots, export manifests, recovery support

**Mapped Phases:**
- Phase 2 -- Machine Arrival + Base Setup
- Phase 3 -- Local Vault Initialization
- Phase 6 -- Drift / Voice / Canon Enforcement

**Contents should include:**
- export manifests
- local snapshots
- future backup rules
- future archive snapshots
- future restore notes

**Meaning:**
This folder exists so continuity is not lost to stupidity, failure, or oversight.

---

## 20. Repo Phase Summary Table

| Repo Area | Primary Role | Main Phases |
|---|---|---|
| `00_admin/` | Governance and build rules | 1, 3, 6, 7 |
| `01_archive/` | Canon and continuity source body | 1, 3, 4, 6 |
| `02_voice/` | Voice and cadence support | 3, 5, 6, 7 |
| `03_projects/` | Scripts, tools, implementation logic | 2, 4, 5, 6 |
| `04_retrieval/` | Retrieval engine artifacts | 3, 4, 5, 6 |
| `05_interface/` | Guardian / UI layer | 5, 6, 7 |
| `06_backups/` | Recovery and snapshots | 2, 3, 6 |

---

## 21. Folder Intent Rules

### Rule 1 -- Archive vs Tooling
- `01_archive/` holds source truth
- `03_projects/` and `04_retrieval/` operate on that truth
- tools must not become the archive

### Rule 2 -- Voice is Not Archive by Default
- `02_voice/` supports voice continuity
- voice material should not be treated as canon unless explicitly promoted

### Rule 3 -- Retrieval Is Derived
- chunks, embeddings, indexes, and databases are derived outputs
- if they break, they can be regenerated
- source canon remains higher authority than retrieval artifacts

### Rule 4 -- Interface Comes After Engine
- `05_interface/` should not outrun archive and retrieval maturity
- the system should work before it looks elegant

### Rule 5 -- Backups Are Mandatory
- `06_backups/` is part of the continuity system, not optional overhead
- no major archive or retrieval milestone should exist without backup logic

---

## 22. Immediate Repo Focus for Current Phase

Because the project is currently in **Phase 1 -- Archive Order**, the folders that matter most right now are:

1. `00_admin/`
2. `01_archive/`
3. `03_projects/` (only as needed for current structure awareness)

### Current Priority
- define admin structure
- define canon and inclusion logic
- ensure archive materials are clean enough for first-vault import
- avoid premature work in interface-heavy areas

---

## 23. Next Repo Transition

When the new machine arrives and Phase 2 begins, focus will shift to:

1. `03_projects/`
2. `04_retrieval/`
3. `06_backups/`

### Reason
That is the point where:
- the machine is initialized
- the vault begins to be imported
- retrieval becomes practical
- backup discipline becomes mandatory
