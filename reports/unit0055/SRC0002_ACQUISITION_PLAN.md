# UNIT-0055 SRC0002 Acquisition Plan

## Objective

Define a controlled first acquisition batch for `SRC0002 Discos Fuentes` that is ready for authority extraction in the next unit.

## Acquisition Method

Manual or scripted extraction from official Discos Fuentes shop product pages into a new staging TSV under `data/src0002/`, followed by validation before any authority promotion.

The first extraction should target product pages with clear release metadata and track lists. Official pages should be treated as primary evidence. MusicBrainz, Discogs, and WorldCat should be used only to corroborate catalog/reference data, not to replace official-source evidence.

## Source URLs

Primary source URLs:

- https://discosfuentes.com.co/
- https://discosfuentes.com.co/artistas/
- https://discosfuentes.com.co/tropical_y_bailable_playlist/
- https://tiendadiscosfuentes.com/
- https://tiendadiscosfuentes.com/productos/14-canonazos-bailables/lp-14-canonazos-bailables-vol-65/
- https://tiendadiscosfuentes.com/productos/vinilos/lp-la-cumbia-une-a-latinoamerica/

Secondary corroboration URLs:

- https://musicbrainz.org/
- https://www.discogs.com/
- https://www.worldcat.org/

## Recommended First Batch

Recommended first batch: official shop product pages with complete track lists.

Batch candidates:

1. `LP - 14 Canonazos Bailables Vol 65`
   - URL: https://tiendadiscosfuentes.com/productos/14-canonazos-bailables/lp-14-canonazos-bailables-vol-65/
   - Expected rows: 14 recordings / 14 songs.
   - Reason: clear compilation page with release title, interpreter, genre, LP format, year, reference number, and side-level track list with performer text.

2. `LP - La Cumbia Une a Latinoamerica | Los Cumbia Stars`
   - URL: https://tiendadiscosfuentes.com/productos/vinilos/lp-la-cumbia-une-a-latinoamerica/
   - Expected rows: 10 recordings / 10 songs.
   - Reason: clear product page with release title, interpreter, genre, format, year, reference number, and track list with featured artists.

Recommended first unit size: 1 product page, preferably `LP - 14 Canonazos Bailables Vol 65`, yielding 14 staged recording rows. If validation is clean, the second page can become the next batch.

## Proposed Staging File

Create this in the next unit:

`data/src0002/SRC0002_DISCOVERY_BATCH_0001.tsv`

Suggested fields:

- raw_source_id
- source_id
- source_name
- source_url
- acquisition_date
- release_title
- release_interpreter
- release_genre
- release_format
- release_year
- reference_number
- side
- track_number
- raw_track_text
- recording_title
- performer_text
- group_text
- featured_artist_text
- label_name
- source_reference
- evidence_text
- confidence
- review_status

## Batch Strategy

1. Capture one official product page only.
2. Preserve raw track text exactly as seen on the page.
3. Split track title and artist text only when the delimiter is explicit.
4. Treat compilation interpreter values like `Varios Interpretes` as release-level text, not as recording artist.
5. Do not promote authority rows during acquisition.
6. Validate row count against the source page's stated track count.
7. Create a review report before any future staging-to-authority promotion.

## Validation Approach

Required validation checks:

- Source URL is present for every staged row.
- Source ID is `SRC0002` for every staged row.
- Track count matches the source page stated count.
- Every row has `release_title`, `recording_title`, `source_reference`, `evidence_text`, `confidence`, and `review_status`.
- Release-level interpreter is not copied into performer/group fields unless the source track row explicitly supports it.
- Featured artist text remains separate until reviewed.
- Candidate recording titles are checked against existing `authority/recordings/recordings_master.tsv` before any future promotion.
- Candidate performer/group names are checked against existing `authority/performers/performers_master.tsv` and `authority/groups/groups_master.tsv`.
- No rows from the 13 UNIT-0053 frozen Peerless/Frontera backlog are touched.

## Expected Unit Size

| batch | expected_release_rows | expected_recording_rows | expected_song_rows | expected_artist_text_values |
|---|---:|---:|---:|---:|
| Batch 0001: 14 Canonazos Bailables Vol 65 | 1 | 14 | 14 | 14-25 |
| Optional Batch 0002: La Cumbia Une a Latinoamerica | 1 | 10 | 10 | 10-20 |

## Acquisition Feasibility

Feasibility: high.

The official shop pages provide enough structured evidence for a controlled first staging batch. The first extraction should remain small so normalization rules for compilation releases, featured artists, and group-heavy Colombian repertoire can be validated before broader acquisition.

## Success Criteria For Next Unit

- `data/src0002/SRC0002_DISCOVERY_BATCH_0001.tsv` exists with one official product page extracted.
- Row count matches the source page track count.
- No master authority or relationship table is modified.
- A validation report documents field completeness and duplicate checks.

