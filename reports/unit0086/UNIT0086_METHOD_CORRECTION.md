# UNIT-0086 — Method Correction

## Problem
Workflow became too small and administrative.

## Decision
Stop micro-units and micro-commits.

## New Mode
SRC0003 FANIA BULK HARVEST

## Objective
Capture larger blocks of release/track data before analysis.

## Rules
- One acquisition script
- One bulk data folder
- One staging TSV
- One report at the end
- No promotion
- No master modification
- No per-release commit unless necessary

## Target
Acquire many release candidates in one pass, then analyze as a batch.
