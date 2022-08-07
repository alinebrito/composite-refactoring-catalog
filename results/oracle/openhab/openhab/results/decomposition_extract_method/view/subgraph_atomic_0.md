<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.openhab.core.jsr223.internal.engine.scriptmanager.Script#initializeSciptGlobals()`\
target: `org.openhab.core.jsr223.internal.engine.scriptmanager.Script#initializeGeneralGlobals()`\
type: `EXTRACT`\
commit: [cf1efb6d2](https://github.com/openhab/openhab/commit/cf1efb6d27a4037cdbe5a780afa6053859a60d4a)\
description: `Extract Method private initializeGeneralGlobals() : void extracted from private initializeSciptGlobals() : void in class org.openhab.core.jsr223.internal.engine.scriptmanager.Script`

id: `1`\
source `org.openhab.core.jsr223.internal.engine.scriptmanager.Script#initializeSciptGlobals()`\
target: `org.openhab.core.jsr223.internal.engine.scriptmanager.Script#initializeNashornGlobals()`\
type: `EXTRACT`\
commit: [cf1efb6d2](https://github.com/openhab/openhab/commit/cf1efb6d27a4037cdbe5a780afa6053859a60d4a)\
description: `Extract Method private initializeNashornGlobals() : void extracted from private initializeSciptGlobals() : void in class org.openhab.core.jsr223.internal.engine.scriptmanager.Script`

