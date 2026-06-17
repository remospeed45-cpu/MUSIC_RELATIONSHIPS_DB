# UNIT-0028 Primary Group Staging Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0028
Action: Stage primary_group_id promotion into recordings master

Source relationship:
- relationships/recording_group.tsv

Target authority:
- authority/recordings/recordings_master.tsv

Staging:
- authority/recordings/staging/UNIT0028_PRIMARY_GROUP_PROMOTION_STAGING.tsv

Counts:
- Rows staged for primary_group_id promotion: 1523
- Skipped existing primary_group_id: 2
- Skipped no group relationship: 3977
- Skipped multiple group relationships: 0
- TSV validation bad rows: 0

Rules:
- Recording remains the primary entity.
- Promote only one unambiguous primary_group relationship per recording.
- Do not invent group relationships.
- Do not modify performer, song, release, genre, label, or source fields.

Evidence:
- recording_group.tsv contains recording_id ↔ group_id relationship.
- Inventory showed zero multi-group conflicts.

Confidence:
- high where relationship confidence is already present in recording_group.tsv.
- human review remains final authority.
