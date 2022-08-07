<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.hadoop.hive.ql.optimizer.ConstantPropagateProcFactory#foldExpr(ExprNodeDesc,Map<ColumnInfo,ExprNodeDesc>,ConstantPropagateProcCtx,Operator<?,int,boolean)`\
target: `org.apache.hadoop.hive.ql.optimizer.ConstantPropagateProcFactory#foldExprFull(ExprNodeDesc,Map<ColumnInfo,ExprNodeDesc>,ConstantPropagateProcCtx,Operator<?,int,boolean)`\
type: `EXTRACT`\
commit: [e2dd54ab1](https://github.com/apache/hive/commit/e2dd54ab180b577b08cf6b0e69310ac81fc99fd3)\
description: `Extract Method private foldExprFull(desc ExprNodeDesc, constants Map<ColumnInfo,ExprNodeDesc>, cppCtx ConstantPropagateProcCtx, op Operator<? extends Serializable>, tag int, propagate boolean) : ExprNodeDesc extracted from private foldExpr(desc ExprNodeDesc, constants Map<ColumnInfo,ExprNodeDesc>, cppCtx ConstantPropagateProcCtx, op Operator<? extends Serializable>, tag int, propagate boolean) : ExprNodeDesc in class org.apache.hadoop.hive.ql.optimizer.ConstantPropagateProcFactory`

id: `1`\
source `org.apache.hadoop.hive.ql.optimizer.ConstantPropagateProcFactory#foldExpr(ExprNodeDesc,Map<ColumnInfo,ExprNodeDesc>,ConstantPropagateProcCtx,Operator<?,int,boolean)`\
target: `org.apache.hadoop.hive.ql.optimizer.ConstantPropagateProcFactory#foldExprShortcut(ExprNodeDesc,Map<ColumnInfo,ExprNodeDesc>,ConstantPropagateProcCtx,Operator<?,int,boolean)`\
type: `EXTRACT`\
commit: [e2dd54ab1](https://github.com/apache/hive/commit/e2dd54ab180b577b08cf6b0e69310ac81fc99fd3)\
description: `Extract Method private foldExprShortcut(desc ExprNodeDesc, constants Map<ColumnInfo,ExprNodeDesc>, cppCtx ConstantPropagateProcCtx, op Operator<? extends Serializable>, tag int, propagate boolean) : ExprNodeDesc extracted from private foldExpr(desc ExprNodeDesc, constants Map<ColumnInfo,ExprNodeDesc>, cppCtx ConstantPropagateProcCtx, op Operator<? extends Serializable>, tag int, propagate boolean) : ExprNodeDesc in class org.apache.hadoop.hive.ql.optimizer.ConstantPropagateProcFactory`

