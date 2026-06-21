# FOUNDATION INFRASTRUCTURE MODEL

STANDARD: FOUNDATION V2.3
PROJECT: OPERATIONAL_FOUNDATION

## CANONICAL ARCHITECTURE

BOSGAME is the single canonical storage authority for all active projects.

Canonical root:

- /srv/storage

Canonical projects root:

- /srv/storage/Projects

Canonical FOUNDATION location:

- /srv/storage/Projects/PROYECTO_00/foundation

All active project state, Foundation state, project documentation, startup packets, status files, project memory files, overlays, registries, and operational records are authoritative only when stored under BOSGAME.

## NODE ROLES

### BOSGAME

Role:

- Canonical storage server
- Source-of-truth project location
- Long-term project authority

Tailscale:

- 100.125.192.45

Authority:

- Authoritative

Canonical paths:

- /srv/storage
- /srv/storage/Projects
- /srv/storage/Projects/PROYECTO_00/foundation

### OPTIPLEX

Role:

- Primary processing workstation
- Main execution node
- Bulk processing node
- Codex/session execution node

Tailscale:

- 100.97.207.91

BOSGAME access path:

- ~/BosgameMedia

Authority:

- Not authoritative

Local project copies:

- Working copies only
- May be recreated from BOSGAME
- Must not be treated as source of truth

### LENOVO

Role:

- Continuity workstation
- Secondary execution node
- Emergency continuity node

Tailscale:

- 100.79.167.69

BOSGAME access path:

- ~/BosgameMedia

Authority:

- Not authoritative

Local project copies:

- Working copies only
- May be recreated from BOSGAME
- Must not be treated as source of truth

## AUTHORITY RULE

Repository location does not define operational authority.

BOSGAME defines operational authority.

Git defines historical traceability.

Local working copies on OPTIPLEX or LENOVO are execution environments only.

If there is a conflict between locations, resolve authority in this order:

1. BOSGAME canonical project location
2. Git history
3. Local working copy

## FOUNDATION FILE ROLES

PROJECT_INSTRUCTIONS.txt:

- Durable operating instructions
- Rules for assistants and project agents

FOUNDATION_CONTEXT.md:

- Foundation-wide context
- Stable operating assumptions

FAST_REORIENTATION.md:

- Fast startup and continuation context

CHAT_BOOTSTRAP.md:

- First-chat startup block

FOUNDATION_REGISTRY.md:

- Registered projects and adoption status

INFRASTRUCTURE_MODEL.md:

- Canonical infrastructure architecture

PROJECT_MEMORY.md:

- Durable project knowledge
- Not a command log

PROJECT_OVERLAY.md:

- Project identity and project-specific behavior

PROJECT_STATUS.md:

- Current operational state
- Next action
- Blockers
- Current phase/unit

## LANGUAGE STANDARD

Operational language:

- Spanish

Use Spanish for:

- Analysis
- Planning
- Reviews
- Status reports
- Continuity handoffs
- Project discussions
- Recommendations
- Assistant responses

Use English only for:

- Commands
- Source code
- File names
- Directory names
- Database objects
- API names
- Technical identifiers
- Git messages when explicitly required

Default behavior:

- If there is doubt, respond in Spanish.

This language standard must not be changed unless the owner explicitly authorizes it.

## LOCAL COPY POLICY

Local folders on OPTIPLEX and LENOVO may contain project repositories or working files.

These local copies are temporary operational mirrors.

They are not canonical.

They must not be used to redefine project authority.

Before major work on any execution node:

1. Confirm BOSGAME access.
2. Confirm the intended project path.
3. Pull or synchronize from the authoritative source when applicable.
4. Verify clean working state before modifications when Git is involved.
5. Commit and push durable changes when appropriate.

## PROHIBITED ASSUMPTIONS

Do not assume:

- OPTIPLEX project folders are authoritative.
- LENOVO project folders are authoritative.
- A local copy is current merely because it exists.
- Foundation is a command log.
- PROJECT_MEMORY.md should store transient execution output.
- PROJECT_STATUS.md should store long-term project knowledge.

## FOUNDATION V2.3 FINAL ARCHITECTURE SUMMARY

BOSGAME is the canonical project authority.

OPTIPLEX executes.

LENOVO continues.

Git records history.

Foundation controls continuity.

Spanish is the operational language.

## EXECUTION TARGET RULE

Foundation operates in a multi-machine environment.

Whenever commands are provided, the execution target must be explicitly identified.

Examples:

PEGA ESTO EN OPTIPLEX

PEGA ESTO EN LENOVO

PEGA ESTO EN BOSGAME

PEGA ESTO EN CODEX (OPTIPLEX)

PEGA ESTO EN CODEX (LENOVO)

PEGA ESTO EN TERMINAL BOSGAME

Never provide command blocks without specifying the target machine.

Assume a multi-machine environment by default.

When a command could be executed on multiple systems, identify the preferred execution location and explain why.

If the execution location is uncertain, resolve the target machine before providing commands.
