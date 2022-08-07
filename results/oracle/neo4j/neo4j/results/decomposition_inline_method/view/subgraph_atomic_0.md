<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.api.store.StoreStatement#acquirePropertyCursor(long)`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractRelationshipCursor#properties()`\
type: `INLINE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Inline Method public acquirePropertyCursor(firstPropertyRecordId long) : Cursor<PropertyItem> moved from class org.neo4j.kernel.impl.api.store.StoreStatement to class org.neo4j.kernel.impl.api.store.StoreAbstractRelationshipCursor & inlined to public properties() : Cursor<PropertyItem>`

id: `1`\
source `org.neo4j.kernel.impl.api.store.StoreStatement#acquirePropertyCursor(long)`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#properties()`\
type: `INLINE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Inline Method public acquirePropertyCursor(firstPropertyRecordId long) : Cursor<PropertyItem> moved from class org.neo4j.kernel.impl.api.store.StoreStatement to class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor & inlined to public properties() : Cursor<PropertyItem>`

