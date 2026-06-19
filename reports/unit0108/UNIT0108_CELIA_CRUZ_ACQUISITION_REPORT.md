# UNIT0108 CELIA CRUZ AUTHORITY ACQUISITION REPORT

## Objective

Stage Celia Cruz authority acquisition candidates for review. No master authority files were modified.

## Target

Celia Cruz

## Sources Searched

Existing project authority and staging sources were searched first:

- `authority/performers/performers_master.tsv`
- `authority/recordings/recordings_master.tsv`
- `authority/songs/songs_master.tsv`
- `authority/releases/releases_master.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_UNKNOWN.tsv`
- existing `SRC0003` / Fania local staging files under `authority/staging/src0003_batch0001_*`
- existing project reports mentioning Celia Cruz and `Celia & Johnny`

Approved external sources already represented in the project were used only through existing local artifacts. No live external promotion was performed.

## Existing Authority Inventory

| Authority type | Count | Notes |
| --- | ---: | --- |
| performers | 1 | `PER000001` Celia Cruz |
| groups | 0 | no Celia-specific group authority detected |
| linked recordings | 10 | current recordings linked to `PER000001` |
| linked songs | 10 | songs linked through Celia recordings |
| linked releases | 1 | release `REL000021` Celia & Johnny |

existing_authority_count: 22

## Acquisition Summary

| Metric | Count |
| --- | ---: |
| Celia-related unknown MP3 rows reviewed | 21 |
| unique recording candidate titles | 18 |
| new_recording_candidates | 17 |
| new_song_candidates | 17 |
| new_release_candidates | 0 |
| estimated_mp3_coverage_gain | 21 |
| promotion_ready | NO |

## Duplicate Validation

- One candidate title matched existing master authority by normalized exact title: `Perdón` matches recording `REC005595` and song `SONG004248`.
- Internal duplicate MP3 instances were detected for repeated titles, especially `Dile Que Por Mi No Tema` and `Sopita En Botella`.
- Remaining new candidate titles did not match existing master recording or song titles by normalized exact title.
- Low-confidence/noisy rows require manual review before promotion, especially `Kinshasa, October 1974` and `Super Salsa 1978 Puerto Rico`.

## Candidate Files

- `authority/staging/unit0108/UNIT0108_CELIA_CRUZ_MP3_CANDIDATES.tsv`
- `authority/staging/unit0108/UNIT0108_RECORDING_CANDIDATES.tsv`
- `authority/staging/unit0108/UNIT0108_SONG_CANDIDATES.tsv`
- `authority/staging/unit0108/UNIT0108_RELEASE_CANDIDATES.tsv`
- `authority/staging/unit0108/UNIT0108_RELATIONSHIP_CANDIDATES.tsv`
- `authority/staging/unit0108/UNIT0108_DUPLICATE_REVIEW.tsv`

## Recommendation

Do not promote this unit directly. Use the staging files for a follow-up review unit that resolves duplicate MP3 instances, corrects noisy titles, and selects only high-confidence Celia Cruz recording/song candidates for authority promotion.
