# PROJECT_OVERLAY.md

PROJECT: MUSIC_RELATIONSHIPS_DB

## Purpose

Build a reusable music relationship database focused on identifying real recordings through evidence-based relationships.

Primary entity:

RECORDING

## Foundation Scope

FOUNDATION is used only as global operational bootstrap.

It provides:
- continuity
- chat migration support
- anti-drift awareness
- work by units
- proportional structure
- separation between CORE global and project overlay

FOUNDATION does not define music rules for this project.

## Project Scope

This project focuses on:

- recordings
- songs
- performers
- groups
- releases
- labels
- genres
- source evidence

The project is an identification and relationship system.

## Primary Rule

Do not prioritize isolated artists or isolated songs.

Prioritize reusable recording relationships.

Good record:

recording ↔ song ↔ performer/group ↔ release ↔ label ↔ source

## Identification Priority

1. Recording
2. Song
3. Performer / Group
4. Release
5. Label
6. Genre
7. Source

## Evidence Rule

Every musical assertion should include:

- source
- evidence
- confidence level

Human review remains final authority.

## Source Priority

Priority A:
- Frontera
- Discos Fuentes
- Victor
- RCA Victor
- Peerless
- Musart

Priority B:
- Díaz-Ayala
- label catalogs
- historical discographies
- academic publications
- library collections

Priority C:
- MusicBrainz
- Discogs
- other documented references

## Import Rule

Import only records that improve identification.

Preferred fields:

raw_text  
canonical_recording  
canonical_song  
canonical_performer  
release  
label  
source  
confidence  

Avoid importing unsupported isolated names.

## Lookup Order

Before analyzing any recording:

1. Recording authority database
2. Recording relationship database
3. Existing approved identities
4. Fingerprint database
5. External sources
6. Human review

## Work Method

- Inventory before modification
- Verify before changing
- Evidence before conclusions
- Build reusable recording relationships first
- Avoid research that cannot improve identification

## Audio Policy

Do not automatically:

- modify MP3 files
- write metadata
- rename files
- move files

Create placement plans before execution.

## Migration Rule

At chat saturation, create a short migration block containing only:

- current unit
- active objective
- files touched
- unresolved risks
- next command or next review action

Do not migrate full history.

## Anti-Drift Rule

If work stops improving recording identification, pause and reorient.

## Success Criterion

Given a title:

Return all known performers.

Given a performer:

Return all known recordings.

Given a recording:

Return song, performer, release, label, source, evidence, and confidence.

------------------------------------------------------------------------------

HIGH-YIELD SOURCE FIRST STRATEGY (MANDATORY)

Project objective:

Acquire authority data as efficiently as possible to maximize MP3 organization,
identification and coverage.

Mandatory rules:

- Prioritize source-level acquisition over release-level acquisition.
- Prioritize inventory-level extraction over artist-by-artist workflows.
- Evaluate pending sources by expected authority volume before starting work.
- Process highest-yield sources first.
- Prefer:

  source inventory
  -> mass extraction
  -> mass normalization
  -> mass promotion

  over:

  source
  -> release
  -> release
  -> release

- Small releases are secondary and should only be processed when:
  - they belong to a larger extraction batch, or
  - no higher-yield source exists.

- Minimize manual review whenever safe automated recovery is possible.

- Avoid strategic drift toward discographic completeness.

Primary optimization metric:

Authority gained per unit of work.

When multiple paths exist, select the path with the highest expected authority gain.

------------------------------------------------------------------------------

------------------------------------------------------------------------------

FOUNDATION V2.3 MIGRATION NOTE

This file becomes the active Foundation project overlay for MUSIC_RELATIONSHIPS_DB.

Original source:

- PROJECT_OVERLAY.md

Rule:

- Root PROJECT_OVERLAY.md remains as historical/current project reference.
- foundation/PROJECT_OVERLAY.md becomes the Foundation V2.3 overlay.
- Future Foundation startup should prefer foundation/PROJECT_OVERLAY.md.

------------------------------------------------------------------------------
