# LESSONS LEARNED

LESSON-0001
UNIT-0095 failed because release_id was assumed.
Always resolve release IDs from releases_master.

LESSON-0002
Tracklist evidence must be compared against promoted recordings.

LESSON-0003
Source tracklists are more reliable than manually assembled title lists.

LESSON-0004
Artist-block promotion is faster than release-by-release promotion.

LESSON-0005
UNIT-0100 showed that many title songs already exist before relationship promotion.
This confirms that the system should prioritize recording relationships over song rediscovery.

LESSON-0006
A successful block unit should be followed by one block audit, not one audit per release.

LESSON-0007
UNIT-0102 showed that not every block will reuse SONG_ID values.
Some artist blocks may add mostly new songs, but block promotion still reduces overhead.

LESSON-0008
Report display names must follow source evidence.
UNIT-0102 source uses Orchestra Harlow, even if discovery note used Larry Harlow.
