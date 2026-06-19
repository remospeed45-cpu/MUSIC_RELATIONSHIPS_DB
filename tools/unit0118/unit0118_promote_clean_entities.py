#!/usr/bin/env python3
import csv
import re
import unicodedata
from pathlib import Path

SRC = Path("authority/staging/unit0117/UNIT0117_ENTITY_CLEANUP_CANDIDATES.tsv")
PERF = Path("authority/performers/performers_master.tsv")
GRP = Path("authority/groups/groups_master.tsv")

ADDED_PERF = Path("authority/staging/unit0118/UNIT0118_PERFORMERS_ADDED.tsv")
ADDED_GRP = Path("authority/staging/unit0118/UNIT0118_GROUPS_ADDED.tsv")
SKIPPED = Path("authority/staging/unit0118/UNIT0118_ENTITIES_SKIPPED.tsv")
REPORT = Path("reports/unit0118/UNIT0118_PROMOTION_REPORT.md")

TODAY = "2026-06-19"

def norm(s):
    s = (s or "").strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def read_tsv(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

def write_tsv(path, rows, fields):
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def next_id(rows, id_col, prefix, width):
    maxn = 0
    for r in rows:
        val = r.get(id_col, "")
        if val.startswith(prefix):
            try:
                maxn = max(maxn, int(val[len(prefix):]))
            except ValueError:
                pass
    return maxn + 1

candidates = read_tsv(SRC)
perf_rows = read_tsv(PERF)
grp_rows = read_tsv(GRP)

perf_fields = list(perf_rows[0].keys())
grp_fields = list(grp_rows[0].keys())

perf_name_col = "canonical_performer_name"
grp_name_col = "canonical_group_name"

existing_perf = {norm(r.get(perf_name_col, "")) for r in perf_rows}
existing_grp = {norm(r.get(grp_name_col, "")) for r in grp_rows}

next_perf = next_id(perf_rows, "performer_id", "PER", 6)
next_grp = next_id(grp_rows, "group_id", "GRP", 4)

added_perf = []
added_grp = []
skipped = []

for c in candidates:
    if c.get("action") != "candidate_entity":
        skipped.append({**c, "skip_reason": "not_candidate_entity"})
        continue

    name = c["clean_name"].strip()
    etype = c["entity_type"].strip()
    n = norm(name)

    if etype == "performer":
        if n in existing_perf:
            skipped.append({**c, "skip_reason": "performer_duplicate"})
            continue
        new = {k: "" for k in perf_fields}
        new["performer_id"] = f"PER{next_perf:06d}"
        new[perf_name_col] = name
        if "performer_type" in new:
            new["performer_type"] = "individual"
        if "country" in new:
            new["country"] = ""
        if "source_id" in new:
            new["source_id"] = "SRC0002"
        if "confidence" in new:
            new["confidence"] = "medium"
        if "review_status" in new:
            new["review_status"] = "approved"
        if "created_at" in new:
            new["created_at"] = TODAY
        if "updated_at" in new:
            new["updated_at"] = TODAY
        perf_rows.append(new)
        added_perf.append(new)
        existing_perf.add(n)
        next_perf += 1

    elif etype == "group":
        if n in existing_grp:
            skipped.append({**c, "skip_reason": "group_duplicate"})
            continue
        new = {k: "" for k in grp_fields}
        new["group_id"] = f"GRP{next_grp:04d}"
        new[grp_name_col] = name
        if "country" in new:
            new["country"] = ""
        if "source_id" in new:
            new["source_id"] = "SRC0002"
        if "confidence" in new:
            new["confidence"] = "medium"
        if "review_status" in new:
            new["review_status"] = "approved"
        if "created_at" in new:
            new["created_at"] = TODAY
        if "updated_at" in new:
            new["updated_at"] = TODAY
        grp_rows.append(new)
        added_grp.append(new)
        existing_grp.add(n)
        next_grp += 1

    else:
        skipped.append({**c, "skip_reason": f"unknown_entity_type:{etype}"})

write_tsv(PERF, perf_rows, perf_fields)
write_tsv(GRP, grp_rows, grp_fields)
write_tsv(ADDED_PERF, added_perf, perf_fields)
write_tsv(ADDED_GRP, added_grp, grp_fields)

skip_fields = list(candidates[0].keys()) + ["skip_reason"]
write_tsv(SKIPPED, skipped, skip_fields)

with REPORT.open("w", encoding="utf-8") as fh:
    fh.write("# UNIT0118 Promotion Report\n\n")
    fh.write("## Objective\n\n")
    fh.write("Promote clean missing performer/group entities from UNIT0117 to unblock SRC0002 recovery rows.\n\n")
    fh.write("## Counts\n\n")
    fh.write(f"- candidates_total: {len(candidates)}\n")
    fh.write(f"- performers_added: {len(added_perf)}\n")
    fh.write(f"- groups_added: {len(added_grp)}\n")
    fh.write(f"- skipped: {len(skipped)}\n\n")
    fh.write("## Added Performers\n\n")
    for r in added_perf:
        fh.write(f"- {r.get('performer_id')} {r.get(perf_name_col)}\n")
    fh.write("\n## Added Groups\n\n")
    for r in added_grp:
        fh.write(f"- {r.get('group_id')} {r.get(grp_name_col)}\n")

print("performers_added", len(added_perf))
print("groups_added", len(added_grp))
print("skipped", len(skipped))
print("wrote", REPORT)
