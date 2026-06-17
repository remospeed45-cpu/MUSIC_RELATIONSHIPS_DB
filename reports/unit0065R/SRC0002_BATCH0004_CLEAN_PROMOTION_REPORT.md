# SRC0002 BATCH0004 CLEAN PROMOTION REPORT

## UNIT-0065R

### Objective
Rebuild clean promotion for SRC0002 batch0004 from restored staging, using current clean master tables only.

### Evidence Before Promotion
- Git status before promotion: clean on main.
- Staged recordings: 60
- Staged songs: 60
- Staged artist candidates: 20
- Staged recording-song relationships: 60
- Staged recording-artist candidate relationships: 60
- Staged recording-release relationships: 60
- Staged recording-source relationships: 60

### Classification Summary
- Recordings added: 60
- Recordings matched: 0
- Songs added: 49
- Songs matched: 11
- Groups added: 6
- Groups matched: 3
- Performers added: 0
- Performers matched: 0
- Releases added for referential recording-release promotion: 6

### Relationships Added
- recording_song: 60
- recording_group: 11
- recording_performer: 0
- recording_release: 60
- recording_source: 60
- Total relationships added: 191

### Review-Only Candidates
- Varios Intérpretes (performer_candidate_needs_review)
- Helenita Vargas (performer_candidate_needs_review)
- Guillermo Portabales (performer_candidate_needs_review)
- Celina y Reutilio (performer_candidate_needs_review)
- Roberto Ledesma (performer_candidate_needs_review)
- Orlando Contreras (performer_candidate_needs_review)
- Varios Artistas (performer_candidate_needs_review)
- Pacho Galán (performer_candidate_needs_review)
- Lito Barrientos (performer_candidate_needs_review)
- Clímaco Sarmiento (performer_candidate_needs_review)
- Pedro Laza (performer_candidate_needs_review)

### Updated Inventory Totals
- recordings_master: 5659
- songs_master: 4299
- groups_master: 274
- performers_master: 332
- releases_master: 15
- recording_song: 5659
- recording_group: 1807
- recording_performer: 3772
- recording_release: 158
- recording_source: 5660

### Validation Summary
- Promotion staging was regenerated from current masters and restored batch0004 staging TSVs.
- Dirty backup master files and dirty_master_diff.patch were not used.
- Existing master rows were not edited; production changes are append-only plus regenerated batch0004 promotion staging.
- Existing source_id values were not overwritten.
- All new authority rows use source_id SRC0002.
- All promoted recording relationships resolve to production recording, song, artist, release, and source IDs.
- recording_performer received no rows because no performer evidence was conclusive after classification.
- Duplicate relationship keys were skipped if already present; batch0004 had no matched recordings.
- Validation script passed: production append-only yes, referential integrity yes, source_id overwrite no.
- git diff --check passed.

### Pre/Post Counts
- recordings_master: 5599 -> 5659
- songs_master: 4250 -> 4299
- groups_master: 268 -> 274
- performers_master: 332 -> 332
- releases_master: 9 -> 15
- recording_song: 5599 -> 5659
- recording_group: 1796 -> 1807
- recording_performer: 3772 -> 3772
- recording_release: 98 -> 158
- recording_source: 5600 -> 5660

### Commit And Git Status
- Promotion commit hash: e5d219c
- Git status after push verification: clean
