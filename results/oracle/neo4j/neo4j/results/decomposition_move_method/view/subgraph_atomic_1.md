<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.api.StateHandlingStatementOperations`\
target: `org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper#getLabels()`\
type: `MOVE_RENAME`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Rename Method public nodeGetLabels(txStateHolder TxStateHolder, storeStatement StoreStatement, node NodeItem) : PrimitiveIntIterator from class org.neo4j.kernel.impl.api.StateHandlingStatementOperations to public getLabels() : PrimitiveIntIterator from class org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper`

id: `1`\
source `org.neo4j.kernel.impl.api.StateHandlingStatementOperations`\
target: `org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper#getRelationships(Direction,int[])`\
type: `MOVE_RENAME`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Rename Method public nodeGetRelationships(state KernelStatement, node NodeItem, direction Direction, relTypes int[]) : RelationshipIterator from class org.neo4j.kernel.impl.api.StateHandlingStatementOperations to public getRelationships(direction Direction, relTypes int[]) : RelationshipIterator from class org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper`

id: `2`\
source `org.neo4j.kernel.impl.api.StateHandlingStatementOperations`\
target: `org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper#hasLabel(int)`\
type: `MOVE_RENAME`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Rename Method public nodeHasLabel(state KernelStatement, node NodeItem, labelId int) : boolean from class org.neo4j.kernel.impl.api.StateHandlingStatementOperations to public hasLabel(labelId int) : boolean from class org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper`

id: `3`\
source `org.neo4j.kernel.impl.api.StateHandlingStatementOperations`\
target: `org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper#getRelationships(Direction)`\
type: `MOVE_RENAME`\
commit: [021d17c82](https://github.com/neo4j/neo4j/commit/021d17c8234904dcb1d54596662352395927fe7b)\
description: `Move And Rename Method public nodeGetRelationships(state KernelStatement, node NodeItem, direction Direction) : RelationshipIterator from class org.neo4j.kernel.impl.api.StateHandlingStatementOperations to public getRelationships(direction Direction) : RelationshipIterator from class org.neo4j.kernel.api.cursor.NodeItem.NodeItemHelper`

