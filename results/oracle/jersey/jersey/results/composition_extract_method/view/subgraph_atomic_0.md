<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.glassfish.jersey.server.internal.scanning.FilesScanner#FilesScanner(String[],boolean)`\
target: `org.glassfish.jersey.server.internal.scanning.FilesScanner#init()`\
type: `EXTRACT`\
commit: [fab151677](https://github.com/jersey/jersey/commit/fab1516773d50bf86d9cc37e2f6db13496f0ecae)\
description: `Extract Method private init() : void extracted from public FilesScanner(fileNames String[], recursive boolean) in class org.glassfish.jersey.server.internal.scanning.FilesScanner`

id: `1`\
source `org.glassfish.jersey.server.internal.scanning.FilesScanner#reset()`\
target: `org.glassfish.jersey.server.internal.scanning.FilesScanner#init()`\
type: `EXTRACT`\
commit: [fab151677](https://github.com/jersey/jersey/commit/fab1516773d50bf86d9cc37e2f6db13496f0ecae)\
description: `Extract Method private init() : void extracted from public reset() : void in class org.glassfish.jersey.server.internal.scanning.FilesScanner`

