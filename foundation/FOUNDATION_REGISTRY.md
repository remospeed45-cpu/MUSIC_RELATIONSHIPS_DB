# FOUNDATION REGISTRY

## FOUNDATION VERSION

FOUNDATION STANDARD V2.2

## STATUS

ACTIVE

## PURPOSE

This file is the authoritative registry of the FOUNDATION framework.

## REQUIRED FILES

PROJECT_INSTRUCTIONS.txt
FOUNDATION_CONTEXT.md
FAST_REORIENTATION.md
CHAT_BOOTSTRAP.md
INFRASTRUCTURE_MODEL.md
PROJECT_OVERLAY.md
PROJECT_STATUS.md
PROJECT_MEMORY.md

## FILE CLASSIFICATION

### FOUNDATION CORE

PROJECT_INSTRUCTIONS.txt
FOUNDATION_CONTEXT.md
FAST_REORIENTATION.md
CHAT_BOOTSTRAP.md
INFRASTRUCTURE_MODEL.md
FOUNDATION_REGISTRY.md

These files are reusable across projects.

### PROJECT FILES

PROJECT_OVERLAY.md
PROJECT_STATUS.md
PROJECT_MEMORY.md

These files are project-specific.

## CANONICAL INFRASTRUCTURE

BOSGAME
- Canonical storage server
- Tailscale: 100.125.192.45
- Root: /srv/storage

OPTIPLEX
- Primary processing workstation
- Tailscale: 100.97.207.91

LENOVO
- Continuity workstation
- Tailscale: 100.79.167.69

## DEPLOYMENT RULE

When creating a new project:

1. Copy FOUNDATION CORE.
2. Create PROJECT_OVERLAY.md.
3. Create PROJECT_STATUS.md.
4. Paste PROJECT_INSTRUCTIONS.txt into ChatGPT Project Instructions.
5. Upload remaining FOUNDATION files to the first chat.

## CHANGE CONTROL

Future FOUNDATION changes must update this registry.
