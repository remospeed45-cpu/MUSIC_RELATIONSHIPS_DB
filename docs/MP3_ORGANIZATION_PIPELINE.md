# MP3 Organization Pipeline

Project: MUSIC_RELATIONSHIPS_DB

## Goal

Build the database by scanning the user's real MP3 collection.

## Safety

- Read-only scan.
- No rename.
- No move.
- No metadata write.
- No tag update.

## Pipeline

MP3 folder
→ filename/tag inventory
→ local database match
→ known/probable/unknown TSV
→ promotion candidates
→ placement plan

## Tools

Allowed:

- Python
- mutagen
- beets
- fpcalc / chromaprint
- pyacoustid

Initial scanner must work even without external services.
