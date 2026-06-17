# UNIT-0031 Recording Song Promotion Report

## Goal

Promote recording ↔ song relationships from exact title matches.

## Inputs

- authority/recordings/recordings_master.tsv
- authority/songs/songs_master.tsv
- imports/unit0031_recording_song/UNIT0031_RECORDING_SONG_EXACT_MATCH_STAGING.tsv

## Promotion

- relationships/recording_song.tsv updated
- authority/recordings/recordings_master.tsv canonical_song_id populated

## Evidence

Relationship was created only when:

canonical_recording_title = canonical_song_title

## Confidence

high

## Review Status

approved
