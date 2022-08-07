<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.javascript.rhino.jstype.FunctionType#isSubtype(JSType)`\
target: `com.google.javascript.rhino.jstype.FunctionType#isSubtype(JSType,ImplCache)`\
type: `EXTRACT`\
commit: [545a7d027](https://github.com/google/closure-compiler/commit/545a7d027b4c55c116dc52d9cd8121fbb09777f0)\
description: `Extract Method protected isSubtype(that JSType, implicitImplCache ImplCache) : boolean extracted from public isSubtype(that JSType) : boolean in class com.google.javascript.rhino.jstype.FunctionType`

id: `1`\
source `com.google.javascript.rhino.jstype.FunctionType#isSubtype(JSType)`\
target: `com.google.javascript.rhino.jstype.FunctionType#treatThisTypesAsCovariant(FunctionType,ImplCache)`\
type: `EXTRACT`\
commit: [545a7d027](https://github.com/google/closure-compiler/commit/545a7d027b4c55c116dc52d9cd8121fbb09777f0)\
description: `Extract Method protected treatThisTypesAsCovariant(other FunctionType, implicitImplCache ImplCache) : boolean extracted from public isSubtype(that JSType) : boolean in class com.google.javascript.rhino.jstype.FunctionType`

