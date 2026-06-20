# INFRASTRUCTURE PHOTO CONSOLIDATION POLICY

PROJECT: INFRASTRUCTURE_REORGANIZATION
PHASE: INFRA-FASE-3
UNIT: INFRA-0022

No migration, deletion, or deduplication is approved by this document.

## Current finding

OPTIPLEX and BOSGAME photo collections are strongly related but not identical.

Known comparison:

- OPTIPLEX photo files: 3410
- BOSGAME photo files: 3320
- Common size+filename keys: 2135
- OPTIPLEX-only keys: 1274
- BOSGAME-only keys: 1185

## Policy decision

Do not replace one photo collection with the other.

Do not delete apparent duplicates.

Do not deduplicate by filename alone.

Do not deduplicate by size+filename alone.

Do not treat folder structure as proof of uniqueness.

## Proposed safe consolidation model

Canonical destination:

BOSGAME:/srv/storage/MASTER_COLLECTION/Photos

Temporary staging destination:

BOSGAME:/srv/storage/RAW_IMPORTS/photo_consolidation_staging

Recommended strategy:

1. Preserve both source collections.
2. Build hash-based manifests before copying.
3. Treat identical content hashes as duplicate candidates, not deletion approvals.
4. Copy unique files into staging first.
5. Preserve source provenance in metadata/reports.
6. Only promote from staging to MASTER_COLLECTION after review.
7. Never modify original legacy folders during consolidation.

## Required before any photo migration

- Hash manifest for OPTIPLEX photos.
- Hash manifest for BOSGAME photos.
- Content-hash comparison.
- Proposed canonical naming rule.
- Dry-run copy plan.
- Estimated final size.
- Explicit approval.

## Current status

Photo migration status: NOT_APPROVED

Photo deletion status: NOT_APPROVED

Photo deduplication status: NOT_APPROVED

## Next action

INFRA-0023:

Create hash-based photo comparison manifests.
