# UNIT-0060 SRC0002 Batch Selection Report

## Scope

Source: SRC0002 Discos Fuentes
Approved acquisition source: official Discos Fuentes shop product pages exposed through `product-sitemap.xml` and official product categories.

UNIT-0060 performs planning only. No recording acquisition files, authority master rows, or production relationships were modified.

## Inventory Summary

| Metric | Count |
|---|---:|
| Official product/release pages inventoried | 24 |
| Previously acquired pages detected | 2 |
| Unprocessed pages with visible tracklists | 19 |
| HIGH ranked releases | 9 |
| MEDIUM ranked releases | 8 |
| LOW ranked releases | 7 |

Previously acquired and excluded:

- `LP - 14 Cañonazos Bailables Vol 65`
- `LP - La Cumbia Une a Latinoamérica | Los Cumbia Stars`

## Batch0003 Selection

Recommended acquisition block size: 7 releases, estimated 99 recordings.

| Order | Release/product | Format | Estimated recordings | Estimated artist relationships |
|---:|---|---|---:|---:|
| 1 | LP - Cumbia y Nada Más \| Afrosound | LP Estereo 33 RPM | 11 | 13 |
| 2 | LP - Historia Musical de Los 50 de Joselito | LP Estereo 33 RPM | 13 | 13 |
| 3 | USB - Colección 100 Exitos de La Sonora Matancera | USB | 15 | 15 |
| 4 | USB - Colección 100 Exitos del Siglo \| Joe Arroyo | USB | 15 | 15 |
| 5 | USB - Colección 100 Exitos de Los Corraleros de Majagual | USB | 15 | 15 |
| 6 | USB - Colección 100 Exitos \| Cuatro Grandes de la Música Tropical | USB | 15 | 15 |
| 7 | USB - Colección Homenaje a Toño Fuentes | USB | 15 | 15 |

## Estimated Growth

| Area | Estimate |
|---|---:|
| selected releases | 7 |
| estimated recordings | 99 |
| estimated songs | 99 |
| estimated artist relationships | 101 |

## Rationale

The selected block is large enough to scale beyond single-release extraction while staying inside the requested 75-150 recording target. It combines two LP pages with strong recording-level evidence and five USB collection pages with visible tracklists. The mix balances:

- recording growth through 99 estimated track rows;
- song growth from product pages not yet acquired in SRC0002 staging;
- relationship growth from artist-focused collections and compilation products;
- operational safety by excluding previously processed batch0001 and batch0002 releases.

## Validation

PASS:

- No selected queue row has `already_processed=Y`.
- No selected queue row lacks a visible tracklist.
- `SRC0002_BATCH0003_QUEUE.tsv` contains only unprocessed official product pages.
- UNIT-0060 did not modify authority masters or production relationships.

Validation details:

- processed release rows in queue: 0
- tracklist-unavailable rows in queue: 0

## Next Extraction Cycle

Use `reports/unit0060/SRC0002_BATCH0003_QUEUE.tsv` as the official acquisition list. The next unit should extract release pages in queue order and may split the queue into smaller extraction commits if one turn should remain bounded.
