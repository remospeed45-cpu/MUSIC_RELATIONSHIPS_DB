#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import unicodedata
from datetime import date

ROOT = Path(".")
OUTDIR = ROOT / "imports/unit0088_bobby_valentin_bulk_titles"
REPORTDIR = ROOT / "reports/unit0088"
OUTDIR.mkdir(parents=True, exist_ok=True)
REPORTDIR.mkdir(parents=True, exist_ok=True)

OUT = OUTDIR / "UNIT0088_BOBBY_VALENTIN_BULK_TITLE_EXTRACTION.tsv"
REVIEW = OUTDIR / "UNIT0088_BOBBY_VALENTIN_REVIEW_ONLY.tsv"
REPORT = REPORTDIR / "UNIT0088_BOBBY_VALENTIN_BULK_EXTRACTION_REPORT.md"

SOURCE_ID = "SRC0003"
UNIT_ID = "UNIT-0088"
ARTIST = "Bobby Valentín"
LABEL = "Fania"
TODAY = date.today().isoformat()

candidate_files = []
for base in ["imports", "reports", "authority/staging"]:
    p = ROOT / base
    if p.exists():
        for f in p.rglob("*"):
            if f.is_file():
                name = f.name.lower()
                textpath = str(f).lower()
                if (
                    "0086" in textpath
                    or "0087" in textpath
                    or "bobby" in textpath
                    or "valentin" in textpath
                    or "valentín" in textpath
                ):
                    candidate_files.append(f)

def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def norm(s):
    s = s or ""
    s = strip_accents(s).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return re.sub(r"\s+", " ", s)

def clean_title(s):
    s = (s or "").strip()
    s = re.sub(r"\s+", " ", s)
    s = s.strip(" \t\r\n-|•*")
    return s

bad_titles = {
    "", "tbd", "title", "recording_title", "canonical_recording_title",
    "raw_title", "song", "songs", "recordings", "candidate", "approved",
    "source", "release", "bobby valentín", "bobby valentin", "fania"
}

rows = []
review = []
seen = set()

def add_row(raw_release, raw_title, source_file, evidence):
    raw_release = clean_title(raw_release)
    raw_title = clean_title(raw_title)
    key_title = norm(raw_title)
    if key_title in bad_titles or len(raw_title) < 2:
        return
    key = (norm(raw_release), key_title)
    if key in seen:
        return
    seen.add(key)
    rows.append({
        "unit_id": UNIT_ID,
        "source_id": SOURCE_ID,
        "raw_artist": ARTIST,
        "raw_release": raw_release,
        "raw_title": raw_title,
        "canonical_recording_title": raw_title,
        "canonical_song_title": raw_title,
        "primary_group_or_performer": ARTIST,
        "label_name": LABEL,
        "evidence_source": str(source_file),
        "evidence_status": evidence,
        "confidence": "high" if evidence == "fania_text_verified" else "medium",
        "review_status": "candidate",
        "notes": "bulk extracted from existing Bobby Valentin harvest"
    })

for f in candidate_files:
    try:
        txt = f.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue

    # TSV files with known patterns
    if f.suffix.lower() == ".tsv":
        lines = txt.splitlines()
        if not lines:
            continue

        sniffed = False
        try:
            reader = csv.DictReader(lines, delimiter="\t")
            if reader.fieldnames:
                fields = [x or "" for x in reader.fieldnames]
                lower = {x.lower(): x for x in fields}
                title_keys = [
                    "recording_title", "raw_title", "canonical_recording_title",
                    "title", "canonical_song_title"
                ]
                release_keys = ["release_title", "raw_release", "release", "album"]
                artist_keys = ["artist", "raw_artist", "performer", "primary_group_or_performer"]

                for r in reader:
                    allvals = " ".join(str(v or "") for v in r.values())
                    if "bobby" not in norm(allvals) and "valentin" not in norm(allvals) and "rey del bajo" not in norm(allvals):
                        continue

                    title = ""
                    release = ""
                    for k in title_keys:
                        if k in lower and r.get(lower[k]):
                            title = r.get(lower[k], "")
                            break
                    for k in release_keys:
                        if k in lower and r.get(lower[k]):
                            release = r.get(lower[k], "")
                            break

                    if not title:
                        vals = [clean_title(v) for v in r.values() if clean_title(v)]
                        for v in vals:
                            nv = norm(v)
                            if nv not in bad_titles and nv not in {"bobby valentin", "bobby valentín", "fania", "candidate", "high"}:
                                if len(v) > 2 and len(v) < 80:
                                    title = v
                                    break

                    if title:
                        add_row(release, title, f, "fania_text_verified")
                        sniffed = True
        except Exception:
            pass

        if sniffed:
            continue

    # Markdown/text fallback: capture bullet/number/list title-like lines
    current_release = ""
    for line in txt.splitlines():
        raw = clean_title(line)
        nraw = norm(raw)

        if not raw:
            continue

        if "bobby" in nraw and "valentin" in nraw and ("—" in raw or "-" in raw or ":" in raw):
            parts = re.split(r"\s+[—-]\s+|:", raw, maxsplit=1)
            if len(parts) == 2:
                left, right = clean_title(parts[0]), clean_title(parts[1])
                if "bobby" not in norm(left) and len(left) < 80:
                    current_release = left
                elif "bobby" not in norm(right) and len(right) < 80:
                    current_release = right

        m = re.match(r"^(?:[-*•]|\d+[.)])\s+(.+)$", raw)
        if m:
            title = clean_title(m.group(1))
            title = re.sub(r"\s+[-—]\s+Bobby Valent[ií]n.*$", "", title, flags=re.I)
            title = re.sub(r"\s+\(.*?\)\s*$", "", title).strip()
            if len(title) < 80 and norm(title) not in bad_titles:
                add_row(current_release, title, f, "source_text_verified")

# Remove obvious previously promoted Rey Del Bajo-only duplicates? Keep useful but mark as candidate.
rows = sorted(rows, key=lambda r: (norm(r["raw_release"]), norm(r["raw_title"])))

fieldnames = [
    "unit_id","source_id","raw_artist","raw_release","raw_title",
    "canonical_recording_title","canonical_song_title",
    "primary_group_or_performer","label_name","evidence_source",
    "evidence_status","confidence","review_status","notes"
]

with OUT.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, delimiter="\t", fieldnames=fieldnames)
    w.writeheader()
    for r in rows:
        w.writerow(r)

with REVIEW.open("w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, delimiter="\t", fieldnames=fieldnames)
    w.writeheader()

release_counts = {}
for r in rows:
    rel = r["raw_release"] or "UNKNOWN_RELEASE"
    release_counts[rel] = release_counts.get(rel, 0) + 1

with REPORT.open("w", encoding="utf-8") as fh:
    fh.write("# UNIT-0088 Bobby Valentín Bulk Title Extraction Report\n\n")
    fh.write(f"Date: {TODAY}\n\n")
    fh.write("## Status\n\n")
    fh.write("Bulk extraction generated from existing UNIT-0086 / UNIT-0087 Bobby Valentín harvest material.\n\n")
    fh.write("## Totals\n\n")
    fh.write(f"- Candidate rows: {len(rows)}\n")
    fh.write(f"- Review-only rows: 0\n")
    fh.write(f"- Source files scanned: {len(candidate_files)}\n\n")
    fh.write("## Release Counts\n\n")
    for rel, count in sorted(release_counts.items(), key=lambda x: (-x[1], x[0])):
        fh.write(f"- {rel}: {count}\n")
    fh.write("\n## Relationship Target\n\n")
    fh.write("recording ↔ song ↔ Bobby Valentín ↔ release ↔ Fania ↔ SRC0003\n")

print("WROTE", OUT, "ROWS", len(rows))
print("WROTE", REVIEW)
print("WROTE", REPORT)
