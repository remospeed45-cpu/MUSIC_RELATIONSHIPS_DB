# UNIT-0027 Recording Promotion Staging Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0027
Action: Stage Peerless recording candidates for recordings master promotion

Source:
- imports/unit0017_recording_candidates/UNIT0017_PEERLESS_RECORDING_CANDIDATES.tsv

Destination staging:
- authority/recordings/staging/UNIT0027_PEERLESS_RECORDINGS_PROMOTION_STAGING.tsv

Model:
- Primary entity: recording
- Promotion target: authority/recordings/recordings_master.tsv

Counts:
- Existing master recording IDs skipped: 0
- Staged recording rows: 5500
- Expected columns: 16
- TSV validation bad rows: 0

Default relationship fields:
- label_id: LBL000003
- source_id: preserved from candidate source_id
- song/group/performer/release/genre: left blank for relationship tables or later authority linkage
- review_status: staged

Evidence:
- Source file is Peerless recording candidate extraction from Frontera source reference.
- Candidate confidence preserved from import file.

Confidence:
- high for source extraction identity fields
- relationship completion remains pending where fields are blank

Human Review:
- Required before final authority interpretation beyond recording title/source/label linkage.
