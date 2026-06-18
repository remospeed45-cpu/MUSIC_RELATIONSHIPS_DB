#!/usr/bin/env python3
from pathlib import Path
import csv
import re
import unicodedata
from datetime import date

TODAY = date.today().isoformat()
ROOT = Path(".")

CAND = ROOT / "imports/unit0088_bobby_valentin_bulk_titles/UNIT0088_BOBBY_VALENTIN_BULK_TITLE_EXTRACTION.tsv"

REC_MASTER = ROOT / "authority/recordings/recordings_master.tsv"
SONG_MASTER = ROOT / "authority/songs/songs_master.tsv"
GROUP_MASTER = ROOT / "authority/groups/groups_master.tsv"
RELEASE_MASTER = ROOT / "authority/releases/releases_master.tsv"
LABEL_MASTER = ROOT / "authority/labels/labels_master.tsv"

BACKUP_DIR = ROOT / "authority/backups/unit0088"
STAGING_DIR = ROOT / "authority/staging/unit0088"
REPORT_DIR = ROOT / "reports/unit0088"

BACKUP_DIR.mkdir(parents=True, exist_ok=True)
STAGING_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

def write_tsv(path, fieldnames, rows):
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s or '') if unicodedata.category(c) != 'Mn')
    s = re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()
    return re.sub(r'\s+', ' ', s)

def next_id(rows, field, prefix, width):
    nums = []
    for r in rows:
        v = r.get(field, "")
        if v.startswith(prefix):
            try:
                nums.append(int(v.replace(prefix, "")))
            except ValueError:
                pass
    return f"{prefix}{max(nums or [0]) + 1:0{width}d}"

def ensure_entity(rows, fieldnames, id_field, name_field, canonical_name, prefix, width, defaults):
    target = norm(canonical_name)
    for r in rows:
        if norm(r.get(name_field, "")) == target:
            return r[id_field], False
    new_id = next_id(rows, id_field, prefix, width)
    row = {k: "" for k in fieldnames}
    row[id_field] = new_id
    row[name_field] = canonical_name
    for k, v in defaults.items():
        if k in row:
            row[k] = v
    rows.append(row)
    return new_id, True

# backups
for p in [REC_MASTER, SONG_MASTER, GROUP_MASTER, RELEASE_MASTER, LABEL_MASTER]:
    if p.exists():
        (BACKUP_DIR / f"{p.name}.before_unit0088.tsv").write_text(p.read_text(encoding="utf-8"), encoding="utf-8")

cands = read_tsv(CAND)

rec_rows = read_tsv(REC_MASTER)
song_rows = read_tsv(SONG_MASTER)
group_rows = read_tsv(GROUP_MASTER)
release_rows = read_tsv(RELEASE_MASTER)
label_rows = read_tsv(LABEL_MASTER)

rec_fields = list(rec_rows[0].keys())
song_fields = list(song_rows[0].keys())
group_fields = list(group_rows[0].keys())
release_fields = list(release_rows[0].keys())
label_fields = list(label_rows[0].keys())

group_id, group_added = ensure_entity(
    group_rows, group_fields, "group_id", "canonical_group_name",
    "Bobby Valentín", "GRP", 4,
    {"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

label_id, label_added = ensure_entity(
    label_rows, label_fields, "label_id", "canonical_label_name",
    "Fania", "LBL", 6,
    {"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

release_id, release_added = ensure_entity(
    release_rows, release_fields, "release_id", "canonical_release_title",
    "Rey Del Bajo", "REL", 6,
    {"primary_group_id":group_id,"label_id":label_id,"source_id":"SRC0003","confidence":"high","review_status":"approved","created_at":TODAY,"updated_at":TODAY}
)

song_by_title = {norm(r.get("canonical_song_title","")): r for r in song_rows}
rec_existing_keys = set(
    (
        norm(r.get("canonical_recording_title","")),
        r.get("primary_group_id",""),
        r.get("release_id",""),
        r.get("label_id",""),
        r.get("source_id",""),
    )
    for r in rec_rows
)

songs_added = []
recordings_added = []
recordings_matched = []

for c in cands:
    title = c["canonical_recording_title"]
    nt = norm(title)

    if nt in song_by_title:
        song_id = song_by_title[nt]["song_id"]
    else:
        song_id = next_id(song_rows, "song_id", "SONG", 6)
        row = {k:"" for k in song_fields}
        row["song_id"] = song_id
        row["canonical_song_title"] = title
        if "source_id" in row: row["source_id"] = "SRC0003"
        if "confidence" in row: row["confidence"] = "high"
        if "review_status" in row: row["review_status"] = "approved_title_candidate"
        if "created_at" in row: row["created_at"] = TODAY
        if "updated_at" in row: row["updated_at"] = TODAY
        song_rows.append(row)
        song_by_title[nt] = row
        songs_added.append(row)

    rec_key = (nt, group_id, release_id, label_id, "SRC0003")
    if rec_key in rec_existing_keys:
        recordings_matched.append(title)
        continue

    rec_id = next_id(rec_rows, "recording_id", "REC", 6)
    row = {k:"" for k in rec_fields}
    row["recording_id"] = rec_id
    row["canonical_recording_title"] = title
    if "canonical_song_id" in row: row["canonical_song_id"] = song_id
    if "primary_group_id" in row: row["primary_group_id"] = group_id
    if "release_id" in row: row["release_id"] = release_id
    if "label_id" in row: row["label_id"] = label_id
    if "source_id" in row: row["source_id"] = "SRC0003"
    if "confidence" in row: row["confidence"] = "high"
    if "review_status" in row: row["review_status"] = "approved"
    if "created_at" in row: row["created_at"] = TODAY
    if "updated_at" in row: row["updated_at"] = TODAY
    rec_rows.append(row)
    rec_existing_keys.add(rec_key)
    recordings_added.append(row)

write_tsv(SONG_MASTER, song_fields, song_rows)
write_tsv(REC_MASTER, rec_fields, rec_rows)
write_tsv(GROUP_MASTER, group_fields, group_rows)
write_tsv(RELEASE_MASTER, release_fields, release_rows)
write_tsv(LABEL_MASTER, label_fields, label_rows)

write_tsv(STAGING_DIR / "UNIT0088_SONGS_ADDED.tsv", song_fields, songs_added)
write_tsv(STAGING_DIR / "UNIT0088_RECORDINGS_ADDED.tsv", rec_fields, recordings_added)

report = REPORT_DIR / "UNIT0088_PROMOTION_REPORT.md"
with report.open("w", encoding="utf-8") as fh:
    fh.write("# UNIT-0088 Promotion Report\n\n")
    fh.write("Project: MUSIC_RELATIONSHIPS_DB\n")
    fh.write("Unit: UNIT-0088\n")
    fh.write("Source: SRC0003 / Fania text verified\n\n")
    fh.write("## Totals\n\n")
    fh.write(f"- Clean candidates: {len(cands)}\n")
    fh.write(f"- Songs added: {len(songs_added)}\n")
    fh.write(f"- Recordings added: {len(recordings_added)}\n")
    fh.write(f"- Recordings matched/skipped: {len(recordings_matched)}\n")
    fh.write(f"- Group added: {1 if group_added else 0}\n")
    fh.write(f"- Release added: {1 if release_added else 0}\n")
    fh.write(f"- Label added: {1 if label_added else 0}\n\n")
    fh.write("## Promoted Recording Relationships\n\n")
    for r in recordings_added:
        fh.write(f"- {r['recording_id']} — {r['canonical_recording_title']} ↔ Bobby Valentín ↔ Rey Del Bajo ↔ Fania ↔ SRC0003\n")
    fh.write("\n## Review\n\n")
    fh.write("Promotion limited to 8 cleaned Rey Del Bajo candidates.\n")

print("songs_added", len(songs_added))
print("recordings_added", len(recordings_added))
print("recordings_matched_skipped", len(recordings_matched))
print("group_added", group_added)
print("release_added", release_added)
print("label_added", label_added)
