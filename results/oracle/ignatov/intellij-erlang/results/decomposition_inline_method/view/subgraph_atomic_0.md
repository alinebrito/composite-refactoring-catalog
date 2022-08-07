<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.intellij.erlang.psi.impl.ErlangFunctionReferenceImpl#getModuleFileName()`\
target: `org.intellij.erlang.psi.impl.ErlangFunctionReferenceImpl#resolve()`\
type: `INLINE`\
commit: [3855f0ca8](https://github.com/ignatov/intellij-erlang/commit/3855f0ca82795f7481b34342c7d9e5644a1d42c3)\
description: `Inline Method private getModuleFileName() : String inlined to public resolve() : PsiElement in class org.intellij.erlang.psi.impl.ErlangFunctionReferenceImpl`

id: `1`\
source `org.intellij.erlang.psi.impl.ErlangFunctionReferenceImpl#getModuleFileName()`\
target: `org.intellij.erlang.psi.impl.ErlangFunctionReferenceImpl#multiResolve(boolean)`\
type: `INLINE`\
commit: [3855f0ca8](https://github.com/ignatov/intellij-erlang/commit/3855f0ca82795f7481b34342c7d9e5644a1d42c3)\
description: `Inline Method private getModuleFileName() : String inlined to public multiResolve(incompleteCode boolean) : ResolveResult[] in class org.intellij.erlang.psi.impl.ErlangFunctionReferenceImpl`

