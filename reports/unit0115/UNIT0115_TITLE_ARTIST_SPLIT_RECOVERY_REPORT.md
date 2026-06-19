# UNIT0115 Title-Artist Split Recovery Report

## Objective

Recover UNIT0114 performer_conflict rows where the actual performer/group is embedded inside candidate_title.

## Inputs

- `authority/staging/unit0114/UNIT0114_REVIEW_REQUIRED.tsv`
- `authority/performers/performers_master.tsv`
- `authority/groups/groups_master.tsv`

## Outputs

- `authority/staging/unit0115/UNIT0115_TITLE_ARTIST_SPLIT_RECOVERY.tsv`

## Counts

- performer_conflict_rows_analyzed: 159
- recovered_entity: 97
- match_type_group: 97
- match_type_none: 62
- split_only: 42
- not_recovered: 20

## Top Extracted Artists

| extracted_artist_name | rows |
|---|---:|
| Los Hispanos | 67 |
| Rodolfo Aicardi Y Su Tipica Ra7 | 17 |
| Los Alegres Parranderos | 5 |
| Los Corraleros de Majagual | 4 |
| Rodolfo Aicardi | 4 |
| La Sonora Dinamita | 3 |
| Calixto Ochoa y Su Conjunto | 2 |
| Lisandro Meza y Su Conjunto | 2 |
| Armando Hernández con el Combo Caribe | 2 |
| Alfredo Gutiérrez y Su Conjunto | 2 |
| Pacho Galán y Su Orquesta | 2 |
| Conjunto Típico Vallenato | 2 |
| Agustín Bedoya y Su Conjunto | 2 |
| Rodolfo Aicardi Con El Grupo Monteadentro | 2 |
| Rodolfo Aicardi Con Los Idolos | 2 |
| Guillermo Portabales | 1 |
| La Sonora Matancera | 1 |
| Orquesta de Bebo Valdés | 1 |
| Celina y Reutilio | 1 |
| Fruko y Orquesta | 1 |
| Los Compadres | 1 |
| Roberto Ledesma | 1 |
| Trío Matamoros | 1 |
| Orlando Contreras | 1 |
| Los Guaracheros de Oriente | 1 |
| Los Cumbiamberos de Pacheco | 1 |
| Lito Barrientos y Su Orquesta | 1 |
| Clímaco Sarmiento y Su Orquesta | 1 |
| Pedro Laza y Sus Pelayeros | 1 |
| Joaquín Bedoya y Su Conjunto | 1 |
| El Manicomio de Vargasvil | 1 |
| Los Integrados | 1 |
| Bobby Cruz | 1 |
| Siente el Vallenato | 1 |
| Rodolfo Aicardi Con Los Bestiales | 1 |
| Rodolfo Aicardi Con Los Hermanos Aicardi | 1 |
