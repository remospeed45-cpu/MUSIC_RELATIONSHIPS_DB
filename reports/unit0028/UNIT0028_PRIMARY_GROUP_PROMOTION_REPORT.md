# UNIT-0028 Primary Group Promotion Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0028
Action: Promote primary_group_id into recordings master

Source staging:
- authority/recordings/staging/UNIT0028_PRIMARY_GROUP_PROMOTION_STAGING.tsv

Target master:
- authority/recordings/recordings_master.tsv

Counts:
- Master data rows: 5502
- Staged rows reviewed: 1523
- Rows updated with primary_group_id: 1523
- Skipped already matching: 0
- Skipped not staged: 3979
- Conflicts: 0
- primary_group_id populated after promotion: 1525
- Duplicate recording IDs after promotion: 0
- TSV validation bad rows: 0

Rules:
- Recording remains primary entity.
- Only unambiguous recording_id ↔ group_id relationships were promoted.
- No performer/song/release/genre fields were modified.
- No invented relationships.

Evidence:
- relationships/recording_group.tsv supplied group_id values.
- UNIT-0028 staging showed 1,523 safe rows and zero multi-group conflicts.

Confidence:
- high for promoted group relationships from approved/staged relationship source.
- human review remains final authority.
