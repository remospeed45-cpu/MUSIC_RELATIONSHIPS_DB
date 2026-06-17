# UNIT-0038 Recovered Candidate Classification Report

## Goal

Classify recovered performer-name candidates before authority promotion.

## Source

- imports/unit0037_recovered_performer_candidates/UNIT0037_RECOVERED_PERFORMER_CANDIDATES.tsv

## Output

- imports/unit0038_recovered_candidate_classification/UNIT0038_RECOVERED_CANDIDATE_CLASSIFICATION.tsv

## Results

- probable_group: 45
- probable_performer: 11
- review_required: 42
- total candidates: 98

## Rules

- Ensemble keywords classify as probable_group.
- Names containing " y " classify as review_required.
- Remaining single-name patterns classify as probable_performer.

## Recommendation

Promote only probable_group and probable_performer in separate units.

Do not promote review_required automatically.

## Confidence

medium-high for classification gate

## Review Status

classified
