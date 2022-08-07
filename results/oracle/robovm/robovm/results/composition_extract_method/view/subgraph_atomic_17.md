<img src=subgraph_atomic_17.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyCanonData#set(CGImagePropertyCanon,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyCanonData#set(CGImagePropertyCanon,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyCanon, value NativeObject) : CGImagePropertyCanonData extracted from public set(property CGImagePropertyCanon, value double) : CGImagePropertyCanonData in class org.robovm.apple.imageio.CGImagePropertyCanonData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyCanonData#set(CGImagePropertyCanon,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyCanonData#set(CGImagePropertyCanon,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyCanon, value NativeObject) : CGImagePropertyCanonData extracted from public set(property CGImagePropertyCanon, value String) : CGImagePropertyCanonData in class org.robovm.apple.imageio.CGImagePropertyCanonData`

