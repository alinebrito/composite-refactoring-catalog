<img src=subgraph_atomic_45.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyPNGData#getString(CGImagePropertyPNG)`\
target: `org.robovm.apple.imageio.CGImagePropertyPNGData#get(CGImagePropertyPNG,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyPNG, type Class<T>) : T extracted from public getString(property CGImagePropertyPNG) : String in class org.robovm.apple.imageio.CGImagePropertyPNGData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyPNGData#getNumber(CGImagePropertyPNG)`\
target: `org.robovm.apple.imageio.CGImagePropertyPNGData#get(CGImagePropertyPNG,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyPNG, type Class<T>) : T extracted from public getNumber(property CGImagePropertyPNG) : double in class org.robovm.apple.imageio.CGImagePropertyPNGData`

