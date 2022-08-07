<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.eclipse.jetty.maven.plugin.ScanTargetPattern`\
target: `org.eclipse.jetty.maven.plugin.ScanPattern#setIncludes(List)`\
type: `MOVE`\
commit: [1f3be625e](https://github.com/eclipse/jetty.project/commit/1f3be625e62f44d929c01f6574678eea05754474)\
description: `Move Method public setIncludes(includes List) : void from class org.eclipse.jetty.maven.plugin.ScanTargetPattern to public setIncludes(includes List<String>) : void from class org.eclipse.jetty.maven.plugin.ScanPattern`

id: `1`\
source `org.eclipse.jetty.maven.plugin.ScanTargetPattern`\
target: `org.eclipse.jetty.maven.plugin.ScanPattern#setExcludes(List)`\
type: `MOVE`\
commit: [1f3be625e](https://github.com/eclipse/jetty.project/commit/1f3be625e62f44d929c01f6574678eea05754474)\
description: `Move Method public setExcludes(excludes List) : void from class org.eclipse.jetty.maven.plugin.ScanTargetPattern to public setExcludes(excludes List<String>) : void from class org.eclipse.jetty.maven.plugin.ScanPattern`

