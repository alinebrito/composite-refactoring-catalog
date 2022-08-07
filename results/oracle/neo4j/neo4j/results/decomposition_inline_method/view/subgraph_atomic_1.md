<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.api.store.StoreStatement#acquireSinglePropertyCursor(long,int)`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractRelationshipCursor#property(int)`\
type: `INLINE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Inline Method public acquireSinglePropertyCursor(firstPropertyRecordId long, propertyKeyId int) : Cursor<PropertyItem> moved from class org.neo4j.kernel.impl.api.store.StoreStatement to class org.neo4j.kernel.impl.api.store.StoreAbstractRelationshipCursor & inlined to public property(propertyKeyId int) : Cursor<PropertyItem>`

id: `1`\
source `org.neo4j.kernel.impl.api.store.StoreStatement#acquireSinglePropertyCursor(long,int)`\
target: `org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor#property(int)`\
type: `INLINE`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Inline Method public acquireSinglePropertyCursor(firstPropertyRecordId long, propertyKeyId int) : Cursor<PropertyItem> moved from class org.neo4j.kernel.impl.api.store.StoreStatement to class org.neo4j.kernel.impl.api.store.StoreAbstractNodeCursor & inlined to public property(propertyKeyId int) : Cursor<PropertyItem>`

