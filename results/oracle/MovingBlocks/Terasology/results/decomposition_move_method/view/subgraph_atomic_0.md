<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.terasology.engine.TerasologyEngine`\
target: `org.terasology.engine.subsystem.common.ConfigurationSubsystem#validateServerIdentity()`\
type: `MOVE`\
commit: [543a9808a](https://github.com/MovingBlocks/Terasology/commit/543a9808a85619dbe5acc2373cb4fe5344442de7)\
description: `Move Method private validateServerIdentity() : boolean from class org.terasology.engine.TerasologyEngine to private validateServerIdentity() : boolean from class org.terasology.engine.subsystem.common.ConfigurationSubsystem`

id: `1`\
source `org.terasology.engine.TerasologyEngine`\
target: `org.terasology.engine.subsystem.common.ConfigurationSubsystem#preInitialise(Context)`\
type: `MOVE_RENAME`\
commit: [543a9808a](https://github.com/MovingBlocks/Terasology/commit/543a9808a85619dbe5acc2373cb4fe5344442de7)\
description: `Move And Rename Method private initConfig() : void from class org.terasology.engine.TerasologyEngine to public preInitialise(rootContext Context) : void from class org.terasology.engine.subsystem.common.ConfigurationSubsystem`

