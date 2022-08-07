<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.graylog2.indexer.searches.SearchesTest`\
target: `org.graylog2.indexer.ranges.EsIndexRangeServiceTest#testTimestampStatsOfIndex()`\
type: `MOVE`\
commit: [767171c90](https://github.com/Graylog2/graylog2-server/commit/767171c90110c4c5781e8f6d19ece1fba0d492e9)\
description: `Move Method public testTimestampStatsOfIndex() : void from class org.graylog2.indexer.searches.SearchesTest to public testTimestampStatsOfIndex() : void from class org.graylog2.indexer.ranges.EsIndexRangeServiceTest`

id: `1`\
source `org.graylog2.indexer.searches.SearchesTest`\
target: `org.graylog2.indexer.ranges.EsIndexRangeServiceTest#testTimestampStatsOfIndexWithNonExistingIndex()`\
type: `MOVE`\
commit: [767171c90](https://github.com/Graylog2/graylog2-server/commit/767171c90110c4c5781e8f6d19ece1fba0d492e9)\
description: `Move Method public testTimestampStatsOfIndexWithNonExistingIndex() : void from class org.graylog2.indexer.searches.SearchesTest to public testTimestampStatsOfIndexWithNonExistingIndex() : void from class org.graylog2.indexer.ranges.EsIndexRangeServiceTest`

id: `2`\
source `org.graylog2.indexer.searches.SearchesTest`\
target: `org.graylog2.indexer.ranges.EsIndexRangeServiceTest#testTimestampStatsOfIndexWithEmptyIndex()`\
type: `MOVE`\
commit: [767171c90](https://github.com/Graylog2/graylog2-server/commit/767171c90110c4c5781e8f6d19ece1fba0d492e9)\
description: `Move Method public testTimestampStatsOfIndexWithEmptyIndex() : void from class org.graylog2.indexer.searches.SearchesTest to public testTimestampStatsOfIndexWithEmptyIndex() : void from class org.graylog2.indexer.ranges.EsIndexRangeServiceTest`

