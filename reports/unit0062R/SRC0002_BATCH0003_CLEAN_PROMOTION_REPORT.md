# SRC0002 BATCH0003 CLEAN PROMOTION REPORT

## UNIT-0062R

### Objective
Rebuild clean promotion for SRC0002 batch0003 from restored staging, using current clean master tables only.

### Evidence Before Promotion
- Git status before promotion: clean on main.
- Staged recordings: 74
- Staged songs: 74
- Staged artist candidates: 12
- Staged recording-song relationships: 74
- Staged recording-artist candidate relationships: 76
- Staged recording-release relationships: 74
- Staged recording-source relationships: 74

### Classification Summary
- Recordings added: 73
- Recordings matched: 1
- Songs added: 63
- Songs matched: 9
- Groups added: 4
- Groups matched: 4
- Performers added: 0
- Performers matched: 0
- Releases added for referential recording-release promotion: 7

### Relationships Added
- recording_song: 73
- recording_group: 53
- recording_performer: 0
- recording_release: 74
- recording_source: 74
- Total relationships added: 274

### Review-Only Candidates
- Fruko (performer_candidate_needs_review)
- Chill Mafia y Ben Yart (performer_candidate_needs_review)
- Joe Arroyo (performer_candidate_needs_review)
- Toño Fuentes (performer_candidate_needs_review)

### Updated Inventory Totals
- recordings_master: 5599
- songs_master: 4250
- groups_master: 268
- performers_master: 332
- releases_master: 9
- recording_song: 5599
- recording_group: 1796
- recording_performer: 3772
- recording_release: 98
- recording_source: 5600

### Validation Summary
- Promotion staging was regenerated from current masters and restored batch0003 staging TSVs.
- Dirty backup master files and dirty_master_diff.patch were not used.
- Existing master rows were not edited; production changes are append-only plus regenerated batch0003 promotion staging.
- Existing source_id values were not overwritten.
- All new authority rows use source_id SRC0002.
- All promoted recording relationships resolve to production recording, song, artist, release, and source IDs.
- recording_performer received no rows because no performer evidence was conclusive after classification.
- Duplicate relationship keys were skipped, including the already-promoted recording-song and recording-group links for matched recording REC005514.

### Pre/Post Counts
- recordings_master: 5526 -> 5599
- songs_master: 4187 -> 4250
- groups_master: 264 -> 268
- performers_master: 332 -> 332
- releases_master: 2 -> 9
- recording_song: 5526 -> 5599
- recording_group: 1743 -> 1796
- recording_performer: 3772 -> 3772
- recording_release: 24 -> 98
- recording_source: 5526 -> 5600

### Commit And Git Status
- Commit hash: pending
- Git status: pending
