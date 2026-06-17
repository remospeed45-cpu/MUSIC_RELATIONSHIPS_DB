# UNIT-0054 Authority Source Inventory

## Objective

Inventory available authority acquisition sources after UNIT-0053 and identify the highest-value next source batch. The 13 unresolved UNIT-0053 recordings are frozen backlog items and are not included as active UNIT-0054 work.

## Repository Verification

- branch: main
- synchronized HEAD at start: 8ab821ffaa158c6a6eb644dc28e39dfeec37e6d2
- working tree before UNIT-0054 changes: clean

## Current Authority Baseline

- recordings_master: 5,502
- songs_master: 4,165
- groups_master: 250
- performers_master: 332
- missing_artist_records: 13

## Source Registry

| source_id | source_name | source_type | source_priority | current_status | repository evidence |
|---|---|---|---|---|---|
| SRC0001 | Frontera | authority | A | processed, with frozen backlog | 5,500 Peerless/Frontera rows imported and promoted through recording, song, label, source, performer, and group relationships; 13 unresolved records frozen by UNIT-0053. |
| SRC0002 | Discos Fuentes | label_catalog | A | partially processed / no acquisition dataset | Present in authority only as one group authority row, `GRP0002 Orquesta Lucho Bermudez`; no recording/song acquisition batch exists in tracked data. |
| SRC0003 | Diaz-Ayala | discography | B | partially processed / seed only | Four Sonora Matancera candidate rows exist in `imports/unit0010_sonora_matancera`; two recordings and two songs are present in master tables with SRC0003. |
| SRC0004 | MusicBrainz | reference | C | unprocessed | Registered source only; no tracked raw, import, staging, or relationship dataset. |
| SRC0005 | Discogs | reference | C | unprocessed | Registered source only; no tracked raw, import, staging, or relationship dataset. |
| SRC0006 | Cuba Canta y Baila | book | B | unprocessed | Registered source only; no tracked raw, import, staging, or relationship dataset. |

## Additional Priority Targets Not Yet Registered

`PROJECT_OVERLAY.md` lists Victor, RCA Victor, Peerless, and Musart as Priority A sources. Peerless has been handled as the SRC0001 Frontera/Peerless batch. Victor, RCA Victor, and Musart do not yet have `sources_master.tsv` rows or tracked acquisition datasets, so they require source registration before an acquisition unit can process them.

## Acquisition Queues And Staging Inventory

### Processed Source-Derived Batches

| path | rows | status |
|---|---:|---|
| imports/unit0015_frontera_peerless/UNIT0015_PEERLESS_RECORDING_RELATIONSHIP_STAGING.tsv | 5,500 | processed source import; source batch closed by UNIT-0026. |
| imports/unit0017_recording_candidates/UNIT0017_PEERLESS_RECORDING_CANDIDATES.tsv | 5,500 | processed into recordings_master by UNIT-0027. |
| imports/unit0017_recording_source/UNIT0017_RECORDING_SOURCE_STAGING.tsv | 5,500 | processed into recording_source. |
| imports/unit0018_recording_label/UNIT0018_RECORDING_LABEL_STAGING.tsv | 5,500 | processed into recording_label. |
| imports/unit0022_recording_group/UNIT0022_RECORDING_GROUP_STAGING.tsv | 1,523 | processed into recording_group and primary_group_id. |
| imports/unit0025_recording_performer/UNIT0025_RECORDING_PERFORMER_STAGING.tsv | 3,425 | processed into recording_performer and primary_performer_id. |
| imports/unit0031_recording_song/UNIT0031_RECORDING_SONG_EXACT_MATCH_STAGING.tsv | 5,502 | processed into recording_song. |
| authority/songs/staging/UNIT0030_SONG_AUTHORITY_CANDIDATES_FROM_RECORDINGS.tsv | 4,163 | processed into songs_master. |
| imports/unit0032_song_artist/UNIT0032_SONG_GROUP_STAGING.tsv | 1,461 | processed into song_group. |
| imports/unit0032_song_artist/UNIT0032_SONG_PERFORMER_STAGING.tsv | 2,865 | processed into song_performer. |
| imports/unit0036_artist_recovery/UNIT0036_RECOVERABLE_PERFORMER_TEXT.tsv | 538 | processed through recovered authority and relationship units. |
| imports/unit0037_recovered_performer_candidates/UNIT0037_RECOVERED_PERFORMER_CANDIDATES.tsv | 98 | processed through UNIT-0038 to UNIT-0045. |
| imports/unit0047a_gemini_decisions/UNIT0047A_GEMINI_DECISIONS.tsv | 42 | processed through UNIT-0048 to UNIT-0050. |
| imports/unit0049_gemini_recording_artist/UNIT0049_GEMINI_RECORDING_GROUP_STAGING.tsv | 191 | processed into recording_group where non-duplicate. |
| imports/unit0049_gemini_recording_artist/UNIT0049_GEMINI_RECORDING_PERFORMER_STAGING.tsv | 347 | processed into recording_performer where non-duplicate. |
| imports/unit0050_song_artist_refresh/UNIT0050_NEW_SONG_GROUP_STAGING.tsv | 4 | processed into song_group. |
| imports/unit0050_song_artist_refresh/UNIT0050_NEW_SONG_PERFORMER_STAGING.tsv | 321 | processed into song_performer. |

### Partially Processed Or Closed Review Artifacts

| path | rows | status |
|---|---:|---|
| imports/unit0010_sonora_matancera/UNIT0010_FIRST_RECORDING_CANDIDATES.tsv | 4 | seed Diaz-Ayala/Sonora Matancera probe; only two SRC0003 recordings are present in master tables. |
| imports/unit0034_missing_artist_review/UNIT0034_MISSING_ARTIST_REVIEW_QUEUE.tsv | 552 | superseded by UNIT-0052 and UNIT-0053; remaining 13 records are frozen backlog. |
| imports/unit0035_artist_gap_analysis/UNIT0035_ARTIST_GAP_SUMMARY.tsv | 52 | analysis artifact, not a new acquisition source. |
| exports/unit0046_gemini_review/UNIT0046_REVIEW_REQUIRED_ARTIST_CANDIDATES_FOR_GEMINI.tsv | 42 | exported review queue, then imported as UNIT0047A decisions. |
| reports/unit0053/UNIT0053_FINAL_UNRESOLVED_QUEUE.tsv | 13 | final unresolved frozen backlog, not active for UNIT-0054. |

### Empty Or Placeholder Areas

| path | rows/files | status |
|---|---:|---|
| data/raw/.gitkeep | 0 | no tracked raw source datasets. |
| data/processed/.gitkeep | 0 | no tracked processed source datasets outside TSV authorities/imports. |
| data/staging/ | 0 | empty. |
| relationships/staging/ | 0 | empty. |
| imports/unit0014b_frontera_recordings/UNIT0014B_RECORDING_RELATIONSHIP_STAGING.tsv | 0 | empty staging artifact. |
| evidence/*_evidence/*.tsv | 0 | evidence tables are header-only. |
| authority/releases/releases_master.tsv | 0 | release authority has no records. |
| relationships/recording_release.tsv | 0 | no recording-release relationships. |

## Source Value Estimates

These estimates distinguish currently tracked data from potential acquisition value. For registered sources without tracked datasets, estimated counts are directional because UNIT-0054 is an inventory unit and does not acquire external data.

| source_id | source_name | source_priority | tracked_dataset_status | estimated_recordings | estimated_songs | estimated_relationship_value |
|---|---|---|---|---:|---:|---|
| SRC0001 | Frontera | A | processed | 0 immediate new recordings from tracked data; 13 frozen unresolved backlog rows not in scope | 0 immediate new songs from tracked data | Low for UNIT-0054 because the Peerless/Frontera batch is already processed; high only if a new Frontera label slice is acquired. |
| SRC0002 | Discos Fuentes | A | no acquisition dataset yet | High potential; current repo has 0 SRC0002 recordings, and the label catalog is a priority A source | High potential; current repo has 0 SRC0002 songs | Highest remaining growth value: likely new recordings, songs, groups, performers, labels, releases, and relationships from a label catalog not yet ingested. |
| SRC0003 | Diaz-Ayala | B | seed only | Medium potential; 4 seed candidates exist, 2 SRC0003 recordings currently promoted | Medium potential, especially for historical Cuban/Caribbean discographic coverage | Strong authority corroboration value, but lower immediate growth than a new Priority A label catalog batch. |
| SRC0004 | MusicBrainz | C | no acquisition dataset yet | Medium potential but reference/corroboration oriented | Medium potential | Useful for identifiers and cross-checking, but not the best primary growth source under project source priority. |
| SRC0005 | Discogs | C | no acquisition dataset yet | Medium potential but reference/corroboration oriented | Medium potential | Useful for release and label metadata, but should corroborate rather than drive primary authority acquisition. |
| SRC0006 | Cuba Canta y Baila | B | no acquisition dataset yet | Low to medium potential until scoped; likely focused historical coverage | Low to medium potential | Good contextual/historical value, but less clearly batchable than Discos Fuentes. |
| UNASSIGNED | Victor / RCA Victor | A | not registered and no dataset | High potential after source registration | High potential after source registration | High priority target, but requires source registration and acquisition definition first. |
| UNASSIGNED | Musart | A | not registered and no dataset | High potential after source registration | High potential after source registration | High priority target, but requires source registration and acquisition definition first. |

## Processed, Partial, And Unprocessed Summary

- Processed registered sources: 1 (`SRC0001 Frontera`, current Peerless/Frontera batch)
- Partially processed registered sources: 2 (`SRC0002 Discos Fuentes`, `SRC0003 Diaz-Ayala`)
- Unprocessed registered sources: 3 (`SRC0004 MusicBrainz`, `SRC0005 Discogs`, `SRC0006 Cuba Canta y Baila`)
- Remaining registered source count: 5
- Additional unregistered Priority A source targets: 3 (`Victor`, `RCA Victor`, `Musart`)

## Inventory Conclusion

There is no large unprocessed tracked acquisition dataset waiting in the repository. The next high-value unit should therefore be an acquisition-definition/import unit, not a promotion unit. Among registered sources, `SRC0002 Discos Fuentes` has the best balance of project priority and growth potential because it is Priority A, underrepresented in current authority tables, and likely to add new recording, song, artist, label, release, and relationship coverage.
