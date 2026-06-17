# UNIT-0058 SRC0002 Batch0002 Extraction Report

## Scope

Source: SRC0002 Discos Fuentes
Batch: batch0002
Release selected: LP - La Cumbia Une a Latinoamérica | Los Cumbia Stars
Source URL: https://tiendadiscosfuentes.com/productos/vinilos/lp-la-cumbia-une-a-latinoamerica/
Captured evidence: `data/src0002/batch0002/source_page.html`

## Selection Rationale

The release was selected from the UNIT-0055 acquisition plan as the next high-value Discos Fuentes product page after batch0001. It is a single official shop product page, has a complete stated 10-track listing, includes release-level artist context, and includes explicit featured artist text on nine tracks. It had not been previously acquired in `data/src0002` or `authority/staging`.

## Source Metadata

| Field | Value |
|---|---|
| release title from source description | La Cumbia Une a Latinamérica |
| product title | LP - La Cumbia Une a Latinoamérica \| Los Cumbia Stars |
| release interpreter | Los Cumbia Stars |
| genre | Tropical - Bailable |
| format | LP Estereo 33 RPM |
| stated content | 10 Tracks |
| year | 2024 |
| reference | 202446 |

## Extracted Tracks

| global_track | side | track | recording_title | artist_text |
|---:|---|---:|---|---|
| 1 | A | 1 | Tanto Que No Aguanto | Los Cumbia Stars |
| 2 | A | 2 | Amapola | Los Cumbia Stars, Papaya Dada |
| 3 | A | 3 | Mi Cocha Pechocha | Los Cumbia Stars, Los Mirlos |
| 4 | A | 4 | Sonidero | Los Cumbia Stars, La Ronda Bogotá |
| 5 | A | 5 | La Canoa Se Va | Los Cumbia Stars, Pascual Ilabaca |
| 6 | B | 1 | Raza | Los Cumbia Stars, C4 Trío |
| 7 | B | 2 | Wepa | Los Cumbia Stars, Onda Sabanera |
| 8 | B | 3 | Coqueto | Los Cumbia Stars, Alemor |
| 9 | B | 4 | Y Volver | Los Cumbia Stars, Cumbia Club |
| 10 | B | 5 | Tierra Mala | Los Cumbia Stars, Aye Alfonso |

## Candidate Counts

| Candidate area | Count |
|---|---:|
| tracks discovered | 10 |
| recording candidates | 10 |
| song candidates | 10 |
| unique artist candidates | 10 |
| recording-song candidate relationships | 10 |
| recording-artist candidate relationships | 19 |
| recording-release candidate relationships | 10 |
| recording-source candidate relationships | 10 |
| total staged candidate relationships | 49 |

## Artist Candidate Notes

The release interpreter `Los Cumbia Stars` is credited on every staged recording. Featured artist candidates were extracted only when the source track row explicitly used `Feat.`. Country qualifiers in parentheses were preserved in the discovery file and stripped from normalized artist candidate text.

Existing current-repo authority signal found during validation:

- `Los Cumbia Stars -> GRP0251`

No production promotion was performed in UNIT-0058.

## Missing Fields

None for required staging fields.

Optional fields intentionally left out of authority staging:

- Composer/lyricist: not present on source page.
- Recording year: source page gives release year only.
- Performer/group production identity for featured artists: staged as candidates only for later validation.

## Validation Results

PASS:

- Source page captured under `data/src0002/batch0002/source_page.html`.
- Track count matches source-stated `10 Tracks`.
- All 10 recording candidates have source URL, release title, recording title, artist text, source reference, evidence text, confidence, and review status.
- All 10 song candidates have source URL, candidate title, source reference, evidence text, confidence, and review status.
- All 10 artist candidates have source URL, raw artist text, candidate type, source reference, evidence text, confidence, and review status.
- Candidate IDs are unique within recording, song, and artist staging files.
- Candidate relationship files resolve to staged recording, song, artist, release, and source identifiers.
- No master authority tables or production relationship tables were modified.

## Files Produced

- `data/src0002/batch0002/SOURCE_EVIDENCE.md`
- `data/src0002/batch0002/SRC0002_DISCOVERY_BATCH_0002.tsv`
- `data/src0002/batch0002/source_page.html`
- `authority/staging/src0002_batch0002_recordings.tsv`
- `authority/staging/src0002_batch0002_songs.tsv`
- `authority/staging/src0002_batch0002_artist_candidates.tsv`
- `relationships/staging/src0002_batch0002_recording_song.tsv`
- `relationships/staging/src0002_batch0002_recording_artist_candidate.tsv`
- `relationships/staging/src0002_batch0002_recording_release.tsv`
- `relationships/staging/src0002_batch0002_recording_source.tsv`
