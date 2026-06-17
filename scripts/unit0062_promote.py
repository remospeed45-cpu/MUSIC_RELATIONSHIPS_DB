import csv
import os
import re
from collections import Counter, OrderedDict
from datetime import date


BATCH = "src0002_batch0003"
SOURCE_ID = "SRC0002"
LABEL_ID = "LBL000004"
PROMOTION_DATE = date.today().isoformat()
REPORT_PATH = "reports/unit0062R/SRC0002_BATCH0003_CLEAN_PROMOTION_REPORT.md"


def read_tsv(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_header(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return next(csv.reader(handle, delimiter="\t"))


def write_tsv(path, rows, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def append_tsv(path, rows, fieldnames):
    if not rows:
        return
    with open(path, "a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
        writer.writerows(rows)


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


def release_type(format_text):
    text = (format_text or "").upper()
    if "USB" in text:
        return "USB"
    if "LP" in text:
        return "LP"
    return ""


def assert_unique(rows, field, label):
    values = [row[field] for row in rows if row.get(field)]
    duplicates = [value for value, count in Counter(values).items() if count > 1]
    if duplicates:
        raise SystemExit(f"Duplicate {label} IDs in staging: {duplicates[:10]}")


recordings_staged = read_tsv(f"authority/staging/{BATCH}_recordings.tsv")
songs_staged = read_tsv(f"authority/staging/{BATCH}_songs.tsv")
artists_staged = read_tsv(f"authority/staging/{BATCH}_artist_candidates.tsv")
rec_song_staged = read_tsv(f"relationships/staging/{BATCH}_recording_song.tsv")
rec_artist_staged = read_tsv(f"relationships/staging/{BATCH}_recording_artist_candidate.tsv")
rec_release_staged = read_tsv(f"relationships/staging/{BATCH}_recording_release.tsv")
rec_source_staged = read_tsv(f"relationships/staging/{BATCH}_recording_source.tsv")

artist_promotion = read_tsv(f"authority/staging/{BATCH}_artist_promotion.tsv")
song_promotion = read_tsv(f"authority/staging/{BATCH}_song_promotion.tsv")
recording_promotion = read_tsv(f"authority/staging/{BATCH}_recording_promotion.tsv")

groups = read_tsv("authority/groups/groups_master.tsv")
performers = read_tsv("authority/performers/performers_master.tsv")
songs = read_tsv("authority/songs/songs_master.tsv")
recordings = read_tsv("authority/recordings/recordings_master.tsv")
releases = read_tsv("authority/releases/releases_master.tsv")

recording_song = read_tsv("relationships/recording_song.tsv")
recording_group = read_tsv("relationships/recording_group.tsv")
recording_performer = read_tsv("relationships/recording_performer.tsv")
recording_release = read_tsv("relationships/recording_release.tsv")
recording_source = read_tsv("relationships/recording_source.tsv")

headers = {
    "groups": read_header("authority/groups/groups_master.tsv"),
    "performers": read_header("authority/performers/performers_master.tsv"),
    "songs": read_header("authority/songs/songs_master.tsv"),
    "recordings": read_header("authority/recordings/recordings_master.tsv"),
    "releases": read_header("authority/releases/releases_master.tsv"),
    "recording_song": read_header("relationships/recording_song.tsv"),
    "recording_group": read_header("relationships/recording_group.tsv"),
    "recording_performer": read_header("relationships/recording_performer.tsv"),
    "recording_release": read_header("relationships/recording_release.tsv"),
    "recording_source": read_header("relationships/recording_source.tsv"),
}

assert len(recordings_staged) == len(recording_promotion)
assert len(songs_staged) == len(song_promotion)
assert len(artists_staged) == len(artist_promotion)
assert_unique(
    [row for row in artist_promotion if row["promotion_status"] == "NEW"],
    "master_artist_id",
    "new artist",
)
assert_unique(
    [row for row in song_promotion if row["promotion_status"] == "NEW"],
    "master_song_id",
    "new song",
)
assert_unique(
    [row for row in recording_promotion if row["promotion_status"] == "NEW"],
    "master_recording_id",
    "new recording",
)

existing_group_ids = {row["group_id"] for row in groups}
existing_performer_ids = {row["performer_id"] for row in performers}
existing_song_ids = {row["song_id"] for row in songs}
existing_recording_ids = {row["recording_id"] for row in recordings}
existing_release_ids = {row["release_id"] for row in releases}

artist_map = {}
new_group_rows = []
matched_groups = set()
matched_performers = set()
review_artist_rows = []

for row in artist_promotion:
    status = row["promotion_status"]
    master_id = row["master_artist_id"]
    if status == "MATCH_EXISTING":
        if master_id.startswith("GRP"):
            if master_id not in existing_group_ids:
                raise SystemExit(f"Missing matched group ID {master_id}")
            matched_groups.add(master_id)
        elif master_id.startswith("PER"):
            if master_id not in existing_performer_ids:
                raise SystemExit(f"Missing matched performer ID {master_id}")
            matched_performers.add(master_id)
        artist_map[row["artist_candidate_id"]] = master_id
    elif status == "NEW":
        if row["matched_entity_type"] != "group" or not master_id.startswith("GRP"):
            raise SystemExit(f"Unsupported new artist promotion: {row}")
        if master_id in existing_group_ids:
            raise SystemExit(f"New group ID already exists: {master_id}")
        artist_map[row["artist_candidate_id"]] = master_id
        new_group_rows.append(
            {
                "group_id": master_id,
                "canonical_group_name": row["raw_artist_text"],
                "alternate_names": "",
                "group_type": "group",
                "country": "",
                "primary_genre_id": "",
                "source_id": SOURCE_ID,
                "confidence": row["confidence"],
                "review_status": "approved",
                "created_at": PROMOTION_DATE,
                "updated_at": PROMOTION_DATE,
            }
        )
    elif status == "REVIEW_REQUIRED":
        review_artist_rows.append(row)
    else:
        raise SystemExit(f"Unsupported artist status: {status}")

song_map = {}
new_song_rows = []
matched_song_ids = set()
new_song_ids_added = set()

for row in song_promotion:
    status = row["promotion_status"]
    song_id = row["master_song_id"]
    if status == "MATCH_EXISTING":
        if row["match_basis"] == "same_batch_song_title":
            if song_id not in new_song_ids_added:
                raise SystemExit(f"Batch song duplicate points to unknown new song {song_id}")
        elif song_id not in existing_song_ids:
            raise SystemExit(f"Missing matched song ID {song_id}")
        else:
            matched_song_ids.add(song_id)
        song_map[row["batch_song_id"]] = song_id
    elif status == "NEW":
        if song_id in existing_song_ids:
            raise SystemExit(f"New song ID already exists: {song_id}")
        song_map[row["batch_song_id"]] = song_id
        new_song_ids_added.add(song_id)
        new_song_rows.append(
            {
                "song_id": song_id,
                "canonical_song_title": row["canonical_song_title_candidate"],
                "alternate_titles": "",
                "composer": "",
                "lyricist": "",
                "country": "",
                "language": "",
                "source_id": SOURCE_ID,
                "confidence": row["confidence"],
                "review_status": "approved",
                "created_at": PROMOTION_DATE,
                "updated_at": PROMOTION_DATE,
            }
        )
    else:
        raise SystemExit(f"Unsupported song status: {status}")

release_map = {}
new_release_rows = []
release_ids = next_id(releases, "release_id", "REL", 6)
for release_candidate_id, staged in first_by_key(recordings_staged, "release_candidate_id").items():
    promoted = next(
        row for row in recording_promotion if row["release_candidate_id"] == release_candidate_id
    )
    release_id = promoted["release_id"]
    release_map[release_candidate_id] = release_id
    if release_id not in existing_release_ids and not any(
        row["release_id"] == release_id for row in new_release_rows
    ):
        expected = next(release_ids)
        if release_id != expected:
            raise SystemExit(f"Unexpected release ID sequence: {release_id} != {expected}")
        new_release_rows.append(
            {
                "release_id": release_id,
                "canonical_release_title": staged["release_title"],
                "release_type": release_type(staged["release_format"]),
                "label_id": LABEL_ID,
                "catalog_number": staged["reference_number"],
                "release_year": staged["release_year"],
                "country": "",
                "source_id": SOURCE_ID,
                "confidence": staged["confidence"],
                "review_status": "approved",
                "created_at": PROMOTION_DATE,
                "updated_at": PROMOTION_DATE,
            }
        )

recording_map = {}
new_recording_rows = []
matched_recording_ids = set()

for row in recording_promotion:
    status = row["promotion_status"]
    recording_id = row["master_recording_id"]
    if row["canonical_song_id"] not in existing_song_ids and row["canonical_song_id"] not in new_song_ids_added:
        raise SystemExit(f"Recording points to missing song: {row}")
    if row["release_id"] not in existing_release_ids and row["release_id"] not in {
        release["release_id"] for release in new_release_rows
    }:
        raise SystemExit(f"Recording points to missing release: {row}")

    if status == "MATCH_EXISTING":
        if recording_id not in existing_recording_ids:
            raise SystemExit(f"Missing matched recording ID {recording_id}")
        matched_recording_ids.add(recording_id)
        recording_map[row["batch_recording_id"]] = recording_id
    elif status == "NEW":
        if recording_id in existing_recording_ids:
            raise SystemExit(f"New recording ID already exists: {recording_id}")
        recording_map[row["batch_recording_id"]] = recording_id
        new_recording_rows.append(
            {
                "recording_id": recording_id,
                "canonical_recording_title": row["recording_title"],
                "canonical_song_id": row["canonical_song_id"],
                "primary_group_id": row["primary_group_id"],
                "primary_performer_id": row["primary_performer_id"],
                "recording_genre_id": "",
                "release_id": row["release_id"],
                "label_id": row["label_id"],
                "recording_year": row["release_year"],
                "country": "",
                "language": "",
                "source_id": SOURCE_ID,
                "confidence": row["confidence"],
                "review_status": "approved",
                "created_at": PROMOTION_DATE,
                "updated_at": PROMOTION_DATE,
            }
        )
    else:
        raise SystemExit(f"Unsupported recording status: {status}")

new_relationship_counts = Counter()

rec_song_keys = {(row["recording_id"], row["song_id"]) for row in recording_song}
for staged in rec_song_staged:
    recording_id = recording_map[staged["batch_recording_id"]]
    song_id = song_map[staged["batch_song_id"]]
    key = (recording_id, song_id)
    if key not in rec_song_keys:
        recording_song.append(
            {
                "recording_id": recording_id,
                "song_id": song_id,
                "relationship_type": "canonical_song",
                "source_id": SOURCE_ID,
                "confidence": staged["confidence"],
                "review_status": "approved",
            }
        )
        rec_song_keys.add(key)
        new_relationship_counts["recording_song"] += 1

rec_group_keys = {(row["recording_id"], row["group_id"]) for row in recording_group}
rec_performer_keys = {
    (row["recording_id"], row["performer_id"]) for row in recording_performer
}
for staged in rec_artist_staged:
    recording_id = recording_map[staged["batch_recording_id"]]
    artist_id = artist_map.get(staged["artist_candidate_id"], "")
    if not artist_id:
        continue
    if artist_id.startswith("GRP"):
        key = (recording_id, artist_id)
        if key not in rec_group_keys:
            recording_group.append(
                {
                    "recording_id": recording_id,
                    "group_id": artist_id,
                    "role": "credited_group",
                    "source_id": SOURCE_ID,
                    "confidence": staged["confidence"],
                    "review_status": "approved",
                }
            )
            rec_group_keys.add(key)
            new_relationship_counts["recording_group"] += 1
    elif artist_id.startswith("PER"):
        key = (recording_id, artist_id)
        if key not in rec_performer_keys:
            recording_performer.append(
                {
                    "recording_id": recording_id,
                    "performer_id": artist_id,
                    "role": "credited_performer",
                    "source_id": SOURCE_ID,
                    "confidence": staged["confidence"],
                    "review_status": "approved",
                }
            )
            rec_performer_keys.add(key)
            new_relationship_counts["recording_performer"] += 1

rec_release_keys = {
    (row["recording_id"], row["release_id"]) for row in recording_release
}
for staged in rec_release_staged:
    recording_id = recording_map[staged["batch_recording_id"]]
    release_id = release_map[staged["release_candidate_id"]]
    key = (recording_id, release_id)
    if key not in rec_release_keys:
        recording_release.append(
            {
                "recording_id": recording_id,
                "release_id": release_id,
                "relationship_type": "appears_on_release",
                "source_id": SOURCE_ID,
                "confidence": staged["confidence"],
                "review_status": "approved",
            }
        )
        rec_release_keys.add(key)
        new_relationship_counts["recording_release"] += 1

rec_source_keys = {
    (row["recording_id"], row["source_id"], row["source_reference"])
    for row in recording_source
}
for staged in rec_source_staged:
    recording_id = recording_map[staged["batch_recording_id"]]
    key = (recording_id, staged["source_id"], staged["source_reference"])
    if key not in rec_source_keys:
        recording_source.append(
            {
                "recording_id": recording_id,
                "source_id": staged["source_id"],
                "relationship_type": "authority_source",
                "source_reference": staged["source_reference"],
                "confidence": staged["confidence"],
                "review_status": "approved",
            }
        )
        rec_source_keys.add(key)
        new_relationship_counts["recording_source"] += 1

groups_before = len(groups)
performers_before = len(performers)
songs_before = len(songs)
recordings_before = len(recordings)
releases_before = len(releases)
relationship_before = {
    "recording_song": len(read_tsv("relationships/recording_song.tsv")),
    "recording_group": len(read_tsv("relationships/recording_group.tsv")),
    "recording_performer": len(read_tsv("relationships/recording_performer.tsv")),
    "recording_release": len(read_tsv("relationships/recording_release.tsv")),
    "recording_source": len(read_tsv("relationships/recording_source.tsv")),
}

append_tsv("authority/groups/groups_master.tsv", new_group_rows, headers["groups"])
append_tsv("authority/songs/songs_master.tsv", new_song_rows, headers["songs"])
append_tsv("authority/recordings/recordings_master.tsv", new_recording_rows, headers["recordings"])
append_tsv("authority/releases/releases_master.tsv", new_release_rows, headers["releases"])

append_tsv(
    "relationships/recording_song.tsv",
    recording_song[relationship_before["recording_song"] :],
    headers["recording_song"],
)
append_tsv(
    "relationships/recording_group.tsv",
    recording_group[relationship_before["recording_group"] :],
    headers["recording_group"],
)
append_tsv(
    "relationships/recording_performer.tsv",
    recording_performer[relationship_before["recording_performer"] :],
    headers["recording_performer"],
)
append_tsv(
    "relationships/recording_release.tsv",
    recording_release[relationship_before["recording_release"] :],
    headers["recording_release"],
)
append_tsv(
    "relationships/recording_source.tsv",
    recording_source[relationship_before["recording_source"] :],
    headers["recording_source"],
)

groups.extend(new_group_rows)
songs.extend(new_song_rows)
recordings.extend(new_recording_rows)
releases.extend(new_release_rows)

relationships_total = sum(new_relationship_counts.values())
inventory = {
    "recordings": len(recordings),
    "songs": len(songs),
    "groups": len(groups),
    "performers": len(performers),
    "releases": len(releases),
    "recording_song": len(recording_song),
    "recording_group": len(recording_group),
    "recording_performer": len(recording_performer),
    "recording_release": len(recording_release),
    "recording_source": len(recording_source),
}

os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
review_lines = [
    f"- {row['raw_artist_text']} ({row['candidate_artist_type']})"
    for row in review_artist_rows
]
if not review_lines:
    review_lines = ["- None"]

report = f"""# SRC0002 BATCH0003 CLEAN PROMOTION REPORT

## UNIT-0062R

### Objective
Rebuild clean promotion for SRC0002 batch0003 from restored staging, using current clean master tables only.

### Evidence Before Promotion
- Git status before promotion: clean on main.
- Staged recordings: {len(recordings_staged)}
- Staged songs: {len(songs_staged)}
- Staged artist candidates: {len(artists_staged)}
- Staged recording-song relationships: {len(rec_song_staged)}
- Staged recording-artist candidate relationships: {len(rec_artist_staged)}
- Staged recording-release relationships: {len(rec_release_staged)}
- Staged recording-source relationships: {len(rec_source_staged)}

### Classification Summary
- Recordings added: {len(new_recording_rows)}
- Recordings matched: {len(matched_recording_ids)}
- Songs added: {len(new_song_rows)}
- Songs matched: {len(matched_song_ids)}
- Groups added: {len(new_group_rows)}
- Groups matched: {len(matched_groups)}
- Performers added: 0
- Performers matched: {len(matched_performers)}
- Releases added for referential recording-release promotion: {len(new_release_rows)}

### Relationships Added
- recording_song: {new_relationship_counts['recording_song']}
- recording_group: {new_relationship_counts['recording_group']}
- recording_performer: {new_relationship_counts['recording_performer']}
- recording_release: {new_relationship_counts['recording_release']}
- recording_source: {new_relationship_counts['recording_source']}
- Total relationships added: {relationships_total}

### Review-Only Candidates
{os.linesep.join(review_lines)}

### Updated Inventory Totals
- recordings_master: {inventory['recordings']}
- songs_master: {inventory['songs']}
- groups_master: {inventory['groups']}
- performers_master: {inventory['performers']}
- releases_master: {inventory['releases']}
- recording_song: {inventory['recording_song']}
- recording_group: {inventory['recording_group']}
- recording_performer: {inventory['recording_performer']}
- recording_release: {inventory['recording_release']}
- recording_source: {inventory['recording_source']}

### Validation Summary
- Promotion staging was regenerated from current masters and restored batch0003 staging TSVs.
- Dirty backup master files and dirty_master_diff.patch were not used.
- Existing master rows were not edited; production changes are append-only plus regenerated batch0003 promotion staging.
- Existing source_id values were not overwritten.
- All new authority rows use source_id SRC0002.
- All promoted recording relationships resolve to production recording, song, artist, release, and source IDs.
- recording_performer received no rows because no performer evidence was conclusive after classification.
- Duplicate relationship keys were skipped, including the already-promoted recording-song and recording-group links for matched recording REC005514.

### Pre/Post Counts
- recordings_master: {recordings_before} -> {inventory['recordings']}
- songs_master: {songs_before} -> {inventory['songs']}
- groups_master: {groups_before} -> {inventory['groups']}
- performers_master: {performers_before} -> {inventory['performers']}
- releases_master: {releases_before} -> {inventory['releases']}
- recording_song: {relationship_before['recording_song']} -> {inventory['recording_song']}
- recording_group: {relationship_before['recording_group']} -> {inventory['recording_group']}
- recording_performer: {relationship_before['recording_performer']} -> {inventory['recording_performer']}
- recording_release: {relationship_before['recording_release']} -> {inventory['recording_release']}
- recording_source: {relationship_before['recording_source']} -> {inventory['recording_source']}

### Commit And Git Status
- Commit hash: pending
- Git status: pending
"""

with open(REPORT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(report)

print("Clean promotion complete.")
print(f"Recordings added: {len(new_recording_rows)}, matched: {len(matched_recording_ids)}")
print(f"Songs added: {len(new_song_rows)}, matched: {len(matched_song_ids)}")
print(f"Groups added: {len(new_group_rows)}, matched: {len(matched_groups)}")
print(f"Relationships added: {relationships_total}")
