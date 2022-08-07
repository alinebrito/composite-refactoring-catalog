<img src=subgraph_atomic_5.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.store.TestNeoStore#deleteNode1(long,DefinedProperty,DefinedProperty,DefinedProperty)`\
target: `org.neo4j.kernel.impl.store.TestNeoStore#assertHasRelationships(long)`\
type: `EXTRACT`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Extract Method private assertHasRelationships(node long) : void extracted from private deleteNode1(node long, prop1 DefinedProperty, prop2 DefinedProperty, prop3 DefinedProperty) : void in class org.neo4j.kernel.impl.store.TestNeoStore`

id: `1`\
source `org.neo4j.kernel.impl.store.TestNeoStore#deleteNode2(long,DefinedProperty,DefinedProperty,DefinedProperty)`\
target: `org.neo4j.kernel.impl.store.TestNeoStore#assertHasRelationships(long)`\
type: `EXTRACT`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Extract Method private assertHasRelationships(node long) : void extracted from private deleteNode2(node long, prop1 DefinedProperty, prop2 DefinedProperty, prop3 DefinedProperty) : void in class org.neo4j.kernel.impl.store.TestNeoStore`

id: `2`\
source `org.neo4j.kernel.impl.store.TestNeoStore#deleteRel1(long,DefinedProperty,DefinedProperty,DefinedProperty,long,long,int)`\
target: `org.neo4j.kernel.impl.store.TestNeoStore#assertHasRelationships(long)`\
type: `EXTRACT`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Extract Method private assertHasRelationships(node long) : void extracted from private deleteRel1(rel long, prop1 DefinedProperty, prop2 DefinedProperty, prop3 DefinedProperty, firstNode long, secondNode long, relType int) : void in class org.neo4j.kernel.impl.store.TestNeoStore`

id: `3`\
source `org.neo4j.kernel.impl.store.TestNeoStore#deleteRel2(long,DefinedProperty,DefinedProperty,DefinedProperty,long,long,int)`\
target: `org.neo4j.kernel.impl.store.TestNeoStore#assertHasRelationships(long)`\
type: `EXTRACT`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Extract Method private assertHasRelationships(node long) : void extracted from private deleteRel2(rel long, prop1 DefinedProperty, prop2 DefinedProperty, prop3 DefinedProperty, firstNode long, secondNode long, relType int) : void in class org.neo4j.kernel.impl.store.TestNeoStore`

