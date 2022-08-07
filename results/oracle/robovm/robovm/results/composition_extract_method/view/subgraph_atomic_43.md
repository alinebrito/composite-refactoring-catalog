<img src=subgraph_atomic_43.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyJFIFData#getString(CGImagePropertyJFIF)`\
target: `org.robovm.apple.imageio.CGImagePropertyJFIFData#get(CGImagePropertyJFIF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyJFIF, type Class<T>) : T extracted from public getString(property CGImagePropertyJFIF) : String in class org.robovm.apple.imageio.CGImagePropertyJFIFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyJFIFData#getNumber(CGImagePropertyJFIF)`\
target: `org.robovm.apple.imageio.CGImagePropertyJFIFData#get(CGImagePropertyJFIF,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyJFIF, type Class<T>) : T extracted from public getNumber(property CGImagePropertyJFIF) : double in class org.robovm.apple.imageio.CGImagePropertyJFIFData`

