<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.store.counts.CountsRotationTest#shouldCreateEmptyCountsTrackerStoreWhenCreatingDatabase()`\
target: `org.neo4j.kernel.impl.store.counts.CountsRotationTest#createCountsTracker(PageCache)`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker(pageCache PageCache) : CountsTracker extracted from public shouldCreateEmptyCountsTrackerStoreWhenCreatingDatabase() : void in class org.neo4j.kernel.impl.store.counts.CountsRotationTest`

id: `1`\
source `org.neo4j.kernel.impl.store.counts.CountsRotationTest#shouldRotateCountsStoreWhenClosingTheDatabase()`\
target: `org.neo4j.kernel.impl.store.counts.CountsRotationTest#createCountsTracker(PageCache)`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker(pageCache PageCache) : CountsTracker extracted from public shouldRotateCountsStoreWhenClosingTheDatabase() : void in class org.neo4j.kernel.impl.store.counts.CountsRotationTest`

id: `2`\
source `org.neo4j.kernel.impl.store.counts.CountsRotationTest#shouldRotateCountsStoreWhenRotatingLog()`\
target: `org.neo4j.kernel.impl.store.counts.CountsRotationTest#createCountsTracker(PageCache)`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker(pageCache PageCache) : CountsTracker extracted from public shouldRotateCountsStoreWhenRotatingLog() : void in class org.neo4j.kernel.impl.store.counts.CountsRotationTest`

