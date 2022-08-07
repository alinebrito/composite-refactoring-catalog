<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.presto.operator.LookupJoinOperator#getOutput()`\
target: `com.facebook.presto.operator.LookupJoinOperator#tryGetLookupSource()`\
type: `EXTRACT`\
commit: [b7f4914d8](https://github.com/facebook/presto/commit/b7f4914d81a7a618acf2eba52af1093fc23cfba9)\
description: `Extract Method private tryGetLookupSource() : void extracted from public getOutput() : Page in class com.facebook.presto.operator.LookupJoinOperator`

id: `1`\
source `com.facebook.presto.operator.LookupJoinOperator#needsInput()`\
target: `com.facebook.presto.operator.LookupJoinOperator#tryGetLookupSource()`\
type: `EXTRACT`\
commit: [b7f4914d8](https://github.com/facebook/presto/commit/b7f4914d81a7a618acf2eba52af1093fc23cfba9)\
description: `Extract Method private tryGetLookupSource() : void extracted from public needsInput() : boolean in class com.facebook.presto.operator.LookupJoinOperator`

