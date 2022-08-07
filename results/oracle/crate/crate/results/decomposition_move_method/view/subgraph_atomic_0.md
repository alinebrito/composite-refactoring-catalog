<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `io.crate.planner.node.dql.join.NestedLoop`\
target: `io.crate.planner.node.dql.join.NestedLoopNode#rightMergeNode(MergeNode)`\
type: `MOVE`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Move Method public rightMergeNode(rightMergeNode MergeNode) : void from class io.crate.planner.node.dql.join.NestedLoop to public rightMergeNode(rightMergeNode MergeNode) : void from class io.crate.planner.node.dql.join.NestedLoopNode`

id: `1`\
source `io.crate.planner.node.dql.join.NestedLoop`\
target: `io.crate.planner.node.dql.join.NestedLoopNode#leftMergeNode(MergeNode)`\
type: `MOVE`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Move Method public leftMergeNode(leftMergeNode MergeNode) : void from class io.crate.planner.node.dql.join.NestedLoop to public leftMergeNode(leftMergeNode MergeNode) : void from class io.crate.planner.node.dql.join.NestedLoopNode`

id: `2`\
source `io.crate.planner.node.dql.join.NestedLoop`\
target: `io.crate.planner.node.dql.join.NestedLoopNode#rightMergeNode()`\
type: `MOVE`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Move Method public rightMergeNode() : MergeNode from class io.crate.planner.node.dql.join.NestedLoop to public rightMergeNode() : MergeNode from class io.crate.planner.node.dql.join.NestedLoopNode`

id: `3`\
source `io.crate.planner.node.dql.join.NestedLoop`\
target: `io.crate.planner.node.dql.join.NestedLoopNode#leftMergeNode()`\
type: `MOVE`\
commit: [72b534830](https://github.com/crate/crate/commit/72b5348307d86b1a118e546c24d97f1ac1895bdb)\
description: `Move Method public leftMergeNode() : MergeNode from class io.crate.planner.node.dql.join.NestedLoop to public leftMergeNode() : MergeNode from class io.crate.planner.node.dql.join.NestedLoopNode`

