<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.hive.hcatalog.mapreduce.PartInfo#writeObject(ObjectOutputStream)`\
target: `org.apache.hive.hcatalog.mapreduce.PartInfo#restoreLocalInfoFromTableInfo()`\
type: `EXTRACT`\
commit: [4ccc0c37a](https://github.com/apache/hive/commit/4ccc0c37aabbd90ecaa36fcc491e2270e7e9bea6)\
description: `Extract Method private restoreLocalInfoFromTableInfo() : void extracted from private writeObject(oos ObjectOutputStream) : void in class org.apache.hive.hcatalog.mapreduce.PartInfo`

id: `1`\
source `org.apache.hive.hcatalog.mapreduce.PartInfo#writeObject(ObjectOutputStream)`\
target: `org.apache.hive.hcatalog.mapreduce.PartInfo#dedupWithTableInfo()`\
type: `EXTRACT`\
commit: [4ccc0c37a](https://github.com/apache/hive/commit/4ccc0c37aabbd90ecaa36fcc491e2270e7e9bea6)\
description: `Extract Method private dedupWithTableInfo() : void extracted from private writeObject(oos ObjectOutputStream) : void in class org.apache.hive.hcatalog.mapreduce.PartInfo`

