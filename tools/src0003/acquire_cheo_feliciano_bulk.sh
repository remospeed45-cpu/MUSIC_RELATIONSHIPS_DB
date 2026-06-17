#!/usr/bin/env bash
set -euo pipefail

OUTDIR="data/src0003/cheo_feliciano"
ARTIST_URL="https://fania.com/artist/cheo-feliciano/"

mkdir -p "$OUTDIR"

echo "===== DOWNLOAD ARTIST PAGE ====="
curl -L "$ARTIST_URL" -o "$OUTDIR/cheo_feliciano_artist_page.html"

echo "===== EXTRACT FANIA RECORD LINKS ====="
grep -oE 'https://fania.com/record/[^"#? ]+/?' "$OUTDIR/cheo_feliciano_artist_page.html" \
  | sort -u \
  > "$OUTDIR/cheo_feliciano_record_urls.txt" || true

grep -oE 'href="/record/[^"#? ]+/?' "$OUTDIR/cheo_feliciano_artist_page.html" \
  | sed 's|href="|https://fania.com|' \
  | sort -u \
  >> "$OUTDIR/cheo_feliciano_record_urls.txt" || true

sort -u "$OUTDIR/cheo_feliciano_record_urls.txt" -o "$OUTDIR/cheo_feliciano_record_urls.txt"

echo "===== DOWNLOAD EACH RECORD PAGE ====="
i=0
while read -r url; do
  [ -z "$url" ] && continue
  i=$((i+1))
  slug="$(basename "$url")"
  outfile="$OUTDIR/record_${i}_${slug}.html"
  echo "$i	$url	$outfile"
  curl -L "$url" -o "$outfile"
done < "$OUTDIR/cheo_feliciano_record_urls.txt" \
  > "$OUTDIR/cheo_feliciano_download_manifest.tsv"

echo "===== CREATE RELEASE INVENTORY DRAFT ====="
{
  echo -e "source_id\tartist\trelease_url\tlocal_html\textraction_status"
  awk -F'\t' '{print "SRC0003\tCheo Feliciano\t"$2"\t"$3"\tdownloaded"}' \
    "$OUTDIR/cheo_feliciano_download_manifest.tsv"
} > "$OUTDIR/CHEO_FELICIANO_RELEASE_INVENTORY.tsv"

echo "===== SUMMARY ====="
echo "Record URLs:"
wc -l "$OUTDIR/cheo_feliciano_record_urls.txt"
echo
echo "Downloaded pages:"
ls "$OUTDIR"/record_*.html 2>/dev/null | wc -l
echo
echo "Inventory:"
cat "$OUTDIR/CHEO_FELICIANO_RELEASE_INVENTORY.tsv"
