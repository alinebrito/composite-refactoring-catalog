<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.api.store.StoreStatement#acquireNodeRelationshipCursor(boolean,long,long,Direction,int[])`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#relationships(Direction,int...)`\
type: `INLINE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Inline Method public acquireNodeRelationshipCursor(dense boolean, nextRel long, id long, direction Direction, relTypes int[]) : Cursor<RelationshipItem> moved from class org.neo4j.kernel.impl.api.store.StoreStatement to class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor & inlined to public relationships(direction Direction, relTypes int...) : Cursor<RelationshipItem>`

id: `1`\
source `org.neo4j.kernel.impl.api.store.StoreStatement#acquireNodeRelationshipCursor(boolean,long,long,Direction,int[])`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#relationships(Direction)`\
type: `INLINE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Inline Method public acquireNodeRelationshipCursor(dense boolean, nextRel long, id long, direction Direction, relTypes int[]) : Cursor<RelationshipItem> moved from class org.neo4j.kernel.impl.api.store.StoreStatement to class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor & inlined to public relationships(direction Direction) : Cursor<RelationshipItem>`

