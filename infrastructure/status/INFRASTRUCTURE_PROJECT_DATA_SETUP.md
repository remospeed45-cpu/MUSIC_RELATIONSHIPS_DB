# INFRASTRUCTURE PROJECT_DATA SETUP

PROJECT: INFRASTRUCTURE_REORGANIZATION
PHASE: INFRA-FASE-3
UNIT: INFRA-0022B

## Result

PROJECT_DATA directory created on BOSGAME.

## Root

BOSGAME:

/srv/storage/PROJECT_DATA/INFRASTRUCTURE_REORGANIZATION

## Subdirectories

- reports
- manifests
- hashes
- inventories
- staging

## Purpose

Store large generated artifacts outside Git, including:

- file manifests
- hash manifests
- large comparison reports
- scan outputs
- temporary staging evidence
- generated inventories

## Git policy

Git will retain:

- summaries
- decisions
- policies
- pointers to PROJECT_DATA artifacts
- reproducible scripts

Git should not retain large raw generated manifests by default.

## Safety note

This setup does not approve migration, deletion, deduplication, or canonical replacement.
