<img src=subgraph_atomic_36.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyDNGData#getString(CGImagePropertyDNG)`\
target: `org.robovm.apple.imageio.CGImagePropertyDNGData#get(CGImagePropertyDNG,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyDNG, type Class<T>) : T extracted from public getString(property CGImagePropertyDNG) : String in class org.robovm.apple.imageio.CGImagePropertyDNGData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyDNGData#getNumber(CGImagePropertyDNG)`\
target: `org.robovm.apple.imageio.CGImagePropertyDNGData#get(CGImagePropertyDNG,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyDNG, type Class<T>) : T extracted from public getNumber(property CGImagePropertyDNG) : double in class org.robovm.apple.imageio.CGImagePropertyDNGData`

