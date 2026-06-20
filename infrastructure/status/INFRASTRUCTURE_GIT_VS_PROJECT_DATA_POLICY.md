# INFRASTRUCTURE GIT VS PROJECT_DATA POLICY

PROJECT: INFRASTRUCTURE_REORGANIZATION
PHASE: INFRA-FASE-3
UNIT: INFRA-0022A

## Purpose

Define what belongs in Git and what belongs in BOSGAME PROJECT_DATA.

## Core rule

Git is for authoritative project memory, decisions, code, schemas, summaries, and small reproducible reports.

BOSGAME PROJECT_DATA is for large generated artifacts, inventories, manifests, scans, hashes, exports, temporary analysis output, and bulky machine-generated evidence.

## Storage destinations

Git repository:

MUSIC_RELATIONSHIPS_DB

BOSGAME project data root:

/srv/storage/PROJECT_DATA/INFRASTRUCTURE_REORGANIZATION

## Git-approved content

| Content type | Git status |
|---|---|
| PROJECT_STATUS.md | APPROVED |
| PROJECT_DECISIONS.md | APPROVED |
| WORK_LOG.md | APPROVED |
| PROJECT_STARTUP_PACKET.md | APPROVED |
| Policies | APPROVED |
| Human-readable summaries | APPROVED |
| Small CSV/TSV reports under practical size | CONDITIONAL |
| Scripts/tools | APPROVED |
| Reproducible report generators | APPROVED |

## PROJECT_DATA-approved content

| Content type | PROJECT_DATA status |
|---|---|
| Full file manifests | APPROVED |
| Hash manifests | APPROVED |
| Large comparison tables | APPROVED |
| Scan outputs | APPROVED |
| Media inventories | APPROVED |
| Temporary analysis exports | APPROVED |
| Large logs | APPROVED |
| Non-Git operational evidence | APPROVED |

## Threshold rule

Default Git threshold:

- Human-readable summary: yes.
- Raw generated table over 100 KB: store in PROJECT_DATA unless there is a strong reason to version it.
- Raw generated table over 1 MB: do not store in Git.
- Hash manifests: do not store in Git by default.
- Media file listings: do not store in Git by default.

## Reference rule

When a large artifact is stored outside Git, Git must keep a summary document that records:

- Artifact name.
- Artifact location.
- Generation date.
- Source paths.
- Row/file counts.
- Key findings.
- Whether migration/deletion/deduplication is approved.

## Safety rule

Moving an artifact from Git to PROJECT_DATA is repository cleanup only.

It does not approve:

- Media migration.
- Media deletion.
- Deduplication.
- Canonical replacement.

## Current remediation note

Photo comparison TSV manifests were committed to Git during INFRA-0021.

Recommended future cleanup:

- Move large TSV manifests to PROJECT_DATA.
- Keep only PHOTO_COLLECTION_COMPARISON_SUMMARY.md or equivalent summary in Git.
- Do not delete Git history for now.

## Next action

INFRA-0022B:

Create PROJECT_DATA directory for INFRASTRUCTURE_REORGANIZATION on BOSGAME.
