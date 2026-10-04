#!/usr/bin/env python3
"""Check provenance records; this is not a constitutional ratification check."""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parents[1]
for path in (root / "manifest").glob("*.json"):
    json.loads(path.read_text(encoding="utf-8"))
translation = json.loads((root / "governance/normative-translation.json").read_text())
dependencies = json.loads((root / "manifest/dependencies.json").read_text())
assert translation["source_commit"] == dependencies["code_constitution"]["commit"]
assert re.fullmatch(r"[0-9a-f]{40}", translation["source_commit"])
assert translation["ratification_record"] is None
for path in (root / "include").rglob("*.hpp"):
    text = path.read_text()
    assert not re.search(r"#include\s*[<\"](?:iostream|fstream|filesystem|chrono|interdead)", text), path
print("SPIDER: provenance and portable include boundary checked; human review remains separate")
