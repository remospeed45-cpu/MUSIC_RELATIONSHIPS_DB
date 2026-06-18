#!/usr/bin/env bash
set -euo pipefail

clear
cd ~/codex_work/MUSIC_RELATIONSHIPS_DB

OUTDIR="data/src0003/unit0086_fania_bulk"
mkdir -p "$OUTDIR"

echo "===== UNIT-0086 FANIA BULK HARVEST PLAN ====="

cat > "$OUTDIR/UNIT0086_TARGETS.tsv" <<'TSV'
priority	artist_or_group	release_title	search_hint	status
A	Bobby Valentín	Rey del Bajo	fania rey del bajo bobby valentin	pending
A	Ismael Miranda		additional Ismael Miranda Fania records	pending
A	Larry Harlow		additional Larry Harlow Fania records	pending
A	Cheo Feliciano		additional Cheo Feliciano Fania records	pending
A	Héctor Lavoe		additional Hector Lavoe Fania records	pending
A	Ray Barretto		additional Ray Barretto Fania records	pending
TSV

echo
echo "===== TARGETS CREATED ====="
column -t -s $'\t' "$OUTDIR/UNIT0086_TARGETS.tsv"

echo
echo "===== NEXT ACTION ====="
echo "Use this target file to run one larger acquisition pass, not one release at a time."

echo
echo "===== GIT STATUS ====="
git status --short
