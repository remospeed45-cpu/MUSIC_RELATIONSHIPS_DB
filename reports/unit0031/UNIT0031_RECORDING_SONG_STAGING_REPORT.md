# UNIT-0031 Recording Song Exact Match Staging Report

## Goal

Build recording ↔ song relationships using exact title matches between:

- authority/recordings/recordings_master.tsv
- authority/songs/songs_master.tsv

## Result

- exact title matches staged: 5,502
- staging file: imports/unit0031_recording_song/UNIT0031_RECORDING_SONG_EXACT_MATCH_STAGING.tsv
- match type: exact_title

## Evidence

All staged rows are derived from exact normalized title equality:

canonical_recording_title = canonical_song_title

## Confidence

high

## Review Status

staged
