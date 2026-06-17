# SRC0002 BATCH0005 EXTRACTION REPORT

## UNIT-0067

### Objective
Acquire and stage the final high/medium value SRC0002 releases.

### Processed Releases
1. **Colección 100 Parranderas del Siglo** (REL001)
2. **Colección 100 Exitos de Diciembre** (REL002)
3. **Colección 100 Villancicos del Siglo** (REL003)
4. **Colección 100 Exitos de Pastor López** (REL004)
5. **Colección 100 Exitos de Los Corraleros de Majagual** (REL005)

### Extraction Summary
- **Releases Processed:** 5
- **Tracks Extracted:** 50
- **Recording Candidates:** 50
- **Song Candidates:** 50
- **Artist Candidates:** 17 (Unique)

### Staged Files
- `authority/staging/src0002_batch0005_recordings.tsv`
- `authority/staging/src0002_batch0005_songs.tsv`
- `authority/staging/src0002_batch0005_artist_candidates.tsv`

### Staged Relationships
- `relationships/staging/src0002_batch0005_recording_song.tsv` (50)
- `relationships/staging/src0002_batch0005_recording_artist_candidate.tsv` (51)
- `relationships/staging/src0002_batch0005_recording_release.tsv` (50)
- `relationships/staging/src0002_batch0005_recording_source.tsv` (50)

### Validation Status
- Row counts verified (50 tracks per file + header).
- ID patterns follow project conventions (SRC0002-B0005-*).
- Required fields (source_url, track_number, recording_title) populated for all records.
- Source evidence preserved with URLs and evidence text.

### Notes
- Extracted visible tracklists (first 10 tracks) from Discos Fuentes product pages for maximum confidence.
- Artist splitting performed for " - " and " y Su..." patterns.
- All records set to `staged_for_review`.
