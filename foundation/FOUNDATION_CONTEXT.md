# FOUNDATION CONTEXT

## PURPOSE

FOUNDATION is an operational continuity framework for long-running ChatGPT-assisted projects.

It exists to preserve project direction, reduce drift, support migration between chats, and keep work reproducible across machines and sessions.

## CORE PRINCIPLES

1. Git is the source of truth.
2. Chat history is temporary working context.
3. Repository files define operational memory.
4. Work must proceed in small validated units.
5. Project-specific rules must not contaminate other projects.
6. Framework evolution must remain separate from project execution.

## STANDARD STRUCTURE

foundation/
├── PROJECT_INSTRUCTIONS.txt
├── FOUNDATION_CONTEXT.md
├── FAST_REORIENTATION.md
├── CHAT_BOOTSTRAP.md
├── PROJECT_OVERLAY.md
└── PROJECT_STATUS.md

## FILE ROLES

PROJECT_INSTRUCTIONS.txt:
Text pasted into ChatGPT Project Instructions.

FOUNDATION_CONTEXT.md:
Global reusable FOUNDATION framework context.

FAST_REORIENTATION.md:
Quick recovery and migration procedure.

CHAT_BOOTSTRAP.md:
Instruction file used in the first chat or after migration.

PROJECT_OVERLAY.md:
Project-specific identity, rules, scope, and conventions.

PROJECT_STATUS.md:
Current operational state, next action, risks, and blockers.

PROJECT_MEMORY.md:
Durable project knowledge, important decisions, stable architecture, operational rules, lessons learned, and important references. Not a command log.

INFRASTRUCTURE_MODEL.md:
Defines canonical machines, storage roots, access paths, node roles, and infrastructure boundaries.

## OPERATIONAL RULE

When starting or migrating a chat, use the files in foundation/ to reconstruct the project context instead of relying only on chat memory.
