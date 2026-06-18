# PROMOTION RULES

RULE-0001
Recording is primary entity.

RULE-0002
Recording -> Song -> Performer -> Release -> Label -> Source.

RULE-0003
Reuse existing SONG_ID whenever possible.

RULE-0004
Reuse existing performer_id whenever possible.

RULE-0005
Reuse existing label_id whenever possible.

RULE-0006
Promote by artist blocks.

RULE-0007
Preserve append-only workflow.

RULE-0008
Git commit every completed unit.

RULE-0009
Push completed units.

RULE-0010
Document every process improvement.

RULE-0011
Use primary_artist exactly as stored in source tracklist unless later authority correction is needed.

RULE-0012
Multi-artist blocks are allowed when all releases come from validated local source tracklists.

RULE-0013
Before new external acquisition, inventory local source tracklists and promote any unpromoted complete tracklists first.

RULE-0014
If source tracklist titles exactly match promoted release recordings, mark the release as PROMOTED_PASS and do not reopen it.

RULE-0015
MP3 organization priority:
1. Identify existing MP3s against local database.
2. Reuse known recording/song/performer/release relationships.
3. Only research unknown or unmatched MP3s.
4. Never modify MP3 files during scan.

RULE-0016
Scanner outputs must be TSV files suitable for later promotion or placement planning.
