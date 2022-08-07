<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.presto.sql.planner.PlanPrinter`\
target: `com.facebook.presto.sql.planner.PlanPrinter.Visitor#formatDomain(TableHandle,ColumnHandle,Domain)`\
type: `MOVE`\
commit: [11048642b](https://github.com/facebook/presto/commit/11048642b1e6b0e35efefab9e4e693b09c8753f5)\
description: `Move Method private formatDomain(table TableHandle, column ColumnHandle, domain Domain) : String from class com.facebook.presto.sql.planner.PlanPrinter to private formatDomain(table TableHandle, column ColumnHandle, domain Domain) : String from class com.facebook.presto.sql.planner.PlanPrinter.Visitor`

id: `1`\
source `com.facebook.presto.sql.planner.PlanPrinter`\
target: `com.facebook.presto.sql.planner.PlanPrinter.Visitor#printConstraint(int,TableHandle,ColumnHandle,TupleDomain<ColumnHandle>)`\
type: `MOVE`\
commit: [11048642b](https://github.com/facebook/presto/commit/11048642b1e6b0e35efefab9e4e693b09c8753f5)\
description: `Move Method private printConstraint(indent int, table TableHandle, column ColumnHandle, constraint TupleDomain<ColumnHandle>) : void from class com.facebook.presto.sql.planner.PlanPrinter to private printConstraint(indent int, table TableHandle, column ColumnHandle, constraint TupleDomain<ColumnHandle>) : void from class com.facebook.presto.sql.planner.PlanPrinter.Visitor`

