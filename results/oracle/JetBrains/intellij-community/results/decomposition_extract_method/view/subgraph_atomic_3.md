<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#registerFixes(QuickFixActionRegistrar,PsiReference)`\
target: `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#addJarsToRootsAndImportClass(List<String>,String,Module,Editor,PsiReference,String)`\
type: `EXTRACT`\
commit: [7c59f2a4f](https://github.com/JetBrains/intellij-community/commit/7c59f2a4f9b03a9e48ca15554291a03477aa19c1)\
description: `Extract Method public addJarsToRootsAndImportClass(jarPaths List<String>, libraryName String, currentModule Module, editor Editor, reference PsiReference, className String) : void extracted from public registerFixes(registrar QuickFixActionRegistrar, reference PsiReference) : List<LocalQuickFix> in class com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix`

id: `1`\
source `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#registerFixes(QuickFixActionRegistrar,PsiReference)`\
target: `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#getJUnit4JarPaths()`\
type: `EXTRACT`\
commit: [7c59f2a4f](https://github.com/JetBrains/intellij-community/commit/7c59f2a4f9b03a9e48ca15554291a03477aa19c1)\
description: `Extract Method private getJUnit4JarPaths() : List<String> extracted from public registerFixes(registrar QuickFixActionRegistrar, reference PsiReference) : List<LocalQuickFix> in class com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix`

