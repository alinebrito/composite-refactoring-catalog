<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.store.hive.HiveScan#HiveScan(String,HiveReadEntry,String,List<SchemaPath>,StoragePluginRegistry)`\
target: `org.apache.drill.exec.store.hive.HiveScan#getSplitsWithUGI()`\
type: `EXTRACT`\
commit: [c1b847acd](https://github.com/apache/drill/commit/c1b847acdc8cb90a1498b236b3bb5c81ca75c044)\
description: `Extract Method private getSplitsWithUGI() : void extracted from public HiveScan(userName String, hiveReadEntry HiveReadEntry, storagePluginName String, columns List<SchemaPath>, pluginRegistry StoragePluginRegistry) in class org.apache.drill.exec.store.hive.HiveScan`

id: `1`\
source `org.apache.drill.exec.store.hive.HiveScan#HiveScan(String,HiveReadEntry,HiveStoragePlugin,List<SchemaPath>)`\
target: `org.apache.drill.exec.store.hive.HiveScan#getSplitsWithUGI()`\
type: `EXTRACT`\
commit: [c1b847acd](https://github.com/apache/drill/commit/c1b847acdc8cb90a1498b236b3bb5c81ca75c044)\
description: `Extract Method private getSplitsWithUGI() : void extracted from public HiveScan(userName String, hiveReadEntry HiveReadEntry, storagePlugin HiveStoragePlugin, columns List<SchemaPath>) in class org.apache.drill.exec.store.hive.HiveScan`

