#!/usr/bin/env python3
from pathlib import Path
import csv, re, unicodedata
from datetime import date

TODAY = date.today().isoformat()
ROOT = Path(".")

CAND = ROOT / "imports/unit0094_hector_lavoe_la_voz/UNIT0094_HECTOR_LAVOE_LA_VOZ_TITLE_CANDIDATES.tsv"

REC_MASTER = ROOT / "authority/recordings/recordings_master.tsv"
SONG_MASTER = ROOT / "authority/songs/songs_master.tsv"
PERF_MASTER = ROOT / "authority/performers/performers_master.tsv"
RELEASE_MASTER = ROOT / "authority/releases/releases_master.tsv"
LABEL_MASTER = ROOT / "authority/labels/labels_master.tsv"

BACKUP_DIR = ROOT / "authority/backups/unit0094"
STAGING_DIR = ROOT / "authority/staging/unit0094"
REPORT_DIR = ROOT / "reports/unit0094"

for d in [BACKUP_DIR, STAGING_DIR, REPORT_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

def write_tsv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def norm(s):
    s = ''.join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return re.sub(r"\s+", " ", s)

def next_id(rows, field, prefix, width):
    nums = []
    for r in rows:
        v = r.get(field, "")
        if v.startswith(prefix):
            try:
                nums.append(int(v.replace(prefix, "")))
            except Exception:
                pass
    return f"{prefix}{max(nums or [0]) + 1:0{width}d}"

def ensure_entity(rows, fields, id_field, name_field, name, prefix, width, defaults):
    nn = norm(name)
    for r in rows:
        if norm(r.get(name_field, "")) == nn:
            return r[id_field], False
    nid = next_id(rows, id_field, prefix, width)
    row = {k:"" for k in fields}
    row[id_field] = nid
    row[name_field] = name
    for k,v in defaults.items():
        if k in row:
            row[k] = v
    rows.append(row)
    return nid, True

for p in [REC_MASTER, SONG_MASTER, PERF_MASTER, RELEASE_MASTER, LABEL_MASTER]:
    (BACKUP_DIR / f"{p.name}.before_unit0094.tsv").write_text(p.read_text(encoding="utf-8"), encoding="utf-8")

cands = read_tsv(CAND)
rec_rows = read_tsv(REC_MASTER)
song_rows = read_tsv(SONG_MASTER)
perf_rows = read_tsv(PERF_MASTER)
release_rows = read_tsv(RELEASE_MASTER)
label_rows = read_tsv(LABEL_MASTER)

rec_fields = list(rec_rows[0].keys())
song_fields = list(song_rows[0].keys())
perf_fields = list(perf_rows[0].keys())
release_fields = list(release_rows[0].keys())
label_fields = list(label_rows[0].keys())

performer_id, performer_added = ensure_entity(
    perf_rows, perf_fields, "performer_id", "canonical_performer_name",
    "Héctor Lavoe", "PER", 6,
    {"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

label_id, label_added = ensure_entity(
    label_rows, label_fields, "label_id", "canonical_label_name",
    "Fania", "LBL", 6,
    {"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

release_id, release_added = ensure_entity(
    release_rows, release_fields, "release_id", "canonical_release_title",
    "La Voz", "REL", 6,
    {"primary_performer_id":performer_id,"label_id":label_id,"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

song_by_title = {norm(r.get("canonical_song_title","")): r for r in song_rows}
rec_keys = set(
    (
        norm(r.get("canonical_recording_title","")),
        r.get("primary_performer_id",""),
        r.get("release_id",""),
        r.get("label_id",""),
        r.get("source_id",""),
    )
    for r in rec_rows
)

songs_added = []
recs_added = []
recs_skipped = []

for c in cands:
    title = c["canonical_recording_title"]
    nt = norm(title)

    if nt in song_by_title:
        song_id = song_by_title[nt]["song_id"]
    else:
        song_id = next_id(song_rows, "song_id", "SONG", 6)
        srow = {k:"" for k in song_fields}
        srow["song_id"] = song_id
        srow["canonical_song_title"] = title
        if "source_id" in srow: srow["source_id"] = "SRC0003"
        if "confidence" in srow: srow["confidence"] = c.get("confidence", "medium")
        if "review_status" in srow: srow["review_status"] = "approved_title_candidate"
        if "created_at" in srow: srow["created_at"] = TODAY
        if "updated_at" in srow: srow["updated_at"] = TODAY
        song_rows.append(srow)
        song_by_title[nt] = srow
        songs_added.append(srow)

    key = (nt, performer_id, release_id, label_id, "SRC0003")
    if key in rec_keys:
        recs_skipped.append(title)
        continue

    rid = next_id(rec_rows, "recording_id", "REC", 6)
    rrow = {k:"" for k in rec_fields}
    rrow["recording_id"] = rid
    rrow["canonical_recording_title"] = title
    if "canonical_song_id" in rrow: rrow["canonical_song_id"] = song_id
    if "primary_performer_id" in rrow: rrow["primary_performer_id"] = performer_id
    if "release_id" in rrow: rrow["release_id"] = release_id
    if "label_id" in rrow: rrow["label_id"] = label_id
    if "source_id" in rrow: rrow["source_id"] = "SRC0003"
    if "confidence" in rrow: rrow["confidence"] = c.get("confidence", "medium")
    if "review_status" in rrow: rrow["review_status"] = "approved"
    if "created_at" in rrow: rrow["created_at"] = TODAY
    if "updated_at" in rrow: rrow["updated_at"] = TODAY
    rec_rows.append(rrow)
    rec_keys.add(key)
    recs_added.append(rrow)

write_tsv(REC_MASTER, rec_fields, rec_rows)
write_tsv(SONG_MASTER, song_fields, song_rows)
write_tsv(PERF_MASTER, perf_fields, perf_rows)
write_tsv(RELEASE_MASTER, release_fields, release_rows)
write_tsv(LABEL_MASTER, label_fields, label_rows)

write_tsv(STAGING_DIR / "UNIT0094_SONGS_ADDED.tsv", song_fields, songs_added)
write_tsv(STAGING_DIR / "UNIT0094_RECORDINGS_ADDED.tsv", rec_fields, recs_added)

with (REPORT_DIR / "UNIT0090_PROMOTION_REPORT.md").open("w", encoding="utf-8") as fh:
    fh.write("# UNIT-0094 Promotion Report\n\n")
    fh.write("Project: MUSIC_RELATIONSHIPS_DB\n")
    fh.write("Unit: UNIT-0094\n")
    fh.write("Target: Héctor Lavoe / La Voz relationships\n\n")
    fh.write("## Totals\n\n")
    fh.write(f"- Candidates: {len(cands)}\n")
    fh.write(f"- Songs added: {len(songs_added)}\n")
    fh.write(f"- Recordings added: {len(recs_added)}\n")
    fh.write(f"- Recordings skipped: {len(recs_skipped)}\n")
    fh.write(f"- Performer added: {1 if performer_added else 0}\n")
    fh.write(f"- Release added: {1 if release_added else 0}\n")
    fh.write(f"- Label added: {1 if label_added else 0}\n\n")
    fh.write("## Added Recordings\n\n")
    for r in recs_added:
        fh.write(f"- {r['recording_id']} — {r['canonical_recording_title']} ↔ Héctor Lavoe ↔ La Voz ↔ Fania ↔ SRC0003\n")

print("songs_added", len(songs_added))
print("recordings_added", len(recs_added))
print("recordings_skipped", len(recs_skipped))
print("performer_added", performer_added)
print("release_added", release_added)
print("label_added", label_added)
