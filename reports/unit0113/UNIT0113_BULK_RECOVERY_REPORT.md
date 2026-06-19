# UNIT0113 SRC0002 Bulk Recovery Report

## Objective
Recover highest-yield remaining SRC0002 authority inventory from `reports/unit0066/REMAINING_RAW.tsv` into staging only. No master authority files were modified.

## Source Inventory
- Source file: `reports/unit0066/REMAINING_RAW.tsv`
- Source rows analyzed: 22
- Estimated recordings in source inventory: 297
- Estimated songs in source inventory: 297
- Official product pages fetched for extraction: 22
- Track titles extracted from pages: 300
- Extracted candidate titles not already in recordings master: 178
- Extracted candidate titles not already in songs master: 178

## Outputs
- `authority/staging/unit0113/UNIT0113_RECORDING_CANDIDATES.tsv`
- `authority/staging/unit0113/UNIT0113_SONG_CANDIDATES.tsv`
- `authority/staging/unit0113/UNIT0113_REVIEW_REQUIRED.tsv`

## Candidate Summary
- Recording candidate rows staged: 300
- Song candidate rows staged: 300
- Release-level review-required rows: 22
- Auto-promotion candidates: 0
- Promotion ready: NO

All staged track candidates remain `REVIEW_REQUIRED`. The source pages frequently expose only sample tracks for 100-song USB collections while `REMAINING_RAW.tsv` carries larger estimated totals. Promotion from partial page extracts would risk incomplete release reconstruction and duplicate/artist assignment errors.

## Authority Matching
- Existing recording title matches among extracted rows: 122
- Existing song title matches among extracted rows: 122
- Release rows with matched performer or group authority: 5
- Groups observed: Afrosound, La Sonora Matancera, Los 50 de Joselito, Los Corraleros de Majagual, The Latin Brothers
- Performers observed: Helenita Vargas, Joe Arroyo, Pastor López, Rodolfo Aicardi, Toño Fuentes, Varios Artistas, Varios Intérpretes
- Releases observed: 22

## Top Bulk Recovery Opportunities
| Rank | Estimated Recordings | Extracted New Titles | Release | Artist | Tracklist Status | Review Reason |
|---:|---:|---:|---|---|---|---|
| 1 | 30 | 9 | USB - Historia Musical / The Latin Brothers | The Latin Brothers | partial_11_of_30 | incomplete_tracklist_vs_remaining_raw_estimate;remaining_raw_note_stated_content_visible_track_items_5 |
| 2 | 28 | 0 | Aniversario 25 Años | Los 50 de Joselito | partial_0_of_28 | no_track_titles_extracted_from_source_page;incomplete_tracklist_vs_remaining_raw_estimate;remaining_raw_note_stated_content_28_canciones_visible_track_items_5 |
| 3 | 15 | 10 | USB - Colección 100 Parranderas del Siglo | Varios Artistas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 4 | 15 | 10 | USB - Colección 100 Exitos / Cuatro Grandes de la Música Tropical | Varios Artistas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 5 | 15 | 10 | USB - Colección 100 Exitos de Música Cubana | Varios Artistas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 6 | 15 | 10 | USB - Colección 100 Exitos de Diciembre | Varios Artistas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 7 | 15 | 10 | USB - Colección 100 Cumbias, Porros y Gaitas del Siglo | Varios Artistas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 8 | 15 | 0 | USB - Colección Homenaje a Toño Fuentes | Toño Fuentes | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 9 | 15 | 0 | USB - Colección 100 Villancicos del Siglo | Varios Artistas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |
| 10 | 15 | 0 | USB - Colección 100 Exitos / Helenita Vargas | Helenita Vargas | partial_10_of_15 | incomplete_tracklist_vs_remaining_raw_estimate;artist_not_matched_to_authority;remaining_raw_note_stated_content_visible_track_items_15 |

## Estimated MP3 Coverage Gain
- Immediate promotable MP3 gain: 0
- Estimated MP3 gain after full review/extraction: up to 191
- Basis: UNIT0112 ranked `reports/unit0066/REMAINING_RAW.tsv` as the top bulk target with up to 191 MP3 candidate rows; UNIT0113 confirms this inventory is high-yield but not promotion-ready from the partial product-page extracts alone.

## Required Next Actions
1. Build a full-tracklist extraction pass for the 100-song USB collections instead of relying on short product samples.
2. Resolve artist/entity assignment for `Varios Intérpretes` collection rows before promotion.
3. Promote only complete, deduplicated release blocks with song and recording IDs assigned in one controlled unit.

## Final Conclusion
READY_FOR_PROMOTION = NO

Blockers:
- Source pages often expose partial sample tracks while `REMAINING_RAW.tsv` estimates larger release totals.
- Several collection rows use `Varios`, requiring track-level performer/group attribution.
- Extracted rows include existing title matches and require duplicate review before ID assignment.
