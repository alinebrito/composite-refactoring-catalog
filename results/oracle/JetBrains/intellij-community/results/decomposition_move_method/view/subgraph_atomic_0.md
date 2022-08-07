<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.siyeh.ig.psiutils.SwitchUtils`\
target: `com.siyeh.ig.psiutils.ExpressionUtils#isAnnotated(PsiExpression,boolean)`\
type: `MOVE_RENAME`\
commit: [cc0eaf7fa](https://github.com/JetBrains/intellij-community/commit/cc0eaf7faa408a04b68e2b5820f3ebcc75420b5b)\
description: `Move And Rename Method private isAnnotatedNotNull(expression PsiExpression) : boolean from class com.siyeh.ig.psiutils.SwitchUtils to private isAnnotated(expression PsiExpression, nullable boolean) : boolean from class com.siyeh.ig.psiutils.ExpressionUtils`

id: `1`\
source `com.siyeh.ig.psiutils.SwitchUtils`\
target: `com.siyeh.ig.psiutils.ExpressionUtils#isAnnotated(PsiExpression,boolean)`\
type: `MOVE_RENAME`\
commit: [cc0eaf7fa](https://github.com/JetBrains/intellij-community/commit/cc0eaf7faa408a04b68e2b5820f3ebcc75420b5b)\
description: `Move And Rename Method private isAnnotatedNullable(expression PsiExpression) : boolean from class com.siyeh.ig.psiutils.SwitchUtils to private isAnnotated(expression PsiExpression, nullable boolean) : boolean from class com.siyeh.ig.psiutils.ExpressionUtils`

