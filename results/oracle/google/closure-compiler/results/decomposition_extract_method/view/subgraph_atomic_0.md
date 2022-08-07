<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.javascript.jscomp.parsing.parser.Parser#parseFormalParameterList()`\
target: `com.google.javascript.jscomp.parsing.parser.Parser#parseFormalParameterList(boolean)`\
type: `EXTRACT`\
commit: [ea9664336](https://github.com/google/closure-compiler/commit/ea96643364e91125f560e9508a5cbcdb776bde64)\
description: `Extract Method private parseFormalParameterList(inTypeExpression boolean) : FormalParameterListTree extracted from private parseFormalParameterList() : FormalParameterListTree in class com.google.javascript.jscomp.parsing.parser.Parser`

id: `1`\
source `com.google.javascript.jscomp.parsing.parser.Parser#parseFormalParameterList()`\
target: `com.google.javascript.jscomp.parsing.parser.Parser#parseParameter(boolean)`\
type: `EXTRACT`\
commit: [ea9664336](https://github.com/google/closure-compiler/commit/ea96643364e91125f560e9508a5cbcdb776bde64)\
description: `Extract Method private parseParameter(inTypeExpression boolean) : ParseTree extracted from private parseFormalParameterList() : FormalParameterListTree in class com.google.javascript.jscomp.parsing.parser.Parser`

id: `2`\
source `com.google.javascript.jscomp.parsing.parser.Parser#parseFormalParameterList()`\
target: `com.google.javascript.jscomp.parsing.parser.Parser#peekParameter(boolean)`\
type: `EXTRACT`\
commit: [ea9664336](https://github.com/google/closure-compiler/commit/ea96643364e91125f560e9508a5cbcdb776bde64)\
description: `Extract Method private peekParameter(inTypeExpression boolean) : boolean extracted from private parseFormalParameterList() : FormalParameterListTree in class com.google.javascript.jscomp.parsing.parser.Parser`

