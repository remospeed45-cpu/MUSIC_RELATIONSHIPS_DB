# UNIT-0046 Gemini Review Export Report

## Goal

Prepare review_required recovered artist candidates for Gemini/human classification.

## Source

- imports/unit0038_recovered_candidate_classification/UNIT0038_RECOVERED_CANDIDATE_CLASSIFICATION.tsv
- imports/unit0036_artist_recovery/UNIT0036_RECOVERABLE_PERFORMER_TEXT.tsv

## Output

- exports/unit0046_gemini_review/UNIT0046_REVIEW_REQUIRED_ARTIST_CANDIDATES_FOR_GEMINI.tsv

## Results

- review_required candidates exported: 42

## Intended Gemini Decision Values

- group
- duo
- multiple_performers
- individual_performer
- review_required

## Human Review

Human review remains final authority before promotion.

## Confidence

high for export structure

## Review Status

pending_external_review
