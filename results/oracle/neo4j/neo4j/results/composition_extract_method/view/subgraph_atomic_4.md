<img src=subgraph_atomic_4.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.store.counts.CountsComputerTest#shouldCreateACountStoreWhenDBContainsDenseNodes()`\
target: `org.neo4j.kernel.impl.store.counts.CountsComputerTest#createCountsTracker()`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker() : CountsTracker extracted from public shouldCreateACountStoreWhenDBContainsDenseNodes() : void in class org.neo4j.kernel.impl.store.counts.CountsComputerTest`

id: `1`\
source `org.neo4j.kernel.impl.store.counts.CountsComputerTest#shouldCreateACountsStoreWhenThereAreNodesAndRelationshipsInTheDB()`\
target: `org.neo4j.kernel.impl.store.counts.CountsComputerTest#createCountsTracker()`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker() : CountsTracker extracted from public shouldCreateACountsStoreWhenThereAreNodesAndRelationshipsInTheDB() : void in class org.neo4j.kernel.impl.store.counts.CountsComputerTest`

id: `2`\
source `org.neo4j.kernel.impl.store.counts.CountsComputerTest#shouldCreateAnEmptyCountsStoreFromAnEmptyDatabase()`\
target: `org.neo4j.kernel.impl.store.counts.CountsComputerTest#createCountsTracker()`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker() : CountsTracker extracted from public shouldCreateAnEmptyCountsStoreFromAnEmptyDatabase() : void in class org.neo4j.kernel.impl.store.counts.CountsComputerTest`

id: `3`\
source `org.neo4j.kernel.impl.store.counts.CountsComputerTest#shouldCreateACountsStoreWhenThereAreUnusedRelationshipRecordsInTheDB()`\
target: `org.neo4j.kernel.impl.store.counts.CountsComputerTest#createCountsTracker()`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker() : CountsTracker extracted from public shouldCreateACountsStoreWhenThereAreUnusedRelationshipRecordsInTheDB() : void in class org.neo4j.kernel.impl.store.counts.CountsComputerTest`

id: `4`\
source `org.neo4j.kernel.impl.store.counts.CountsComputerTest#shouldCreateACountsStoreWhenThereAreNodesInTheDB()`\
target: `org.neo4j.kernel.impl.store.counts.CountsComputerTest#createCountsTracker()`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker() : CountsTracker extracted from public shouldCreateACountsStoreWhenThereAreNodesInTheDB() : void in class org.neo4j.kernel.impl.store.counts.CountsComputerTest`

id: `5`\
source `org.neo4j.kernel.impl.store.counts.CountsComputerTest#shouldCreateACountsStoreWhenThereAreUnusedNodeRecordsInTheDB()`\
target: `org.neo4j.kernel.impl.store.counts.CountsComputerTest#createCountsTracker()`\
type: `EXTRACT`\
commit: [5fa74fbb4](https://github.com/neo4j/neo4j/commit/5fa74fbb4a307571e3807c1201b8b05d3d60a99b)\
description: `Extract Method private createCountsTracker() : CountsTracker extracted from public shouldCreateACountsStoreWhenThereAreUnusedNodeRecordsInTheDB() : void in class org.neo4j.kernel.impl.store.counts.CountsComputerTest`

