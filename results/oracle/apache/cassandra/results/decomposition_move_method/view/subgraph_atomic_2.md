<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.StaticColumnsQueryTest`\
target: `org.apache.cassandra.cql3.validation.operations.SelectTest#testSingleClustering()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testSingleClustering() : void from class org.apache.cassandra.cql3.StaticColumnsQueryTest to public testSingleClustering() : void from class org.apache.cassandra.cql3.validation.operations.SelectTest`

id: `1`\
source `org.apache.cassandra.cql3.StaticColumnsQueryTest`\
target: `org.apache.cassandra.cql3.validation.operations.SelectTest#testSingleClusteringReversed()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testSingleClusteringReversed() : void from class org.apache.cassandra.cql3.StaticColumnsQueryTest to public testSingleClusteringReversed() : void from class org.apache.cassandra.cql3.validation.operations.SelectTest`

