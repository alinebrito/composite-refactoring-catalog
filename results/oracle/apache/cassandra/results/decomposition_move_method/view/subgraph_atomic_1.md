<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#failInsert(String,Object...)`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public failInsert(insertCQL String, args Object...) : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public failInsert(insertCQL String, args Object...) : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `1`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#succeedInsert(String,Object...)`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public succeedInsert(insertCQL String, args Object...) : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public succeedInsert(insertCQL String, args Object...) : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `2`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testCompactTableWithValueOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testCompactTableWithValueOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testCompactTableWithValueOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `3`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnClusteringColumnInsertPartitionKeyAndClusteringsOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnClusteringColumnInsertPartitionKeyAndClusteringsOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnClusteringColumnInsertPartitionKeyAndClusteringsOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `4`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnClusteringColumnInsertValueOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnClusteringColumnInsertValueOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnClusteringColumnInsertValueOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `5`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnCollectionKeyInsertPartitionKeyAndClusteringOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnCollectionKeyInsertPartitionKeyAndClusteringOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnCollectionKeyInsertPartitionKeyAndClusteringOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `6`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnCollectionValueInsertPartitionKeyAndCollectionKeyOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnCollectionValueInsertPartitionKeyAndCollectionKeyOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnCollectionValueInsertPartitionKeyAndCollectionKeyOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `7`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnCompositeValueOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnCompositeValueOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnCompositeValueOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `8`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnFullCollectionEntryInsertCollectionValueOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnFullCollectionEntryInsertCollectionValueOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnFullCollectionEntryInsertCollectionValueOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

id: `9`\
source `org.apache.cassandra.cql3.IndexedValuesValidationTest`\
target: `org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest#testIndexOnPartitionKeyInsertValueOver64k()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testIndexOnPartitionKeyInsertValueOver64k() : void from class org.apache.cassandra.cql3.IndexedValuesValidationTest to public testIndexOnPartitionKeyInsertValueOver64k() : void from class org.apache.cassandra.cql3.validation.entities.SecondaryIndexTest`

