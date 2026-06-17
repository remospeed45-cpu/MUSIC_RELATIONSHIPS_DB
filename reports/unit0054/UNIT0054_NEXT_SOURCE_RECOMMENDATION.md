# UNIT-0054 Next Source Recommendation

## Recommendation

Next source batch: `SRC0002 Discos Fuentes` label catalog acquisition.

## Rationale

`SRC0002 Discos Fuentes` maximizes expected growth among registered sources:

- It is Priority A in `authority/sources/sources_master.tsv`.
- Current master tables contain no SRC0002 recordings and no SRC0002 songs.
- Current authority usage for SRC0002 is limited to one group authority row, `GRP0002 Orquesta Lucho Bermudez`.
- A label catalog batch is likely to provide reusable recording-centered relationships: recording -> song, recording -> performer/group, recording -> label, recording -> release, and recording -> source.
- It avoids spending UNIT-0054 effort on the 13 frozen unresolved Peerless/Frontera backlog rows.

## Compared Sources

| source_id | source_name | priority | recommendation status | reason |
|---|---|---|---|---|
| SRC0001 | Frontera | A | do not select now | Current Peerless/Frontera batch is processed; remaining 13 unresolved records are frozen backlog. |
| SRC0002 | Discos Fuentes | A | select next | Highest registered-source growth potential; almost absent from current recording and song authority. |
| SRC0003 | Diaz-Ayala | B | later | Valuable historical discography source, but only a small seed exists and priority is lower than Discos Fuentes. |
| SRC0004 | MusicBrainz | C | later / corroboration | Better as a reference cross-check than primary recording acquisition. |
| SRC0005 | Discogs | C | later / corroboration | Useful for release metadata, but lower source priority and weaker as primary authority. |
| SRC0006 | Cuba Canta y Baila | B | later | Historical value, but no scoped tracked dataset exists yet. |

## Proposed Next Unit Shape

The next unit should acquire or define a Discos Fuentes source batch with recording-centered fields:

- raw_recording_title
- canonical_recording_title
- canonical_song_title
- performer_name
- group_name
- release_title
- label_name
- catalog_number
- recording_year
- country
- source_reference
- evidence_text
- confidence
- review_status

## Estimated Value

| metric | estimate |
|---|---|
| estimated_recordings | High; current repo has 0 SRC0002 recording rows, so any valid batch expands coverage rather than only filling gaps. |
| estimated_songs | High; Discos Fuentes catalog titles should create new song authority candidates and recording-song links. |
| estimated_relationship_value | High; expected to add recording-source, recording-label, recording-song, recording-performer/group, song-artist, and likely release relationships. |

## Required Guardrails

- Do not work on the 13 UNIT-0053 frozen unresolved Peerless/Frontera records.
- Do not promote source rows without recording-centered evidence.
- Prefer an initial bounded Discos Fuentes batch over an open-ended web crawl.
- Create staging first, then validate row counts and required fields before promotion.

## Final Recommendation

Start UNIT-0055 with a bounded `SRC0002 Discos Fuentes` label catalog acquisition/import plan. This is the highest-value next source because it is registered, Priority A, materially underrepresented, and likely to grow recordings, songs, and relationships simultaneously.
