<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#nodeDegreeByDirection(long,RelationshipGroupRecord,Direction)`\
type: `MOVE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move Method private nodeDegreeByDirection(nodeId long, group RelationshipGroupRecord, direction Direction) : long from class org.neo4j.kernel.impl.api.store.DiskLayer to private nodeDegreeByDirection(group RelationshipGroupRecord, direction Direction) : long from class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor`

id: `1`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#directionOf(long,long,long,long)`\
type: `MOVE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move Method private directionOf(nodeId long, relationshipId long, startNode long, endNode long) : Direction from class org.neo4j.kernel.impl.api.store.DiskLayer to private directionOf(nodeId long, relationshipId long, startNode long, endNode long) : Direction from class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor`

id: `2`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#countByFirstPrevPointer(long,long)`\
type: `MOVE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move Method private countByFirstPrevPointer(nodeId long, relationshipId long) : long from class org.neo4j.kernel.impl.api.store.DiskLayer to private countByFirstPrevPointer(relationshipId long) : long from class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor`

id: `3`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreStatement#nodesGetAllCursor(StoreStatement)`\
type: `MOVE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move Method public nodesGetAllCursor(statement StoreStatement) : Cursor<NodeItem> from class org.neo4j.kernel.impl.api.store.DiskLayer to public nodesGetAllCursor() : Cursor<NodeItem> from class org.neo4j.kernel.impl.api.store.StoreStatement`

id: `4`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreStatement#relationshipsGetAllCursor(StoreStatement)`\
type: `MOVE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move Method public relationshipsGetAllCursor(storeStatement StoreStatement) : Cursor<RelationshipItem> from class org.neo4j.kernel.impl.api.store.DiskLayer to public relationshipsGetAllCursor() : Cursor<RelationshipItem> from class org.neo4j.kernel.impl.api.store.StoreStatement`

id: `5`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#degree(Direction)`\
type: `MOVE_RENAME`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Rename Method public nodeGetDegree(statement StoreStatement, nodeId long, direction Direction) : int from class org.neo4j.kernel.impl.api.store.DiskLayer to public degree(direction Direction) : int from class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor`

id: `6`\
source `org.neo4j.kernel.impl.api.store.DiskLayer`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#degree(Direction,int)`\
type: `MOVE_RENAME`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Rename Method public nodeGetDegree(statement StoreStatement, nodeId long, direction Direction, relType int) : int from class org.neo4j.kernel.impl.api.store.DiskLayer to public degree(direction Direction, relType int) : int from class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor`

