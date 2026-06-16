# UNIT-0015 IMPORT REPORT

Status: COMPLETE

Source:
LATIN_MUSIC_AUTHORITY_DB
data/src0010/peerless_ajax_full_0001/peerless_ajax_records_0001.tsv

Imported into:
imports/unit0015_frontera_peerless/UNIT0015_PEERLESS_RECORDING_RELATIONSHIP_STAGING.tsv

Rows imported:
5500

Validation:
All rows have 17 fields.

Review status:
raw_extracted: 5485
needs_review: 15

Promotion:
None.

Next:
UNIT-0016 should normalize Peerless staging into reusable relationship candidates:
- recording -> source
- recording -> label
- recording -> performer/group candidate
- recording -> song candidate
