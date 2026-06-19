# UNIT0112 HIGH-VOLUME AUTHORITY STRATEGY

## Objective

Stop artist-by-artist acquisition and identify the highest-volume local source pools available for bulk authority expansion.

## Current Source Inventory

Approved source registry:

| Source | Name | Type | Priority | Current local status |
| --- | --- | --- | --- | --- |
| SRC0001 | Frontera | authority | A | Existing authority source, no local PDF inventory found in this repository |
| SRC0002 | Discos Fuentes | label_catalog | A | Largest structured local inventory and staging pool |
| SRC0003 | Diaz-Ayala / Fania local artifacts | discography | B | Multiple harvested tracklists and promotion staging files |
| SRC0004 | MusicBrainz | reference | C | Approved reference source, no high-volume local harvested pool found |
| SRC0005 | Discogs | reference | C | Approved reference source, no high-volume local harvested pool found |
| SRC0006 | Cuba Canta y Baila | book | B | Approved source, no local PDF inventory found in this repository |

PDF inventory:

- Local PDFs found under this repository: 0

Harvested tracklists found:

- `data/src0003/batch0002/SRC0003_BATCH0002_ACID_TRACKLIST.tsv` - 8 tracks
- `data/src0003/batch0002/SRC0003_BATCH0002_ASI_SE_COMPONE_UN_SON_TRACKLIST.tsv` - 10 tracks
- `data/src0003/batch0002/SRC0003_BATCH0002_DE_TI_DEPENDE_TRACKLIST.tsv` - 8 tracks
- `data/src0003/batch0002/SRC0003_BATCH0002_ESTE_ES_ISMAEL_MIRANDA_TRACKLIST.tsv` - 7 tracks
- `data/src0003/batch0002/SRC0003_BATCH0002_LA_VOZ_TRACKLIST.tsv` - 8 tracks
- `data/src0003/batch0002/SRC0003_BATCH0002_SALSA_LARRY_HARLOW_TRACKLIST.tsv` - 5 tracks
- `data/src0003/unit0086_fania_bulk/UNIT0086_REY_DEL_BAJO_TRACKLIST.tsv` - 8 tracks

Authority staging pools found:

- SRC0002 batch staging: 208 historical staged recording rows across batches 0001-0005.
- SRC0003 batch0001 staging: 51 staged recording rows.
- SRC0003 batch0002 candidate staging: 44 staged candidate rows.
- Cheo Feliciano staging: 36 candidate rows.
- Bobby Valentin / Rey Del Bajo staging: 8 candidate rows.
- UNIT0108-UNIT0110 Celia Cruz staging/promotion: completed focused promotion path.

Acquisition reports found:

- SRC0002 acquisition/extraction/promotion reports: units 0055-0069.
- SRC0003 discovery/extraction/promotion reports: units 0069-0078, 0084-0088, 0100-0104.
- Cheo Feliciano acquisition/promotion reports: units 0079-0083, 0089-0094.
- MP3 coverage and target reports: units 0105-0111.

## Ranking Method

Sources were ranked by:

- estimated_new_recordings
- estimated_new_songs
- automation_level
- effort_required
- expected MP3 coverage leverage from current UNIT0105 unknown rows

Automation levels:

- High: structured TSV inventory or tracklists already available.
- Medium: structured report exists, but extraction/normalization still required.
- Low: source exists conceptually but lacks local structured artifacts.

Effort:

- Low: candidate rows can be generated from existing TSVs.
- Medium: extraction plus validation required.
- High: source acquisition or OCR/parsing required.

## TOP_10_HIGHEST_YIELD_EXPANSION_OPPORTUNITIES

| Rank | Opportunity | Source pool | estimated_new_recordings | estimated_new_songs | automation_level | effort_required | expected_mp3_coverage_gain | Rationale |
| ---: | --- | --- | ---: | ---: | --- | --- | ---: | --- |
| 1 | Complete SRC0002 Discos Fuentes remaining inventory | `reports/unit0066/REMAINING_RAW.tsv` | 297 | 297 | High | Medium | up to 191 candidate MP3 rows | Largest structured source pool and strongest overlap with unknown MP3 evidence |
| 2 | SRC0002 current remaining queue | `reports/unit0066/SRC0002_REMAINING_INVENTORY.tsv` | 143 | 143 | High | Low-Medium | high | Smaller, cleaner subset of remaining Fuentes inventory |
| 3 | SRC0002 high-rank remaining releases | HIGH rows in `REMAINING_RAW.tsv` | 99 | 99 | High | Medium | high | Prioritizes source-ranked high-value Fuentes collections |
| 4 | SRC0002 medium-rank remaining releases | MEDIUM rows in `REMAINING_RAW.tsv` | 120 | 120 | High | Medium | medium-high | Large structured pool with moderate authority value |
| 5 | SRC0002 batch0003-style expansion model | existing 74-row batch pattern | 74 | 74 | High | Low | medium | Proven extraction/promotion pattern already exists |
| 6 | SRC0003/Fania harvested tracklist leftovers | `authority/staging/unit0104/UNIT0104_SRC0003_TRACKLIST_COVERAGE.tsv` | 1-8 | 1-8 | High | Low | low-medium | Nearly exhausted but easy to close |
| 7 | SRC0003 new Fania release harvesting | existing Fania text/tracklist workflow | 50-100 | 50-100 | Medium | Medium | medium | Workflow exists, but new release selection is needed |
| 8 | Cheo Feliciano unresolved/extended candidates | `authority/staging/unit0083/UNIT0083_CHEO_PROMOTION_CANDIDATES.tsv` | up to 36 | up to 36 | Medium | Medium | medium | Existing candidate file, but artist-specific and less aligned with stop-artist-by-artist goal |
| 9 | SRC0003 batch0002 candidate cleanup | `authority/staging/src0003_batch0002_*_candidates.tsv` | up to 44 | up to 44 | Medium | Medium | low-medium | Several rows already promoted; cleanup yield is limited |
| 10 | PDF/OCR source expansion | all PDFs | 0 local | 0 local | Low | High | unknown | No local PDFs found in this repository; not actionable until source files are present |

## Recommended Bulk Target

NEXT_BULK_ACQUISITION_TARGET:

- Complete SRC0002 Discos Fuentes remaining inventory from `reports/unit0066/REMAINING_RAW.tsv`.

Reason:

- Highest estimated authority yield: 297 recordings and 297 songs.
- Strongest known MP3 overlap: 191 current unknown MP3 rows match Fuentes/SRC0002-adjacent labels, artists, or genre terms.
- Existing extraction, staging, promotion, and cleanup patterns already exist from SRC0002 units 0055-0069.
- This target stops artist-by-artist expansion and works by structured source inventory.

## Expected Gains

For the recommended bulk target:

| Metric | Estimate |
| --- | ---: |
| expected_recordings_gain | 297 |
| expected_song_gain | 297 |
| expected_mp3_coverage_gain | up to 191 candidate MP3 rows |

Conservative strict coverage note:

- The actual strict coverage gain will depend on whether promoted recording titles match UNIT0105 `candidate_title` values exactly after normalization.
- Based on UNIT0111, scanner-title mismatch can reduce realized coverage.
- Recommended next bulk unit should include a title-normalization pass before promotion to preserve the high expected coverage gain.

## Execution Recommendation

Next unit should not acquire a single artist.

Recommended next unit:

- Build `SRC0002_REMAINING_RAW_BULK_PROMOTION_PREP` from `reports/unit0066/REMAINING_RAW.tsv`.

Required steps:

1. Normalize all 22 remaining release inventory rows.
2. Generate release, recording, song, performer/group, and source relationship candidates.
3. Match candidates against current master authority before promotion.
4. Prioritize rows whose titles appear in UNIT0105 unknown MP3 scan evidence.
5. Produce promotion-ready and review-required splits before any master authority update.
