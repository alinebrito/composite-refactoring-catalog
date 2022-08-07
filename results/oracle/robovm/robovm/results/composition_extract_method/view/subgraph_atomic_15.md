<img src=subgraph_atomic_15.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyExifAuxData#set(CGImagePropertyExifAux,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyExifAuxData#set(CGImagePropertyExifAux,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyExifAux, value NativeObject) : CGImagePropertyExifAuxData extracted from public set(property CGImagePropertyExifAux, value double) : CGImagePropertyExifAuxData in class org.robovm.apple.imageio.CGImagePropertyExifAuxData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyExifAuxData#set(CGImagePropertyExifAux,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyExifAuxData#set(CGImagePropertyExifAux,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyExifAux, value NativeObject) : CGImagePropertyExifAuxData extracted from public set(property CGImagePropertyExifAux, value String) : CGImagePropertyExifAuxData in class org.robovm.apple.imageio.CGImagePropertyExifAuxData`

