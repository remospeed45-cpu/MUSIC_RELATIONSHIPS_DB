#!/usr/bin/env python3
from pathlib import Path
import csv, re, unicodedata

ROOT = Path(".")
TRACKLISTS = [
    ROOT / "data/src0003/batch0002/SRC0003_BATCH0002_ASI_SE_COMPONE_UN_SON_TRACKLIST.tsv",
    ROOT / "data/src0003/batch0002/SRC0003_BATCH0002_ESTE_ES_ISMAEL_MIRANDA_TRACKLIST.tsv",
]
REC = ROOT / "authority/recordings/recordings_master.tsv"
REL = ROOT / "authority/releases/releases_master.tsv"
STAGING = ROOT / "authority/staging/unit0101"
REPORT = ROOT / "reports/unit0101/UNIT0101_ISMAEL_BLOCK0001_AUDIT_REPORT.md"
STAGING.mkdir(parents=True, exist_ok=True)
REPORT.parent.mkdir(parents=True, exist_ok=True)

def norm(s):
    s = ''.join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn")
    s = s.replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)

def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

releases = read_tsv(REL)
recordings = read_tsv(REC)

release_by_title = {norm(r["canonical_release_title"]): r for r in releases}

audit_rows = []
summary = []

for tracklist in TRACKLISTS:
    source_rows = read_tsv(tracklist)
    release_title = source_rows[0]["release_title"]
    rel = release_by_title.get(norm(release_title))
    if not rel:
        summary.append((release_title, "MISSING_RELEASE", 0, len(source_rows), 0, len(source_rows), 0))
        for s in source_rows:
            audit_rows.append({"release_title":release_title,"status":"ADD","title":s["recording_title"]})
        continue

    release_id = rel["release_id"]
    promoted = [r for r in recordings if r.get("release_id") == release_id]

    source_norm = {norm(r["recording_title"]): r["recording_title"] for r in source_rows}
    promoted_norm = {norm(r["canonical_recording_title"]): r["canonical_recording_title"] for r in promoted}

    match = sorted([promoted_norm[k] for k in promoted_norm if k in source_norm], key=norm)
    remove = sorted([promoted_norm[k] for k in promoted_norm if k not in source_norm], key=norm)
    add = sorted([source_norm[k] for k in source_norm if k not in promoted_norm], key=norm)

    summary.append((release_title, release_id, len(promoted), len(source_rows), len(match), len(add), len(remove)))

    for x in match:
        audit_rows.append({"release_title":release_title,"status":"MATCH","title":x})
    for x in add:
        audit_rows.append({"release_title":release_title,"status":"ADD","title":x})
    for x in remove:
        audit_rows.append({"release_title":release_title,"status":"REMOVE","title":x})

with (STAGING / "UNIT0101_ISMAEL_BLOCK0001_AUDIT.tsv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, delimiter="\t", fieldnames=["release_title","status","title"], lineterminator="\n")
    w.writeheader()
    w.writerows(audit_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# UNIT-0101 — Ismael Miranda Block 0001 Audit Report\n\n")
    f.write("Project: MUSIC_RELATIONSHIPS_DB\n")
    f.write("Unit: UNIT-0101\n\n")
    f.write("## Scope\n\n")
    for t in TRACKLISTS:
        f.write(f"- {t}\n")
    f.write("\n## Summary\n\n")
    f.write("| Release | Release ID | Promoted | Source | Match | Add | Remove |\n")
    f.write("|---|---:|---:|---:|---:|---:|---:|\n")
    for s in summary:
        f.write(f"| {s[0]} | {s[1]} | {s[2]} | {s[3]} | {s[4]} | {s[5]} | {s[6]} |\n")
    f.write("\n## Status\n\n")
    if all(s[5] == 0 and s[6] == 0 for s in summary):
        f.write("PASS: promoted recordings match source tracklists.\n")
    else:
        f.write("REVIEW REQUIRED: add/remove differences detected.\n")

print("audit_rows", len(audit_rows))
for s in summary:
    print("release", s[0], "release_id", s[1], "promoted", s[2], "source", s[3], "match", s[4], "add", s[5], "remove", s[6])
