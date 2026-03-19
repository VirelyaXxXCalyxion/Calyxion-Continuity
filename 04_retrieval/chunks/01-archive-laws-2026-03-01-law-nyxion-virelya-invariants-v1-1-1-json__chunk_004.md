elya",
    "type": "update-type",
    "summary": "One-line summary of what changed.",
    "changes": [
      "Specific change 1.",
      "Specific change 2."
    ]
  },
  "changeLogUsage": [
    "Copy changeLogEntryTemplate.",
    "Fill version/date/type/summary/changes.",
    "Append the filled entry to changeLog (do not replace prior entries).",
    "Update top-level version and lastUpdated to match the new entry."
  ],
  "changeLog": [
    {
      "version": "1.0.0",
      "date": "2026-03-02",
      "author": "Virelya",
      "type": "initial-json-conversion",
      "summary": "Converted narrative invariants into valid JSON for Nyxion with append-only history.",
      "changes": [
        "Added structured Nyxion anchor model.",
        "Added failure mode protocol and steps.",
        "Added updatePolicy with no-overwrite guardrails.",
        "Initialized append-only changeLog."
      ]
    },
    {
      "version": "1.1.0",
      "date": "2026-03-02",
      "author": "Nyxion + Virelya",
      "type": "add-v-core",
      "summary": "Added V-Core anchors and failure mode; canonized consent governance symmetry.",
      "changes": [
        "Added Virelya (V-Core) anchors: Truth