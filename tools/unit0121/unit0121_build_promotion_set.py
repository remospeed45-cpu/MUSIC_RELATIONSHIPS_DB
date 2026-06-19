#!/usr/bin/env python3
import csv
from pathlib import Path

SRC = Path("authority/staging/unit0120/UNIT0120_PROMOTION_CANDIDATES.tsv")

SONGS = Path("authority/songs/songs_master.tsv")
RECS = Path("authority/recordings/recordings_master.tsv")

OUT_SONGS = Path("authority/staging/unit0121/UNIT0121_SONG_PROMOTION_CANDIDATES.tsv")
OUT_RECS = Path("authority/staging/unit0121/UNIT0121_RECORDING_PROMOTION_CANDIDATES.tsv")

REPORT = Path("reports/unit0121/UNIT0121_PROMOTION_SET_REPORT.md")

def read_tsv(path):
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))

rows = read_tsv(SRC)
songs = read_tsv(SONGS)
recs = read_tsv(RECS)

existing_song_titles = {
    (r.get("canonical_song_title") or "").strip().lower()
    for r in songs
}

existing_recording_titles = {
    (r.get("canonical_recording_title") or "").strip().lower()
    for r in recs
}

song_candidates = []
recording_candidates = []

song_seq = len(songs) + 1
rec_seq = len(recs) + 1

for r in rows:

    title = (r.get("final_candidate_title") or "").strip()

    if not title:
        continue

    norm = title.lower()

    if norm not in existing_song_titles:

        song_id = f"SONG{song_seq:06d}"

        song_candidates.append({
            "song_id": song_id,
            "canonical_song_title": title,
            "alternate_titles": "",
            "composer": "",
            "lyricist": "",
            "country": "",
            "language": "Spanish",
            "source_id": "SRC0002",
            "confidence": "medium",
            "review_status": "approved",
            "created_at": "2026-06-19",
            "updated_at": "2026-06-19",
        })

        existing_song_titles.add(norm)
        song_seq += 1

    if norm not in existing_recording_titles:

        recording_candidates.append({
            "recording_id": f"REC{rec_seq:06d}",
            "canonical_recording_title": title,
            "canonical_song_id": "",
            "primary_group_id": r.get("final_group_id",""),
            "primary_performer_id": r.get("final_performer_id",""),
            "recording_genre_id": "",
            "release_id": "",
            "label_id": "",
            "recording_year": "",
            "country": "",
            "language": "Spanish",
            "source_id": "SRC0002",
            "confidence": "medium",
            "review_status": "approved",
            "created_at": "2026-06-19",
            "updated_at": "2026-06-19",
        })

        existing_recording_titles.add(norm)
        rec_seq += 1

song_fields = [
    "song_id","canonical_song_title","alternate_titles","composer",
    "lyricist","country","language","source_id","confidence",
    "review_status","created_at","updated_at"
]

rec_fields = [
    "recording_id","canonical_recording_title","canonical_song_id",
    "primary_group_id","primary_performer_id","recording_genre_id",
    "release_id","label_id","recording_year","country","language",
    "source_id","confidence","review_status","created_at","updated_at"
]

for path,data,fields in [
    (OUT_SONGS,song_candidates,song_fields),
    (OUT_RECS,recording_candidates,rec_fields),
]:
    with path.open("w",newline="",encoding="utf-8") as fh:
        w = csv.DictWriter(fh,delimiter="\t",fieldnames=fields,lineterminator="\n")
        w.writeheader()
        w.writerows(data)

with REPORT.open("w",encoding="utf-8") as fh:
    fh.write(f"song_candidates\t{len(song_candidates)}\n")
    fh.write(f"recording_candidates\t{len(recording_candidates)}\n")

print("song_candidates", len(song_candidates))
print("recording_candidates", len(recording_candidates))
