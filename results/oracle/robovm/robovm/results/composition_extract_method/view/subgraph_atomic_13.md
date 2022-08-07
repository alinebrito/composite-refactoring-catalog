<img src=subgraph_atomic_13.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyDNGData#set(CGImagePropertyDNG,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyDNGData#set(CGImagePropertyDNG,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyDNG, value NativeObject) : CGImagePropertyDNGData extracted from public set(property CGImagePropertyDNG, value String) : CGImagePropertyDNGData in class org.robovm.apple.imageio.CGImagePropertyDNGData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyDNGData#set(CGImagePropertyDNG,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyDNGData#set(CGImagePropertyDNG,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyDNG, value NativeObject) : CGImagePropertyDNGData extracted from public set(property CGImagePropertyDNG, value double) : CGImagePropertyDNGData in class org.robovm.apple.imageio.CGImagePropertyDNGData`

