#!/usr/bin/env python3

import csv
from pathlib import Path
from collections import Counter

SRC = Path("authority/staging/unit0115/UNIT0115_TITLE_ARTIST_SPLIT_RECOVERY.tsv")

OUT_ALL = Path("authority/staging/unit0116/UNIT0116_SPLIT_ONLY_UNIQUE_ARTISTS.tsv")
OUT_GROUPS = Path("authority/staging/unit0116/UNIT0116_MISSING_GROUPS.tsv")
OUT_PERFORMERS = Path("authority/staging/unit0116/UNIT0116_MISSING_PERFORMERS.tsv")
REPORT = Path("reports/unit0116/UNIT0116_AUTHORITY_GAP_REPORT.md")

with SRC.open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t"))

split_only = [r for r in rows if r.get("recovery_status") == "split_only"]

artists = Counter()

for r in split_only:
    a = r.get("extracted_artist_name", "").strip()
    if a:
        artists[a] += 1

with OUT_ALL.open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["artist_name", "rows"])
    for artist, cnt in artists.most_common():
        w.writerow([artist, cnt])

group_keywords = [
    "orquesta",
    "conjunto",
    "grupo",
    "trio",
    "trío",
    "band",
    "banda",
    "sonora",
]

groups = []
performers = []

for artist, cnt in artists.most_common():
    low = artist.lower()

    is_group = any(k in low for k in group_keywords)

    if is_group:
        groups.append((artist, cnt))
    else:
        performers.append((artist, cnt))

with OUT_GROUPS.open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["group_name", "rows"])
    for row in groups:
        w.writerow(row)

with OUT_PERFORMERS.open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, delimiter="\t")
    w.writerow(["performer_name", "rows"])
    for row in performers:
        w.writerow(row)

with REPORT.open("w", encoding="utf-8") as fh:
    fh.write("# UNIT0116 Authority Gap Report\n\n")
    fh.write(f"- split_only_rows: {len(split_only)}\n")
    fh.write(f"- unique_artists: {len(artists)}\n")
    fh.write(f"- candidate_groups: {len(groups)}\n")
    fh.write(f"- candidate_performers: {len(performers)}\n\n")

    fh.write("## Top Missing Entities\n\n")

    for artist, cnt in artists.most_common(50):
        fh.write(f"- {artist}: {cnt}\n")

print("split_only_rows =", len(split_only))
print("unique_artists =", len(artists))
print("candidate_groups =", len(groups))
print("candidate_performers =", len(performers))
