<img src=subgraph_atomic_34.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyCIFFData#getString(CGImagePropertyCIFF)`\
target: `org.robovm.apple.imageio.CGImagePropertyCIFFData#get(CGImagePropertyCIFF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyCIFF, type Class<T>) : T extracted from public getString(property CGImagePropertyCIFF) : String in class org.robovm.apple.imageio.CGImagePropertyCIFFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyCIFFData#getNumber(CGImagePropertyCIFF)`\
target: `org.robovm.apple.imageio.CGImagePropertyCIFFData#get(CGImagePropertyCIFF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyCIFF, type Class<T>) : T extracted from public getNumber(property CGImagePropertyCIFF) : double in class org.robovm.apple.imageio.CGImagePropertyCIFFData`

