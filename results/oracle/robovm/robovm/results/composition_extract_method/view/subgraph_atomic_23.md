<img src=subgraph_atomic_23.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyGPSData#set(CGImagePropertyGPS,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyGPSData#set(CGImagePropertyGPS,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyGPS, value NativeObject) : CGImagePropertyGPSData extracted from public set(property CGImagePropertyGPS, value String) : CGImagePropertyGPSData in class org.robovm.apple.imageio.CGImagePropertyGPSData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyGPSData#set(CGImagePropertyGPS,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyGPSData#set(CGImagePropertyGPS,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyGPS, value NativeObject) : CGImagePropertyGPSData extracted from public set(property CGImagePropertyGPS, value double) : CGImagePropertyGPSData in class org.robovm.apple.imageio.CGImagePropertyGPSData`

