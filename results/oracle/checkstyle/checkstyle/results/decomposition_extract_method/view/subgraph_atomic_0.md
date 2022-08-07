<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.puppycrawl.tools.checkstyle.checks.coding.RequireThisCheck#processIDENT(DetailAST)`\
target: `com.puppycrawl.tools.checkstyle.checks.coding.RequireThisCheck#processField(DetailAST,int)`\
type: `EXTRACT`\
commit: [5a9b7249e](https://github.com/checkstyle/checkstyle/commit/5a9b7249e3d092a78ac8e7d48aeeb62bf1c44e20)\
description: `Extract Method private processField(ast DetailAST, parentType int) : void extracted from private processIDENT(ast DetailAST) : void in class com.puppycrawl.tools.checkstyle.checks.coding.RequireThisCheck`

id: `1`\
source `com.puppycrawl.tools.checkstyle.checks.coding.RequireThisCheck#processIDENT(DetailAST)`\
target: `com.puppycrawl.tools.checkstyle.checks.coding.RequireThisCheck#isDeclarationToken(int)`\
type: `EXTRACT`\
commit: [5a9b7249e](https://github.com/checkstyle/checkstyle/commit/5a9b7249e3d092a78ac8e7d48aeeb62bf1c44e20)\
description: `Extract Method private isDeclarationToken(parentType int) : boolean extracted from private processIDENT(ast DetailAST) : void in class com.puppycrawl.tools.checkstyle.checks.coding.RequireThisCheck`

