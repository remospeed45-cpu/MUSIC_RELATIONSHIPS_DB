# SRC0003 BATCH0001 CLEAN PROMOTION REPORT

## UNIT-0071

### Objective
Clean promote SRC0003 batch0001 from restored staging, using current clean master tables only.

### Evidence Before Promotion
- Git status before promotion: clean on main.
- Staged recordings: 51
- Staged songs: 51
- Staged artist candidates: 13
- Staged recording-song relationships: 51
- Staged recording-artist candidate relationships: 103
- Staged recording-release relationships: 51
- Staged recording-source relationships: 51
- Evidence fields present for all applicable staging rows: source_id, source_reference, evidence_text, confidence, review_status.
- All staging source_id values: SRC0003.
- All authority staging source_name values: Fania Records.
- Source authority note: staging source_name is Fania Records, while current sources_master names SRC0003 as Diaz-Ayala; no existing source row was edited.

### Classification Summary
- Recordings added: 51
- Recordings matched: 0
- Songs added: 48
- Songs matched: 3 (3 existing master matches, 0 same-batch duplicates)
- Groups added: 1
- Groups matched: 0
- Performers added: 0
- Performers matched: 1
- Releases added for referential recording-release promotion: 7

### Relationships Added
- recording_song: 51
- recording_group: 10
- recording_performer: 12
- recording_release: 51
- recording_source: 51
- Total relationships added: 175

### Review-Only Candidates
- Willie Colón (performer_candidate_needs_review)
- Rubén Blades (performer_candidate_needs_review)
- Johnny Pacheco (performer_candidate_needs_review)
- Ismael Miranda (performer_candidate_needs_review)
- Santos Colón (performer_candidate_needs_review)
- Pete "Conde" Rodríguez (performer_candidate_needs_review)
- Héctor Lavoe (performer_candidate_needs_review)
- Bobby Cruz (performer_candidate_needs_review)
- Ismael Quintana (performer_candidate_needs_review)
- Justo Betancourt (performer_candidate_needs_review)
- Cheo Feliciano (performer_candidate_needs_review)

### Updated Inventory Totals
- recordings_master: 5750
- songs_master: 4382
- groups_master: 279
- performers_master: 332
- releases_master: 26
- recording_song: 5750
- recording_group: 1828
- recording_performer: 3784
- recording_release: 250
- recording_source: 5752

### Validation Summary
- Promotion staging was generated from current masters and restored SRC0003 batch0001 staging TSVs.
- Dirty backup master files were not used.
- Existing master rows were not edited; production changes are append-only plus generated batch0001 promotion staging.
- Existing source_id values were not overwritten.
- New authority rows use source_id SRC0003 to preserve staging traceability.
- Fania All Stars was promoted as a conclusive group; Fania All-Stars is stored as an alternate name on the new group row.
- Celia Cruz matched existing performer authority PER000001.
- No new performers were created.
- Other named performer candidates remained REVIEW_REQUIRED unless current repo had clear performer authority.
- recording_group was promoted only for conclusive group evidence.
- recording_performer was promoted only for conclusive matched performer evidence.
- All promoted recording relationships resolve to production recording, song, artist, release, and source IDs.
- Validation script passed: production append-only yes, referential integrity yes, source_id overwrite no.
- git diff --check passed.

### Pre/Post Counts
- recordings_master: 5699 -> 5750
- songs_master: 4334 -> 4382
- groups_master: 278 -> 279
- performers_master: 332 -> 332
- releases_master: 19 -> 26
- recording_song: 5699 -> 5750
- recording_group: 1818 -> 1828
- recording_performer: 3772 -> 3784
- recording_release: 199 -> 250
- recording_source: 5701 -> 5752

### Commit And Git Status
- Promotion commit hash: 0ba26e4
- Git status after push verification: clean
