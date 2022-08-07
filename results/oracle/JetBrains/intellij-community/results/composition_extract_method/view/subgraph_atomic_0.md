<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.intellij.debugger.engine.RemappedSourcePosition#getLine()`\
target: `com.intellij.debugger.engine.RemappedSourcePosition#checkRemap()`\
type: `EXTRACT`\
commit: [7655200f5](https://github.com/JetBrains/intellij-community/commit/7655200f58293e5a30bf8b3cbb29ebadae374564)\
description: `Extract Method private checkRemap() : void extracted from public getLine() : int in class com.intellij.debugger.engine.RemappedSourcePosition`

id: `1`\
source `com.intellij.debugger.engine.RemappedSourcePosition#getOffset()`\
target: `com.intellij.debugger.engine.RemappedSourcePosition#checkRemap()`\
type: `EXTRACT`\
commit: [7655200f5](https://github.com/JetBrains/intellij-community/commit/7655200f58293e5a30bf8b3cbb29ebadae374564)\
description: `Extract Method private checkRemap() : void extracted from public getOffset() : int in class com.intellij.debugger.engine.RemappedSourcePosition`

