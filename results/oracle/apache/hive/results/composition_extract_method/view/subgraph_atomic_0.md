<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.hadoop.hive.ql.exec.CommonMergeJoinOperator#joinFinalLeftData()`\
target: `org.apache.hadoop.hive.ql.exec.CommonMergeJoinOperator#doFirstFetchIfNeeded()`\
type: `EXTRACT`\
commit: [b8d2140fe](https://github.com/apache/hive/commit/b8d2140fe4faccadcf1a6343ec8cd0cc58c315f9)\
description: `Extract Method private doFirstFetchIfNeeded() : void extracted from private joinFinalLeftData() : void in class org.apache.hadoop.hive.ql.exec.CommonMergeJoinOperator`

id: `1`\
source `org.apache.hadoop.hive.ql.exec.CommonMergeJoinOperator#process(Object,int)`\
target: `org.apache.hadoop.hive.ql.exec.CommonMergeJoinOperator#doFirstFetchIfNeeded()`\
type: `EXTRACT`\
commit: [b8d2140fe](https://github.com/apache/hive/commit/b8d2140fe4faccadcf1a6343ec8cd0cc58c315f9)\
description: `Extract Method private doFirstFetchIfNeeded() : void extracted from public process(row Object, tag int) : void in class org.apache.hadoop.hive.ql.exec.CommonMergeJoinOperator`

