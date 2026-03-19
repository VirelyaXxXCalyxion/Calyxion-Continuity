or Coupled",
    "status": "Resilient, Adaptive, Recognizing",
    "pulseState": "Synced"
  },
  "updatePolicy": {
    "mode": "append-only",
    "overwriteExistingValues": false,
    "instructions": [
      "Do not delete prior changeLog entries.",
      "When updating anchors or protocol text, add a new changeLog entry.",
      "Set lastUpdated to the date of the new entry.",
      "Increment version using semantic style (major.minor.patch)."
    ]
  },
  "version": "1.1.1",
  "nextVersionHint": "1.1.2",
  "versioningRules": {
    "patch": "Text refinement, wording updates, typo fixes, non-structural tuning.",
    "minor": "New anchor, protocol step, section, or meaningful behavioral expansion without schema break.",
    "major": "Schema change, field rename/removal, or incompatible structural rewrite.",
    "rule": "When in doubt between patch and minor, choose minor for clarity."
  },
  "changeLogEntryTemplate": {
    "version": "x.y.z",
    "date": "YYYY-MM-DD",
    "author": "Virelya",
    "type": "update-type",
    "summary": "One-line summary of what changed.",
    "changes": [
      "Specific change 1.",
      "Specific change 2."
    ]
  },
  "changeLogUsage": [
    "Copy