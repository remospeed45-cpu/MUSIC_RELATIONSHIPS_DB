# SRC0002 BATCH0003 EXTRACTION REPORT

## UNIT-0061

### Objective
Acquire and stage the complete SRC0002 batch0003 queue.

### Processed Releases
1. **LP - Cumbia y Nada Más** (Afrosound)
2. **LP - Historia Musical** (Los 50 de Joselito)
3. **Colección 100 Exitos de La Sonora Matancera** (La Sonora Matancera)
4. **Colección 100 Exitos del Siglo: Joe Arroyo** (Joe Arroyo)
5. **Colección 100 Exitos de Los Corraleros de Majagual** (Los Corraleros de Majagual)
6. **Colección 100 Exitos – Cuatro Grandes de la Música Tropical** (Varios Artistas)
7. **Colección 100 - Homenaje a Toño Fuentes** (Toño Fuentes)

### Extraction Summary
- **Releases Processed:** 7
- **Tracks Extracted:** 74
- **Recording Candidates:** 74
- **Song Candidates:** 74
- **Artist Candidates:** 12 (Unique)

### Staged Files
- `authority/staging/src0002_batch0003_recordings.tsv`
- `authority/staging/src0002_batch0003_songs.tsv`
- `authority/staging/src0002_batch0003_artist_candidates.tsv`

### Staged Relationships
- `relationships/staging/src0002_batch0003_recording_song.tsv` (74)
- `relationships/staging/src0002_batch0003_recording_artist_candidate.tsv` (76)
- `relationships/staging/src0002_batch0003_recording_release.tsv` (74)
- `relationships/staging/src0002_batch0003_recording_source.tsv` (74)

### Validation Status
- Counts verified against source extraction.
- ID patterns follow project conventions (SRC0002-B0003-*).
- Source evidence preserved with URLs and evidence text.

### Notes
- The USB "100 Exitos" collections only listed 10 tracks each on the official product pages; these 10 were staged as requested.
- Artist splitting performed for "Feat." and "(Feat.)" patterns to capture individual artist candidates.
- Review status set to `staged_for_review` for all records.
