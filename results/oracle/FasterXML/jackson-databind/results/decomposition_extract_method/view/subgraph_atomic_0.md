<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.fasterxml.jackson.databind.type.TypeFactory#findClass(String)`\
target: `com.fasterxml.jackson.databind.type.TypeFactory#classForName(String)`\
type: `EXTRACT`\
commit: [cfe88fe3f](https://github.com/FasterXML/jackson-databind/commit/cfe88fe3fbcc6b02ca55cee7b1f4ab13e249edea)\
description: `Extract Method protected classForName(name String) : Class<?> extracted from public findClass(className String) : Class<?> in class com.fasterxml.jackson.databind.type.TypeFactory`

id: `1`\
source `com.fasterxml.jackson.databind.type.TypeFactory#findClass(String)`\
target: `com.fasterxml.jackson.databind.type.TypeFactory#classForName(String,boolean,ClassLoader)`\
type: `EXTRACT`\
commit: [cfe88fe3f](https://github.com/FasterXML/jackson-databind/commit/cfe88fe3fbcc6b02ca55cee7b1f4ab13e249edea)\
description: `Extract Method protected classForName(name String, initialize boolean, loader ClassLoader) : Class<?> extracted from public findClass(className String) : Class<?> in class com.fasterxml.jackson.databind.type.TypeFactory`

