# SRC0002 BATCH0005 CLEAN PROMOTION REPORT

## UNIT-0068R

### Objective
Rebuild clean promotion for SRC0002 batch0005 from restored staging, using current clean master tables only.

### Evidence Before Promotion
- Git status before promotion: clean on main.
- Staged recordings: 50
- Staged songs: 50
- Staged artist candidates: 17
- Staged recording-song relationships: 50
- Staged recording-artist candidate relationships: 51
- Staged recording-release relationships: 50
- Staged recording-source relationships: 50

### Classification Summary
- Recordings added: 40
- Recordings matched: 10
- Songs added: 35
- Songs matched: 15 (14 existing master matches, 1 same-batch duplicate)
- Groups added: 4
- Groups matched: 4
- Performers added: 0
- Performers matched: 0
- Releases added for referential recording-release promotion: 4

### Relationships Added
- recording_song: 40
- recording_group: 11
- recording_performer: 0
- recording_release: 41
- recording_source: 41
- Total relationships added: 133

### Review-Only Candidates
- Joaquín Bedoya (performer_candidate_needs_review)
- Agustín Bedoya (performer_candidate_needs_review)
- Ricardo Ray (performer_candidate_needs_review)
- Bobby Cruz (performer_candidate_needs_review)
- Guillermo Buitrago (performer_candidate_needs_review)
- Pastor López (performer_candidate_needs_review)
- Gabriel Romero (performer_candidate_needs_review)
- Luis Felipe González (performer_candidate_needs_review)
- Varios Artistas (performer_candidate_needs_review)

### Updated Inventory Totals
- recordings_master: 5699
- songs_master: 4334
- groups_master: 278
- performers_master: 332
- releases_master: 19
- recording_song: 5699
- recording_group: 1818
- recording_performer: 3772
- recording_release: 199
- recording_source: 5701

### Validation Summary
- Promotion staging was regenerated from current masters and restored batch0005 staging TSVs.
- Dirty backup master files and dirty_master_diff.patch were not used.
- Existing master rows were not edited; production changes are append-only plus regenerated batch0005 promotion staging.
- Existing source_id values were not overwritten.
- All new authority rows use source_id SRC0002.
- All promoted recording relationships resolve to production recording, song, artist, release, and source IDs.
- recording_performer received no rows because no performer evidence was conclusive after classification.
- Duplicate relationship keys were skipped if already present, including existing links for matched batch0005 recordings.
- Validation script passed: production append-only yes, referential integrity yes, source_id overwrite no.
- git diff --check passed.

### Pre/Post Counts
- recordings_master: 5659 -> 5699
- songs_master: 4299 -> 4334
- groups_master: 274 -> 278
- performers_master: 332 -> 332
- releases_master: 15 -> 19
- recording_song: 5659 -> 5699
- recording_group: 1807 -> 1818
- recording_performer: 3772 -> 3772
- recording_release: 158 -> 199
- recording_source: 5660 -> 5701

### Commit And Git Status
- Commit hash: pending
- Git status: pending
