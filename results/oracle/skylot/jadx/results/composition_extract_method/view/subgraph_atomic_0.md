<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `jadx.core.utils.RegionUtils#getAllRegionBlocks(IContainer,Set<IBlock>)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public getAllRegionBlocks(container IContainer, blocks Set<IBlock>) : void in class jadx.core.utils.RegionUtils`

id: `1`\
source `jadx.core.utils.RegionUtils#isRegionContainsBlock(IContainer,BlockNode)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public isRegionContainsBlock(container IContainer, block BlockNode) : boolean in class jadx.core.utils.RegionUtils`

id: `2`\
source `jadx.core.utils.RegionUtils#getBlockContainer(IContainer,BlockNode)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public getBlockContainer(container IContainer, block BlockNode) : IContainer in class jadx.core.utils.RegionUtils`

id: `3`\
source `jadx.core.utils.RegionUtils#isDominatedBy(BlockNode,IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public isDominatedBy(dom BlockNode, cont IContainer) : boolean in class jadx.core.utils.RegionUtils`

id: `4`\
source `jadx.core.utils.RegionUtils#hasPathThroughBlock(BlockNode,IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public hasPathThroughBlock(block BlockNode, cont IContainer) : boolean in class jadx.core.utils.RegionUtils`

id: `5`\
source `jadx.core.utils.RegionUtils#hasExitEdge(IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public hasExitEdge(container IContainer) : boolean in class jadx.core.utils.RegionUtils`

id: `6`\
source `jadx.core.utils.RegionUtils#getLastInsn(IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public getLastInsn(container IContainer) : InsnNode in class jadx.core.utils.RegionUtils`

id: `7`\
source `jadx.core.utils.RegionUtils#hasExitBlock(IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public hasExitBlock(container IContainer) : boolean in class jadx.core.utils.RegionUtils`

id: `8`\
source `jadx.core.utils.RegionUtils#insnsCount(IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public insnsCount(container IContainer) : int in class jadx.core.utils.RegionUtils`

id: `9`\
source `jadx.core.utils.RegionUtils#notEmpty(IContainer)`\
target: `jadx.core.utils.RegionUtils#unknownContainerType(IContainer)`\
type: `EXTRACT`\
commit: [2d8d41648](https://github.com/skylot/jadx/commit/2d8d4164830631d3125575f055b417c5addaa22f)\
description: `Extract Method protected unknownContainerType(container IContainer) : String extracted from public notEmpty(container IContainer) : boolean in class jadx.core.utils.RegionUtils`

