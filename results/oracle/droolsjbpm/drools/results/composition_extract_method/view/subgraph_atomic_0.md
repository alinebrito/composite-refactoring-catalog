<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.drools.core.rule.JavaDialectRuntimeData#onAdd(DialectRuntimeRegistry,ClassLoader)`\
target: `org.drools.core.rule.JavaDialectRuntimeData#makeClassLoader()`\
type: `EXTRACT`\
commit: [c8e09e205](https://github.com/droolsjbpm/drools/commit/c8e09e2056c54ead97bce4386a25b222154223b1)\
description: `Extract Method private makeClassLoader() : ClassLoader extracted from public onAdd(registry DialectRuntimeRegistry, rootClassLoader ClassLoader) : void in class org.drools.core.rule.JavaDialectRuntimeData`

id: `1`\
source `org.drools.core.rule.JavaDialectRuntimeData#reload()`\
target: `org.drools.core.rule.JavaDialectRuntimeData#makeClassLoader()`\
type: `EXTRACT`\
commit: [c8e09e205](https://github.com/droolsjbpm/drools/commit/c8e09e2056c54ead97bce4386a25b222154223b1)\
description: `Extract Method private makeClassLoader() : ClassLoader extracted from public reload() : void in class org.drools.core.rule.JavaDialectRuntimeData`

