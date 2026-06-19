# UNIT0114 Bulk Recovery Audit Report

## Objective
Convert UNIT0113 SRC0002 bulk recovery staging into a promotion-ready subset while keeping unresolved rows in review. No master authority files were modified.

## Inputs
- `authority/staging/unit0113/UNIT0113_RECORDING_CANDIDATES.tsv`
- `authority/staging/unit0113/UNIT0113_SONG_CANDIDATES.tsv`

## Outputs
- `authority/staging/unit0114/UNIT0114_PROMOTION_READY_RECORDINGS.tsv`
- `authority/staging/unit0114/UNIT0114_PROMOTION_READY_SONGS.tsv`
- `authority/staging/unit0114/UNIT0114_REVIEW_REQUIRED.tsv`

## Audit Counts
- Recording candidates audited: 300
- Song candidates audited: 300
- Promotion-ready recordings: 0
- Promotion-ready songs: 0
- Review-required candidate pairs: 300
- Expected MP3 gain after promotion: 0

## Promotion-Ready Criteria
Promotion-ready rows require all of the following:
- No existing recording or song title match in authority.
- No internal duplicate in UNIT0113.
- No title parse conflict, including embedded `Feat.` or separator artifacts.
- Complete structured tracklist evidence.
- Resolved performer or group authority ID.
- Resolved release authority ID.

No UNIT0113 candidate passed all promotion gates.

## Review Required Classification
| Review Class | Candidate Pairs |
|---|---:|
| duplicate | 122 |
| title_conflict | 10 |
| performer_conflict | 159 |
| release_conflict | 9 |
| other | 0 |

## Review Source Status
| Source Tracklist Status | Candidate Pairs |
|---|---:|
| complete_or_exceeds_track_count | 159 |
| partial_10_of_15 | 130 |
| partial_11_of_30 | 11 |

## Notes
The UNIT0113 bulk inventory remains high-yield, but none of the 300 candidate pairs is promotion-ready under strict authority rules. Most rows are blocked by unresolved performers/groups or exact authority duplicates. The two otherwise clean Afrosound rows contain featured-artist text in the title field and must be normalized before promotion.

Existing title matches were classified as duplicates even when a later promotion unit might reuse those songs for release/recording relationship enrichment.

## Final Conclusion
READY_FOR_PROMOTION = NO

Blockers:
- 122 candidate pairs have existing authority title matches.
- 159 candidate pairs have unresolved performer/group authority assignment.
- 10 candidate pairs have title normalization conflicts involving featured artists or parse separators.
- 9 candidate pairs have release/source completeness conflicts.
