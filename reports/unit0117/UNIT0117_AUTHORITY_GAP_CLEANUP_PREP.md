# UNIT0117 Authority Gap Cleanup Prep

## Objective

Normalize UNIT0116 split_only authority gaps before promoting missing performer/group entities.

## Inputs

- authority/staging/unit0116/UNIT0116_MISSING_GROUPS.tsv
- authority/staging/unit0116/UNIT0116_MISSING_PERFORMERS.tsv

## Output

- authority/staging/unit0117/UNIT0117_ENTITY_CLEANUP_CANDIDATES.tsv

## Summary

- raw_unique_entities: 19
- promotion_candidate_entities: 18
- review_required_entities: 1

## Review Required

- Siente el Vallenato

Reason: ambiguous name. It may be a collection/release phrase rather than a performer/group identity.

## Recommendation

Proceed to UNIT0118 to promote the 18 clean missing entities before rebuilding the SRC0002 recovery promotion set.
