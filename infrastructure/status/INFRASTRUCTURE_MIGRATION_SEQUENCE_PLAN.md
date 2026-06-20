# INFRASTRUCTURE MIGRATION SEQUENCE PLAN

PROJECT: INFRASTRUCTURE_REORGANIZATION
PHASE: INFRA-FASE-3
UNIT: INFRA-0020

No migrations are approved by this document.

## Purpose

Define the recommended migration order before any file movement.

## Migration principle

Migrate only after each category has:

1. Source inventory.
2. Destination confirmation.
3. Dry-run command.
4. Size and file-count summary.
5. Conflict/duplicate policy.
6. Rollback/checkpoint note.
7. Explicit approval.

## Recommended sequence

| Step | Category | Source candidates | Destination | Reason | Status |
|---|---|---|---|---|---|
| 1 | Project repositories | GitHub + local working copies | GitHub + clean local clones | Lowest risk; metadata only; supports all later work | PLANNING |
| 2 | Project generated data | OPTIPLEX reports/scans/exports | BOSGAME:/srv/storage/PROJECT_DATA | Prevents large artifacts from polluting Git | PLANNING |
| 3 | Source libraries | PDFs/reference docs | BOSGAME:/srv/storage/SOURCE_LIBRARY | Supports music authority work without touching media collections | PLANNING |
| 4 | Raw imports | Downloads, Windows ingest, removable media | BOSGAME:/srv/storage/RAW_IMPORTS | Creates controlled intake area | PLANNING |
| 5 | Photos | Legacy photo folders | BOSGAME:/srv/storage/MASTER_COLLECTION/Photos | High personal value; requires careful date/duplicate policy | PLANNING |
| 6 | Videos | Legacy video folders | BOSGAME:/srv/storage/MASTER_COLLECTION/Videos | Large files; simpler than music but needs duplicate checks | PLANNING |
| 7 | Documents | Legacy document folders | BOSGAME:/srv/storage/MASTER_COLLECTION/Documents | Mixed content; requires classification | PLANNING |
| 8 | Music | Legacy music folders | BOSGAME:/srv/storage/MASTER_COLLECTION/Music | Must wait for authority/dedup policy; do not migrate dirty collections | DEFERRED |
| 9 | Backups | Backup sets | BOSGAME:/srv/storage/BACKUPS | Only after canonical locations stabilize | PLANNING |
| 10 | Quarantine | Trash/generated/uncertain artifacts | BOSGAME:/srv/storage/QUARANTINE | No deletion until reviewed | PLANNING |

## Current priority

Do not begin with music migration.

Music remains deferred because:

- Existing music is not clean.
- Names may be inconsistent.
- Duplicate policy is not ready.
- Authority database work is still ongoing.
- BOSGAME music should contain only organized playback-ready material.

## Next action

INFRA-0021:

Synchronize OPTIPLEX repository state safely without losing uncommitted work.

