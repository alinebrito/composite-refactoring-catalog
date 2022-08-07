<img src=subgraph_atomic_24.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyJFIFData#set(CGImagePropertyJFIF,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyJFIFData#set(CGImagePropertyJFIF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyJFIF, value NativeObject) : CGImagePropertyJFIFData extracted from public set(property CGImagePropertyJFIF, value double) : CGImagePropertyJFIFData in class org.robovm.apple.imageio.CGImagePropertyJFIFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyJFIFData#set(CGImagePropertyJFIF,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyJFIFData#set(CGImagePropertyJFIF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyJFIF, value NativeObject) : CGImagePropertyJFIFData extracted from public set(property CGImagePropertyJFIF, value String) : CGImagePropertyJFIFData in class org.robovm.apple.imageio.CGImagePropertyJFIFData`

