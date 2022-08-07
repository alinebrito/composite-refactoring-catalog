<img src=subgraph_atomic_4.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.statements.CreateTableStatement.RawStatement`\
target: `org.apache.cassandra.cql3.statements.CFProperties#setCompactStorage()`\
type: `MOVE`\
commit: [3bdcaa336](https://github.com/apache/cassandra/commit/3bdcaa336a6e6a9727c333b433bb9f5d3afc0fb1)\
description: `Move Method public setCompactStorage() : void from class org.apache.cassandra.cql3.statements.CreateTableStatement.RawStatement to public setCompactStorage() : void from class org.apache.cassandra.cql3.statements.CFProperties`

id: `1`\
source `org.apache.cassandra.cql3.statements.CreateTableStatement.RawStatement`\
target: `org.apache.cassandra.cql3.statements.CFProperties#setOrdering(ColumnIdentifier,boolean)`\
type: `MOVE`\
commit: [3bdcaa336](https://github.com/apache/cassandra/commit/3bdcaa336a6e6a9727c333b433bb9f5d3afc0fb1)\
description: `Move Method public setOrdering(alias ColumnIdentifier, reversed boolean) : void from class org.apache.cassandra.cql3.statements.CreateTableStatement.RawStatement to public setOrdering(alias ColumnIdentifier, reversed boolean) : void from class org.apache.cassandra.cql3.statements.CFProperties`

