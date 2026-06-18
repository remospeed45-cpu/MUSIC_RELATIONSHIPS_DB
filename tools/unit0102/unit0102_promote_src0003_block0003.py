#!/usr/bin/env python3
from pathlib import Path
import csv, re, unicodedata
from datetime import date

TODAY = date.today().isoformat()
ROOT = Path(".")

TRACKLISTS = [
    ROOT / "data/src0003/batch0002/SRC0003_BATCH0002_ACID_TRACKLIST.tsv",
    ROOT / "data/src0003/batch0002/SRC0003_BATCH0002_SALSA_LARRY_HARLOW_TRACKLIST.tsv",
]

REC = ROOT / "authority/recordings/recordings_master.tsv"
SONG = ROOT / "authority/songs/songs_master.tsv"
PERF = ROOT / "authority/performers/performers_master.tsv"
REL = ROOT / "authority/releases/releases_master.tsv"
LABEL = ROOT / "authority/labels/labels_master.tsv"

IMPORT_DIR = ROOT / "imports/unit0102_src0003_block0003"
STAGING = ROOT / "authority/staging/unit0102"
REPORT_DIR = ROOT / "reports/unit0102"

for d in [IMPORT_DIR, STAGING, REPORT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def norm(s):
    s = ''.join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn")
    s = s.replace("’", "'").replace("‘", "'")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)

def read_tsv(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write_tsv(p, fields, rows):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, delimiter="\t", fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def next_id(rows, field, prefix, width):
    nums = []
    for r in rows:
        v = r.get(field, "")
        if v.startswith(prefix):
            try:
                nums.append(int(v.replace(prefix, "")))
            except:
                pass
    return f"{prefix}{max(nums or [0])+1:0{width}d}"

def ensure(rows, fields, id_field, name_field, name, prefix, width, defaults):
    nn = norm(name)
    for r in rows:
        if norm(r.get(name_field, "")) == nn:
            return r[id_field], False, r
    nid = next_id(rows, id_field, prefix, width)
    row = {k:"" for k in fields}
    row[id_field] = nid
    row[name_field] = name
    for k,v in defaults.items():
        if k in row:
            row[k] = v
    rows.append(row)
    return nid, True, row

rec_rows = read_tsv(REC)
song_rows = read_tsv(SONG)
perf_rows = read_tsv(PERF)
rel_rows = read_tsv(REL)
label_rows = read_tsv(LABEL)

rec_fields = list(rec_rows[0].keys())
song_fields = list(song_rows[0].keys())
perf_fields = list(perf_rows[0].keys())
rel_fields = list(rel_rows[0].keys())
label_fields = list(label_rows[0].keys())

label_id, label_added, _ = ensure(
    label_rows, label_fields, "label_id", "canonical_label_name",
    "Fania", "LBL", 6,
    {"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

candidates = []
for path in TRACKLISTS:
    if not path.exists():
        raise SystemExit(f"Missing tracklist: {path}")
    for r in read_tsv(path):
        title = r["recording_title"]
        candidates.append({
            "unit_id":"UNIT-0102",
            "source_id":r.get("source_id","SRC0003"),
            "raw_artist":r.get("primary_artist",""),
            "raw_release":r.get("release_title",""),
            "raw_title":title,
            "canonical_recording_title":title,
            "canonical_song_title":title,
            "primary_performer":r.get("primary_artist",""),
            "label_name":"Fania",
            "track_position":r.get("track_position",""),
            "release_year":r.get("release_year",""),
            "evidence_source":str(path),
            "source_url":r.get("source_url",""),
            "evidence_status":r.get("evidence_status","source_verified"),
            "confidence":"high",
            "review_status":"candidate",
            "notes":"SRC0003 block 0003 source tracklist title",
        })

cand_fields = [
    "unit_id","source_id","raw_artist","raw_release","raw_title",
    "canonical_recording_title","canonical_song_title","primary_performer",
    "label_name","track_position","release_year","evidence_source","source_url",
    "evidence_status","confidence","review_status","notes"
]
write_tsv(IMPORT_DIR / "UNIT0102_SRC0003_BLOCK0003_CANDIDATES.tsv", cand_fields, candidates)

song_by_title = {norm(r.get("canonical_song_title","")): r for r in song_rows}

recording_keys = {
    (
        norm(r.get("canonical_recording_title","")),
        r.get("primary_performer_id",""),
        r.get("release_id",""),
        r.get("label_id",""),
        r.get("source_id",""),
    )
    for r in rec_rows
}

performer_cache = {}
release_cache = {}
performers_added = []
performers_reused = []
releases_added = []
releases_reused = []
songs_added = []
songs_reused = []
recordings_added = []
recordings_skipped = []

for c in candidates:
    performer_name = c["primary_performer"]
    pkey = norm(performer_name)
    if pkey not in performer_cache:
        performer_id, performer_added, performer_row = ensure(
            perf_rows, perf_fields, "performer_id", "canonical_performer_name",
            performer_name, "PER", 6,
            {"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
        )
        performer_cache[pkey] = performer_id
        if performer_added:
            performers_added.append(performer_row)
        else:
            performers_reused.append(performer_row)
    else:
        performer_id = performer_cache[pkey]

    release_title = c["raw_release"]
    rkey = (norm(release_title), performer_id)
    if rkey not in release_cache:
        release_id, release_added, release_row = ensure(
            rel_rows, rel_fields, "release_id", "canonical_release_title",
            release_title, "REL", 6,
            {
                "release_year":c.get("release_year",""),
                "label_id":label_id,
                "primary_performer_id":performer_id,
                "source_id":"SRC0003",
                "confidence":"high",
                "review_status":"approved",
                "created_at":TODAY,
                "updated_at":TODAY,
            }
        )
        release_cache[rkey] = release_id
        if release_added:
            releases_added.append(release_row)
        else:
            releases_reused.append(release_row)
    else:
        release_id = release_cache[rkey]

    title = c["canonical_recording_title"]
    nt = norm(title)

    if nt in song_by_title:
        song_id = song_by_title[nt]["song_id"]
        songs_reused.append(song_by_title[nt])
    else:
        song_id = next_id(song_rows, "song_id", "SONG", 6)
        s = {k:"" for k in song_fields}
        s["song_id"] = song_id
        s["canonical_song_title"] = title
        if "source_id" in s: s["source_id"] = "SRC0003"
        if "confidence" in s: s["confidence"] = "high"
        if "review_status" in s: s["review_status"] = "approved_title_candidate"
        if "created_at" in s: s["created_at"] = TODAY
        if "updated_at" in s: s["updated_at"] = TODAY
        song_rows.append(s)
        song_by_title[nt] = s
        songs_added.append(s)

    rec_key = (nt, performer_id, release_id, label_id, "SRC0003")
    if rec_key in recording_keys:
        recordings_skipped.append(c)
        continue

    rid = next_id(rec_rows, "recording_id", "REC", 6)
    rr = {k:"" for k in rec_fields}
    rr["recording_id"] = rid
    rr["canonical_recording_title"] = title
    if "canonical_song_id" in rr: rr["canonical_song_id"] = song_id
    if "primary_performer_id" in rr: rr["primary_performer_id"] = performer_id
    if "release_id" in rr: rr["release_id"] = release_id
    if "label_id" in rr: rr["label_id"] = label_id
    if "recording_year" in rr: rr["recording_year"] = c.get("release_year","")
    if "source_id" in rr: rr["source_id"] = "SRC0003"
    if "confidence" in rr: rr["confidence"] = "high"
    if "review_status" in rr: rr["review_status"] = "approved"
    if "created_at" in rr: rr["created_at"] = TODAY
    if "updated_at" in rr: rr["updated_at"] = TODAY
    rec_rows.append(rr)
    recording_keys.add(rec_key)
    recordings_added.append(rr)

write_tsv(REC, rec_fields, rec_rows)
write_tsv(SONG, song_fields, song_rows)
write_tsv(PERF, perf_fields, perf_rows)
write_tsv(REL, rel_fields, rel_rows)
write_tsv(LABEL, label_fields, label_rows)

write_tsv(STAGING / "UNIT0102_RECORDINGS_ADDED.tsv", rec_fields, recordings_added)
write_tsv(STAGING / "UNIT0102_RECORDINGS_SKIPPED.tsv", cand_fields, recordings_skipped)
write_tsv(STAGING / "UNIT0102_SONGS_ADDED.tsv", song_fields, songs_added)
write_tsv(STAGING / "UNIT0102_SONGS_REUSED.tsv", song_fields, songs_reused)
write_tsv(STAGING / "UNIT0102_RELEASES_ADDED.tsv", rel_fields, releases_added)
write_tsv(STAGING / "UNIT0102_RELEASES_REUSED.tsv", rel_fields, releases_reused)
write_tsv(STAGING / "UNIT0102_PERFORMERS_ADDED.tsv", perf_fields, performers_added)
write_tsv(STAGING / "UNIT0102_PERFORMERS_REUSED.tsv", perf_fields, performers_reused)

with (REPORT_DIR / "UNIT0102_SRC0003_BLOCK0003_PROMOTION_REPORT.md").open("w", encoding="utf-8") as f:
    f.write("# UNIT-0102 — SRC0003 Block 0003 Promotion Report\n\n")
    f.write("Project: MUSIC_RELATIONSHIPS_DB\n")
    f.write("Unit: UNIT-0102\n\n")
    f.write("## Scope\n\n")
    f.write("- Ray Barretto — Acid\n")
    f.write("- Larry Harlow — Salsa\n\n")
    f.write("## Totals\n\n")
    f.write(f"- Candidate recordings: {len(candidates)}\n")
    f.write(f"- Recordings added: {len(recordings_added)}\n")
    f.write(f"- Recordings skipped: {len(recordings_skipped)}\n")
    f.write(f"- Songs added: {len(songs_added)}\n")
    f.write(f"- Songs reused: {len(songs_reused)}\n")
    f.write(f"- Performers added: {len(performers_added)}\n")
    f.write(f"- Performers reused: {len(performers_reused)}\n")
    f.write(f"- Releases added: {len(releases_added)}\n")
    f.write(f"- Releases reused: {len(releases_reused)}\n")
    f.write(f"- Label added: {1 if label_added else 0}\n\n")
    f.write("## Added Recordings\n\n")
    for r in recordings_added:
        f.write(f"- {r['recording_id']} — {r['canonical_recording_title']}\n")

print("candidate_recordings", len(candidates))
print("recordings_added", len(recordings_added))
print("recordings_skipped", len(recordings_skipped))
print("songs_added", len(songs_added))
print("songs_reused", len(songs_reused))
print("performers_added", len(performers_added))
print("performers_reused", len(performers_reused))
print("releases_added", len(releases_added))
print("releases_reused", len(releases_reused))
print("label_added", label_added)
