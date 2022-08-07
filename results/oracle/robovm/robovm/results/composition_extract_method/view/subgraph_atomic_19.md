<img src=subgraph_atomic_19.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyGIFData#set(CGImagePropertyGIF,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyGIFData#set(CGImagePropertyGIF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyGIF, value NativeObject) : CGImagePropertyGIFData extracted from public set(property CGImagePropertyGIF, value double) : CGImagePropertyGIFData in class org.robovm.apple.imageio.CGImagePropertyGIFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyGIFData#set(CGImagePropertyGIF,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyGIFData#set(CGImagePropertyGIF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyGIF, value NativeObject) : CGImagePropertyGIFData extracted from public set(property CGImagePropertyGIF, value String) : CGImagePropertyGIFData in class org.robovm.apple.imageio.CGImagePropertyGIFData`

