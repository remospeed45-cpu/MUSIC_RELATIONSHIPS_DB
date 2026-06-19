# MIGRATION_AUDIT_REPORT.md

PROJECT: FOUNDATION + MUSIC_RELATIONSHIPS_DB

MODE: AUDIT ONLY

AUTHORITATIVE TARGET NODE: OptiPlex 7010

CLIENT NODE: Lenovo G70

## Final Conclusion

READY_FOR_MASTER_NODE_MIGRATION = NO

Blockers:

- OptiPlex SSH endpoint is reachable at `remospeed@100.97.207.91`, but authentication failed from Lenovo with `Permission denied (publickey,password)`.
- OptiPlex repository and Music-folder verification could not be completed because remote SSH commands could not be authenticated.
- Multiple operational documents contain hardcoded node/user paths. Most are historical or governance references, but they should be reviewed before making OptiPlex the single authoritative node.
- Do not delete Lenovo copies until OptiPlex clone integrity, remotes, latest commits, and authoritative Music storage are verified on the target node.

## A. Repository Inventory

Repositories found under `/home/remo-speed/codex_work`:

| Repository | Branch | HEAD | Remote origin | Ahead/Behind | Working tree | Untracked files | Uncommitted files |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `/home/remo-speed/codex_work/Codex_Normalizar_Musica` | `master` | `219d667` | `git@github.com:remospeed45-cpu/Codex_Normalizar_Musica.git` | `0 behind / 0 ahead` | clean | none | none |
| `/home/remo-speed/codex_work/Hycrete_Core` | `master` | `302d3a1` | `git@github.com:remospeed45-cpu/Hycrete_Core.git` | `0 behind / 0 ahead` | clean | none | none |
| `/home/remo-speed/codex_work/LATIN_MUSIC_AUTHORITY_DB` | `main` | `4778be0` | `git@github.com:remospeed45-cpu/LATIN_MUSIC_AUTHORITY_DB.git` | `0 behind / 0 ahead` | clean | none | none |
| `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB` | `main` | `57eb52d` | `git@github.com:remospeed45-cpu/MUSIC_MP3_AUTHORITY_DB.git` | `0 behind / 0 ahead` | clean | none | none |
| `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB` | `main` | `484d08c` | `git@github.com:remospeed45-cpu/MUSIC_RELATIONSHIPS_DB.git` | `0 behind / 0 ahead` before this report | clean before this report | none before this report | none before this report |
| `/home/remo-speed/codex_work/Music_Reference_DB` | `main` | `2903974` | `git@github.com:remospeed45-cpu/Music_Reference_DB.git` | `0 behind / 1 ahead` | clean | none | none |

Important local-only commit:

- `/home/remo-speed/codex_work/Music_Reference_DB`: `2903974 Add unmatched entity genre audit`
- `origin/main` for that repository remains at `b7e9fbd Add SRC-0003 Antillana publication plan seed`.

Non-Git top-level directories/files under `/home/remo-speed/codex_work`:

- `/home/remo-speed/codex_work/Operational_Foundation`
- `/home/remo-speed/codex_work/music_sandbox`
- `/home/remo-speed/codex_work/Documento vacío.txt`

## B. Foundation Inventory

Named Foundation-related files found:

- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/LATIN_MUSIC_AUTHORITY_DB/reports/PROJECT_STATUS.md`
- `/home/remo-speed/codex_work/Hycrete_Core/foundation/FOUNDATION_CONTEXT.md`
- `/home/remo-speed/codex_work/Hycrete_Core/WORKFLOW_REFERENCE.md`
- `/home/remo-speed/codex_work/Operational_Foundation/FOUNDATION_CONTEXT.md`
- `/home/remo-speed/codex_work/Operational_Foundation/legacy/projects/CODEX_NORMALIZAR_MUSICA.deprecated/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Operational_Foundation/projects/HYCRETE/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Operational_Foundation/projects/MUSIC/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Operational_Foundation/chat_bootstrap/HYCRETE/FOUNDATION_CONTEXT.md`
- `/home/remo-speed/codex_work/Operational_Foundation/chat_bootstrap/HYCRETE/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Operational_Foundation/chat_bootstrap/MUSIC/FOUNDATION_CONTEXT.md`
- `/home/remo-speed/codex_work/Operational_Foundation/chat_bootstrap/MUSIC/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Codex_Normalizar_Musica/foundation/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Codex_Normalizar_Musica/foundation/chat_bootstrap/FOUNDATION_CONTEXT.md`
- `/home/remo-speed/codex_work/Codex_Normalizar_Musica/foundation/chat_bootstrap/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/foundation/FAST_REORIENTATION.md`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/foundation/CHAT_BOOTSTRAP.md`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/foundation/FOUNDATION_CONTEXT.md`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/foundation/PROJECT_STATUS.md`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/foundation/PROJECT_OVERLAY.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/foundation/FAST_REORIENTATION.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/foundation/FOUNDATION_CONTEXT.md`

Requested Foundation filenames not found under `/home/remo-speed/codex_work`:

- `PROJECT_STARTUP_PACKET.md`
- `PROJECT_MEMORY.md`

Starter/startup packages found:

- `/home/remo-speed/codex_work/Hycrete_Core/HYCRETE_STARTUP_PACKET.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/ACTIVE_SESSION_STARTUP.md`
- `/home/remo-speed/codex_work/Hycrete_Core/templates/PROJECT_STARTUP_PACKET_TEMPLATE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/startup_check.sh`

`PROYECTO_00`:

- No file or directory matching `PROYECTO_00` was found under `/home/remo-speed/codex_work`.

## MUSIC_RELATIONSHIPS_DB Verification

`MUSIC_RELATIONSHIPS_DB` exists on this machine at:

- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB`

Repository state before this report was created:

- Branch: `main`
- HEAD: `484d08c Add UNIT-0105 fast MP3 safe scan results`
- Remote: `git@github.com:remospeed45-cpu/MUSIC_RELATIONSHIPS_DB.git`
- Ahead/behind: `0 behind / 0 ahead`
- Working tree: clean
- Untracked files: none
- Uncommitted files: none
- Local-only files: none detected by `git ls-files --others --exclude-standard`

Latest completed unit identified:

- `UNIT0105`
- Latest report: `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/reports/unit0105/UNIT0105_MP3_SCAN_REPORT.md`
- Latest commits:
  - `484d08c Add UNIT-0105 fast MP3 safe scan results`
  - `4c79100 Add UNIT-0105 safe MP3 organization scanner`
  - `348c786 Document UNIT-0104 SRC0003 coverage and next block actions`

After this audit report is created, `reports/MIGRATION_AUDIT_REPORT.md` is local work until committed, pushed, or copied to the target node.

## C. Username/Path Mismatch Findings

Search terms:

- `remospeed`
- `remo-speed`
- `/home/remospeed/`
- `/home/remo-speed/`

Summary:

- 211 files contain `remospeed` or `remo-speed`.
- 143 files contain absolute `/home/remospeed/` or `/home/remo-speed/` paths.
- Many matches are data provenance rows in music authority TSV/M3U files, especially source media paths. These are not necessarily operational defects, but they are not portable without a path mapping policy.
- Operational hardcoded username/path references were found in docs and scripts, especially Hycrete node-switch documents and one Codex/Ollama helper.

Operational scripts/documentation/configuration files with username or node references:

- `/home/remo-speed/codex_work/Hycrete_Core/docs/PROJECT_CONTEXT.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/DATABASE_LAYER_GOVERNANCE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/ETL_EXECUTION_GOVERNANCE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/ACTIVE_SESSION_STARTUP.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/P_HYC_02_REMOTE_SYNC_FOUNDATION_CLOSURE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/ACTIVE_OPERATIONAL_NODE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/DATABASE_AUTHORITY_RULES.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/NODE_SWITCH_PROTOCOL.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/docs/units/FP0001_FIRST_FINGERPRINT_PILOT.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/docs/units/FP0002_DUPLICATE_DETECTION_PILOT.md`
- `/home/remo-speed/codex_work/LATIN_MUSIC_AUTHORITY_DB/docs/infrastructure/NETWORK_EQUIPMENT_MAP_0001.md`
- `/home/remo-speed/codex_work/Codex_Normalizar_Musica/docs/P_OPS_38_CODEX_TO_OLLAMA_HELPER_SMOKE_INTEGRATION.md`
- `/home/remo-speed/codex_work/Codex_Normalizar_Musica/scripts/python/dev/ollama_smoke_summarizer.py`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/docs/SOURCE_PATH_PORTABILITY.md`

Files containing absolute `/home/remospeed/` or `/home/remo-speed/` paths:

- `/home/remo-speed/codex_work/Music_Reference_DB/reports/PLAYLIST_FIRST_MIGRATION_MODEL.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/strategy/SRC0003_PUBLICATION_BLOCK_STRATEGY.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/codex_tasks/SRC0003_GUARACHAS_EXTERNAL_RESEARCH.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/pilots/src0003_playlist_guarachas_work.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/pilots/src0003_playlist_guarachas_publication_plan.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/pilots/playlists/SRC0003_PLAYALIST_GUARACHAS_original_sequence.m3u8`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/publication/src0003_antillana_publication_plan_seed.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/src0003_master_mapping.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/src0003_playlist_sequence.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/review/src0003_playlist_classification.tsv`
- `/home/remo-speed/codex_work/music_sandbox/output/summary.json`
- `/home/remo-speed/codex_work/music_sandbox/output/canonical_artists.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/fingerprint_queue.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/canonical_recordings.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/fingerprint_candidates.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/parsed_metadata.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/fingerprint_execution_plan.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/inventory_scan.json`
- `/home/remo-speed/codex_work/music_sandbox/output/inventory.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/canonical_index.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/external_reconciliation_candidates.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/summary.txt`
- `/home/remo-speed/codex_work/music_sandbox/output/canonical_titles.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/duplicates.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/fingerprint_results.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/inventory_parsed.csv`
- `/home/remo-speed/codex_work/music_sandbox/output/musicbrainz_preparation.csv`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/docs/SOURCE_PATH_PORTABILITY.md`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/review/src0003_priority_playlist_candidates.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/review/src0003_existing_playlist_name_candidates.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/src0003_playlist_inventory.tsv`
- `/home/remo-speed/codex_work/Music_Reference_DB/recordings/optiplex_media/src0003_mp3_inventory.txt`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/authority/sources/source_status_registry.tsv`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/authority/sources/sources_master.tsv`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/P_HYC_02_REMOTE_SYNC_FOUNDATION_CLOSURE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/ACTIVE_OPERATIONAL_NODE.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/DATABASE_AUTHORITY_RULES.md`
- `/home/remo-speed/codex_work/Hycrete_Core/docs/NODE_SWITCH_PROTOCOL.md`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB/tools/music_authority/sources/source_status_registry_builder.py`
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/imports/unit0105_mp3_scan/UNIT0105_MP3_SCAN_ALL.tsv`
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/imports/unit0105_mp3_scan/UNIT0105_MP3_KNOWN_RECORDINGS.tsv`
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/imports/unit0105_mp3_scan/UNIT0105_MP3_UNKNOWN.tsv`
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/imports/unit0105_mp3_scan/UNIT0105_MP3_PROBABLE_SONGS.tsv`
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/reports/unit0105/UNIT0105_MP3_SCAN_REPORT.md`

Additional absolute-path files are present in `MUSIC_MP3_AUTHORITY_DB/authority/staging`, `MUSIC_MP3_AUTHORITY_DB/reports/unit0004` through `unit0046`, and `LATIN_MUSIC_AUTHORITY_DB/music_reference_db`/`reports`. These are primarily evidence, staging, and source-tracking artifacts rather than executable startup files.

## D. Duplicate Repository Findings

`MUSIC_RELATIONSHIPS_DB`:

- One copy found: `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB`
- Appears active: yes
- Evidence: Git repository, clean, synchronized to `origin/main`, latest unit `UNIT0105`.

`FOUNDATION`:

- `/home/remo-speed/codex_work/Operational_Foundation`: appears active as global bootstrap/project overlay store, but it is not a Git repository.
- `/home/remo-speed/codex_work/Operational_Foundation/legacy/projects/CODEX_NORMALIZAR_MUSICA.deprecated`: appears abandoned/deprecated by path name.
- Project-local `foundation` directories exist in `Hycrete_Core`, `Codex_Normalizar_Musica`, `MUSIC_MP3_AUTHORITY_DB`, and `Music_Reference_DB`. These appear project-specific, not byte-for-byte duplicate repositories.
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/docs/foundation`: appears project-local documentation area.

`PROYECTO_00`:

- No copies found.

Other possible abandoned/non-authoritative areas:

- `/home/remo-speed/codex_work/music_sandbox`: non-Git sandbox with input/output artifacts and hardcoded local media paths. Treat as non-authoritative unless separately verified.
- `/home/remo-speed/codex_work/Documento vacío.txt`: standalone top-level file, not part of a Git repository.

## E. Uncommitted Work Findings

Before creating this audit report:

- No repository had uncommitted tracked changes.
- No repository had untracked files.
- `Music_Reference_DB` had local committed work ahead of origin by one commit.

After creating this audit report:

- `MUSIC_RELATIONSHIPS_DB` contains new local report artifact: `reports/MIGRATION_AUDIT_REPORT.md`.
- This file must be committed/pushed or copied to OptiPlex before Lenovo cleanup.

## F. Safe Migration Recommendations

1. On Lenovo, preserve all current repositories until OptiPlex verification is complete.
2. Push or otherwise migrate `Music_Reference_DB` commit `2903974` before deleting any Lenovo copy.
3. Commit/push or copy `MUSIC_RELATIONSHIPS_DB/reports/MIGRATION_AUDIT_REPORT.md`.
4. On OptiPlex, clone or update all Git repositories and verify exact HEADs:
   - `Codex_Normalizar_Musica`: `219d667`
   - `Hycrete_Core`: `302d3a1`
   - `LATIN_MUSIC_AUTHORITY_DB`: `4778be0`
   - `MUSIC_MP3_AUTHORITY_DB`: `57eb52d`
   - `MUSIC_RELATIONSHIPS_DB`: `484d08c` plus this audit report if committed later
   - `Music_Reference_DB`: `2903974` if the local-only commit is accepted
5. Copy or intentionally archive non-Git directories before Lenovo cleanup:
   - `/home/remo-speed/codex_work/Operational_Foundation`
   - `/home/remo-speed/codex_work/music_sandbox`
   - `/home/remo-speed/codex_work/Documento vacío.txt`
6. Establish path mapping for `/home/remo-speed` and `/home/remospeed` references before running scripts or startup instructions on OptiPlex.
7. Treat source media paths in TSV/M3U/catalog artifacts as evidence records. Do not rewrite them unless the project has a formal provenance-path migration plan.

## G. Safe Deletion Candidates

Current state:

- No exact deletion candidate is safe yet.
- Lenovo deletion is blocked until OptiPlex verification and local-only work migration are complete.

Potential deletion candidates after successful OptiPlex verification:

- `/home/remo-speed/codex_work/Operational_Foundation/legacy/projects/CODEX_NORMALIZAR_MUSICA.deprecated`
- `/home/remo-speed/codex_work/music_sandbox`
- `/home/remo-speed/codex_work/Documento vacío.txt`

These are only candidates. They require explicit verification that no needed local evidence, scripts, or bootstrap material exists only in those locations.

## H. Items That Must NOT Be Deleted

Do not delete from Lenovo until OptiPlex has been verified with matching content:

- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB`
- `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB/reports/MIGRATION_AUDIT_REPORT.md`
- `/home/remo-speed/codex_work/Music_Reference_DB`
- `Music_Reference_DB` local commit `2903974`
- `/home/remo-speed/codex_work/Operational_Foundation`
- `/home/remo-speed/codex_work/MUSIC_MP3_AUTHORITY_DB`
- `/home/remo-speed/codex_work/LATIN_MUSIC_AUTHORITY_DB`
- `/home/remo-speed/codex_work/Codex_Normalizar_Musica`
- `/home/remo-speed/codex_work/Hycrete_Core`
- Any `foundation`, `reports`, `authority`, `imports`, `evidence`, `recordings`, `sources`, or `tools` directories until they are verified on OptiPlex.
- Any source-path or media-path TSV/M3U evidence files until their role is understood.

## Audit Commands Used

- `find /home/remo-speed/codex_work -name .git -type d -prune`
- `find /home/remo-speed/codex_work -type f` for named Foundation files
- `find /home/remo-speed/codex_work -iname '*PROYECTO_00*' -o -iname '*starter*' -o -iname '*STARTER*' -o -iname '*startup*' -o -iname '*STARTUP*'`
- `git branch --show-current`
- `git rev-parse --short HEAD`
- `git remote get-url origin`
- `git status --short --branch`
- `git rev-list --left-right --count @{u}...HEAD`
- `git ls-files --others --exclude-standard`
- `git diff --name-only`
- `rg -l 'remospeed|remo-speed' /home/remo-speed/codex_work`
- `rg -l '/home/remospeed/|/home/remo-speed/' /home/remo-speed/codex_work`

## OPTIPLEX_VERIFICATION

Verification date: 2026-06-18 from Lenovo G70 path `/home/remo-speed/codex_work/MUSIC_RELATIONSHIPS_DB`.

Local synchronization completed before OptiPlex verification:

- `Music_Reference_DB` was verified clean and ahead by the expected commit `2903974 Add unmatched entity genre audit`.
- `Music_Reference_DB` was pushed to `origin/main`; post-push status was clean and synchronized.
- `MUSIC_RELATIONSHIPS_DB` committed and pushed this report as `d5518e9 Add migration audit report for OptiPlex master node transition`.
- `MUSIC_RELATIONSHIPS_DB` post-push status was clean and synchronized.

OptiPlex SSH target discovered from local docs:

- Hostname / Tailscale name: `remospeed-optiplex-7010`
- Tailscale IP: `100.97.207.91`
- SSH user: `remospeed`
- Expected workspace root: `/home/remospeed/codex_work`

SSH checks:

- `ssh remospeed@100.97.207.91` initially failed before network access because local system SSH config reported `Bad owner or permissions on /etc/ssh/ssh_config.d/20-systemd-ssh-proxy.conf`.
- Retried with `ssh -F /dev/null ... remospeed@100.97.207.91`.
- Result: host reachable, authentication failed with `Permission denied (publickey,password)`.
- Retried hostname `remospeed-optiplex-7010`; DNS resolution failed from Lenovo.

Required fields:

| Field | Result |
| --- | --- |
| SSH reachable | YES, TCP/SSH endpoint responded at `100.97.207.91`; usable login NO due authentication failure |
| OptiPlex hostname/user/path | `remospeed-optiplex-7010` / `remospeed` / expected `/home/remospeed/codex_work` from docs |
| `MUSIC_RELATIONSHIPS_DB` present | UNKNOWN, remote command not authenticated |
| `MUSIC_RELATIONSHIPS_DB` HEAD | UNKNOWN, remote command not authenticated |
| `MUSIC_RELATIONSHIPS_DB` git clean | UNKNOWN, remote command not authenticated |
| `Music_Reference_DB` present | UNKNOWN, remote command not authenticated |
| `Music_Reference_DB` HEAD | UNKNOWN, remote command not authenticated |
| `Music_Reference_DB` git clean | UNKNOWN, remote command not authenticated |
| `PROYECTO_00` present | UNKNOWN, remote command not authenticated |
| Music folder present | UNKNOWN, remote command not authenticated |

Remaining blockers:

- Remote SSH authentication to OptiPlex must be fixed or credentials/keys must be provided.
- After SSH works, verify on OptiPlex:
  - `/home/remospeed/codex_work/MUSIC_RELATIONSHIPS_DB`
  - `/home/remospeed/codex_work/Music_Reference_DB`
  - `/home/remospeed/codex_work/PROYECTO_00`
  - `/home/remospeed/Music` or the authoritative Music folder
- For each existing OptiPlex Git repository, run `git status`, `git log --oneline -5`, and `git remote -v`.

READY_FOR_MASTER_NODE_MIGRATION = NO

Exact blockers:

- OptiPlex SSH login is not usable from Lenovo: `remospeed@100.97.207.91` returns `Permission denied (publickey,password)`.
- OptiPlex copies of `MUSIC_RELATIONSHIPS_DB`, `Music_Reference_DB`, and `PROYECTO_00` are unverified.
- OptiPlex authoritative Music folder is unverified.

Lenovo deletion candidates:

- None approved at this time.
- Do not delete any Lenovo copy until OptiPlex verification is completed and recorded.
