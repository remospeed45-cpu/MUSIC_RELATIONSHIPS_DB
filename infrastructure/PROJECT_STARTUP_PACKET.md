# PROJECT STARTUP PACKET

PROJECT:
INFRASTRUCTURE_REORGANIZATION

STATUS:
ACTIVE

CURRENT_PHASE:
INFRA-FASE-3

CURRENT_UNIT:
INFRA-0022

CURRENT_CHECKPOINT:
47c5486

AUTHORITATIVE REPOSITORY:
MUSIC_RELATIONSHIPS_DB

INFRASTRUCTURE ROLES:

BOSGAME:
Canonical storage server.

OPTIPLEX:
Primary processing workstation.

LENOVO:
Continuity workstation.

COMPLETED:

- Asset inventory.
- Location classification.
- Destination policy.
- Canonical storage verification.
- Migration sequence planning.

NOT APPROVED:

- Migrations.
- Deletions.
- Deduplication.

NEXT ACTION:

INFRA-0022
Define photo collection consolidation policy before any photo migration.

REORIENTATION RULE:

Read:
- PROJECT_STATUS.md
- PROJECT_DECISIONS.md
- WORK_LOG.md

Then continue from CURRENT_UNIT.


LATEST FINDING:

INFRA-0021 found that OPTIPLEX and BOSGAME photo collections are strongly related but not identical.

Photo comparison:
- Common size+filename keys: 2135
- OPTIPLEX-only keys: 1274
- BOSGAME-only keys: 1185

No photo migration, deletion, or deduplication is approved.
