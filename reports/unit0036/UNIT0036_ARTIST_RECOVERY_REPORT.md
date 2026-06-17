# UNIT-0036 Artist Recovery Report

## Goal

Recover performer text for recordings missing performer/group relationships.

## Source Queue

- imports/unit0034_missing_artist_review/UNIT0034_MISSING_ARTIST_REVIEW_QUEUE.tsv

## Recovery Source

- imports/unit0017_recording_candidates/UNIT0017_PEERLESS_RECORDING_CANDIDATES.tsv

## Results

- missing artist records: 552
- recoverable performer text rows: 538
- unrecovered records: 14

## Evidence

Recovered performer text comes directly from the original Peerless/Frontera candidate import field:

- performer_name

## Confidence

high for text recovery

## Review Status

recovered_text_staged
