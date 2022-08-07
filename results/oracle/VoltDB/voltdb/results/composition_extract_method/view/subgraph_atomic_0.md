<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.voltdb.TestAdhocCreateDropIndex#testBasicCreateIndex()`\
target: `org.voltdb.TestAdhocCreateDropIndex#createSchema(VoltDB.Configuration,String,int,int,int)`\
type: `EXTRACT`\
commit: [c1359c843](https://github.com/VoltDB/voltdb/commit/c1359c843bd03a694f846c8140e24ed646bbb913)\
description: `Extract Method private createSchema(config VoltDB.Configuration, ddl String, sitesPerHost int, hostCount int, replication int) : void extracted from public testBasicCreateIndex() : void in class org.voltdb.TestAdhocCreateDropIndex`

id: `1`\
source `org.voltdb.TestAdhocCreateDropIndex#testCreateDropIndexonView()`\
target: `org.voltdb.TestAdhocCreateDropIndex#createSchema(VoltDB.Configuration,String,int,int,int)`\
type: `EXTRACT`\
commit: [c1359c843](https://github.com/VoltDB/voltdb/commit/c1359c843bd03a694f846c8140e24ed646bbb913)\
description: `Extract Method private createSchema(config VoltDB.Configuration, ddl String, sitesPerHost int, hostCount int, replication int) : void extracted from public testCreateDropIndexonView() : void in class org.voltdb.TestAdhocCreateDropIndex`

