# INFRASTRUCTURE CANONICAL STORAGE VERIFICATION

PROJECT: INFRASTRUCTURE_REORGANIZATION
PHASE: INFRA-FASE-3
UNIT: INFRA-0019

Verification date: 2026-06-19

## Result

Canonical storage skeleton already exists on BOSGAME.

Verified root:

/srv/storage

## Canonical directories present

- /srv/storage/MASTER_COLLECTION
- /srv/storage/SOURCE_LIBRARY
- /srv/storage/RAW_IMPORTS
- /srv/storage/PROJECT_DATA
- /srv/storage/BACKUPS

## Legacy data still present

- /srv/storage/Fotos
- /srv/storage/Videos
- /srv/storage/Compartido
- /srv/storage/Musica
- /srv/storage/_INGESTA_WINDOWS

## Findings

- Canonical structure exists.
- Legacy structure exists.
- No migration performed.
- No deletion performed.
- No deduplication performed.
- Canonical and legacy data remain separated.

## Capacity

Filesystem size: approximately 4.6 TB

Used: approximately 72 GB

Available: approximately 4.3 TB

## Next required unit

INFRA-0020

Create migration candidate inventory and migration sequencing plan.

