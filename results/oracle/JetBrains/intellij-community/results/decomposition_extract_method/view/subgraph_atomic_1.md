<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.jetbrains.plugins.javaFX.fxml.refs.FxmlReferencesContributor.MyJavaClassReferenceProvider.JavaClassReferenceWrapper#handleElementRename(String)`\
target: `org.jetbrains.plugins.javaFX.fxml.refs.FxmlReferencesContributor.MyJavaClassReferenceProvider.JavaClassReferenceWrapper#setNewName(String)`\
type: `EXTRACT`\
commit: [a97341973](https://github.com/JetBrains/intellij-community/commit/a97341973c3b683d62d1422e5404ed5c7ccf45f8)\
description: `Extract Method private setNewName(newText String) : PsiElement extracted from public handleElementRename(newElementName String) : PsiElement in class org.jetbrains.plugins.javaFX.fxml.refs.FxmlReferencesContributor.MyJavaClassReferenceProvider.JavaClassReferenceWrapper`

id: `1`\
source `org.jetbrains.plugins.javaFX.fxml.refs.FxmlReferencesContributor.MyJavaClassReferenceProvider.JavaClassReferenceWrapper#handleElementRename(String)`\
target: `org.jetbrains.plugins.javaFX.fxml.refs.FxmlReferencesContributor.MyJavaClassReferenceProvider.JavaClassReferenceWrapper#getOldName()`\
type: `EXTRACT`\
commit: [a97341973](https://github.com/JetBrains/intellij-community/commit/a97341973c3b683d62d1422e5404ed5c7ccf45f8)\
description: `Extract Method private getOldName() : String extracted from public handleElementRename(newElementName String) : PsiElement in class org.jetbrains.plugins.javaFX.fxml.refs.FxmlReferencesContributor.MyJavaClassReferenceProvider.JavaClassReferenceWrapper`

