#!/usr/bin/env python3
import csv
from pathlib import Path
from collections import Counter

SRC = Path("authority/staging/unit0119/UNIT0119_STILL_REVIEW_REQUIRED.tsv")

OUT_PROMO = Path("authority/staging/unit0120/UNIT0120_PROMOTION_CANDIDATES.tsv")
OUT_REVIEW = Path("authority/staging/unit0120/UNIT0120_REMAINING_REVIEW.tsv")
REPORT = Path("reports/unit0120/UNIT0120_RELAXED_PROMOTION_REPORT.md")

with SRC.open(newline="", encoding="utf-8") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t"))

promotion = []
review = []

reasons = Counter()

for r in rows:

    title = (r.get("final_candidate_title") or "").strip()

    performer_id = (r.get("final_performer_id") or "").strip()
    group_id = (r.get("final_group_id") or "").strip()

    has_identity = bool(performer_id or group_id)

    blockers = []

    if not title:
        blockers.append("missing_title")

    if not has_identity:
        blockers.append("missing_performer_group")

    if "short_description_only_source" in r.get("unit0119_recheck_reasons",""):
        blockers.append("short_description_only_source")

    nr = dict(r)

    if blockers:
        nr["unit0120_status"] = "review_required"
        nr["unit0120_blockers"] = ";".join(blockers)
        review.append(nr)

        for b in blockers:
            reasons[b] += 1

    else:
        nr["unit0120_status"] = "promotion_candidate"
        nr["unit0120_blockers"] = ""
        promotion.append(nr)

fields = list(rows[0].keys()) + [
    "unit0120_status",
    "unit0120_blockers",
]

for path, data in [
    (OUT_PROMO, promotion),
    (OUT_REVIEW, review),
]:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(
            fh,
            delimiter="\t",
            fieldnames=fields,
            lineterminator="\n"
        )
        w.writeheader()
        w.writerows(data)

with REPORT.open("w", encoding="utf-8") as fh:

    fh.write("# UNIT0120 Relaxed Promotion Eligibility Report\n\n")

    fh.write("## Rule\n\n")
    fh.write("Promotion candidate if title exists and performer/group is resolved.\n\n")

    fh.write("## Counts\n\n")
    fh.write(f"- input_rows: {len(rows)}\n")
    fh.write(f"- promotion_candidates: {len(promotion)}\n")
    fh.write(f"- remaining_review: {len(review)}\n\n")

    fh.write("## Remaining Blockers\n\n")

    for k,v in reasons.most_common():
        fh.write(f"- {k}: {v}\n")

print("input_rows", len(rows))
print("promotion_candidates", len(promotion))
print("remaining_review", len(review))
