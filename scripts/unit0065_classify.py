import csv
import os

# Helper to read TSV into a list of dicts
def read_tsv(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

# Load staged data
staged_recs = read_tsv('authority/staging/src0002_batch0004_recordings.tsv')
staged_songs = read_tsv('authority/staging/src0002_batch0004_songs.tsv')
staged_artists = read_tsv('authority/staging/src0002_batch0004_artist_candidates.tsv')

# Load master data for matching
master_groups = read_tsv('authority/groups/groups_master.tsv')
master_performers = read_tsv('authority/performers/performers_master.tsv')
master_songs = read_tsv('authority/songs/songs_master.tsv')
master_recs = read_tsv('authority/recordings/recordings_master.tsv')

# Normalize names for matching
def norm(text):
    if not text: return ""
    return text.lower().strip().replace('  ', ' ')

# Artist matching
group_map = {norm(g['canonical_group_name']): g['group_id'] for g in master_groups}
performer_map = {norm(p['canonical_performer_name']): p['performer_id'] for p in master_performers}

# Song matching
song_map = {norm(s['canonical_song_title']): s['song_id'] for s in master_songs}

# Recording matching
group_id_to_norm = {g['group_id']: norm(g['canonical_group_name']) for g in master_groups}
performer_id_to_norm = {p['performer_id']: norm(p['canonical_performer_name']) for p in master_performers}

master_rec_map = {}
for r in master_recs:
    t = norm(r['canonical_recording_title'])
    a = ""
    if r['primary_group_id']:
        a = group_id_to_norm.get(r['primary_group_id'], "")
    elif r['primary_performer_id']:
        a = performer_id_to_norm.get(r['primary_performer_id'], "")
    if a:
        master_rec_map[(t, a)] = r['recording_id']

# Promotion containers
artist_promotion = []
song_promotion = []
rec_promotion = []

# Process Artists
for sa in staged_artists:
    name = norm(sa['raw_artist_text'])
    match_id = group_map.get(name) or performer_map.get(name)
    if match_id:
        sa['promotion_status'] = 'MATCH_EXISTING'
        sa['master_artist_id'] = match_id
    else:
        sa['master_artist_id'] = ''
        if sa['candidate_artist_type'] == 'group_candidate':
            sa['promotion_status'] = 'NEW'
        else:
            sa['promotion_status'] = 'REVIEW_REQUIRED'
    artist_promotion.append(sa)

# Process Songs
for ss in staged_songs:
    title = norm(ss['canonical_song_title_candidate'])
    match_id = song_map.get(title)
    if match_id:
        ss['promotion_status'] = 'MATCH_EXISTING'
        ss['master_song_id'] = match_id
    else:
        ss['promotion_status'] = 'NEW'
        ss['master_song_id'] = ''
    song_promotion.append(ss)

# Process Recordings
for sr in staged_recs:
    title = norm(sr['recording_title'])
    artist = norm(sr['artist_text'])
    match_id = master_rec_map.get((title, artist))
    if match_id:
        sr['promotion_status'] = 'MATCH_EXISTING'
        sr['master_recording_id'] = match_id
    else:
        sr['promotion_status'] = 'NEW'
        sr['master_recording_id'] = ''
    rec_promotion.append(sr)

# Write Promotion Staging
def write_tsv(filename, data):
    if not data: return
    fieldnames = sorted(list(data[0].keys()))
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)

write_tsv('authority/staging/src0002_batch0004_artist_promotion.tsv', artist_promotion)
write_tsv('authority/staging/src0002_batch0004_song_promotion.tsv', song_promotion)
write_tsv('authority/staging/src0002_batch0004_recording_promotion.tsv', rec_promotion)

print(f"Promotion staging complete. Artists: {len(artist_promotion)}, Songs: {len(song_promotion)}, Recordings: {len(rec_promotion)}")
