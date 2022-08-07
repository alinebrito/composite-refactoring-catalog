<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.objectfilter.impl.syntax.BooleanFilterNormalizer`\
target: `org.infinispan.objectfilter.impl.syntax.PredicateOptimisations#optimizeEqAndInterval(ComparisonExpr,ComparisonExpr,boolean,int)`\
type: `MOVE_RENAME`\
commit: [35b6c8695](https://github.com/infinispan/infinispan/commit/35b6c869546a7968b6fd2f640add6eea87e03c22)\
description: `Move And Rename Method private eqAndInterval(first ComparisonExpr, second ComparisonExpr, isConjunction boolean, cmp int) : BooleanExpr from class org.infinispan.objectfilter.impl.syntax.BooleanFilterNormalizer to private optimizeEqAndInterval(first ComparisonExpr, second ComparisonExpr, isConjunction boolean, cmp int) : BooleanExpr from class org.infinispan.objectfilter.impl.syntax.PredicateOptimisations`

id: `1`\
source `org.infinispan.objectfilter.impl.syntax.BooleanFilterNormalizer`\
target: `org.infinispan.objectfilter.impl.syntax.PredicateOptimisations#optimizeNotEqAndInterval(ComparisonExpr,ComparisonExpr,boolean,int)`\
type: `MOVE_RENAME`\
commit: [35b6c8695](https://github.com/infinispan/infinispan/commit/35b6c869546a7968b6fd2f640add6eea87e03c22)\
description: `Move And Rename Method private notEqAndInterval(first ComparisonExpr, second ComparisonExpr, isConjunction boolean, cmp int) : BooleanExpr from class org.infinispan.objectfilter.impl.syntax.BooleanFilterNormalizer to private optimizeNotEqAndInterval(first ComparisonExpr, second ComparisonExpr, isConjunction boolean, cmp int) : BooleanExpr from class org.infinispan.objectfilter.impl.syntax.PredicateOptimisations`

