<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.devtools.j2objc.gen.StatementGenerator#visit(LambdaExpression)`\
target: `com.google.devtools.j2objc.gen.StatementGenerator#printLambdaCall(IMethodBinding,ITypeBinding,IMethodBinding,List<VariableDeclaration>,boolean)`\
type: `EXTRACT`\
commit: [d05d92de4](https://github.com/google/j2objc/commit/d05d92de40542e85f9f26712d976e710be82914e)\
description: `Extract Method public printLambdaCall(functionalInterface IMethodBinding, functionalTypeBinding ITypeBinding, methodBinding IMethodBinding, parameters List<VariableDeclaration>, isCapturing boolean) : void extracted from public visit(node LambdaExpression) : boolean in class com.google.devtools.j2objc.gen.StatementGenerator`

id: `1`\
source `com.google.devtools.j2objc.gen.StatementGenerator#visit(LambdaExpression)`\
target: `com.google.devtools.j2objc.gen.StatementGenerator#printLambdaCallWithoutBlocks(IMethodBinding,String,String,IMethodBinding,boolean)`\
type: `EXTRACT`\
commit: [d05d92de4](https://github.com/google/j2objc/commit/d05d92de40542e85f9f26712d976e710be82914e)\
description: `Extract Method public printLambdaCallWithoutBlocks(functionalInterface IMethodBinding, functionalClassName String, newClassName String, methodBinding IMethodBinding, isCapturing boolean) : void extracted from public visit(node LambdaExpression) : boolean in class com.google.devtools.j2objc.gen.StatementGenerator`

id: `2`\
source `com.google.devtools.j2objc.gen.StatementGenerator#visit(LambdaExpression)`\
target: `com.google.devtools.j2objc.gen.StatementGenerator#printLambdaCallBlocks(IMethodBinding,List<VariableDeclaration>,boolean)`\
type: `EXTRACT`\
commit: [d05d92de4](https://github.com/google/j2objc/commit/d05d92de40542e85f9f26712d976e710be82914e)\
description: `Extract Method public printLambdaCallBlocks(functionalInterface IMethodBinding, parameters List<VariableDeclaration>, isCapturing boolean) : void extracted from public visit(node LambdaExpression) : boolean in class com.google.devtools.j2objc.gen.StatementGenerator`

