# UNIT0109 CELIA CRUZ PROMOTION PREPARATION

## Objective

Convert UNIT0108 Celia Cruz staging into promotion-ready authority candidates without modifying master authority files.

## Input

- `authority/staging/unit0108/`

## Audit Scope

UNIT0108 produced 18 unique recording-title rows. One row, `Perdón`, is an existing master duplicate (`REC005595` / `SONG004248`), leaving 17 new recording/song candidates for promotion preparation.

## Validation Rules

Candidates were checked for:

- master recording duplicate by normalized exact title
- master song duplicate by normalized exact title
- title normalization issues
- performer text containing Celia Cruz
- consistency with existing performer authority `PER000001`
- group signal for Sonora Matancera where applicable
- release evidence from UNIT0108 staging
- low-confidence event/mix/compilation rows

## Results

| Split | Count | MP3 instances represented |
| --- | ---: | ---: |
| PROMOTION_READY | 13 | 16 |
| REVIEW_REQUIRED | 4 | 4 |

actual_mp3_gain_after_promotion: 16

ready_for_promotion: YES

## Promotion Ready Summary

Promotion-ready rows are clean new candidate titles with no normalized master duplicate, usable confidence, and performer text that includes Celia Cruz. Duplicate MP3 instances are allowed when they collapse to one authority candidate title.

## Review Required Summary

Review-required rows include low-confidence event or compilation-like rows, incomplete title extraction, and spelling/title normalization issues.

Excluded existing authority match:

- `Perdón` was excluded from the 17 new-candidate split because it already exists as recording `REC005595` and song `SONG004248`.

## Output Files

- `authority/staging/unit0109/UNIT0109_PROMOTION_READY.tsv`
- `authority/staging/unit0109/UNIT0109_REVIEW_REQUIRED.tsv`

## Recommendation

Proceed with a controlled promotion unit using only `UNIT0109_PROMOTION_READY.tsv`. Do not promote review-required rows until each issue is resolved.
