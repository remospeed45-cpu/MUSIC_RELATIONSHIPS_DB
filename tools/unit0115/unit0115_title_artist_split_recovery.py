#!/usr/bin/env python3
import csv
import re
import unicodedata
from pathlib import Path
from collections import Counter

SRC = Path("authority/staging/unit0114/UNIT0114_REVIEW_REQUIRED.tsv")
PERF = Path("authority/performers/performers_master.tsv")
GRP = Path("authority/groups/groups_master.tsv")

OUT = Path("authority/staging/unit0115/UNIT0115_TITLE_ARTIST_SPLIT_RECOVERY.tsv")
SUMMARY = Path("reports/unit0115/UNIT0115_TITLE_ARTIST_SPLIT_RECOVERY_REPORT.md")

DASH_RE = re.compile(r"\s+[–—-]\s+")

def norm(s):
    s = (s or "").strip().lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def load_master(path, id_col_candidates, name_col_candidates):
    rows = []
    if not path.exists():
        return rows
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        cols = reader.fieldnames or []
        id_col = next((c for c in id_col_candidates if c in cols), None)
        name_col = next((c for c in name_col_candidates if c in cols), None)
        if not id_col or not name_col:
            raise SystemExit(f"Missing expected columns in {path}: {cols}")
        for r in reader:
            name = r.get(name_col, "").strip()
            if name:
                rows.append((norm(name), r.get(id_col, "").strip(), name))
    return rows

performers = load_master(
    PERF,
    ["performer_id", "artist_id", "entity_id"],
    ["canonical_performer_name", "performer_name", "canonical_artist_name", "entity_name"]
)
groups = load_master(
    GRP,
    ["group_id", "entity_id"],
    ["canonical_group_name", "group_name", "entity_name"]
)

perf_map = {n: (i, name) for n, i, name in performers}
grp_map = {n: (i, name) for n, i, name in groups}

with SRC.open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t"))

out_rows = []
counts = Counter()
artist_counts = Counter()

for r in rows:
    if r.get("review_class") != "performer_conflict":
        continue

    raw_title = r.get("candidate_title", "").strip()
    parts = DASH_RE.split(raw_title, maxsplit=1)

    clean_title = raw_title
    extracted_artist = ""
    split_status = "no_split"

    if len(parts) == 2 and parts[0].strip() and parts[1].strip():
        clean_title = parts[0].strip()
        extracted_artist = parts[1].strip()
        split_status = "split"

    nartist = norm(extracted_artist)
    matched_performer_id = ""
    matched_group_id = ""
    matched_entity_name = ""
    match_type = "none"

    if nartist in perf_map:
        matched_performer_id, matched_entity_name = perf_map[nartist]
        match_type = "performer"
    elif nartist in grp_map:
        matched_group_id, matched_entity_name = grp_map[nartist]
        match_type = "group"

    recovery_status = "not_recovered"
    if split_status == "split" and match_type != "none":
        recovery_status = "recovered_entity"
    elif split_status == "split":
        recovery_status = "split_only"

    counts[recovery_status] += 1
    counts[f"match_type_{match_type}"] += 1
    if extracted_artist:
        artist_counts[extracted_artist] += 1

    nr = dict(r)
    nr.update({
        "candidate_title_clean": clean_title,
        "extracted_artist_name": extracted_artist,
        "split_status": split_status,
        "recovered_match_type": match_type,
        "recovered_performer_id": matched_performer_id,
        "recovered_group_id": matched_group_id,
        "recovered_entity_name": matched_entity_name,
        "recovery_status": recovery_status,
    })
    out_rows.append(nr)

fieldnames = list(rows[0].keys()) + [
    "candidate_title_clean",
    "extracted_artist_name",
    "split_status",
    "recovered_match_type",
    "recovered_performer_id",
    "recovered_group_id",
    "recovered_entity_name",
    "recovery_status",
]

with OUT.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, delimiter="\t", fieldnames=fieldnames)
    w.writeheader()
    w.writerows(out_rows)

with SUMMARY.open("w", encoding="utf-8") as fh:
    fh.write("# UNIT0115 Title-Artist Split Recovery Report\n\n")
    fh.write("## Objective\n\n")
    fh.write("Recover UNIT0114 performer_conflict rows where the actual performer/group is embedded inside candidate_title.\n\n")
    fh.write("## Inputs\n\n")
    fh.write(f"- `{SRC}`\n")
    fh.write(f"- `{PERF}`\n")
    fh.write(f"- `{GRP}`\n\n")
    fh.write("## Outputs\n\n")
    fh.write(f"- `{OUT}`\n\n")
    fh.write("## Counts\n\n")
    fh.write(f"- performer_conflict_rows_analyzed: {len(out_rows)}\n")
    for k, v in counts.most_common():
        fh.write(f"- {k}: {v}\n")
    fh.write("\n## Top Extracted Artists\n\n")
    fh.write("| extracted_artist_name | rows |\n|---|---:|\n")
    for name, cnt in artist_counts.most_common(40):
        fh.write(f"| {name} | {cnt} |\n")

print("wrote", OUT)
print("wrote", SUMMARY)
print()
print("COUNTS")
for k, v in counts.most_common():
    print(f"{k}\t{v}")
print()
print("TOP EXTRACTED ARTISTS")
for k, v in artist_counts.most_common(25):
    print(f"{k}\t{v}")
