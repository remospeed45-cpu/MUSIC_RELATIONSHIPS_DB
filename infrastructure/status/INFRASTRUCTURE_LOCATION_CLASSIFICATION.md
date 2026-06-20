# INFRASTRUCTURE LOCATION CLASSIFICATION

PROJECT: INFRASTRUCTURE_REORGANIZATION  
PHASE: INFRA-FASE-1A MASTER DISCOVERY  
UNIT: INFRA-0017

No files were moved, deleted, deduplicated, renamed, or cleaned during this unit.

## Classification labels

- CANONICAL: intended permanent authoritative location.
- LEGACY: older location containing real data, not yet migrated or resolved.
- WORKING_COPY: active local work area.
- RAW_IMPORT: unprocessed incoming material.
- BACKUP: backup-only storage.
- QUARANTINE: isolated artifact requiring review.
- UNKNOWN_REVIEW: needs further inspection before classification.

## BOSGAME

| Location | Classification | Reason |
|---|---|---|
| /srv/storage | CANONICAL_ROOT | Approved long-term storage root |
| /srv/storage/SOURCE_LIBRARY | CANONICAL | Intended source/reference library |
| /srv/storage/RAW_IMPORTS | CANONICAL | Intended raw import landing zone |
| /srv/storage/MASTER_COLLECTION | CANONICAL | Intended clean master collection |
| /srv/storage/PROJECT_DATA | CANONICAL | Intended non-Git project data |
| /srv/storage/BACKUPS | CANONICAL | Intended backup storage |
| /srv/storage/Fotos | LEGACY | Existing 46 GB photo collection |
| /srv/storage/Videos | LEGACY | Existing 2.7 GB video collection |
| /srv/storage/Compartido | LEGACY | Existing 23 GB mixed shared data and Takeout |
| /srv/storage/Musica | LEGACY | Existing small music folder |
| /srv/storage/_INGESTA_WINDOWS | RAW_IMPORT | Existing Windows ingest structure |
| /home/remo-speed/codex_work | WORKING_COPY | Local project checkout area |
| /home/remo-speed/BOSGAME_HELPER | WORKING_COPY | Local helper repository |
| /home/remo-speed/.local/share/Trash/files | QUARANTINE | Contains large Takeout duplicates; no deletion approved |

## OPTIPLEX

| Location | Classification | Reason |
|---|---|---|
| ~/codex_work | WORKING_COPY | Main processing repositories |
| ~/Media | LEGACY | Existing local media collection |
| ~/Media/Musica | LEGACY | 82 GB local music collection |
| ~/Media/Fotos | LEGACY | 44 GB local photo collection |
| ~/Media/Documentos | LEGACY | Local document collection |
| ~/Media/Videos | LEGACY | Local video collection |
| ~/Downloads | RAW_IMPORT | Download/import area |
| ~/Pictures | LEGACY | Local pictures |
| ~/Documents/Fuente Musical | SOURCE_LIBRARY_CANDIDATE | Music reference PDFs/documents |
| /mnt/windows_music | SOURCE_LIBRARY_CANDIDATE | Large Windows music source, 341 GB used |
| ~/infra_discovery/quarantine | QUARANTINE | Large generated artifact isolation |

## LENOVO

| Location | Classification | Reason |
|---|---|---|
| ~/codex_work | WORKING_COPY | Continuity workstation repositories |
| ~/LenovoMedia | LEGACY | 27 GB older local media collection |
| ~/LenovoMedia/Fotos | LEGACY | Local photos inside LenovoMedia |
| ~/LenovoMedia/Videos | LEGACY | Local videos inside LenovoMedia |
| ~/LenovoMedia/Musica | LEGACY | Local music inside LenovoMedia |
| ~/Music | LEGACY | 8.4 GB local music collection |
| ~/Pictures | LEGACY | 1.9 GB local pictures |
| ~/Downloads | RAW_IMPORT | Download/import area |
| ~/LenovoMedia/Compartido/codex | UNKNOWN_REVIEW | Duplicate old repository copies |
| /run/media/remo-speed/046C-431B | UNKNOWN_REVIEW | Removable device, 8.4 GB used |

## Immediate implications

- BOSGAME is the intended future canonical storage server.
- Existing BOSGAME folders are not yet clean canonical collections.
- OPTIPLEX remains the correct processing machine.
- LENOVO should not be treated as canonical.
- No location is approved for deletion yet.
- No legacy location is approved for migration yet.
- Repository duplicates must be verified before cleanup.
- Large generated artifacts must stay out of Git.

## Next action

INFRA-0018: Define asset category destination policy.

Required categories:

- Music
- Photos
- Videos
- Documents
- Project repositories
- Project generated data
- Backups
- Raw imports
- Quarantine
