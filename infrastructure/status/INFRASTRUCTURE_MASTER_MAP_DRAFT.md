# INFRASTRUCTURE MASTER MAP DRAFT

PROJECT: INFRASTRUCTURE_REORGANIZATION  
STATUS: ACTIVE  
PHASE: INFRA-FASE-1A MASTER DISCOVERY

## Objective

Organize all digital assets across all machines.

No migrations, deletions, cleanup, or deduplication are approved yet.

## Machines

### BOSGAME

Role: Central data server  
User: remo-speed  
Hostname: remo-speed-Ecolite-Series  
Tailscale: 100.125.192.45  
Storage root: /srv/storage

Current major assets:

- /srv/storage/Fotos: 46 GB
- /srv/storage/Compartido: 23 GB
- /srv/storage/Videos: 2.7 GB
- /srv/storage/Musica: 184 MB
- /home/remo-speed/snap: 6.6 GB
- /home/remo-speed/gpt4all: 2.0 GB

Important findings:

- Approved /srv/storage structure exists.
- Actual assets still live in older folders such as Fotos, Videos, Compartido, Musica.
- MASTER_COLLECTION, RAW_IMPORTS, SOURCE_LIBRARY and PROJECT_DATA are mostly empty.
- Google Takeout ZIPs exist in /srv/storage/Compartido.
- Matching Google Takeout ZIPs also appear in user Trash.
- Do not delete yet.

### OPTIPLEX

Role: Primary workstation / main processing node  
User: remospeed  
Local IP: 192.168.30.106  
Tailscale: 100.97.207.91

Current major assets:

- ~/Media: 125 GB
- ~/codex_work: 14 GB
- ~/Downloads: 13 GB
- ~/Pictures: 11 GB
- ~/snap: 8 GB

Media breakdown:

- ~/Media/Musica: 82 GB
- ~/Media/Fotos: 44 GB
- ~/Media/Documentos: 40 MB
- ~/Media/Videos: 36 MB

Additional mounted asset source:

- /mnt/windows_music: 341 GB used

Important findings:

- 75 music-related PDFs/documents found.
- Major document locations:
  - ~/Documents/Fuente Musical
  - LATIN_MUSIC_AUTHORITY_DB/sources/acquired
- MUSIC_RELATIONSHIPS_DB was reduced from 13 GB to 54 MB after quarantining a 12.64 GB generated artifact.
- Large generated artifacts do not belong in Git repositories.

### LENOVO

Role: Continuity workstation  
User: remo-speed  
Hostname: remo-speed-Lenovo-G70-70  
Local IP: 192.168.12.115  
Tailscale: 100.79.167.69

Current major assets:

- ~/LenovoMedia: 27 GB
- ~/Music: 8.4 GB
- ~/Pictures: 1.9 GB
- ~/codex_work: 925 MB
- ~/Downloads: 512 MB

External/removable:

- /run/media/remo-speed/046C-431B: 30 GB device, 8.4 GB used

Important findings:

- Repositories exist in ~/codex_work.
- Additional older repository copies exist under ~/LenovoMedia/Compartido/codex.
- This may create confusion and must not be treated as canonical without verification.
- 60 PDF/DOC files found under home.

## Current strategic decisions

1. BOSGAME remains intended central data server.
2. OPTIPLEX remains primary processing node.
3. LENOVO remains continuity workstation.
4. No mass migration yet.
5. No deletion yet.
6. No deduplication yet.
7. No cleanup yet.
8. Macro-level asset map must be completed before consolidation.

## Current risks

- Multiple music locations across all machines.
- Multiple photo locations across all machines.
- Old and new BOSGAME folder structures coexist.
- Takeout ZIPs appear both in Compartido and Trash.
- Duplicate repository copies exist on Lenovo.
- Windows music source is large and not yet classified.
- Some project data is in local workstations instead of BOSGAME PROJECT_DATA.
- Git repositories may contain generated reports or artifacts if not controlled.

## Proposed permanent destination model

BOSGAME /srv/storage should become the long-term canonical storage root:

- /srv/storage/SOURCE_LIBRARY
  - Original external sources and reference material.
- /srv/storage/RAW_IMPORTS
  - Temporary raw incoming files before classification.
- /srv/storage/MASTER_COLLECTION
  - Clean canonical media collections.
- /srv/storage/PROJECT_DATA
  - Project support data, reports, inventories and non-Git large artifacts.
- /srv/storage/BACKUPS
  - Backups only.
- /srv/storage/Fotos
  - Existing legacy photos location until migrated or mapped.
- /srv/storage/Videos
  - Existing legacy videos location until migrated or mapped.

## Next required action

INFRA-0017: Create machine-by-machine asset classification table.

The table should classify each major asset location as:

- CANONICAL
- LEGACY
- WORKING_COPY
- RAW_IMPORT
- BACKUP
- QUARANTINE
- UNKNOWN_REVIEW

No files should be moved during INFRA-0017.
