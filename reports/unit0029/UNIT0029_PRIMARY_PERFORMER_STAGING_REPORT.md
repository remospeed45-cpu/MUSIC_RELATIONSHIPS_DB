# UNIT-0029 Primary Performer Staging Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0029
Action: Stage primary_performer_id promotion into recordings master

Source relationship:
- relationships/recording_performer.tsv

Target authority:
- authority/recordings/recordings_master.tsv

Staging:
- authority/recordings/staging/UNIT0029_PRIMARY_PERFORMER_PROMOTION_STAGING.tsv

Counts:
- Rows staged for primary_performer_id promotion: 3425
- Skipped existing primary_performer_id: 0
- Skipped no performer relationship: 2077
- Skipped multiple performer relationships: 0
- TSV validation bad rows: 0

Rules:
- Recording remains the primary entity.
- Promote only one unambiguous performer relationship per recording.
- Do not invent performer relationships.
- Do not modify song, group, release, genre, label, or source fields.

Evidence:
- recording_performer.tsv contains recording_id ↔ performer_id relationship.
- Inventory showed zero multi-performer conflicts.

Confidence:
- high where relationship confidence is already present in recording_performer.tsv.
- human review remains final authority.
