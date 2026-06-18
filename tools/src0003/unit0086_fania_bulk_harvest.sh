#!/usr/bin/env bash
set -euo pipefail

clear
cd ~/codex_work/MUSIC_RELATIONSHIPS_DB

OUTDIR="data/src0003/unit0086_fania_bulk"
mkdir -p "$OUTDIR/html" "$OUTDIR/text"

TARGETS="$OUTDIR/UNIT0086_TARGETS.tsv"
MANIFEST="$OUTDIR/UNIT0086_DOWNLOAD_MANIFEST.tsv"

cat > "$MANIFEST" <<'TSV'
target_id	artist_or_group	release_title	url	local_html	status
TSV

echo "===== UNIT-0086 FANIA BULK HARVEST ====="
echo "Manual URL seed mode."
echo "Paste/add discovered URLs into:"
echo "$MANIFEST"

cat > "$OUTDIR/UNIT0086_SEED_URLS.tsv" <<'TSV'
target_id	artist_or_group	release_title	url	status
BOBVAL001	Bobby Valentín	Rey del Bajo	https://fania.com/record/rey-del-bajo/	pending
ISMIR001	Ismael Miranda		https://fania.com/artist/ismael-miranda/	pending
LARHAR001	Larry Harlow		https://fania.com/artist/larry-harlow/	pending
CHEO001	Cheo Feliciano		https://fania.com/artist/cheo-feliciano/	pending
HECLAV001	Héctor Lavoe		https://fania.com/artist/hector-lavoe/	pending
RAYBAR001	Ray Barretto		https://fania.com/artist/ray-barretto/	pending
TSV

echo
echo "===== SEED URLS ====="
column -t -s $'\t' "$OUTDIR/UNIT0086_SEED_URLS.tsv"

echo
echo "===== DOWNLOAD SEED URLS ====="

tail -n +2 "$OUTDIR/UNIT0086_SEED_URLS.tsv" | while IFS=$'\t' read -r target_id artist release url status
do
    safe_id="$(echo "$target_id" | tr '[:upper:]' '[:lower:]')"
    local_html="$OUTDIR/html/${safe_id}.html"

    echo "Downloading $target_id :: $url"
    curl -L --fail --silent --show-error "$url" -o "$local_html" || true

    if [ -s "$local_html" ]; then
        echo -e "${target_id}\t${artist}\t${release}\t${url}\t${local_html}\tdownloaded" >> "$MANIFEST"
        python3 - <<PY
from pathlib import Path
import re, html
p = Path("$local_html")
out = Path("$OUTDIR/text/${safe_id}.txt")
text = p.read_text(errors="ignore")
text = re.sub(r"<script.*?</script>", " ", text, flags=re.S|re.I)
text = re.sub(r"<style.*?</style>", " ", text, flags=re.S|re.I)
text = re.sub(r"<[^>]+>", " ", text)
text = html.unescape(text)
text = re.sub(r"\\s+", " ", text).strip()
out.write_text(text, encoding="utf-8")
PY
    else
        echo -e "${target_id}\t${artist}\t${release}\t${url}\t${local_html}\tfailed" >> "$MANIFEST"
    fi
done

echo
echo "===== DISCOVER RECORD LINKS FROM DOWNLOADED HTML ====="
grep -RhoE 'https://fania.com/record/[^" )<]+' "$OUTDIR/html" 2>/dev/null | sort -u > "$OUTDIR/UNIT0086_DISCOVERED_RECORD_URLS.txt" || true
grep -RhoE '/record/[^" )<]+' "$OUTDIR/html" 2>/dev/null | sed 's#^#https://fania.com#' | sort -u >> "$OUTDIR/UNIT0086_DISCOVERED_RECORD_URLS.txt" || true
sort -u -o "$OUTDIR/UNIT0086_DISCOVERED_RECORD_URLS.txt" "$OUTDIR/UNIT0086_DISCOVERED_RECORD_URLS.txt"

echo
echo "===== DISCOVERED RECORD URL COUNT ====="
wc -l "$OUTDIR/UNIT0086_DISCOVERED_RECORD_URLS.txt"

echo
echo "===== FIRST 100 DISCOVERED RECORD URLS ====="
head -100 "$OUTDIR/UNIT0086_DISCOVERED_RECORD_URLS.txt"

echo
echo "===== KEY TEXT HITS ====="
grep -RniE "Rey del Bajo|Ismael Miranda|Larry Harlow|Cheo Feliciano|Héctor Lavoe|Hector Lavoe|Ray Barretto|track|songs|album" "$OUTDIR/text" | head -300 || true

echo
echo "===== FILES CREATED ====="
find "$OUTDIR" -type f | sort

echo
echo "===== GIT STATUS ====="
git status --short
