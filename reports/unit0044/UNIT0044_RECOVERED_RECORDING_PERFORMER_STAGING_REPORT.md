# UNIT-0044 Recovered Recording Performer Staging Report

## Goal

Create recording ↔ performer links from recovered performer text matched to promoted recovered performers.

## Inputs

- imports/unit0036_artist_recovery/UNIT0036_RECOVERABLE_PERFORMER_TEXT.tsv
- authority/performers/performers_master.tsv

## Output

- imports/unit0044_recovered_recording_performer/UNIT0044_RECOVERED_RECORDING_PERFORMER_STAGING.tsv

## Results

- recording_performer links staged: 19
- unmatched recovered text rows: 519

## Evidence

Each relationship is derived from exact match:

performer_name = canonical_performer_name

after UNIT-0043 performer promotion.

## Confidence

medium-high

## Review Status

staged
