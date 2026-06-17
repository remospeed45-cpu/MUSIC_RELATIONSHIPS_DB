# UNIT-0030 Song Authority Promotion Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0030
Action: Promote title-derived song authority candidates into songs master

Source staging:
- authority/songs/staging/UNIT0030_SONG_AUTHORITY_CANDIDATES_FROM_RECORDINGS.tsv

Target master:
- authority/songs/songs_master.tsv

Counts:
- Song master rows before promotion: 2
- Staged rows reviewed: 4163
- Rows promoted: 4163
- Skipped duplicate song_id: 0
- Skipped duplicate title: 0
- Song master rows after promotion: 4165
- Duplicate song IDs after promotion: 0
- Duplicate song titles after promotion: 0
- TSV validation bad rows: 0

Rules:
- Recording remains primary entity.
- Song authority candidates were derived from canonical recording titles.
- No composer/lyricist claims added.
- No recording master fields modified in this step.

Evidence:
- canonical_recording_title from recordings_master.tsv.
- Peerless recording titles trace to SRC0001 Frontera extraction.

Confidence:
- medium for title-level song identity.
- human review required for composition identity, duplicate works, alternate titles, and authorship.
