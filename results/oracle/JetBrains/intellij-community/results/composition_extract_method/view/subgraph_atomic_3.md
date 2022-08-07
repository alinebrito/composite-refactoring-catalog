<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#addJarToRoots(String,Module,PsiElement)`\
target: `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#addJarsToRoots(List<String>,String,Module,PsiElement)`\
type: `EXTRACT`\
commit: [7c59f2a4f](https://github.com/JetBrains/intellij-community/commit/7c59f2a4f9b03a9e48ca15554291a03477aa19c1)\
description: `Extract Method public addJarsToRoots(jarPaths List<String>, libraryName String, module Module, location PsiElement) : void extracted from public addJarToRoots(libPath String, module Module, location PsiElement) : void in class com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix`

id: `1`\
source `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#addJUnit4Library(boolean,Module)`\
target: `com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix#addJarsToRoots(List<String>,String,Module,PsiElement)`\
type: `EXTRACT`\
commit: [7c59f2a4f](https://github.com/JetBrains/intellij-community/commit/7c59f2a4f9b03a9e48ca15554291a03477aa19c1)\
description: `Extract Method public addJarsToRoots(jarPaths List<String>, libraryName String, module Module, location PsiElement) : void extracted from public addJUnit4Library(inTests boolean, currentModule Module) : void in class com.intellij.codeInsight.daemon.impl.quickfix.OrderEntryFix`

