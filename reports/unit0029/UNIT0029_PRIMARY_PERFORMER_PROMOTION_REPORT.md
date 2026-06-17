# UNIT-0029 Primary Performer Promotion Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0029
Action: Promote primary_performer_id into recordings master

Source staging:
- authority/recordings/staging/UNIT0029_PRIMARY_PERFORMER_PROMOTION_STAGING.tsv

Target master:
- authority/recordings/recordings_master.tsv

Counts:
- Master data rows: 5502
- Staged rows reviewed: 3425
- Rows updated with primary_performer_id: 3425
- Skipped already matching: 0
- Skipped not staged: 2077
- Conflicts: 0
- primary_group_id populated after promotion: 1525
- primary_performer_id populated after promotion: 3425
- either group or performer populated: 4950
- both group and performer populated: 0
- Duplicate recording IDs after promotion: 0
- TSV validation bad rows: 0

Rules:
- Recording remains primary entity.
- Only unambiguous recording_id ↔ performer_id relationships were promoted.
- No group/song/release/genre fields were modified.
- No invented relationships.

Evidence:
- relationships/recording_performer.tsv supplied performer_id values.
- UNIT-0029 staging showed 3,425 safe rows and zero multi-performer conflicts.

Confidence:
- high for promoted performer relationships from extracted relationship source.
- human review remains final authority.
