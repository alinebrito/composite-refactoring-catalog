<img src=subgraph_atomic_22.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyTIFFData#set(CGImagePropertyTIFF,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyTIFFData#set(CGImagePropertyTIFF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyTIFF, value NativeObject) : CGImagePropertyTIFFData extracted from public set(property CGImagePropertyTIFF, value double) : CGImagePropertyTIFFData in class org.robovm.apple.imageio.CGImagePropertyTIFFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyTIFFData#set(CGImagePropertyTIFF,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyTIFFData#set(CGImagePropertyTIFF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyTIFF, value NativeObject) : CGImagePropertyTIFFData extracted from public set(property CGImagePropertyTIFF, value String) : CGImagePropertyTIFFData in class org.robovm.apple.imageio.CGImagePropertyTIFFData`

