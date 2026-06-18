#!/usr/bin/env python3
from pathlib import Path
import csv, re, unicodedata
from datetime import date

TODAY = date.today().isoformat()

REC = Path("authority/recordings/recordings_master.tsv")
SONG = Path("authority/songs/songs_master.tsv")
AUDIT = Path("authority/staging/unit0096/UNIT0096_LA_VOZ_ROBUST_AUDIT.tsv")
STAGING = Path("authority/staging/unit0097")
REPORT = Path("reports/unit0097/UNIT0097_LA_VOZ_CORRECTION_REPORT.md")
STAGING.mkdir(parents=True, exist_ok=True)

def norm(s):
    s=''.join(c for c in unicodedata.normalize("NFD", s or "") if unicodedata.category(c)!="Mn")
    s=re.sub(r"[^a-z0-9]+"," ",s.lower()).strip()
    return re.sub(r"\s+"," ",s)

def read(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))

def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as f:
        w=csv.DictWriter(f, delimiter="\t", fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

rec_rows = read(REC)
song_rows = read(SONG)
audit_rows = read(AUDIT)
rec_fields = list(rec_rows[0].keys())
song_fields = list(song_rows[0].keys())

release_id = None
performer_id = None
label_id = None

# Detect from La Voz promoted rows
for r in rec_rows:
    if norm(r.get("canonical_recording_title","")) == "el todopoderoso" and r.get("source_id") == "SRC0003":
        release_id = r.get("release_id","")
        performer_id = r.get("primary_performer_id","")
        label_id = r.get("label_id","")
        break

if not release_id:
    raise SystemExit("Could not detect La Voz release_id from El Todopoderoso")

remove_titles = [r["title"] for r in audit_rows if r["status"] == "REMOVE"]
add_titles = [r["title"] for r in audit_rows if r["status"] == "ADD"]

remove_norm = {norm(x) for x in remove_titles}
add_norm = {norm(x): x for x in add_titles}

removed_rows = []
kept_rows = []

for r in rec_rows:
    if r.get("release_id","") == release_id and norm(r.get("canonical_recording_title","")) in remove_norm:
        removed_rows.append(r)
    else:
        kept_rows.append(r)

song_by_norm = {norm(r.get("canonical_song_title","")): r for r in song_rows}
song_added = []
rec_added = []

def next_id(rows, field, prefix, width):
    nums=[]
    for r in rows:
        v=r.get(field,"")
        if v.startswith(prefix):
            try:
                nums.append(int(v.replace(prefix,"")))
            except:
                pass
    return f"{prefix}{max(nums or [0])+1:0{width}d}"

existing_rec_keys = {
    (norm(r.get("canonical_recording_title","")), r.get("primary_performer_id",""), r.get("release_id",""), r.get("label_id",""), r.get("source_id",""))
    for r in kept_rows
}

for nt, title in add_norm.items():
    if nt in song_by_norm:
        song_id = song_by_norm[nt]["song_id"]
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
        song_by_norm[nt] = s
        song_added.append(s)

    key = (nt, performer_id, release_id, label_id, "SRC0003")
    if key in existing_rec_keys:
        continue

    rid = next_id(kept_rows, "recording_id", "REC", 6)
    r = {k:"" for k in rec_fields}
    r["recording_id"] = rid
    r["canonical_recording_title"] = title
    if "canonical_song_id" in r: r["canonical_song_id"] = song_id
    if "primary_performer_id" in r: r["primary_performer_id"] = performer_id
    if "release_id" in r: r["release_id"] = release_id
    if "label_id" in r: r["label_id"] = label_id
    if "source_id" in r: r["source_id"] = "SRC0003"
    if "confidence" in r: r["confidence"] = "high"
    if "review_status" in r: r["review_status"] = "approved"
    if "created_at" in r: r["created_at"] = TODAY
    if "updated_at" in r: r["updated_at"] = TODAY
    kept_rows.append(r)
    existing_rec_keys.add(key)
    rec_added.append(r)

write(REC, rec_fields, kept_rows)
write(SONG, song_fields, song_rows)

write(STAGING/"UNIT0097_LA_VOZ_RECORDINGS_REMOVED.tsv", rec_fields, removed_rows)
write(STAGING/"UNIT0097_LA_VOZ_RECORDINGS_ADDED.tsv", rec_fields, rec_added)
write(STAGING/"UNIT0097_LA_VOZ_SONGS_ADDED.tsv", song_fields, song_added)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# UNIT-0097 — La Voz Master Correction Report\n\n")
    f.write("Project: MUSIC_RELATIONSHIPS_DB\n")
    f.write("Unit: UNIT-0097\n\n")
    f.write("## Action\n\n")
    f.write("Corrected UNIT-0094 La Voz promotion using UNIT-0096 robust audit.\n\n")
    f.write("## Removed Incorrect Recordings\n\n")
    for r in removed_rows:
        f.write(f"- {r['recording_id']} — {r['canonical_recording_title']}\n")
    f.write("\n## Added Correct Recordings\n\n")
    for r in rec_added:
        f.write(f"- {r['recording_id']} — {r['canonical_recording_title']} ↔ Héctor Lavoe ↔ La Voz ↔ Fania ↔ SRC0003\n")
    f.write("\n## Totals\n\n")
    f.write(f"- Recordings removed: {len(removed_rows)}\n")
    f.write(f"- Recordings added: {len(rec_added)}\n")
    f.write(f"- Songs added: {len(song_added)}\n")

print("release_id", release_id)
print("performer_id", performer_id)
print("label_id", label_id)
print("recordings_removed", len(removed_rows))
print("recordings_added", len(rec_added))
print("songs_added", len(song_added))
