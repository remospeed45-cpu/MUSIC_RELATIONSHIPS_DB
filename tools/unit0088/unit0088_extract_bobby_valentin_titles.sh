#!/usr/bin/env bash
set -euo pipefail

OUT="imports/unit0088_bobby_valentin_bulk_titles/UNIT0088_BOBBY_VALENTIN_BULK_TITLE_EXTRACTION.tsv"

echo "===== UNIT-0088 BOBBY VALENTIN EXTRACTION HELPER ====="

echo
echo "Working file:"
echo "$OUT"

echo
echo "Current rows:"
wc -l "$OUT"

echo
echo "Preview:"
column -t -s $'\t' "$OUT" | head -40
