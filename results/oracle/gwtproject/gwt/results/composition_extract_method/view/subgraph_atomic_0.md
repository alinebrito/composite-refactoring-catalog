<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#visit(JInterfaceType,Context)`\
target: `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#rescueMembersAndInstantiateSuperInterfaces(JDeclaredType)`\
type: `EXTRACT`\
commit: [22fb2c9c6](https://github.com/gwtproject/gwt/commit/22fb2c9c6974bd1fe0f6ff684f52e6cfbed1a387)\
description: `Extract Method private rescueMembersAndInstantiateSuperInterfaces(type JDeclaredType) : void extracted from public visit(type JInterfaceType, ctx Context) : boolean in class com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor`

id: `1`\
source `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#visit(JClassType,Context)`\
target: `com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor#rescueMembersAndInstantiateSuperInterfaces(JDeclaredType)`\
type: `EXTRACT`\
commit: [22fb2c9c6](https://github.com/gwtproject/gwt/commit/22fb2c9c6974bd1fe0f6ff684f52e6cfbed1a387)\
description: `Extract Method private rescueMembersAndInstantiateSuperInterfaces(type JDeclaredType) : void extracted from public visit(type JClassType, ctx Context) : boolean in class com.google.gwt.dev.jjs.impl.ControlFlowAnalyzer.RescueVisitor`

