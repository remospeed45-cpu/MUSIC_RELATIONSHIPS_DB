import csv
import os
from datetime import datetime

# Current Date
today = datetime.now().strftime('%Y-%m-%d')

# Helper to read TSV
def read_tsv(filename):
    if not os.path.exists(filename): return []
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

# Helper to write TSV
def write_tsv(filename, data, fieldnames=None):
    if not data: return
    if fieldnames is None:
        fn = set()
        for d in data: fn.update(d.keys())
        fieldnames = sorted(list(fn))
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

# Load Promotion Staging
art_promo = read_tsv('authority/staging/src0002_batch0003_artist_promotion.tsv')
song_promo = read_tsv('authority/staging/src0002_batch0003_song_promotion.tsv')
rec_promo = read_tsv('authority/staging/src0002_batch0003_recording_promotion.tsv')

# Load Relationships Staging
rel_rec_song = read_tsv('relationships/staging/src0002_batch0003_recording_song.tsv')
rel_rec_artist = read_tsv('relationships/staging/src0002_batch0003_recording_artist_candidate.tsv')
rel_rec_rel = read_tsv('relationships/staging/src0002_batch0003_recording_release.tsv')
rel_rec_src = read_tsv('relationships/staging/src0002_batch0003_recording_source.tsv')

# Load Master Tables
m_groups = read_tsv('authority/groups/groups_master.tsv')
m_performers = read_tsv('authority/performers/performers_master.tsv')
m_songs = read_tsv('authority/songs/songs_master.tsv')
m_recs = read_tsv('authority/recordings/recordings_master.tsv')

# Load Relationships Masters
m_rec_song = read_tsv('relationships/recording_song.tsv')
m_rec_group = read_tsv('relationships/recording_group.tsv')
m_rec_perf = read_tsv('relationships/recording_performer.tsv')
m_rec_rel = read_tsv('relationships/recording_release.tsv')
m_rec_src = read_tsv('relationships/recording_source.tsv')

# Get next IDs
def get_next_id(master_list, id_field, prefix, length=4):
    if not master_list: return f"{prefix}{'1'.zfill(length)}"
    ids = []
    for r in master_list:
        try:
            ids.append(int(r[id_field].replace(prefix, '')))
        except: pass
    if not ids: return f"{prefix}{'1'.zfill(length)}"
    return f"{prefix}{str(max(ids) + 1).zfill(length)}"

next_grp_id = get_next_id(m_groups, 'group_id', 'GRP', 4)
next_perf_id = get_next_id(m_performers, 'performer_id', 'PER', 6)
next_song_id = get_next_id(m_songs, 'song_id', 'SONG', 6)
next_rec_id = get_next_id(m_recs, 'recording_id', 'REC', 6)

# Maps for promotion
artist_map = {} # staged_id -> master_id
song_map = {}
rec_map = {}

# Promote Artists
for a in art_promo:
    staged_id = a['artist_candidate_id']
    if a['promotion_status'] == 'MATCH_EXISTING':
        artist_map[staged_id] = a['master_artist_id']
    elif a['promotion_status'] == 'NEW':
        if a['candidate_artist_type'] == 'group_candidate':
            new_id = next_grp_id
            artist_map[staged_id] = new_id
            m_groups.append({
                "group_id": new_id,
                "canonical_group_name": a['raw_artist_text'],
                "alternate_names": "",
                "group_type": "group",
                "country": "",
                "primary_genre_id": "",
                "source_id": "SRC0002",
                "confidence": "medium-high",
                "review_status": "approved",
                "created_at": today,
                "updated_at": today
            })
            # Increment next_grp_id
            num = int(next_grp_id.replace('GRP', '')) + 1
            next_grp_id = f"GRP{str(num).zfill(4)}"
        # Performers handled similarly if needed, but here only group candidates are 'NEW'
    # REVIEW_REQUIRED artists are not promoted

# Promote Songs
for s in song_promo:
    staged_id = s['batch_song_id']
    if s['promotion_status'] == 'MATCH_EXISTING':
        song_map[staged_id] = s['master_song_id']
    elif s['promotion_status'] == 'NEW':
        new_id = next_song_id
        song_map[staged_id] = new_id
        m_songs.append({
            "song_id": new_id,
            "canonical_song_title": s['canonical_song_title_candidate'],
            "alternate_titles": "",
            "composer_text": "",
            "year": "",
            "work_type": "musical_work",
            "primary_genre_id": "",
            "source_id": "SRC0002",
            "confidence": "medium",
            "review_status": "approved_title_candidate",
            "created_at": today,
            "updated_at": today
        })
        num = int(next_song_id.replace('SONG', '')) + 1
        next_song_id = f"SONG{str(num).zfill(6)}"

# Promote Recordings
for r in rec_promo:
    staged_id = r['batch_recording_id']
    if r['promotion_status'] == 'MATCH_EXISTING':
        rec_map[staged_id] = r['master_recording_id']
    elif r['promotion_status'] == 'NEW':
        new_id = next_rec_id
        rec_map[staged_id] = new_id
        
        # Determine primary artist for recording master record
        # This is a simplification: take the first artist from relationships if multiple
        primary_grp = ""
        primary_perf = ""
        for ra in rel_rec_artist:
            if ra['batch_recording_id'] == staged_id:
                m_id = artist_map.get(ra['artist_candidate_id'])
                if m_id:
                    if m_id.startswith('GRP'): primary_grp = m_id
                    elif m_id.startswith('PER'): primary_perf = m_id
                    break
        
        m_recs.append({
            "recording_id": new_id,
            "canonical_recording_title": r['recording_title'],
            "primary_song_id": song_map.get(r['batch_recording_id'].replace('REC', 'SONG')), # Fallback if direct map not available
            "primary_group_id": primary_grp,
            "primary_performer_id": primary_perf,
            "recording_year": r['release_year'],
            "recording_type": "studio",
            "primary_label_id": "LBL000002", # Discos Fuentes
            "isrc": "",
            "matrix_number": "",
            "catalog_number": r['reference_number'],
            "source_id": "SRC0002",
            "confidence": "high",
            "review_status": "approved",
            "created_at": today,
            "updated_at": today
        })
        # Note: Fix primary_song_id if it's not simply REC->SONG
        # Actually I should use the rel_rec_song
        for rs in rel_rec_song:
            if rs['batch_recording_id'] == staged_id:
                m_recs[-1]['primary_song_id'] = song_map.get(rs['batch_song_id'], "")
                break

        num = int(next_rec_id.replace('REC', '')) + 1
        next_rec_id = f"REC{str(num).zfill(6)}"

# Promote Relationships
for rs in rel_rec_song:
    m_rid = rec_map.get(rs['batch_recording_id'])
    m_sid = song_map.get(rs['batch_song_id'])
    if m_rid and m_sid:
        m_rec_song.append({
            "recording_id": m_rid,
            "song_id": m_sid,
            "relationship_type": rs['relationship_type'],
            "source_id": rs['source_id'],
            "source_reference": rs['source_reference'],
            "evidence_text": rs['evidence_text'],
            "confidence": rs['confidence'],
            "review_status": "approved",
            "created_at": today,
            "updated_at": today
        })

for ra in rel_rec_artist:
    m_rid = rec_map.get(ra['batch_recording_id'])
    m_aid = artist_map.get(ra['artist_candidate_id'])
    if m_rid and m_aid:
        if m_aid.startswith('GRP'):
            m_rec_group.append({
                "recording_id": m_rid,
                "group_id": m_aid,
                "relationship_type": ra['relationship_type'],
                "source_id": ra['source_id'],
                "source_reference": ra['source_reference'],
                "evidence_text": ra['evidence_text'],
                "confidence": ra['confidence'],
                "review_status": "approved",
                "created_at": today,
                "updated_at": today
            })
        elif m_aid.startswith('PER'):
            m_rec_perf.append({
                "recording_id": m_rid,
                "performer_id": m_aid,
                "relationship_type": ra['relationship_type'],
                "source_id": ra['source_id'],
                "source_reference": ra['source_reference'],
                "evidence_text": ra['evidence_text'],
                "confidence": ra['confidence'],
                "review_status": "approved",
                "created_at": today,
                "updated_at": today
            })

for rr in rel_rec_rel:
    m_rid = rec_map.get(rr['batch_recording_id'])
    if m_rid:
        m_rec_rel.append({
            "recording_id": m_rid,
            "release_id": rr['release_candidate_id'], # Keep candidate ID for now as instructed
            "relationship_type": rr['relationship_type'],
            "source_id": rr['source_id'],
            "source_reference": rr['source_reference'],
            "evidence_text": rr['evidence_text'],
            "confidence": rr['confidence'],
            "review_status": "approved",
            "created_at": today,
            "updated_at": today
        })

for rsrc in rel_rec_src:
    m_rid = rec_map.get(rsrc['batch_recording_id'])
    if m_rid:
        m_rec_src.append({
            "recording_id": m_rid,
            "source_id": rsrc['source_id'],
            "source_url": rsrc['source_url'],
            "relationship_type": rsrc['relationship_type'],
            "source_reference": rsrc['source_reference'],
            "evidence_text": rsrc['evidence_text'],
            "confidence": rsrc['confidence'],
            "review_status": "approved",
            "created_at": today,
            "updated_at": today
        })

# Save Masters
write_tsv('authority/groups/groups_master.tsv', m_groups)
write_tsv('authority/performers/performers_master.tsv', m_performers)
write_tsv('authority/songs/songs_master.tsv', m_songs)
write_tsv('authority/recordings/recordings_master.tsv', m_recs)

write_tsv('relationships/recording_song.tsv', m_rec_song)
write_tsv('relationships/recording_group.tsv', m_rec_group)
write_tsv('relationships/recording_performer.tsv', m_rec_perf)
write_tsv('relationships/recording_release.tsv', m_rec_rel)
write_tsv('relationships/recording_source.tsv', m_rec_src)

print(f"Promotion complete.")
print(f"New groups: {len(m_groups)}")
print(f"New songs: {len(m_songs)}")
print(f"New recordings: {len(m_recs)}")
