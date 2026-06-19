# UNIT0110 CELIA CRUZ PROMOTION REPORT

## Objective

Promote approved UNIT0109 Celia Cruz candidates into master authority files.

## Input

- `authority/staging/unit0109/UNIT0109_PROMOTION_READY.tsv`

## Backups

- `authority/backups/unit0110/recordings_master.before_unit0110.tsv`
- `authority/backups/unit0110/songs_master.before_unit0110.tsv`

## Master Files Updated

- `authority/recordings/recordings_master.tsv`
- `authority/songs/songs_master.tsv`

## Promotion Summary

| Metric | Count |
| --- | ---: |
| recordings_added | 13 |
| songs_added | 13 |
| mp3_instances_represented | 16 |
| previous_recordings_total | 5897 |
| new_recordings_total | 5910 |
| previous_songs_total | 4473 |
| new_songs_total | 4486 |

## Added ID Ranges

| Authority | First ID | Last ID |
| --- | --- | --- |
| recordings | `REC005898` | `REC005910` |
| songs | `SONG004474` | `SONG004486` |

## Coverage Estimate

UNIT0106 strict baseline:

- `known_recordings = 108`
- `total_mp3_scanned = 2072`
- `coverage_percent = 5.21%`

UNIT0110 estimated coverage after promotion:

- `estimated_known_recordings = 124`
- `total_mp3_scanned = 2072`
- `estimated_coverage_percent = 5.98%`
- `estimated_coverage_gain = +16 MP3 instances`
- `estimated_coverage_gain_points = +0.77 percentage points`

## Validation

| Check | Result |
| --- | --- |
| no duplicate recording_ids | PASS |
| no duplicate song_ids | PASS |
| no broken recording -> song references | PASS |
| no broken recording -> performer references | PASS |
| no broken recording -> group references | PASS |
| no broken recording -> release references | PASS |

## Output Files

- `authority/staging/unit0110/UNIT0110_RECORDINGS_ADDED.tsv`
- `authority/staging/unit0110/UNIT0110_SONGS_ADDED.tsv`

## Notes

- No release authority rows were added in this unit because UNIT0109 promotion-ready rows did not include release evidence.
- Review-required UNIT0109 rows were not promoted.
