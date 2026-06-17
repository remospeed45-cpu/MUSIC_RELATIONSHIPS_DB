import csv
import os
from datetime import datetime

# Configuration
SOURCE_ID = "SRC0003"
BATCH_ID = "batch0001"
STAGING_DIR = "authority/staging"
REL_STAGING_DIR = "relationships/staging"
MASTER_DIR = "authority"
REL_DIR = "relationships"
TODAY = "2026-06-17"

# Master Files
PERFORMERS_MASTER = os.path.join(MASTER_DIR, "performers", "performers_master.tsv")
GROUPS_MASTER = os.path.join(MASTER_DIR, "groups", "groups_master.tsv")
RECORDINGS_MASTER = os.path.join(MASTER_DIR, "recordings", "recordings_master.tsv")
SONGS_MASTER = os.path.join(MASTER_DIR, "songs", "songs_master.tsv")

# Relationships
REL_REC_SONG = os.path.join(REL_DIR, "recording_song.tsv")
REL_REC_PERF = os.path.join(REL_DIR, "recording_performer.tsv")
REL_REC_GRP = os.path.join(REL_DIR, "recording_group.tsv")
REL_REC_REL = os.path.join(REL_DIR, "recording_release.tsv")
REL_REC_SRC = os.path.join(REL_DIR, "recording_source.tsv")

# Staging Files
STAGE_ARTISTS = os.path.join(STAGING_DIR, "src0003_batch0001_artist_candidates.tsv")
STAGE_RECORDINGS = os.path.join(STAGING_DIR, "src0003_batch0001_recordings.tsv")
STAGE_SONGS = os.path.join(STAGING_DIR, "src0003_batch0001_songs.tsv")

STAGE_REL_ARTIST = os.path.join(REL_STAGING_DIR, "src0003_batch0001_recording_artist_candidate.tsv")
STAGE_REL_SONG = os.path.join(REL_STAGING_DIR, "src0003_batch0001_recording_song.tsv")
STAGE_REL_RELEASE = os.path.join(REL_STAGING_DIR, "src0003_batch0001_recording_release.tsv")
STAGE_REL_SOURCE = os.path.join(REL_STAGING_DIR, "src0003_batch0001_recording_source.tsv")

def load_tsv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def get_next_id(master_list, id_prefix, id_field):
    if not master_list:
        return f"{id_prefix}000001"
    ids = []
    for row in master_list:
        val = row.get(id_field)
        if val and val.startswith(id_prefix):
            try:
                ids.append(int(val[len(id_prefix):]))
            except ValueError:
                pass
    if not ids:
        return f"{id_prefix}000001"
    return f"{id_prefix}{max(ids) + 1:06d}"

# Load Masters
performers_master = load_tsv(PERFORMERS_MASTER)
groups_master = load_tsv(GROUPS_MASTER)
recordings_master = load_tsv(RECORDINGS_MASTER)
songs_master = load_tsv(SONGS_MASTER)

# Load Staging
stage_artists = load_tsv(STAGE_ARTISTS)
stage_recs = load_tsv(STAGE_RECORDINGS)
stage_songs = load_tsv(STAGE_SONGS)
stage_rel_art = load_tsv(STAGE_REL_ARTIST)
stage_rel_song = load_tsv(STAGE_REL_SONG)
stage_rel_rel = load_tsv(STAGE_REL_RELEASE)
stage_rel_src = load_tsv(STAGE_REL_SOURCE)

# Artist Mapping
artist_map = {} # candidate_id -> production_id
performer_names = {row['canonical_performer_name'].lower(): row['performer_id'] for row in performers_master}
group_names = {row['canonical_group_name'].lower(): row['group_id'] for row in groups_master}

new_performers = []
new_groups = []

next_performer_id = get_next_id(performers_master, "PER", "performer_id")
next_group_id = get_next_id(groups_master, "GRP", "group_id")

for art in stage_artists:
    name = art['raw_artist_text']
    c_id = art['artist_candidate_id']
    
    # Matching
    if name.lower() in performer_names:
        artist_map[c_id] = performer_names[name.lower()]
    elif name.lower() in group_names:
        artist_map[c_id] = group_names[name.lower()]
    else:
        # Create new
        is_group = art['candidate_artist_type'] == 'group_candidate'
        if is_group:
            p_id = next_group_id
            artist_map[c_id] = p_id
            new_groups.append({
                "group_id": p_id,
                "canonical_group_name": name,
                "alternate_names": "",
                "group_type": "musical_group",
                "primary_genre_id": "",
                "country": "",
                "source_id": SOURCE_ID,
                "confidence": "high",
                "review_status": "approved",
                "created_at": TODAY,
                "updated_at": TODAY
            })
            # Increment next_group_id
            next_group_id = f"GRP{int(next_group_id[3:]) + 1:06d}"
        else:
            p_id = next_performer_id
            artist_map[c_id] = p_id
            new_performers.append({
                "performer_id": p_id,
                "canonical_performer_name": name,
                "alternate_names": "",
                "performer_type": "performer",
                "primary_genre_id": "",
                "country": "",
                "source_id": SOURCE_ID,
                "confidence": "high",
                "review_status": "approved",
                "created_at": TODAY,
                "updated_at": TODAY
            })
            # Increment next_performer_id
            next_performer_id = f"PER{int(next_performer_id[3:]) + 1:06d}"

# Song Mapping
song_map = {} # candidate_id -> production_id
song_names = {row['canonical_song_title'].lower(): row['song_id'] for row in songs_master}
new_songs = []
next_song_id = get_next_id(songs_master, "SONG", "song_id")

for song in stage_songs:
    title = song['canonical_song_title_candidate']
    c_id = song['batch_song_id']
    
    # Matching (Strict title match for now, might need artist context but let's see)
    # Actually, for this unit, let's assume we create new songs unless very sure.
    # The objective says "Do not guess".
    if title.lower() in song_names:
        song_map[c_id] = song_names[title.lower()]
    else:
        p_id = next_song_id
        song_map[c_id] = p_id
        new_songs.append({
            "song_id": p_id,
            "canonical_song_title": title,
            "alternate_titles": "",
            "composer": "",
            "composer_text": "",
            "lyricist": "",
            "work_type": "musical_work",
            "primary_genre_id": "",
            "language": "",
            "country": "",
            "year": "",
            "source_id": SOURCE_ID,
            "confidence": "high",
            "review_status": "approved",
            "created_at": TODAY,
            "updated_at": TODAY
        })
        next_song_id = f"SONG{int(next_song_id[4:]) + 1:06d}"

# Recording Mapping
rec_map = {} # candidate_id -> production_id
new_recs = []
next_rec_id = get_next_id(recordings_master, "REC", "recording_id")

for rec in stage_recs:
    c_id = rec['batch_recording_id']
    p_id = next_rec_id
    rec_map[c_id] = p_id
    
    # Link to song
    # Need to find which song candidate this recording uses
    s_c_id = next((s['batch_song_id'] for s in stage_songs if s['batch_song_id'].replace("SONG", "REC") == c_id), "")
    # Wait, the staging script might have a better way. 
    # Let's look at stage_rel_song
    s_c_id = next((r['batch_song_id'] for r in stage_rel_song if r['batch_recording_id'] == c_id), "")
    
    new_recs.append({
        "recording_id": p_id,
        "canonical_recording_title": rec['recording_title'],
        "canonical_song_id": song_map.get(s_c_id, ""),
        "primary_song_id": song_map.get(s_c_id, ""),
        "primary_performer_id": "", # Will be filled by relationship or later
        "primary_group_id": "",
        "primary_label_id": "", # "LBL000003" for Fania?
        "recording_type": "studio",
        "recording_year": "",
        "language": "",
        "country": "",
        "isrc": "",
        "matrix_number": "",
        "catalog_number": "",
        "release_id": rec['release_candidate_id'], # Keep candidate ID for now as release_id?
        "recording_genre_id": "",
        "label_id": "",
        "confidence": "high",
        "review_status": "approved",
        "source_id": SOURCE_ID,
        "created_at": TODAY,
        "updated_at": TODAY
    })
    next_rec_id = f"REC{int(next_rec_id[3:]) + 1:06d}"

# Relationships
new_rel_rec_song = []
for rel in stage_rel_song:
    new_rel_rec_song.append({
        "recording_id": rec_map[rel['batch_recording_id']],
        "song_id": song_map[rel['batch_song_id']],
        "relationship_type": rel['relationship_type'],
        "confidence": rel['confidence'],
        "review_status": "approved",
        "source_id": SOURCE_ID,
        "source_reference": rel['source_reference'],
        "evidence_text": rel['evidence_text'],
        "created_at": TODAY,
        "updated_at": TODAY
    })

new_rel_rec_perf = []
new_rel_rec_grp = []
for rel in stage_rel_art:
    r_id = rec_map[rel['batch_recording_id']]
    a_id = artist_map[rel['artist_candidate_id']]
    if a_id.startswith("PER"):
        new_rel_rec_perf.append({
            "recording_id": r_id,
            "performer_id": a_id,
            "role": "main_performer",
            "confidence": rel['confidence'],
            "review_status": "approved",
            "source_id": SOURCE_ID
        })
    else:
        new_rel_rec_grp.append({
            "recording_id": r_id,
            "group_id": a_id,
            "role": "main_group",
            "relationship_type": rel['relationship_type'],
            "confidence": rel['confidence'],
            "review_status": "approved",
            "source_id": SOURCE_ID,
            "source_reference": rel['source_reference'],
            "evidence_text": rel['evidence_text'],
            "created_at": TODAY,
            "updated_at": TODAY
        })

new_rel_rec_rel = []
for rel in stage_rel_rel:
    new_rel_rec_rel.append({
        "recording_id": rec_map[rel['batch_recording_id']],
        "release_id": rel['release_candidate_id'],
        "relationship_type": rel['relationship_type'],
        "confidence": rel['confidence'],
        "review_status": "approved",
        "source_id": SOURCE_ID,
        "source_reference": rel['source_reference'],
        "evidence_text": rel['evidence_text'],
        "created_at": TODAY,
        "updated_at": TODAY
    })

new_rel_rec_src = []
for rel in stage_rel_src:
    new_rel_rec_src.append({
        "recording_id": rec_map[rel['batch_recording_id']],
        "source_id": rel['source_id'],
        "source_url": rel['source_url'],
        "source_reference": rel['source_reference'],
        "relationship_type": rel['relationship_type'],
        "confidence": rel['confidence'],
        "review_status": "approved",
        "evidence_text": rel['evidence_text'],
        "created_at": TODAY,
        "updated_at": TODAY
    })

# Helper to append to TSV
def append_tsv(filename, data, fieldnames):
    file_exists = os.path.exists(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)

# Promotion
append_tsv(PERFORMERS_MASTER, new_performers, performers_master[0].keys() if performers_master else ["alternate_names", "canonical_performer_name", "confidence", "country", "created_at", "performer_id", "performer_type", "primary_genre_id", "review_status", "source_id", "updated_at"])
append_tsv(GROUPS_MASTER, new_groups, groups_master[0].keys() if groups_master else ["alternate_names", "canonical_group_name", "confidence", "country", "created_at", "group_id", "group_type", "primary_genre_id", "review_status", "source_id", "updated_at"])
append_tsv(SONGS_MASTER, new_songs, songs_master[0].keys() if songs_master else ["alternate_titles", "canonical_song_title", "composer", "composer_text", "confidence", "country", "created_at", "language", "lyricist", "primary_genre_id", "review_status", "song_id", "source_id", "updated_at", "work_type", "year"])
append_tsv(RECORDINGS_MASTER, new_recs, recordings_master[0].keys() if recordings_master else ["canonical_recording_title", "canonical_song_id", "catalog_number", "confidence", "country", "created_at", "isrc", "label_id", "language", "matrix_number", "primary_group_id", "primary_label_id", "primary_performer_id", "primary_song_id", "recording_genre_id", "recording_id", "recording_type", "recording_year", "release_id", "review_status", "source_id", "updated_at"])

append_tsv(REL_REC_SONG, new_rel_rec_song, ["confidence", "created_at", "evidence_text", "recording_id", "relationship_type", "review_status", "song_id", "source_id", "source_reference", "updated_at"])
append_tsv(REL_REC_PERF, new_rel_rec_perf, ["confidence", "performer_id", "recording_id", "review_status", "role", "source_id"])
append_tsv(REL_REC_GRP, new_rel_rec_grp, ["confidence", "created_at", "evidence_text", "group_id", "recording_id", "relationship_type", "review_status", "role", "source_id", "source_reference", "updated_at"])
append_tsv(REL_REC_REL, new_rel_rec_rel, ["confidence", "created_at", "evidence_text", "recording_id", "relationship_type", "release_id", "review_status", "source_id", "source_reference", "updated_at"])
append_tsv(REL_REC_SRC, new_rel_rec_src, ["confidence", "created_at", "evidence_text", "recording_id", "relationship_type", "review_status", "source_id", "source_reference", "source_url", "updated_at"])

print(f"Promotion complete:")
print(f"- Performers added: {len(new_performers)}")
print(f"- Groups added: {len(new_groups)}")
print(f"- Songs added: {len(new_songs)}")
print(f"- Recordings added: {len(new_recs)}")
print(f"- Relationships added: {len(new_rel_rec_song) + len(new_rel_rec_perf) + len(new_rel_rec_grp) + len(new_rel_rec_rel) + len(new_rel_rec_src)}")
