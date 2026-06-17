# UNIT-0070 SRC0003 Batch0001 Extraction Report

## Objective
Extract a controlled recording-centered staging batch from seven `SRC0003 Fania Records` releases without promoting any master authority or production relationship rows.

## Source
- source_id: SRC0003
- source_name: Fania Records
- releases: 7 (Siembra, Celia & Johnny, Live At Yankee Stadium Vol. 1 & 2, Cosa Nuestra, Asalto Navideño, El Juicio)
- source URL: various fania.com product pages
- captured source script: scripts/unit0070_staging.py

## Extraction Results
- tracks discovered: 51
- recording candidates: 51
- song candidates: 51
- artist candidates: 13
- recording-song candidate relationships: 51
- recording-artist candidate relationships: 103
- recording-release candidate relationships: 51
- recording-source candidate relationships: 51

## Output Files
- authority/staging/src0003_batch0001_recordings.tsv
- authority/staging/src0003_batch0001_songs.tsv
- authority/staging/src0003_batch0001_artist_candidates.tsv
- relationships/staging/src0003_batch0001_recording_song.tsv
- relationships/staging/src0003_batch0001_recording_artist_candidate.tsv
- relationships/staging/src0003_batch0001_recording_release.tsv
- relationships/staging/src0003_batch0001_recording_source.tsv

## Missing Fields
- missing required fields: 0

## Duplicate Review Signals
- recording title matches in existing recordings_master: 0
- song title matches in existing songs_master: 0
- artist text matches existing performer/group authority: 1
  - Celia Cruz -> PER000001

## Validation Results
| check | result |
|---|---|
| source_url_present_all_rows | PASS |
| source_id_src0003_all_rows | PASS |
| track_count_matches_source | PASS |
| recording_titles_present | PASS |
| artist_text_present_all_tracks | PASS |
| relationship_counts_match | PASS |
| no_master_tables_modified | PASS |

## Validation Status
PASS

## Review Status
staged_for_authority_review_no_promotion
