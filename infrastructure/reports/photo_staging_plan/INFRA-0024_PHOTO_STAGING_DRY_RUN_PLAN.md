# INFRA-0024 PHOTO STAGING DRY-RUN PLAN

PROJECT: INFRASTRUCTURE_REORGANIZATION
UNIT: INFRA-0024

Purpose:
Create a dry-run staging copy plan for hash-unique photo files.

This unit creates planning manifests only.

No files were copied.
No files were moved.
No files were deleted.
No deduplication was executed.
No canonical replacement was executed.

## Source comparison basis

Input reports:
- infrastructure/reports/photo_hash_compare/photo_optiplex_only_by_sha256.tsv
- infrastructure/reports/photo_hash_compare/photo_bosgame_only_by_sha256.tsv

Comparison key:
SHA256 content hash.

## Planned staging policy

BOSGAME remains canonical storage.

OPTIPLEX-only SHA256 files are candidates for staged review before possible future ingestion into BOSGAME canonical storage.

BOSGAME-only SHA256 files are not copied anywhere in this plan. They are recorded as protected canonical-side unique files for review/reference.

## Dry-run output manifests

- INFRA-0024_optiplex_unique_to_bosgame_staging_dry_run.tsv
- INFRA-0024_bosgame_unique_protect_review_dry_run.tsv

## Counts

OPTIPLEX-only planned file rows: 1244
OPTIPLEX-only unique SHA256 hashes: 1240
OPTIPLEX internal duplicate rows inside unique-hash set: 4
OPTIPLEX planned review size bytes: 12518773619
OPTIPLEX planned review size GB: 11.66

BOSGAME-only protected file rows: 1148
BOSGAME-only unique SHA256 hashes: 1143
BOSGAME internal duplicate rows inside unique-hash set: 5
BOSGAME protected review size bytes: 14347095263
BOSGAME protected review size GB: 13.36

## Proposed future staging locations

OPTIPLEX unique review staging:
`/srv/storage/PROJECT_DATA/INFRASTRUCTURE_REORGANIZATION/staging/photo_review/from_optiplex_unique_sha256`

BOSGAME unique reference staging:
`/srv/storage/PROJECT_DATA/INFRASTRUCTURE_REORGANIZATION/staging/photo_review/bosgame_unique_reference_only`

These directories are proposed only. This unit does not create them on BOSGAME as migration staging targets.

## OPTIPLEX top source directories

- 727: /home/remospeed/Media/Fotos/iPhone/omer’s iPhone/Recents
- 200: /home/remospeed/Media/Fotos/Fotos/2005
- 113: /home/remospeed/Media/Fotos/Fotos/From：iPhone
- 69: /home/remospeed/Media/Fotos/Fotos/Work
- 44: /home/remospeed/Media/Fotos/Fotos/Grado Felipe
- 27: /home/remospeed/Media/Fotos/Fotos/Ejercicio
- 17: /home/remospeed/Media/Fotos/Fotos/Chocolate
- 11: /home/remospeed/Media/Fotos/Fotos/Cali
- 10: /home/remospeed/Media/Fotos/Fotos
- 10: /home/remospeed/Media/Fotos/Fotos/Familia
- 5: /home/remospeed/Media/Fotos/Fotos/Food
- 5: /home/remospeed/Media/Fotos/Fotos/Rocket Stove
- 4: /home/remospeed/Media/Fotos/Fotos/Telefono
- 1: /home/remospeed/Media/Fotos
- 1: /home/remospeed/Media/Fotos/Fotos/Orfa

## BOSGAME top source directories

- 108: /srv/storage/Fotos/Isabel
- 102: /srv/storage/Fotos/paola
- 100: /srv/storage/Fotos/Food
- 82: /srv/storage/Fotos/Familia
- 81: /srv/storage/Fotos/Hycrete
- 78: /srv/storage/Fotos/Matisse
- 59: /srv/storage/Fotos/Isabel Envios
- 58: /srv/storage/Fotos/Docs
- 45: /srv/storage/Fotos/Misc
- 43: /srv/storage/Fotos/Yuli
- 39: /srv/storage/Fotos/Oldies
- 33: /srv/storage/Fotos/Booz
- 33: /srv/storage/Fotos/Robinson
- 33: /srv/storage/Fotos/Gorda
- 28: /srv/storage/Fotos/ChatGpt
- 22: /srv/storage/Fotos/Orfa
- 21: /srv/storage/Fotos/Bolo
- 19: /srv/storage/Fotos/Ilustraciones
- 19: /srv/storage/Fotos/Chocolate
- 18: /srv/storage/Fotos/Orfa Work Time

## Required next action

Review the dry-run staging manifests and decide whether INFRA-0025 should:
1. create empty staging directories only,
2. generate rsync --dry-run command files,
3. sample-review high-risk folders first,
4. or pause before any migration-adjacent action.
