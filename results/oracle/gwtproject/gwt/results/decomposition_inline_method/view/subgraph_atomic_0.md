<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#rescueAndInstantiate(JClassType)`\
target: `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#visit(JNewInstance,Context)`\
type: `INLINE`\
commit: [22fb2c9c6](https://github.com/gwtproject/gwt/commit/22fb2c9c6974bd1fe0f6ff684f52e6cfbed1a387)\
description: `Inline Method private rescueAndInstantiate(type JClassType) : void inlined to public visit(x JNewInstance, ctx Context) : boolean in class com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor`

id: `1`\
source `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#rescueAndInstantiate(JClassType)`\
target: `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#visit(JsniMethodRef,Context)`\
type: `INLINE`\
commit: [22fb2c9c6](https://github.com/gwtproject/gwt/commit/22fb2c9c6974bd1fe0f6ff684f52e6cfbed1a387)\
description: `Inline Method private rescueAndInstantiate(type JClassType) : void inlined to public visit(x JsniMethodRef, ctx Context) : boolean in class com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor`

