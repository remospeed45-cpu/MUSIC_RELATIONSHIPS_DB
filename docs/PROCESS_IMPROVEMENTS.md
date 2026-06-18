# PROCESS IMPROVEMENTS

IMPROVEMENT-0001
Reuse existing SONG_ID when title already exists.

IMPROVEMENT-0002
Promote by artist blocks instead of single releases.

IMPROVEMENT-0003
Audit artist blocks instead of every release.

IMPROVEMENT-0004
Prefer relationship growth over authority rediscovery.

IMPROVEMENT-0005
Use source tracklists directly when validated.

IMPROVEMENT-0006
Avoid full-master backups when delta staging is sufficient.

IMPROVEMENT-0007
Measure growth primarily through recordings added.

IMPROVEMENT-0008
Resolve release IDs dynamically.
Never hardcode release IDs.

IMPROVEMENT-0009
UNIT-0100 confirmed block promotion works:
17 candidate recordings promoted in one unit, with 0 songs added and 17 SONG_ID values reused.

IMPROVEMENT-0010
Delta staging is sufficient for block promotion:
UNIT-0100 avoided full master backup and committed only useful staging/report/script artifacts.

IMPROVEMENT-0011
UNIT-0102 confirmed multi-artist block promotion works:
13 recordings promoted across 2 performers and 2 releases in one unit.

IMPROVEMENT-0012
For SRC0003 tracklists already stored locally, promotion should proceed directly from source TSV files without additional research.

IMPROVEMENT-0013
UNIT-0100 through UNIT-0103 confirmed block mode is stable:
30 recordings promoted across 4 releases using two promotion units and two block audits.

IMPROVEMENT-0014
Coverage reports should identify already-promoted local tracklists before opening new acquisition work.

IMPROVEMENT-0015
Shift from manual relationship entry to MP3-driven database growth.

The project goal is organizing MP3 files. Therefore future work should prioritize:
- scanning MP3 filenames and tags
- matching against recordings_master and songs_master
- identifying unknown MP3s
- promoting relationships needed for actual files

IMPROVEMENT-0016
External tools such as beets, chromaprint/fpcalc, mutagen, and pyacoustid may be used only in safe read-only mode first.
No MP3 rename, move, or metadata write is allowed without a placement plan.
