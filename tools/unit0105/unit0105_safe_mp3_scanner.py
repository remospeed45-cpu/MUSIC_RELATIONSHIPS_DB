#!/usr/bin/env python3
from pathlib import Path
import csv, os, re, unicodedata, hashlib, subprocess, shutil

ROOT = Path(".")
MP3_ROOT = Path(os.environ.get("MP3_ROOT", str(Path.home() / "Music"))).expanduser()

OUTDIR = ROOT / "imports/unit0105_mp3_scan"
REPORTDIR = ROOT / "reports/unit0105"
OUTDIR.mkdir(parents=True, exist_ok=True)
REPORTDIR.mkdir(parents=True, exist_ok=True)

RECORDINGS = ROOT / "authority/recordings/recordings_master.tsv"
SONGS = ROOT / "authority/songs/songs_master.tsv"
PERFORMERS = ROOT / "authority/performers/performers_master.tsv"
RELEASES = ROOT / "authority/releases/releases_master.tsv"

def norm(s):
    s = s or ""
    s = ''.join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    s = s.replace("’","'").replace("‘","'")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)

def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def safe_id(path):
    return hashlib.sha1(str(path).encode("utf-8", errors="ignore")).hexdigest()[:16]

def parse_filename(path):
    stem = path.stem
    cleaned = re.sub(r"^\d+\s*[-_. ]+", "", stem).strip()
    parts = re.split(r"\s+-\s+|\s+–\s+|\s+—\s+", cleaned, maxsplit=1)
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    return "", cleaned

def get_tags(path):
    tags = {"tag_artist":"","tag_title":"","tag_album":""}
    try:
        from mutagen import File
        audio = File(path, easy=True)
        if audio:
            tags["tag_artist"] = "; ".join(audio.get("artist", []) or [])
            tags["tag_title"] = "; ".join(audio.get("title", []) or [])
            tags["tag_album"] = "; ".join(audio.get("album", []) or [])
    except Exception:
        pass
    return tags

def maybe_fpcalc(path):
    # Fast scan mode: fingerprint disabled unless ENABLE_FPCALC=1
    if os.environ.get("ENABLE_FPCALC", "0") != "1":
        return "available" if shutil.which("fpcalc") else "", "skipped_fast_scan"
    fpcalc = shutil.which("fpcalc")
    if not fpcalc:
        return "", ""
    try:
        p = subprocess.run([fpcalc, "-json", str(path)], capture_output=True, text=True, timeout=20)
        if p.returncode == 0:
            return "available", "generated"
        return "available", "failed"
    except Exception:
        return "available", "failed"

recordings = read_tsv(RECORDINGS)
songs = read_tsv(SONGS)
performers = read_tsv(PERFORMERS) if PERFORMERS.exists() else []
releases = read_tsv(RELEASES) if RELEASES.exists() else []

rec_by_title = {}
for r in recordings:
    rec_by_title.setdefault(norm(r.get("canonical_recording_title","")), []).append(r)

song_by_title = {}
for r in songs:
    song_by_title.setdefault(norm(r.get("canonical_song_title","")), []).append(r)

performer_by_id = {r.get("performer_id",""): r.get("canonical_performer_name","") for r in performers}
release_by_id = {r.get("release_id",""): r.get("canonical_release_title","") for r in releases}

mp3s = []
if MP3_ROOT.exists():
    for ext in ("*.mp3","*.MP3","*.m4a","*.M4A","*.flac","*.FLAC"):
        mp3s.extend(MP3_ROOT.rglob(ext))

rows = []
known = []
probable = []
unknown = []

for path in sorted(set(mp3s)):
    file_artist, file_title = parse_filename(path)
    tags = get_tags(path)

    candidate_title = tags["tag_title"] or file_title
    candidate_artist = tags["tag_artist"] or file_artist

    ntitle = norm(candidate_title)
    rec_hits = rec_by_title.get(ntitle, [])
    song_hits = song_by_title.get(ntitle, [])

    status = "unknown"
    best_recording_id = ""
    best_song_id = ""
    best_performer = ""
    best_release = ""

    if rec_hits:
        status = "known_recording_title"
        r = rec_hits[0]
        best_recording_id = r.get("recording_id","")
        best_song_id = r.get("canonical_song_id","")
        best_performer = performer_by_id.get(r.get("primary_performer_id",""), "")
        best_release = release_by_id.get(r.get("release_id",""), "")
    elif song_hits:
        status = "probable_song_title"
        s = song_hits[0]
        best_song_id = s.get("song_id","")

    fpcalc_status, fingerprint_status = maybe_fpcalc(path)

    row = {
        "scan_id": safe_id(path),
        "file_path": str(path),
        "file_name": path.name,
        "file_artist_guess": file_artist,
        "file_title_guess": file_title,
        "tag_artist": tags["tag_artist"],
        "tag_title": tags["tag_title"],
        "tag_album": tags["tag_album"],
        "candidate_artist": candidate_artist,
        "candidate_title": candidate_title,
        "match_status": status,
        "recording_hits": str(len(rec_hits)),
        "song_hits": str(len(song_hits)),
        "best_recording_id": best_recording_id,
        "best_song_id": best_song_id,
        "best_performer": best_performer,
        "best_release": best_release,
        "fpcalc_status": fpcalc_status,
        "fingerprint_status": fingerprint_status,
    }

    rows.append(row)
    if status == "known_recording_title":
        known.append(row)
    elif status == "probable_song_title":
        probable.append(row)
    else:
        unknown.append(row)

fields = [
    "scan_id","file_path","file_name","file_artist_guess","file_title_guess",
    "tag_artist","tag_title","tag_album","candidate_artist","candidate_title",
    "match_status","recording_hits","song_hits","best_recording_id","best_song_id",
    "best_performer","best_release","fpcalc_status","fingerprint_status"
]

def write(path, data):
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, delimiter="\t", fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(data)

write(OUTDIR / "UNIT0105_MP3_SCAN_ALL.tsv", rows)
write(OUTDIR / "UNIT0105_MP3_KNOWN_RECORDINGS.tsv", known)
write(OUTDIR / "UNIT0105_MP3_PROBABLE_SONGS.tsv", probable)
write(OUTDIR / "UNIT0105_MP3_UNKNOWN.tsv", unknown)

with (REPORTDIR / "UNIT0105_MP3_SCAN_REPORT.md").open("w", encoding="utf-8") as f:
    f.write("# UNIT-0105 MP3 Safe Scan Report\n\n")
    f.write("Project: MUSIC_RELATIONSHIPS_DB\n")
    f.write("Unit: UNIT-0105\n\n")
    f.write("## Scan root\n\n")
    f.write(f"{MP3_ROOT}\n\n")
    f.write("## Safety\n\n")
    f.write("- Read-only scan\n")
    f.write("- No rename\n")
    f.write("- No move\n")
    f.write("- No metadata write\n\n")
    f.write("## Totals\n\n")
    f.write(f"- Audio files scanned: {len(rows)}\n")
    f.write(f"- Known recording-title matches: {len(known)}\n")
    f.write(f"- Probable song-title matches: {len(probable)}\n")
    f.write(f"- Unknown files: {len(unknown)}\n\n")
    f.write("## Tool availability\n\n")
    f.write(f"- mutagen import: attempted\n")
    f.write(f"- fpcalc path: {shutil.which('fpcalc') or 'not found'}\n")

print("MP3_ROOT", MP3_ROOT)
print("audio_files_scanned", len(rows))
print("known_recording_title", len(known))
print("probable_song_title", len(probable))
print("unknown", len(unknown))
print("outputs", OUTDIR)
