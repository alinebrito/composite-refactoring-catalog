<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `buildcraft.builders.TileFiller#initialize()`\
target: `buildcraft.builders.TileFiller#initTemplate()`\
type: `EXTRACT`\
commit: [6abc40ed4](https://github.com/BuildCraft/BuildCraft/commit/6abc40ed4850d74ee6c155f5a28f8b34881a0284)\
description: `Extract Method private initTemplate() : void extracted from public initialize() : void in class buildcraft.builders.TileFiller`

id: `1`\
source `buildcraft.builders.TileFiller#updateEntity()`\
target: `buildcraft.builders.TileFiller#initTemplate()`\
type: `EXTRACT`\
commit: [6abc40ed4](https://github.com/BuildCraft/BuildCraft/commit/6abc40ed4850d74ee6c155f5a28f8b34881a0284)\
description: `Extract Method private initTemplate() : void extracted from public updateEntity() : void in class buildcraft.builders.TileFiller`

