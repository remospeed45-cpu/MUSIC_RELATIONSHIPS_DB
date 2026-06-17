# UNIT-0032 Song Artist Relationship Staging Report

## Goal

Build reusable song ↔ performer and song ↔ group relationships derived from recording relationships.

## Inputs

- relationships/recording_song.tsv
- relationships/recording_performer.tsv
- relationships/recording_group.tsv

## Outputs

- imports/unit0032_song_artist/UNIT0032_SONG_PERFORMER_STAGING.tsv
- imports/unit0032_song_artist/UNIT0032_SONG_GROUP_STAGING.tsv

## Results

- song_performer staged: 2,865
- song_group staged: 1,461

## Evidence

Each relationship is derived only when the same recording has:

- recording ↔ song
- recording ↔ performer or recording ↔ group

## Confidence

high

## Review Status

staged
