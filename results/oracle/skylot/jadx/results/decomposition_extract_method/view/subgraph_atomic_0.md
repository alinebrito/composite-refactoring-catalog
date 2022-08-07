<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `jadx.api.JavaClass#getDefinitionPosition(int,int)`\
target: `jadx.api.JavaClass#getJavaNodeAtPosition(int,int)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method public getJavaNodeAtPosition(line int, offset int) : JavaNode extracted from public getDefinitionPosition(line int, offset int) : CodePosition in class jadx.api.JavaClass`

id: `1`\
source `jadx.api.JavaClass#getDefinitionPosition(int,int)`\
target: `jadx.api.JavaClass#getDefinitionPosition(JavaNode)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method public getDefinitionPosition(javaNode JavaNode) : CodePosition extracted from public getDefinitionPosition(line int, offset int) : CodePosition in class jadx.api.JavaClass`

id: `2`\
source `jadx.api.JavaClass#getDefinitionPosition(int,int)`\
target: `jadx.api.JavaClass#convertNode(Object)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method private convertNode(obj Object) : JavaNode extracted from public getDefinitionPosition(line int, offset int) : CodePosition in class jadx.api.JavaClass`

