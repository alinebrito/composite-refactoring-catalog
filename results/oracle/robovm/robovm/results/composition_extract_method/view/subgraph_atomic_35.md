<img src=subgraph_atomic_35.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyCanonData#getString(CGImagePropertyCanon)`\
target: `org.robovm.apple.imageio.CGImagePropertyCanonData#get(CGImagePropertyCanon,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyCanon, type Class<T>) : T extracted from public getString(property CGImagePropertyCanon) : String in class org.robovm.apple.imageio.CGImagePropertyCanonData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyCanonData#getNumber(CGImagePropertyCanon)`\
target: `org.robovm.apple.imageio.CGImagePropertyCanonData#get(CGImagePropertyCanon,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyCanon, type Class<T>) : T extracted from public getNumber(property CGImagePropertyCanon) : double in class org.robovm.apple.imageio.CGImagePropertyCanonData`

