<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `io.crate.planner.node.dql.MergeNode#downstreamNodes(Set<String>)`\
target: `io.crate.planner.node.dql.AbstractDQLPlanNode#downstreamNodes(Set<String>)`\
type: `PULL_UP`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Pull Up Method public downstreamNodes(nodes Set<String>) : void from class io.crate.planner.node.dql.MergeNode to public downstreamNodes(downStreamNodes Set<String>) : void from class io.crate.planner.node.dql.AbstractDQLPlanNode`

id: `1`\
source `io.crate.planner.node.dql.join.NestedLoopNode#downstreamNodes(Set<String>)`\
target: `io.crate.planner.node.dql.AbstractDQLPlanNode#downstreamNodes(Set<String>)`\
type: `PULL_UP`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Pull Up Method public downstreamNodes(nodes Set<String>) : void from class io.crate.planner.node.dql.join.NestedLoopNode to public downstreamNodes(downStreamNodes Set<String>) : void from class io.crate.planner.node.dql.AbstractDQLPlanNode`

