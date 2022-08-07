<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.planner.sql.handlers.DefaultSqlHandler#getPlan(SqlNode)`\
target: `org.apache.drill.exec.planner.sql.handlers.DefaultSqlHandler#validateAndConvert(SqlNode)`\
type: `EXTRACT`\
commit: [ffae1691c](https://github.com/apache/drill/commit/ffae1691c0cd526ed1095fbabbc0855d016790d7)\
description: `Extract Method protected validateAndConvert(sqlNode SqlNode) : ConvertedRelNode extracted from public getPlan(sqlNode SqlNode) : PhysicalPlan in class org.apache.drill.exec.planner.sql.handlers.DefaultSqlHandler`

id: `1`\
source `org.apache.drill.exec.planner.sql.handlers.ExplainHandler#getPlan(SqlNode)`\
target: `org.apache.drill.exec.planner.sql.handlers.DefaultSqlHandler#validateAndConvert(SqlNode)`\
type: `EXTRACT_MOVE`\
commit: [ffae1691c](https://github.com/apache/drill/commit/ffae1691c0cd526ed1095fbabbc0855d016790d7)\
description: `Extract And Move Method protected validateAndConvert(sqlNode SqlNode) : ConvertedRelNode extracted from public getPlan(node SqlNode) : PhysicalPlan in class org.apache.drill.exec.planner.sql.handlers.ExplainHandler & moved to class org.apache.drill.exec.planner.sql.handlers.DefaultSqlHandler`

