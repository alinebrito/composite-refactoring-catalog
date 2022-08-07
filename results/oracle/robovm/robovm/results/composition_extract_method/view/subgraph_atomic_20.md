<img src=subgraph_atomic_20.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyCIFFData#set(CGImagePropertyCIFF,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyCIFFData#set(CGImagePropertyCIFF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyCIFF, value NativeObject) : CGImagePropertyCIFFData extracted from public set(property CGImagePropertyCIFF, value double) : CGImagePropertyCIFFData in class org.robovm.apple.imageio.CGImagePropertyCIFFData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyCIFFData#set(CGImagePropertyCIFF,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyCIFFData#set(CGImagePropertyCIFF,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyCIFF, value NativeObject) : CGImagePropertyCIFFData extracted from public set(property CGImagePropertyCIFF, value String) : CGImagePropertyCIFFData in class org.robovm.apple.imageio.CGImagePropertyCIFFData`

