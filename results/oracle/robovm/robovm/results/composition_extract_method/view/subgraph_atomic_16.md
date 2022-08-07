<img src=subgraph_atomic_16.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyExifData#set(CGImagePropertyExif,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyExifData#set(CGImagePropertyExif,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyExif, value NativeObject) : CGImagePropertyExifData extracted from public set(property CGImagePropertyExif, value String) : CGImagePropertyExifData in class org.robovm.apple.imageio.CGImagePropertyExifData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyExifData#set(CGImagePropertyExif,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyExifData#set(CGImagePropertyExif,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyExif, value NativeObject) : CGImagePropertyExifData extracted from public set(property CGImagePropertyExif, value double) : CGImagePropertyExifData in class org.robovm.apple.imageio.CGImagePropertyExifData`

