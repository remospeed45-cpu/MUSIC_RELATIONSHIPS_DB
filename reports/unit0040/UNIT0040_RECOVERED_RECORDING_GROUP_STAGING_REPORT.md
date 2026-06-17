# UNIT-0040 Recovered Recording Group Staging Report

## Goal

Create recording ↔ group links from recovered performer text matched to promoted recovered groups.

## Inputs

- imports/unit0036_artist_recovery/UNIT0036_RECOVERABLE_PERFORMER_TEXT.tsv
- authority/groups/groups_master.tsv

## Output

- imports/unit0040_recovered_recording_group/UNIT0040_RECOVERED_RECORDING_GROUP_STAGING.tsv

## Results

- recording_group links staged: 187
- unmatched recovered text rows: 351

## Evidence

Each relationship is derived from exact match:

performer_name = canonical_group_name

after UNIT-0039 group promotion.

## Confidence

medium-high

## Review Status

staged
