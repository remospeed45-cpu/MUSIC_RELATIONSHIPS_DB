# UNIT-0001 — RECORDING-CENTRIC MODEL

Primary entity: RECORDING

Core relationship:

RECORDING
↔ SONG
↔ GROUP
↔ PERFORMER
↔ GENRE
↔ RELEASE
↔ LABEL
↔ SOURCE

## Rules

1. RECORDING is the primary entity.
2. Do not store isolated songs, artists, or groups as the main useful unit.
3. Minimum useful unit: RECORDING ↔ SONG ↔ GROUP/PERFORMER.
4. GROUP has priority over PERFORMER.
5. If GROUP exists, MP3 visible name uses GROUP - SONG.
6. If GROUP does not exist, MP3 visible name uses PERFORMER - SONG.
7. Album Artist = GROUP when group exists.
8. Artist = vocalist/interpreter/performer.
9. RECORDING_GENRE overrides GROUP_GENRE.
10. GROUP_GENRE overrides PERFORMER_GENRE.
11. Every relationship must include source, evidence, confidence, review_status.
12. Human review is final authority.

## MP3 Organization Rule

GENRE/
  GROUP/
    GROUP - SONG.mp3

If no group:

GENRE/
  PERFORMER/
    PERFORMER - SONG.mp3

## Example

Filename:
Sonora Matancera - Burundanga.mp3

Tags:
Title = Burundanga
Album Artist = Sonora Matancera
Artist = Celia Cruz
Genre = Son Cubano
Subgenre = Guaracha
Source = Frontera
Confidence = high
