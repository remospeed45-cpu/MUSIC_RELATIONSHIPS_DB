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
