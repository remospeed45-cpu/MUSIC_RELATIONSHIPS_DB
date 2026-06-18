# UNIT-0096 — La Voz Robust Audit

Project: MUSIC_RELATIONSHIPS_DB
Unit: UNIT-0096

## Purpose

Correct the UNIT-0095 audit method.

UNIT-0095 searched hardcoded release_id REL000033 and returned no promoted records.
UNIT-0096 identifies the La Voz release_id from releases_master by title, then compares recordings_master against the validated source tracklist.

## Source Tracklist

data/src0003/batch0002/SRC0003_BATCH0002_LA_VOZ_TRACKLIST.tsv

## Output

authority/staging/unit0096/UNIT0096_LA_VOZ_ROBUST_AUDIT.tsv

## Status

Audit only.
No master corrections performed in this unit.
