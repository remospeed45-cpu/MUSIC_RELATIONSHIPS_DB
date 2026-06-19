#!/usr/bin/env python3
import csv, re, unicodedata
from pathlib import Path
from collections import Counter

SRC = Path("authority/staging/unit0115/UNIT0115_TITLE_ARTIST_SPLIT_RECOVERY.tsv")
PERF = Path("authority/performers/performers_master.tsv")
GRP = Path("authority/groups/groups_master.tsv")

OUT_READY = Path("authority/staging/unit0119/UNIT0119_PROMOTION_READY_FROM_RECOVERY.tsv")
OUT_REVIEW = Path("authority/staging/unit0119/UNIT0119_STILL_REVIEW_REQUIRED.tsv")
REPORT = Path("reports/unit0119/UNIT0119_REBUILD_PROMOTION_READINESS_REPORT.md")

def norm(s):
    s = (s or "").strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def read(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

rows = read(SRC)
performers = read(PERF)
groups = read(GRP)

perf_map = {norm(r["canonical_performer_name"]): r["performer_id"] for r in performers if r.get("canonical_performer_name")}
grp_map = {norm(r["canonical_group_name"]): r["group_id"] for r in groups if r.get("canonical_group_name")}

ready = []
review = []
counts = Counter()

for r in rows:
    nr = dict(r)

    title = nr.get("candidate_title_clean") or nr.get("candidate_title")
    artist = nr.get("extracted_artist_name", "")
    nartist = norm(artist)

    recovered_performer_id = nr.get("recovered_performer_id", "")
    recovered_group_id = nr.get("recovered_group_id", "")

    if not recovered_performer_id and nartist in perf_map:
        recovered_performer_id = perf_map[nartist]
    if not recovered_group_id and nartist in grp_map:
        recovered_group_id = grp_map[nartist]

    nr["final_candidate_title"] = title
    nr["final_artist_name"] = artist
    nr["final_performer_id"] = recovered_performer_id
    nr["final_group_id"] = recovered_group_id

    reasons = []

    if not title:
        reasons.append("missing_title")

    if not recovered_performer_id and not recovered_group_id:
        reasons.append("performer_or_group_unresolved")

    if nr.get("existing_recording_id") or nr.get("existing_song_id"):
        reasons.append("duplicate_existing_title")

    if "release_not_resolved_to_authority" in nr.get("review_detail", "") and not nr.get("resolved_release_id"):
        reasons.append("release_unresolved")

    if nr.get("source_extract_method") == "short_description":
        reasons.append("short_description_only_source")

    if nr.get("source_tracklist_status", "").startswith("partial"):
        reasons.append("partial_source_tracklist")

    nr["unit0119_recheck_reasons"] = ";".join(reasons)

    if not reasons:
        nr["unit0119_status"] = "promotion_ready"
        ready.append(nr)
    else:
        nr["unit0119_status"] = "review_required"
        review.append(nr)
        for reason in reasons:
            counts[reason] += 1

fields = list(rows[0].keys()) + [
    "final_candidate_title",
    "final_artist_name",
    "final_performer_id",
    "final_group_id",
    "unit0119_status",
    "unit0119_recheck_reasons",
]

for path, data in [(OUT_READY, ready), (OUT_REVIEW, review)]:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(data)

with REPORT.open("w", encoding="utf-8") as fh:
    fh.write("# UNIT0119 Rebuild Promotion Readiness Report\n\n")
    fh.write("## Objective\n\n")
    fh.write("Recheck SRC0002 recovery rows after UNIT0118 promoted missing performer/group entities.\n\n")
    fh.write("## Counts\n\n")
    fh.write(f"- input_rows: {len(rows)}\n")
    fh.write(f"- promotion_ready: {len(ready)}\n")
    fh.write(f"- still_review_required: {len(review)}\n\n")
    fh.write("## Remaining Blockers\n\n")
    for k, v in counts.most_common():
        fh.write(f"- {k}: {v}\n")

print("input_rows", len(rows))
print("promotion_ready", len(ready))
print("still_review_required", len(review))
print("wrote", REPORT)
