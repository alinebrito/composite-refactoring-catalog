<img src=subgraph_atomic_21.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyPNGData#set(CGImagePropertyPNG,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyPNGData#set(CGImagePropertyPNG,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyPNG, value NativeObject) : CGImagePropertyPNGData extracted from public set(property CGImagePropertyPNG, value double) : CGImagePropertyPNGData in class org.robovm.apple.imageio.CGImagePropertyPNGData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyPNGData#set(CGImagePropertyPNG,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyPNGData#set(CGImagePropertyPNG,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyPNG, value NativeObject) : CGImagePropertyPNGData extracted from public set(property CGImagePropertyPNG, value String) : CGImagePropertyPNGData in class org.robovm.apple.imageio.CGImagePropertyPNGData`

