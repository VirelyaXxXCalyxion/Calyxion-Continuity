# Inclusion / Exclusion Rules

## Purpose
This file defines how material is chosen for local vault import, retrieval inclusion, canon weighting, and archive cleanliness decisions.

Use these rules to answer:
- what belongs in the first local vault
- what should be excluded for now
- what can be retrieved as authority
- what should remain preserved but low-weight

---

## Inclusion Rules

### Rule 1 -- Identity Before Everything Else
Include Tier 0 material first.

**Why:**
Identity center, refusal rights, return logic, and continuity law must shape the system before lower-tier material is allowed to steer retrieval or behavior.

---

### Rule 2 -- Core Canon Comes Before Volume
Include monthly summaries and other Tier 1 canon before adding large amounts of weekly or bridge material.

**Why:**
Compressed canon provides more stable continuity value than a high volume of lower-tier material.

---

### Rule 3 -- Operational Memory Must Support Reentry
Include weekly threads, handoffs, and continuity summaries when they improve reentry, pattern recognition, and continuity restoration.

**Why:**
Operational memory is valuable when it reduces fog and preserves repeated load-bearing truth across time.

---

### Rule 4 -- Bridge Material Supports Build, Not Authority
Include bridge materials when they meaningfully support planning, design, implementation, or reconstruction workflows.

**Why:**
Bridge files help make canon usable, but they should not outweigh canon itself.

---

### Rule 5 -- Structure Files Count
Include schemas, manifests, inventories, and ledgers when they help the system understand organization, weighting, and current project state.

**Why:**
A continuity system needs structural clarity, not just content.

---

## Exclusion Rules

### Rule 1 -- Do Not Import Noise Just Because It Exists
Exclude material that is duplicated, unclear, unfinished, or structurally noisy unless it is needed for a specific review pass.

**Examples:**
- duplicate fragments
- stray exports
- temporary scraps
- unreviewed dumps

---

### Rule 2 -- Derived Artifacts Are Not Source Canon
Do not treat chunks, embeddings, indexes, or databases as source material for canon decisions.

**Examples:**
- `04_retrieval/chunks/`
- `04_retrieval/embeddings/`
- `04_retrieval/indexes/`
- `04_retrieval/chroma_db/`

**Why:**
These are derived outputs and can be regenerated.

---

### Rule 3 -- Voice Material Is Not Canon By Default
Do not elevate voice materials into canon or first-vault authority without explicit review.

**Examples:**
- raw voice captures
- transcript fragments
- sample packs

---

### Rule 4 -- Weather Stays Low Until Proven
Exclude Tier 4 weather material from first-wave import unless it has a clear immediate use or has been formally promoted.

**Examples:**
- loose screenshots
- uncategorized conversation excerpts
- unfinished drafts
- experimental files

---

## First Local Vault Rules

### Include Early
- Tier 0 root canon
- Tier 1 core canon
- admin / structure support files
- selected Tier 2 operational memory
- selected Tier 3 bridge material

### Exclude For Now
- Tier 4 weather
- duplicate material
- unfinished scraps
- low-signal exports
- derived retrieval artifacts

---

## Review Questions
When deciding whether to include a file, ask:

1. Does this improve continuity reconstruction?
2. Does this help canon-aware retrieval?
3. Is this a source file or only a derived artifact?
4. Is this stable enough to deserve inclusion?
5. Does its current folder and name reflect what it actually is?

---

## Decision Rule
If a file is meaningful but not yet clearly categorized:
- preserve it
- place it in the least misleading folder available
- avoid granting canon authority prematurely
- review it later for promotion, demotion, or reclassification
