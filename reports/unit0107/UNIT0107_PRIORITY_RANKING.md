# UNIT0107 HIGH IMPACT AUTHORITY EXPANSION PRIORITIES

## Objective

Rank high-impact authority expansion targets from UNIT0106 unknown MP3 coverage data.

## Inputs

- `reports/unit0106/UNIT0106_TOP_UNKNOWN_ARTISTS.tsv`
- `reports/unit0106/UNIT0106_TOP_UNKNOWN_FOLDERS.tsv`

## Method

Target coverage potential uses the UNIT0106 unknown MP3 count for each named artist.

Authority presence was measured against:

- `authority/recordings/recordings_master.tsv`
- `authority/songs/songs_master.tsv`
- `authority/performers/performers_master.tsv`
- `authority/groups/groups_master.tsv`
- `authority/releases/releases_master.tsv`

Linked authority counts are based on recordings where `primary_performer_id` or `primary_group_id` resolves to the target artist/group.

Effort score:

- `1.0`: target performer/group exists and has linked recordings.
- `2.0`: target has a release/name seed but no linked performer/group authority.
- `3.0`: target has no detected performer/group/release seed.

`expected_new_recordings_per_effort = unknown_mp3 / effort_score`

## Authority Presence

| Target | unknown_mp3 | performers | groups | linked_recordings | linked_songs | linked_releases | release_name_seed | effort_score | expected_new_recordings_per_effort |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Celia Cruz | 10 | 1 | 0 | 10 | 10 | 1 | 0 | 1.0 | 10.00 |
| Ray Barretto | 9 | 1 | 0 | 8 | 8 | 1 | 0 | 1.0 | 9.00 |
| Joe Arroyo | 12 | 0 | 0 | 0 | 0 | 0 | 1 | 2.0 | 6.00 |
| Willie Colón | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 4.33 |
| Rufo Garrido | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 3.33 |
| Francisco Canaro | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 3.33 |
| Tito Rojas | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 3.00 |
| Sonora Ponceña | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 3.00 |
| Ismael Rivera | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 3.00 |
| Fernando Villalona | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 3.0 | 3.00 |

## Priority Ranking

| Rank | Target | expected_new_recordings_per_effort | likely_new_recordings | Rationale |
| ---: | --- | ---: | ---: | --- |
| 1 | Celia Cruz | 10.00 | 10 | Existing performer authority and linked recordings make this the fastest high-confidence coverage gain. |
| 2 | Ray Barretto | 9.00 | 9 | Existing performer authority and linked recordings reduce setup effort. |
| 3 | Joe Arroyo | 6.00 | 12 | Largest non-seeded target after Willie Colón, with a release title seed already present. |
| 4 | Willie Colón | 4.33 | 13 | Highest raw unknown count, but no detected authority seed increases setup effort. |
| 5 | Rufo Garrido | 3.33 | 10 | Solid raw gain, no detected authority seed. |
| 6 | Francisco Canaro | 3.33 | 10 | Solid raw gain, no detected authority seed. |
| 7 | Tito Rojas | 3.00 | 9 | Moderate raw gain, no detected authority seed. |
| 8 | Sonora Ponceña | 3.00 | 9 | Moderate raw gain, no detected authority seed; group authority must be established first. |
| 9 | Ismael Rivera | 3.00 | 9 | Moderate raw gain, no detected authority seed. |
| 10 | Fernando Villalona | 3.00 | 9 | Moderate raw gain, no detected authority seed. |

## Recommendations

NEXT_SINGLE_ARTIST_TARGET:

- Celia Cruz

Reason:

- Highest expected new recordings per effort.
- Existing performer authority (`PER000001`) and linked recording base allow controlled expansion without first creating core identity authority.
- Expected strict coverage gain from target rows: up to 10 MP3 files.

NEXT_BATCH_TARGET:

- Celia Cruz
- Ray Barretto
- Joe Arroyo
- Willie Colón

Reason:

- This combines the two fastest seeded targets with the two largest raw-gain targets.
- Expected strict coverage gain from target rows: up to 44 MP3 files.
- The batch balances fast wins with setup of missing high-value authority identities.

## Expected Coverage Gain

Current UNIT0106 strict coverage:

- `known_recordings = 108`
- `total_mp3_scanned = 2072`
- `coverage_percent = 5.21%`

Recommended single target expected gain:

- `+10` known recordings if all Celia Cruz unknown rows are promoted to recording-level authority.
- Projected known recordings: `118`
- Projected coverage: `5.69%`
- Coverage increase: `+0.48 percentage points`

Recommended batch expected gain:

- `+44` known recordings if all recommended batch unknown rows are promoted to recording-level authority.
- Projected known recordings: `152`
- Projected coverage: `7.34%`
- Coverage increase: `+2.12 percentage points`

## Next Unit

Run a single-artist controlled promotion for Celia Cruz before attempting the broader batch. Use the batch target list only after confirming the UNIT0107 scoring approach produces clean authority additions.
