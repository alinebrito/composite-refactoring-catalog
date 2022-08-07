<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.jetbrains.jps.cmdline.BuildMain`\
target: `org.jetbrains.jps.cmdline.LogSetup#initLoggers()`\
type: `MOVE`\
commit: [97811cf97](https://github.com/JetBrains/intellij-community/commit/97811cf971f7ccf6a5fc5e90a491db2f58d49da1)\
description: `Move Method private initLoggers() : void from class org.jetbrains.jps.cmdline.BuildMain to public initLoggers() : void from class org.jetbrains.jps.cmdline.LogSetup`

id: `1`\
source `org.jetbrains.jps.cmdline.BuildMain`\
target: `org.jetbrains.jps.cmdline.LogSetup#ensureLogConfigExists(File)`\
type: `MOVE`\
commit: [97811cf97](https://github.com/JetBrains/intellij-community/commit/97811cf971f7ccf6a5fc5e90a491db2f58d49da1)\
description: `Move Method private ensureLogConfigExists(logConfig File) : void from class org.jetbrains.jps.cmdline.BuildMain to private ensureLogConfigExists(logConfig File) : void from class org.jetbrains.jps.cmdline.LogSetup`

