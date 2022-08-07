<img src=subgraph_atomic_40.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyGPSData#getNumber(CGImagePropertyGPS)`\
target: `org.robovm.apple.imageio.CGImagePropertyGPSData#get(CGImagePropertyGPS,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyGPS, type Class<T>) : T extracted from public getNumber(property CGImagePropertyGPS) : double in class org.robovm.apple.imageio.CGImagePropertyGPSData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyGPSData#getString(CGImagePropertyGPS)`\
target: `org.robovm.apple.imageio.CGImagePropertyGPSData#get(CGImagePropertyGPS,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyGPS, type Class<T>) : T extracted from public getString(property CGImagePropertyGPS) : String in class org.robovm.apple.imageio.CGImagePropertyGPSData`

