<img src=subgraph_atomic_39.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyGIFData#getString(CGImagePropertyGIF)`\
target: `org.robovm.apple.imageio.CGImagePropertyGIFData#get(CGImagePropertyGIF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyGIF, type Class<T>) : T extracted from public getString(property CGImagePropertyGIF) : String in class org.robovm.apple.imageio.CGImagePropertyGIFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyGIFData#getNumber(CGImagePropertyGIF)`\
target: `org.robovm.apple.imageio.CGImagePropertyGIFData#get(CGImagePropertyGIF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyGIF, type Class<T>) : T extracted from public getNumber(property CGImagePropertyGIF) : double in class org.robovm.apple.imageio.CGImagePropertyGIFData`

