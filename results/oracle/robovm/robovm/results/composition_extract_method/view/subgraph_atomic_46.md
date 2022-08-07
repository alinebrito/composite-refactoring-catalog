<img src=subgraph_atomic_46.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyTIFFData#getString(CGImagePropertyTIFF)`\
target: `org.robovm.apple.imageio.CGImagePropertyTIFFData#get(CGImagePropertyTIFF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyTIFF, type Class<T>) : T extracted from public getString(property CGImagePropertyTIFF) : String in class org.robovm.apple.imageio.CGImagePropertyTIFFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyTIFFData#getNumber(CGImagePropertyTIFF)`\
target: `org.robovm.apple.imageio.CGImagePropertyTIFFData#get(CGImagePropertyTIFF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyTIFF, type Class<T>) : T extracted from public getNumber(property CGImagePropertyTIFF) : double in class org.robovm.apple.imageio.CGImagePropertyTIFFData`

