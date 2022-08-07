<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.voltdb.compiler.DDLCompiler#findBestMatchIndexForMatviewMinOrMax(MaterializedViewInfo,Table,List<AbstractExpression>,AbstractExpression)`\
target: `org.voltdb.compiler.DDLCompiler#isGroupbyMatchingIndex(MatViewIndexMacthingGroupby,List<ColumnRef>,List<AbstractExpression>,List<ColumnRef>,List<AbstractExpression>,List<Column>)`\
type: `EXTRACT`\
commit: [ebb1c2c36](https://github.com/VoltDB/voltdb/commit/ebb1c2c364e888d4a0f47abe691cb2bad4eb4e75)\
description: `Extract Method private isGroupbyMatchingIndex(matchingCase MatViewIndexMacthingGroupby, groupbyColRefs List<ColumnRef>, groupbyExprs List<AbstractExpression>, indexedColRefs List<ColumnRef>, indexedExprs List<AbstractExpression>, srcColumnArray List<Column>) : boolean extracted from private findBestMatchIndexForMatviewMinOrMax(matviewinfo MaterializedViewInfo, srcTable Table, groupbyExprs List<AbstractExpression>, singleUniqueMinMaxAggExpr AbstractExpression) : Index in class org.voltdb.compiler.DDLCompiler`

id: `1`\
source `org.voltdb.compiler.DDLCompiler#findBestMatchIndexForMatviewMinOrMax(MaterializedViewInfo,Table,List<AbstractExpression>,AbstractExpression)`\
target: `org.voltdb.compiler.DDLCompiler#isIndexOptimalForMinMax(MatViewIndexMacthingGroupby,AbstractExpression,List<ColumnRef>,List<AbstractExpression>,List<Column>)`\
type: `EXTRACT`\
commit: [ebb1c2c36](https://github.com/VoltDB/voltdb/commit/ebb1c2c364e888d4a0f47abe691cb2bad4eb4e75)\
description: `Extract Method private isIndexOptimalForMinMax(matchingCase MatViewIndexMacthingGroupby, singleUniqueMinMaxAggExpr AbstractExpression, indexedColRefs List<ColumnRef>, indexedExprs List<AbstractExpression>, srcColumnArray List<Column>) : boolean extracted from private findBestMatchIndexForMatviewMinOrMax(matviewinfo MaterializedViewInfo, srcTable Table, groupbyExprs List<AbstractExpression>, singleUniqueMinMaxAggExpr AbstractExpression) : Index in class org.voltdb.compiler.DDLCompiler`

