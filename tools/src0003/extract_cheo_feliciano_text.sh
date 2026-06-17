#!/usr/bin/env bash
set -euo pipefail

OUTDIR="data/src0003/cheo_feliciano"

echo -e "source_id\tartist\trelease_slug\tlocal_html\tpage_title\tcandidate_text" \
> "$OUTDIR/CHEO_FELICIANO_TEXT_EXTRACT.tsv"

for f in "$OUTDIR"/record_*.html; do
  slug="$(basename "$f" .html | sed 's/^record_[0-9]*_//')"

  title="$(grep -oP '(?<=<title>).*?(?=</title>)' "$f" \
    | sed 's/&#8211;/-/g; s/&amp;/\&/g; s/[[:space:]]\+/ /g' \
    | head -1)"

  text="$(tr '\n' ' ' < "$f" \
    | sed 's/<script[^>]*>.*<\/script>//Ig; s/<style[^>]*>.*<\/style>//Ig' \
    | sed 's/<[^>]*>/ /g' \
    | sed 's/&amp;/\&/g; s/&#8217;/'"'"'/g; s/&#8216;/'"'"'/g; s/&#8220;/"/g; s/&#8221;/"/g; s/&#8211;/-/g; s/&#8212;/-/g; s/&nbsp;/ /g' \
    | sed 's/[[:space:]]\+/ /g' \
    | cut -c1-4000)"

  echo -e "SRC0003\tCheo Feliciano\t$slug\t$f\t$title\t$text" \
  >> "$OUTDIR/CHEO_FELICIANO_TEXT_EXTRACT.tsv"
done

echo "===== TEXT EXTRACT CREATED ====="
wc -l "$OUTDIR/CHEO_FELICIANO_TEXT_EXTRACT.tsv"

echo
echo "===== PAGE TITLES ====="
cut -f1-5 "$OUTDIR/CHEO_FELICIANO_TEXT_EXTRACT.tsv"

echo
echo "===== SEARCH TRACK-LIKE MARKERS ====="
grep -RniE "Track|Songs|Listen|Cheo|Felicidades|La Herencia|Sentimiento|Estampas" "$OUTDIR"/record_*.html | head -80 || true
