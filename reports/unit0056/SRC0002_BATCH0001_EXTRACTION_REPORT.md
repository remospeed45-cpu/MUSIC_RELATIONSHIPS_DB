# UNIT-0056 SRC0002 Batch0001 Extraction Report

## Objective

Extract a controlled recording-centered staging batch from one `SRC0002 Discos Fuentes` release without promoting any master authority or production relationship rows.

## Source

- source_id: SRC0002
- source_name: Discos Fuentes
- release: LP - 14 Cañonazos Bailables Vol 65
- source URL: https://tiendadiscosfuentes.com/productos/14-canonazos-bailables/lp-14-canonazos-bailables-vol-65/
- captured source file: data/src0002/batch0001/source_page.html
- source evidence summary: data/src0002/batch0001/SOURCE_EVIDENCE.md

## Release Metadata Captured

- release title: 14 Cañonazos Bailables Vol 65
- release interpreter: Varios Intérpretes
- genre: Tropical – Bailable
- format: LP Estereo 33 RPM | 170 Gramos
- stated content count: 14 tracks
- year: 2025
- reference number: 202450

## Extraction Results

- tracks discovered: 14
- recording candidates: 14
- song candidates: 14
- artist candidates: 18
- recording-song candidate relationships: 14
- recording-artist candidate relationships: 19
- recording-release candidate relationships: 14
- recording-source candidate relationships: 14

## Output Files

- data/src0002/batch0001/SRC0002_DISCOVERY_BATCH_0001.tsv
- data/src0002/batch0001/SOURCE_EVIDENCE.md
- data/src0002/batch0001/source_page.html
- authority/staging/src0002_batch0001_recordings.tsv
- authority/staging/src0002_batch0001_songs.tsv
- authority/staging/src0002_batch0001_artist_candidates.tsv
- relationships/staging/src0002_batch0001_recording_song.tsv
- relationships/staging/src0002_batch0001_recording_artist_candidate.tsv
- relationships/staging/src0002_batch0001_recording_release.tsv
- relationships/staging/src0002_batch0001_recording_source.tsv

## Missing Fields

- missing required fields: 0

## Duplicate Review Signals

- recording title matches in existing recordings_master: 0
- song title matches in existing songs_master: 0
- artist text matches existing performer/group authority: 1
  - Los Corraleros De Majagual -> GRP0088

These are review signals only. No candidates were promoted.

## Validation Results

| check | result |
|---|---|
| source_url_present_all_rows | PASS |
| source_id_src0002_all_rows | PASS |
| track_count_matches_source | PASS |
| recording_titles_present | PASS |
| artist_text_present_all_tracks | PASS |
| relationship_counts_match | PASS |
| no_master_tables_modified | PASS |

## Validation Status

PASS

## Review Status

staged_for_authority_review_no_promotion
