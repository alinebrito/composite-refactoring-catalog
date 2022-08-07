<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `io.crate.planner.node.dql.MergeNode#downstreamExecutionNodeId(int)`\
target: `io.crate.planner.node.dql.AbstractDQLPlanNode#downstreamExecutionNodeId(int)`\
type: `PULL_UP`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Pull Up Method public downstreamExecutionNodeId(downstreamExecutionNodeId int) : void from class io.crate.planner.node.dql.MergeNode to public downstreamExecutionNodeId(downstreamExecutionNodeId int) : void from class io.crate.planner.node.dql.AbstractDQLPlanNode`

id: `1`\
source `io.crate.planner.node.dql.join.NestedLoopNode#downstreamExecutionNodeId(int)`\
target: `io.crate.planner.node.dql.AbstractDQLPlanNode#downstreamExecutionNodeId(int)`\
type: `PULL_UP`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Pull Up Method public downstreamExecutionNodeId(downstreamExecutionNodeId int) : void from class io.crate.planner.node.dql.join.NestedLoopNode to public downstreamExecutionNodeId(downstreamExecutionNodeId int) : void from class io.crate.planner.node.dql.AbstractDQLPlanNode`

id: `2`\
source `io.crate.planner.node.dql.CollectNode#downstreamExecutionNodeId(int)`\
target: `io.crate.planner.node.dql.AbstractDQLPlanNode#downstreamExecutionNodeId(int)`\
type: `PULL_UP`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Pull Up Method public downstreamExecutionNodeId(executionNodeId int) : void from class io.crate.planner.node.dql.CollectNode to public downstreamExecutionNodeId(downstreamExecutionNodeId int) : void from class io.crate.planner.node.dql.AbstractDQLPlanNode`

