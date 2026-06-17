# UNIT-0030 Song Authority Staging Report

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0030
Action: Stage song authority candidates from recording titles

Source:
- authority/recordings/recordings_master.tsv

Existing song authority:
- authority/songs/songs_master.tsv

Staging:
- authority/songs/staging/UNIT0030_SONG_AUTHORITY_CANDIDATES_FROM_RECORDINGS.tsv

Counts:
- Existing song titles skipped: 2
- New unique song title candidates staged: 4163
- Duplicate staged song IDs: 0
- Duplicate staged titles: 0
- TSV validation bad rows: 0

Rules:
- Recording remains primary entity.
- Song candidates are derived only from existing recording titles.
- These are title-based song candidates, not externally validated compositions.
- No recording master fields modified in this step.

Evidence:
- canonical_recording_title in recordings_master.tsv.
- Source assigned SRC0001 because the Peerless recording titles came from Frontera extraction.

Confidence:
- medium, because title identity is reusable but composition/song authority still needs later validation.

Human Review:
- Required for duplicate compositions, alternate titles, spelling normalization, and composer/lyricist attribution.
