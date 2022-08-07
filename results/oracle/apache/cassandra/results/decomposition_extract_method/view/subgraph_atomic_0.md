<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.db.compaction.CompactionsCQLTest#testTriggerMinorCompaction()`\
target: `org.apache.cassandra.db.compaction.CompactionsCQLTest#minorWasTriggered(String,String)`\
type: `EXTRACT`\
commit: [1a2c1bcdc](https://github.com/apache/cassandra/commit/1a2c1bcdc7267abec9b19d77726aedbb045d79a8)\
description: `Extract Method public minorWasTriggered(keyspace String, cf String) : boolean extracted from public testTriggerMinorCompaction() : void in class org.apache.cassandra.db.compaction.CompactionsCQLTest`

id: `1`\
source `org.apache.cassandra.db.compaction.CompactionsCQLTest#testTriggerMinorCompaction()`\
target: `org.apache.cassandra.db.compaction.CompactionsCQLTest#getCurrentColumnFamilyStore()`\
type: `EXTRACT`\
commit: [1a2c1bcdc](https://github.com/apache/cassandra/commit/1a2c1bcdc7267abec9b19d77726aedbb045d79a8)\
description: `Extract Method private getCurrentColumnFamilyStore() : ColumnFamilyStore extracted from public testTriggerMinorCompaction() : void in class org.apache.cassandra.db.compaction.CompactionsCQLTest`

