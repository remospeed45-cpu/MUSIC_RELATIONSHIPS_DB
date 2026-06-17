# UNIT-0027 Recording Promotion Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0027
Action: Promote Peerless staged recordings into recordings master

Source staging:
- authority/recordings/staging/UNIT0027_PEERLESS_RECORDINGS_PROMOTION_STAGING.tsv

Target master:
- authority/recordings/recordings_master.tsv

Counts:
- Master rows before promotion: 2
- Staged rows reviewed: 5500
- Duplicate staged IDs skipped: 0
- Rows promoted: 5500
- Master rows after promotion: 5502
- Duplicate IDs after promotion: 0
- TSV validation bad rows: 0

Promotion Rules:
- Preserve recording-centric model.
- Preserve recording_id from candidate extraction.
- Preserve canonical recording title from staging.
- Preserve label_id LBL000003.
- Preserve source_id SRC0001 from Frontera extraction.
- Set review_status from staged to approved on promoted rows.
- Leave song/group/performer/release/genre fields blank where relationships are handled by relationship tables.

Evidence:
- Peerless recording candidates from UNIT-0017 source extraction.
- Staging committed before promotion in commit 12420a0.

Confidence:
- high for extracted recording title/source/label relationship.
- pending for blank song/group/performer/release/genre fields.

Human Review:
- Final musical identity authority remains subject to human review when relationships conflict or duplicates appear.
