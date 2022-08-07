<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.devtools.j2objc.translate.Autoboxer#rewriteBoxedPrefixOrPostfix(TreeNode,Expression,String)`\
target: `com.google.devtools.j2objc.translate.Autoboxer#getOperatorFunctionModifier(Expression)`\
type: `EXTRACT`\
commit: [fa3e6fa02](https://github.com/google/j2objc/commit/fa3e6fa02dadc675f0d487a15cd842b3ac4a0c11)\
description: `Extract Method private getOperatorFunctionModifier(expr Expression) : String extracted from private rewriteBoxedPrefixOrPostfix(node TreeNode, operand Expression, funcName String) : void in class com.google.devtools.j2objc.translate.Autoboxer`

id: `1`\
source `com.google.devtools.j2objc.translate.Autoboxer#rewriteBoxedAssignment(Assignment)`\
target: `com.google.devtools.j2objc.translate.Autoboxer#getOperatorFunctionModifier(Expression)`\
type: `EXTRACT`\
commit: [fa3e6fa02](https://github.com/google/j2objc/commit/fa3e6fa02dadc675f0d487a15cd842b3ac4a0c11)\
description: `Extract Method private getOperatorFunctionModifier(expr Expression) : String extracted from private rewriteBoxedAssignment(node Assignment) : void in class com.google.devtools.j2objc.translate.Autoboxer`

