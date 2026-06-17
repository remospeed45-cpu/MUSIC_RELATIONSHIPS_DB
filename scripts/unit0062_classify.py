import csv
import re
import unicodedata
from collections import OrderedDict


BATCH = "src0002_batch0003"
SOURCE_ID = "SRC0002"
LABEL_ID = "LBL000004"


def read_tsv(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore"
        )
        writer.writeheader()
        writer.writerows(rows)


def norm(value, drop_leading_article=False):
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.lower().strip()
    if drop_leading_article:
        value = re.sub(r"^(la|el|los|las)\s+", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def next_id(rows, id_field, prefix, width):
    current = 0
    for row in rows:
        value = row.get(id_field, "")
        if value.startswith(prefix):
            try:
                current = max(current, int(value[len(prefix) :]))
            except ValueError:
                pass
    current += 1
    while True:
        yield f"{prefix}{current:0{width}d}"
        current += 1


def first_by_key(rows, key):
    out = OrderedDict()
    for row in rows:
        out.setdefault(row[key], row)
    return out


recordings = read_tsv(f"authority/staging/{BATCH}_recordings.tsv")
songs = read_tsv(f"authority/staging/{BATCH}_songs.tsv")
artists = read_tsv(f"authority/staging/{BATCH}_artist_candidates.tsv")
rec_song = read_tsv(f"relationships/staging/{BATCH}_recording_song.tsv")
rec_artist = read_tsv(f"relationships/staging/{BATCH}_recording_artist_candidate.tsv")

master_groups = read_tsv("authority/groups/groups_master.tsv")
master_performers = read_tsv("authority/performers/performers_master.tsv")
master_songs = read_tsv("authority/songs/songs_master.tsv")
master_recordings = read_tsv("authority/recordings/recordings_master.tsv")
master_releases = read_tsv("authority/releases/releases_master.tsv")

group_by_name = {
    norm(row["canonical_group_name"], drop_leading_article=True): row
    for row in master_groups
}
performer_by_name = {
    norm(row["canonical_performer_name"], drop_leading_article=True): row
    for row in master_performers
}
song_by_title = {
    norm(row["canonical_song_title"]): row
    for row in master_songs
}
release_by_title = {
    norm(row["canonical_release_title"]): row
    for row in master_releases
}

group_rows_by_id = {row["group_id"]: row for row in master_groups}
performer_rows_by_id = {row["performer_id"]: row for row in master_performers}

artist_promotion = []
artist_map = {}
new_group_ids = next_id(master_groups, "group_id", "GRP", 4)

for artist in artists:
    raw_name = artist["raw_artist_text"]
    key = norm(raw_name, drop_leading_article=True)
    group_match = group_by_name.get(key)
    performer_match = performer_by_name.get(key)
    row = dict(artist)
    row["matched_entity_type"] = ""
    row["master_artist_id"] = ""
    row["promotion_status"] = "REVIEW_REQUIRED"
    row["match_basis"] = "artist_candidate_requires_review"

    if group_match:
        row["promotion_status"] = "MATCH_EXISTING"
        row["master_artist_id"] = group_match["group_id"]
        row["matched_entity_type"] = "group"
        row["match_basis"] = "normalized_group_name"
        artist_map[artist["artist_candidate_id"]] = group_match["group_id"]
    elif performer_match:
        row["promotion_status"] = "MATCH_EXISTING"
        row["master_artist_id"] = performer_match["performer_id"]
        row["matched_entity_type"] = "performer"
        row["match_basis"] = "normalized_performer_name"
        artist_map[artist["artist_candidate_id"]] = performer_match["performer_id"]
    elif artist["candidate_artist_type"] == "group_candidate":
        new_id = next(new_group_ids)
        row["promotion_status"] = "NEW"
        row["master_artist_id"] = new_id
        row["matched_entity_type"] = "group"
        row["match_basis"] = "new_group_candidate"
        artist_map[artist["artist_candidate_id"]] = new_id

    artist_promotion.append(row)

song_promotion = []
song_map = {}
new_song_ids = next_id(master_songs, "song_id", "SONG", 6)
batch_song_by_title = {}

for song in songs:
    title_key = norm(song["canonical_song_title_candidate"])
    row = dict(song)
    row["master_song_id"] = ""
    row["promotion_status"] = "NEW"
    row["match_basis"] = "new_song_title"

    if title_key in song_by_title:
        row["promotion_status"] = "MATCH_EXISTING"
        row["master_song_id"] = song_by_title[title_key]["song_id"]
        row["match_basis"] = "normalized_song_title"
    elif title_key in batch_song_by_title:
        row["promotion_status"] = "MATCH_EXISTING"
        row["master_song_id"] = batch_song_by_title[title_key]
        row["match_basis"] = "same_batch_song_title"
    else:
        row["master_song_id"] = next(new_song_ids)
        batch_song_by_title[title_key] = row["master_song_id"]

    song_map[song["batch_song_id"]] = row["master_song_id"]
    song_promotion.append(row)

release_map = {}
new_release_ids = next_id(master_releases, "release_id", "REL", 6)
for release_candidate_id, recording in first_by_key(recordings, "release_candidate_id").items():
    release_key = norm(recording["release_title"])
    if release_key in release_by_title:
        release_map[release_candidate_id] = release_by_title[release_key]["release_id"]
    else:
        release_map[release_candidate_id] = next(new_release_ids)

song_for_recording = {
    row["batch_recording_id"]: song_map[row["batch_song_id"]]
    for row in rec_song
}
artists_for_recording = {}
for row in rec_artist:
    artists_for_recording.setdefault(row["batch_recording_id"], []).append(
        artist_map.get(row["artist_candidate_id"], "")
    )

recording_by_title_artist = {}
for recording in master_recordings:
    title = norm(recording["canonical_recording_title"])
    primary_artist_id = recording["primary_group_id"] or recording["primary_performer_id"]
    if primary_artist_id:
        recording_by_title_artist[(title, primary_artist_id)] = recording

recording_promotion = []
recording_map = {}
new_recording_ids = next_id(master_recordings, "recording_id", "REC", 6)

for recording in recordings:
    title_key = norm(recording["recording_title"])
    promoted_artists = [
        artist_id
        for artist_id in artists_for_recording.get(recording["batch_recording_id"], [])
        if artist_id
    ]
    match = None
    for artist_id in promoted_artists:
        match = recording_by_title_artist.get((title_key, artist_id))
        if match:
            break

    primary_group_id = next(
        (artist_id for artist_id in promoted_artists if artist_id.startswith("GRP")), ""
    )
    primary_performer_id = ""
    if not primary_group_id:
        primary_performer_id = next(
            (artist_id for artist_id in promoted_artists if artist_id.startswith("PER")), ""
        )

    row = dict(recording)
    row["master_recording_id"] = ""
    row["canonical_song_id"] = song_for_recording[recording["batch_recording_id"]]
    row["release_id"] = release_map[recording["release_candidate_id"]]
    row["label_id"] = LABEL_ID
    row["primary_group_id"] = primary_group_id
    row["primary_performer_id"] = primary_performer_id
    row["promotion_status"] = "NEW"
    row["match_basis"] = "no_exact_title_artist_match"

    if match:
        row["promotion_status"] = "MATCH_EXISTING"
        row["master_recording_id"] = match["recording_id"]
        row["match_basis"] = "normalized_title_primary_artist"
    else:
        row["master_recording_id"] = next(new_recording_ids)

    recording_map[recording["batch_recording_id"]] = row["master_recording_id"]
    recording_promotion.append(row)

write_tsv(
    f"authority/staging/{BATCH}_artist_promotion.tsv",
    artist_promotion,
    [
        "artist_candidate_id",
        "source_id",
        "source_name",
        "source_url",
        "raw_artist_text",
        "candidate_artist_type",
        "promotion_status",
        "matched_entity_type",
        "master_artist_id",
        "match_basis",
        "release_candidate_id",
        "release_title",
        "source_reference",
        "evidence_text",
        "confidence",
        "review_status",
    ],
)

write_tsv(
    f"authority/staging/{BATCH}_song_promotion.tsv",
    song_promotion,
    [
        "batch_song_id",
        "promotion_status",
        "master_song_id",
        "canonical_song_title_candidate",
        "match_basis",
        "source_id",
        "source_name",
        "source_url",
        "release_candidate_id",
        "release_title",
        "side",
        "track_number",
        "source_reference",
        "evidence_text",
        "confidence",
        "review_status",
    ],
)

write_tsv(
    f"authority/staging/{BATCH}_recording_promotion.tsv",
    recording_promotion,
    [
        "batch_recording_id",
        "promotion_status",
        "master_recording_id",
        "recording_title",
        "canonical_song_id",
        "primary_group_id",
        "primary_performer_id",
        "release_id",
        "label_id",
        "match_basis",
        "source_id",
        "source_name",
        "source_url",
        "release_candidate_id",
        "release_title",
        "release_interpreter",
        "release_genre",
        "release_format",
        "release_year",
        "reference_number",
        "side",
        "track_number",
        "global_track_number",
        "raw_track_title",
        "artist_text",
        "source_reference",
        "evidence_text",
        "confidence",
        "review_status",
    ],
)

print(
    "Promotion staging regenerated: "
    f"{len(recording_promotion)} recordings, "
    f"{len(song_promotion)} songs, "
    f"{len(artist_promotion)} artist candidates"
)
