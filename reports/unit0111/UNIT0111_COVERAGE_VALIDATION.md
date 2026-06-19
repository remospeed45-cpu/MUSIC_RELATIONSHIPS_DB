# UNIT0111 POST-PROMOTION COVERAGE VALIDATION

## Objective

Measure the real MP3 coverage impact of UNIT0110 after promoting Celia Cruz authority candidates.

## Inputs

- `authority/recordings/recordings_master.tsv`
- `authority/songs/songs_master.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_SCAN_ALL.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_KNOWN_RECORDINGS.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_PROBABLE_SONGS.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_UNKNOWN.tsv`

## Method

Coverage was recalculated using the same title matching rule used by `tools/unit0105/unit0105_safe_mp3_scanner.py`:

- normalize `candidate_title`
- match against normalized `canonical_recording_title`
- count recording-title matches as strict known coverage
- song-title-only matches remain probable and are not counted as strict coverage

## Coverage Results

| Metric | Value |
| --- | ---: |
| total_mp3_scanned | 2072 |
| matched_mp3_before | 108 |
| matched_mp3_after | 115 |
| previous_coverage_percent | 5.21% |
| current_coverage_percent | 5.55% |
| coverage_delta | +0.34 percentage points |

## UNIT0110 Gain Validation

| Metric | Value |
| --- | ---: |
| estimated_mp3_gain_from_UNIT0110 | 16 |
| actual_mp3_gain_after_recalculation | 7 |
| estimated_gain_achieved | NO |

UNIT0110 promoted 13 recording titles representing 16 staged MP3 instances, but only 7 MP3 rows became strict recording-title matches under the UNIT0105 scanner logic.

New strict matches attributable to UNIT0110:

| scan_id | candidate_title | file_name |
| --- | --- | --- |
| `bf60888821c4d19a` | Guede Zaina | 02. Celia Cruz - Guede Zaina.mp3 |
| `3df053f662f1b4c4` | Guede Zaina | 045. Guede Zaina.mp3 |
| `35d9962350ff41f3` | Juancito Trucupey | 038. Juancito Trucupey.mp3 |
| `99490961463d1740` | Rock and Roll | 08 Celia Cruz & La Sonora Matancera - Rock and Roll.mp3 |
| `6f4e764fcd708a36` | Usted Abusó | 082. Usted Abusó.mp3 |
| `43a88abd3fee5365` | Sopita En Botella | 08. Celia Cruz - Sopita En Botella.mp3 |
| `9d91f5c642aa8d7f` | Dile Que Por Mi No Tema | 09. Celia Cruz - Dile Que Por Mi No Tema.mp3 |

## Why Estimate Was Not Fully Achieved

Several UNIT0110 promoted titles did not match the scan rows because the UNIT0105 `candidate_title` field often preserved artist text or extra context. Examples include rows where the candidate title contains artist-plus-title rather than title-only.

This means future target selection should favor rows where `candidate_title` is already a clean title string, or a future scanner normalization unit should improve title extraction before promotion.

## Next Target Analysis

Remaining high-priority targets were reviewed for clean `candidate_title` rows, because clean candidate-title rows are more likely to convert into immediate strict coverage gains.

| Target | target_mentions | clean_candidate_title_rows | Notes |
| --- | ---: | ---: | --- |
| Rufo Garrido | 16 | 13 | Strongest clean-title signal among reviewed high-priority targets |
| Sonora Ponceña | 22 | 9 | Good potential, but group authority setup needed |
| Joe Arroyo | 19 | 2 | Many rows preserve artist text in candidate title |
| Ismael Rivera | 16 | 2 | Some clean rows, but lower immediate yield |
| Fernando Villalona | 9 | 2 | Lower immediate yield |
| Willie Colón | 29 | 1 | High raw mentions but poor clean-title matchability |
| Ray Barretto | 10 | 0 | Poor clean-title matchability under current scanner logic |
| Francisco Canaro | 15 | 0 | Poor clean-title matchability under current scanner logic |
| Tito Rojas | 11 | 0 | Poor clean-title matchability under current scanner logic |

NEXT_TARGET_ARTIST:

- Rufo Garrido

Reason:

- Highest clean candidate-title count among reviewed high-impact targets.
- Expected to produce a better real strict-coverage conversion than Celia Cruz under current UNIT0105 scanner rules.

## Recommendation

Proceed with a Rufo Garrido acquisition/prep/promotion sequence, or first improve title normalization in the MP3 scan pipeline if the goal is to recover artist-plus-title rows without requiring exact title-only candidate strings.
