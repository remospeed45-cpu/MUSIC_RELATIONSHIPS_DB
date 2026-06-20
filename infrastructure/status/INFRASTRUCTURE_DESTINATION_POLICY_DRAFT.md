# INFRASTRUCTURE DESTINATION POLICY DRAFT

PROJECT: INFRASTRUCTURE_REORGANIZATION
PHASE: INFRA-FASE-3
UNIT: INFRA-0018

No migrations, deletions, deduplication, or cleanup have been approved by this document.

## Destination policy table

| Category | Canonical destination | Processing location | Continuity copy | Migration status | Notes |
|---|---|---|---|---|---|
| Music | BOSGAME:/srv/storage/MASTER_COLLECTION/Music | OPTIPLEX:~/Media/Musica | LENOVO: none by default | PLANNING_ONLY | Only clean, organized, non-duplicate music should enter canonical collection. Existing music remains legacy until reviewed. |
| Photos | BOSGAME:/srv/storage/MASTER_COLLECTION/Photos | OPTIPLEX:~/Media/Fotos | LENOVO: optional review copy only | PLANNING_ONLY | Existing BOSGAME /srv/storage/Fotos remains legacy until photo policy is defined. |
| Videos | BOSGAME:/srv/storage/MASTER_COLLECTION/Videos | OPTIPLEX:~/Media/Videos | LENOVO: optional review copy only | PLANNING_ONLY | Existing BOSGAME /srv/storage/Videos remains legacy until reviewed. |
| Documents | BOSGAME:/srv/storage/MASTER_COLLECTION/Documents | OPTIPLEX:~/Media/Documentos | LENOVO: optional review copy only | PLANNING_ONLY | Includes non-Git personal/reference documents after classification. |
| Source libraries | BOSGAME:/srv/storage/SOURCE_LIBRARY | OPTIPLEX:~/Documents/Fuente Musical and mounted sources | LENOVO: none by default | PLANNING_ONLY | Reference PDFs and source material used for authority work. |
| Project repositories | GitHub authoritative + local working copies | OPTIPLEX:~/codex_work | LENOVO:~/codex_work continuity clone | ACTIVE_GIT_ONLY | Repositories are not migrated as media. Sync through Git only. |
| Project generated data | BOSGAME:/srv/storage/PROJECT_DATA | OPTIPLEX local generation area | LENOVO: none by default | PLANNING_ONLY | Large reports, scans, exports, and generated artifacts stay out of Git. |
| Raw imports | BOSGAME:/srv/storage/RAW_IMPORTS | OPTIPLEX:~/Downloads and mounted sources | LENOVO:~/Downloads temporary only | PLANNING_ONLY | Incoming material lands here before classification. |
| Backups | BOSGAME:/srv/storage/BACKUPS | OPTIPLEX creates backup sets | LENOVO may hold emergency copy | PLANNING_ONLY | Backup policy not yet implemented. |
| Quarantine | BOSGAME:/srv/storage/QUARANTINE | OPTIPLEX quarantine/review folders | LENOVO none by default | PLANNING_ONLY | No deletion until reviewed and explicitly approved. |

## Operational decisions

- BOSGAME is the future canonical storage server.
- OPTIPLEX is the primary processing workstation.
- LENOVO is the continuity workstation only.
- GitHub remains authoritative for repositories.
- Large generated artifacts must not be committed to Git.
- Existing legacy folders are not automatically canonical.
- Canonical folders may be created before migration, but creation does not approve moving files.
- Every migration must have a source, destination, dry-run, size summary, and rollback/checkpoint note.

## Not yet approved

- No file movement.
- No deletion.
- No deduplication.
- No repository cleanup.
- No legacy folder replacement.
- No automatic sync jobs.

## Next required unit

INFRA-0019: Create canonical directory skeleton on BOSGAME without moving legacy data.
