# UNIT-0055 SRC0002 Discovery Report

## Objective

Begin controlled authority acquisition for `SRC0002 Discos Fuentes` through source discovery only. This unit creates no master authority records, no relationship rows, and no mass import.

## Repository Verification

- branch: main
- synchronized HEAD at start: 789db6183a8a74ba30ed89e084b9a9dcd52bac4a
- working tree before UNIT-0055 changes: clean

## Source Profile

| field | value |
|---|---|
| source_id | SRC0002 |
| source_name | Discos Fuentes |
| source_type | label_catalog |
| source_priority | A |
| expected_authority_value | High: Colombian tropical, cumbia, porro, vallenato, salsa, artist, release, and recording authority. |

## Existing SRC0002 References In Repository

| area | count | current SRC0002 coverage |
|---|---:|---|
| authority/sources/sources_master.tsv | 1 | `SRC0002 Discos Fuentes` registered as Priority A label catalog. |
| authority/genre_families/genre_families_master.tsv | 1 | `GFAM0002 Colombian Tropical`. |
| authority/genres/genres_master.tsv | 4 | `Porro`, `Cumbia`, `Paseo`, `Vallenato`. |
| authority/groups/groups_master.tsv | 1 | `GRP0002 Orquesta Lucho Bermudez`. |
| relationships/genre_family.tsv | 4 | SRC0002 genre-family links. |
| relationships/group_genre.tsv | 2 | SRC0002 group-genre links for `GRP0002`. |
| authority/recordings/recordings_master.tsv | 0 | No SRC0002 recordings. |
| authority/songs/songs_master.tsv | 0 | No SRC0002 songs. |
| relationships/recording_source.tsv | 0 | No SRC0002 recording-source links. |
| relationships/recording_release.tsv | 0 | No SRC0002 release links. |

## Discovery Sources Reviewed

| acquisition_path | URL | source_type | observed_value | feasibility |
|---|---|---|---|---|
| Official Discos Fuentes site home/catalog navigation | https://discosfuentes.com.co/ | official catalog portal | Site exposes catalog categories including Balada, Bolero, Instrumental, Llanera, Pop-Rock, Popular, Tango, Tropical y Bailable, Reggaeton-Urbano, and Vallenato y Cumbia. | Good for artist/category discovery; weaker for row-level extraction because many category links route to media or visual playlist pages. |
| Official artist directory | https://discosfuentes.com.co/artistas/ | official artist catalog | Lists major artists/groups and category filters; visible examples include Afrosound, Los Corraleros de Majagual, The Latin Brothers, Fruko y sus Tesos, La Sonora Dinamita, Guillermo Buitrago, Pastor Lopez, Daniel Santos, Joe Arroyo y La Verdad, and others. | Good seed source for performer/group authority candidates. |
| Official Tropical y Bailable catalog page | https://discosfuentes.com.co/tropical_y_bailable_playlist/ | official genre/category catalog | Lists a visual genre page with many likely catalog artists, including Los Corraleros de Majagual, Rodolfo Aicardi, Climaco Sarmiento, Guillermo Buitrago, La Sonora Dinamita, Pedro Laza, Pastor Lopez, Wganda Kenya, and others. | Useful for bounded artist/group seed list; not enough alone for recording rows. |
| Official Discos Fuentes shop | https://tiendadiscosfuentes.com/ | official product catalog | Product index exposes purchasable LP, USB, and collection products. | Best first controlled source because product pages expose structured release metadata and track lists. |
| Official shop product page example: 14 Canonazos Bailables Vol 65 | https://tiendadiscosfuentes.com/productos/14-canonazos-bailables/lp-14-canonazos-bailables-vol-65/ | official product/release page | Page includes title, interpreter, genre, format, year, reference number, side/track listing, and track-level performer text. | Strong first-batch template. |
| Official shop product page example: La Cumbia Une a Latinoamerica | https://tiendadiscosfuentes.com/productos/vinilos/lp-la-cumbia-une-a-latinoamerica/ | official product/release page | Page includes title, interpreter, genre, format, year, reference number, and 10 track titles with featured performers. | Strong first-batch template. |
| MusicBrainz | https://musicbrainz.org/ | structured reference database | Broad open music metadata database, useful for release/recording identifiers and corroboration. | Secondary corroboration; do not use as primary SRC0002 authority unless official pages are insufficient. |
| Discogs | https://www.discogs.com/ | structured/user-contributed discography | Large release-level discography marketplace/database, useful for catalog numbers and historical release variants. | Secondary corroboration; good for validating historical catalog numbers after official-source seed extraction. |
| WorldCat | https://www.worldcat.org/ | library catalog | Useful for library-held Discos Fuentes releases and compilation records. | Secondary corroboration for historical release metadata. |

## External Source Evidence Notes

- The official Discos Fuentes home page exposes a catalog menu and states a broad catalog experience through genre/category links.
- The official artist page provides a visible artist directory and genre/category filters.
- The official shop product pages expose structured fields directly useful to this repository: release title, interpreter, genre, format, year, reference number, and track list.
- Public reference summaries describe Discos Fuentes as a Colombian label founded in 1934 with major importance for cumbia, porro, vallenato, salsa, and related Colombian/Latin repertoire.

## Expected Authority Value

| estimate_area | expected_value |
|---|---|
| expected_recordings | First controlled batch: 10-25 recording rows, depending on 1-2 selected product pages. Larger source potential is high because product catalog pages contain track lists. |
| expected_songs | First controlled batch: 10-25 song candidates from product track lists. |
| expected_performers | First controlled batch: 5-20 performer/group candidates, depending on compilations and featured artists. |
| expected_groups | First controlled batch: 5-20 group candidates; Discos Fuentes catalog is group-heavy for tropical, cumbia, salsa, and vallenato. |
| expected_releases | First controlled batch: 1-2 release candidates, which would also begin filling the empty release authority area. |
| expected_relationships | High: recording-source, recording-song, recording-release, recording-label, recording-performer/group, song-artist, release-label, and genre relationships. |

## Feasibility Assessment

Acquisition feasibility: high.

The official shop pages are the safest first acquisition path because they provide bounded pages with explicit metadata and track lists. The official artist and genre pages should be used as context and authority seed support, while MusicBrainz, Discogs, and WorldCat should be used only for corroboration during validation.

## Discovery Status

SRC0002 is acquisition-ready for a small controlled extraction in the next unit. No source rows were imported in UNIT-0055.

