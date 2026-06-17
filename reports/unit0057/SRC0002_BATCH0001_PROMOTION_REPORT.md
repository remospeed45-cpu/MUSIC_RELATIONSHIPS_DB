# UNIT-0057 SRC0002 Batch0001 Promotion Report

## Scope

Source: SRC0002 Discos Fuentes
Batch: batch0001
Release: LP - 14 Canonazos Bailables Vol 65
Source URL: https://tiendadiscosfuentes.com/productos/14-canonazos-bailables/lp-14-canonazos-bailables-vol-65/

UNIT-0057 reviewed the validated UNIT-0056 staging files and promoted only entities supported by exact repository validation and current source evidence. No performer identities were guessed from artist text.

## Candidate Classification

| Candidate type | Count |
|---|---:|
| Recording candidates reviewed | 14 |
| Recording candidates classified NEW | 14 |
| Recording candidates matched existing | 0 |
| Song candidates reviewed | 14 |
| Song candidates classified NEW | 14 |
| Song candidates matched existing | 0 |
| Artist candidates reviewed | 18 |
| Artist candidates classified NEW | 9 |
| Artist candidates matched existing | 1 |
| Artist candidates requiring review | 8 |

## Promoted Entities

| Entity | Added | Matched |
|---|---:|---:|
| Recordings | 14 | 0 |
| Songs | 14 | 0 |
| Groups | 9 | 1 |
| Performers | 0 | 0 |
| Releases | 1 | 0 |

New groups: Los Cumbia Stars, The Latin Brothers, VEBA, AEME, La Sonora Dinamita, Los 50 De Joselito, Afrosound, Los Conquistadores De La Salsa, Los Titanes.

Matched group: Los Corraleros De Majagual -> GRP0088.

Review-required artist candidates retained in staging only: La Delio Valdez, Yeison Landero, Esparragoza, Yandar Y Yostin, J Kalder, Santibel, Chesca, Maldy.

## Promoted Relationships

| Relationship table | Rows added |
|---|---:|
| recording_song | 14 |
| recording_group | 11 |
| recording_performer | 0 |
| recording_source | 14 |
| recording_release | 14 |
| Total production relationships | 53 |

Notes:

- `recording_song` rows use `primary_song` because each staged track title produced one validated song candidate.
- `recording_group` rows use `credited_group` and were created only for artist candidates classified as `group_candidate` or matched to an existing group.
- `recording_source` rows preserve per-track source references from the Discos Fuentes product page.
- `recording_release` rows link all 14 recordings to the promoted release `REL000001`.

## Updated Inventory Totals

| Inventory | Total |
|---|---:|
| recordings_master | 5516 |
| songs_master | 4179 |
| groups_master | 259 |
| performers_master | 332 |
| releases_master | 1 |
| recording_song | 5516 |
| recording_group | 1728 |
| recording_performer | 3772 |
| recording_source | 5516 |
| recording_release | 14 |

## Validation Summary

PASS:

- No exact normalized recording title matches were found in `recordings_master.tsv` for the 14 batch recordings.
- No exact normalized song title matches were found in `songs_master.tsv` for the 14 batch songs.
- One exact normalized group match was found: `Los Corraleros De Majagual -> GRP0088`.
- No duplicate primary IDs were introduced in recordings, songs, groups, performers, or releases.
- All production relationship foreign keys resolve to existing master records.
- Review-only artist candidates remain documented in `authority/staging/src0002_batch0001_artist_promotion.tsv` and were not promoted.

## Files Produced

- `authority/staging/src0002_batch0001_recording_promotion.tsv`
- `authority/staging/src0002_batch0001_song_promotion.tsv`
- `authority/staging/src0002_batch0001_artist_promotion.tsv`
- `reports/unit0057/SRC0002_BATCH0001_PROMOTION_REPORT.md`
