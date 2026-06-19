# UNIT0106 MP3 COVERAGE AUDIT

## Objective

Measure authority coverage against UNIT0105 MP3 scan results.

## Inputs

- `imports/unit0105_mp3_scan/UNIT0105_MP3_SCAN_ALL.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_KNOWN_RECORDINGS.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_PROBABLE_SONGS.tsv`
- `imports/unit0105_mp3_scan/UNIT0105_MP3_UNKNOWN.tsv`

## Coverage Summary

| Metric | Count |
| --- | ---: |
| total_mp3_scanned | 2072 |
| known_recordings | 108 |
| probable_song_matches | 2 |
| unknown_mp3 | 1962 |
| coverage_percent | 5.21% |

Coverage definition:

- `coverage_percent = known_recordings / total_mp3_scanned`
- Probable song matches are partial identity signals and are not counted as known recording coverage.
- If known recordings and probable song matches are combined, partial coverage is 5.31%.

## Findings

- Strict recording-level authority coverage is low: 108 of 2072 scanned MP3 files.
- Unknown MP3 inventory dominates the scan: 1962 files.
- The largest non-actionable bucket is `UNKNOWN_ARTIST` with 382 files; this is a metadata/filename parsing target before authority promotion.
- Named artist expansion targets are concentrated enough to support batch authority expansion.
- Folder-level unknowns are spread across repeated playlist-like folders, with `Revisar/Musica Vieja Colombiana` as the largest folder target.

## TOP_AUTHORITY_EXPANSION_TARGETS

Ranked by unknown MP3 count for named artist signals only. Generic `UNKNOWN_ARTIST` and `[unknown]` were excluded from authority expansion ranking.

| Rank | Target | unknown_mp3 | Recommended action |
| ---: | --- | ---: | --- |
| 1 | Willie Colón | 13 | Build recording/song authority batch from unknown MP3 rows |
| 2 | Joe Arroyo | 12 | Build recording/song authority batch from unknown MP3 rows |
| 3 | Rufo Garrido | 10 | Build recording/song authority batch from unknown MP3 rows |
| 4 | Francisco Canaro | 10 | Build recording/song authority batch from unknown MP3 rows |
| 5 | Celia Cruz | 10 | Build recording/song authority batch from unknown MP3 rows |
| 6 | Tito Rojas | 9 | Build recording/song authority batch from unknown MP3 rows |
| 7 | Sonora Ponceña | 9 | Build recording/song authority batch from unknown MP3 rows |
| 8 | Ray Barretto | 9 | Build recording/song authority batch from unknown MP3 rows |
| 9 | Ismael Rivera | 9 | Build recording/song authority batch from unknown MP3 rows |
| 10 | Fernando Villalona | 9 | Build recording/song authority batch from unknown MP3 rows |
| 11 | Trio La Rosa | 8 | Build recording/song authority batch from unknown MP3 rows |
| 12 | Rubén Blades | 8 | Build recording/song authority batch from unknown MP3 rows |
| 13 | Leonardo Favio | 8 | Build recording/song authority batch from unknown MP3 rows |
| 14 | La Sonora Ponceña | 8 | Build recording/song authority batch from unknown MP3 rows |
| 15 | Héctor Lavoe | 8 | Build recording/song authority batch from unknown MP3 rows |
| 16 | Fruko y sus Tesos | 8 | Build recording/song authority batch from unknown MP3 rows |
| 17 | Tito Nieves | 7 | Build recording/song authority batch from unknown MP3 rows |
| 18 | The Latin Brothers | 7 | Build recording/song authority batch from unknown MP3 rows |
| 19 | Los Corraleros de Majagual | 7 | Build recording/song authority batch from unknown MP3 rows |
| 20 | Leo Dan | 7 | Build recording/song authority batch from unknown MP3 rows |

## Output Files

- `reports/unit0106/UNIT0106_MP3_COVERAGE_AUDIT.md`
- `reports/unit0106/UNIT0106_TOP_UNKNOWN_ARTISTS.tsv`
- `reports/unit0106/UNIT0106_TOP_UNKNOWN_FOLDERS.tsv`

## Next Safe Unit

Use the named artist target ranking to stage one controlled authority expansion batch. Keep `UNKNOWN_ARTIST` as a separate metadata parsing and folder-context review unit.
