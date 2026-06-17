# UNIT-0059 SRC0002 Batch0002 Promotion Report

## Scope

Source: SRC0002 Discos Fuentes
Batch: batch0002
Release: LP - La Cumbia Une a Latinoamérica | Los Cumbia Stars
Source URL: https://tiendadiscosfuentes.com/productos/vinilos/lp-la-cumbia-une-a-latinoamerica/

UNIT-0059 validated batch0002 staging and promoted only source-supported production authority records and relationships. The frozen unresolved backlog was not modified.

## Candidate Classification

| Candidate type | NEW | MATCH_EXISTING | REVIEW_REQUIRED |
|---|---:|---:|---:|
| Recordings | 10 | 0 | 0 |
| Songs | 8 | 2 | 0 |
| Artist candidates | 5 | 1 | 4 |
| Releases | 1 | 0 | 0 |
| Labels | 1 | 0 | 0 |

Matched songs: Amapola -> SONG000155, Tierra Mala -> SONG003751.

Matched artist: Los Cumbia Stars -> GRP0251.

New groups: Los Mirlos, La Ronda Bogotá, C4 Trío, Onda Sabanera, Cumbia Club.

Review-only candidates: Papaya Dada, Pascual Ilabaca, Alemor, Aye Alfonso.

## Promotion Summary

| Entity | Added | Matched |
|---|---:|---:|
| Recordings | 10 | 0 |
| Songs | 8 | 2 |
| Groups | 5 | 1 |
| Performers | 0 | 0 |
| Releases | 1 | 0 |
| Labels | 1 | 0 |

Notes:

- `Amapola` and `Tierra Mala` reused existing song authority rows by exact normalized title.
- Batch recording title matches for `Amapola` and `Tierra Mala` were not reused as recordings because existing records are SRC0001/Peerless-derived recordings with different artist/source/release context.
- Performer candidate names were retained for review and not inserted as performers.

## Promoted Relationships

| Relationship table | Rows added |
|---|---:|
| recording_song | 10 |
| recording_group | 15 |
| recording_performer | 0 |
| recording_source | 10 |
| recording_release | 10 |
| Total production relationships | 45 |

## Updated Inventory Totals

| Inventory | Total |
|---|---:|
| recordings_master | 5526 |
| songs_master | 4187 |
| groups_master | 264 |
| performers_master | 332 |
| recording_song | 5526 |
| recording_group | 1743 |
| recording_performer | 3772 |
| recording_source | 5526 |
| recording_release | 24 |
| releases_master | 2 |
| labels_master | 3 |

## Validation Summary

PASS:

- Reviewed all batch0002 recording, song, artist, and relationship staging rows.
- Detected existing recordings, songs, performers, groups, releases, and labels before insertion.
- No duplicate primary IDs were introduced.
- New recording rows resolve to valid song, group, release, and label IDs.
- Production relationship foreign keys resolve to master records.
- Source traceability was preserved through `recording_source` and `recording_release` rows.
- Review-only artist candidates remain documented in `authority/staging/src0002_batch0002_artist_promotion.tsv`.

## Files Produced

- `authority/staging/src0002_batch0002_recording_promotion.tsv`
- `authority/staging/src0002_batch0002_song_promotion.tsv`
- `authority/staging/src0002_batch0002_artist_promotion.tsv`
- `reports/unit0059/SRC0002_BATCH0002_PROMOTION_REPORT.md`
