<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.functions.Functions`\
target: `org.apache.cassandra.schema.Functions#typesMatch(AbstractType<?>,AbstractType<?>)`\
type: `MOVE_RENAME`\
commit: [356684350](https://github.com/apache/cassandra/commit/35668435090eb47cf8c5e704243510b6cee35a7b)\
description: `Move And Rename Method public typeEquals(t1 AbstractType<?>, t2 AbstractType<?>) : boolean from class org.apache.cassandra.cql3.functions.Functions to public typesMatch(t1 AbstractType<?>, t2 AbstractType<?>) : boolean from class org.apache.cassandra.schema.Functions`

id: `1`\
source `org.apache.cassandra.cql3.functions.Functions`\
target: `org.apache.cassandra.schema.Functions#typesMatch(List<AbstractType<?>>,List<AbstractType<?>>)`\
type: `MOVE_RENAME`\
commit: [356684350](https://github.com/apache/cassandra/commit/35668435090eb47cf8c5e704243510b6cee35a7b)\
description: `Move And Rename Method public typeEquals(t1 List<AbstractType<?>>, t2 List<AbstractType<?>>) : boolean from class org.apache.cassandra.cql3.functions.Functions to public typesMatch(t1 List<AbstractType<?>>, t2 List<AbstractType<?>>) : boolean from class org.apache.cassandra.schema.Functions`

