<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.store.hive.HiveTestDataGenerator`\
target: `org.apache.drill.exec.hive.HiveTestUtilities#executeQuery(Driver,String)`\
type: `MOVE`\
commit: [c1b847acd](https://github.com/apache/drill/commit/c1b847acdc8cb90a1498b236b3bb5c81ca75c044)\
description: `Move Method private executeQuery(hiveDriver Driver, query String) : void from class org.apache.drill.exec.store.hive.HiveTestDataGenerator to public executeQuery(hiveDriver Driver, query String) : void from class org.apache.drill.exec.hive.HiveTestUtilities`

id: `1`\
source `org.apache.drill.exec.store.hive.HiveTestDataGenerator`\
target: `org.apache.drill.BaseTestQuery#getPhysicalFileFromResource(String)`\
type: `MOVE_RENAME`\
commit: [c1b847acd](https://github.com/apache/drill/commit/c1b847acdc8cb90a1498b236b3bb5c81ca75c044)\
description: `Move And Rename Method private getSchemaFile(resource String) : String from class org.apache.drill.exec.store.hive.HiveTestDataGenerator to public getPhysicalFileFromResource(resource String) : String from class org.apache.drill.BaseTestQuery`

