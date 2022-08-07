<img src=subgraph_atomic_44.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyNikonData#getString(CGImagePropertyNikon)`\
target: `org.robovm.apple.imageio.CGImagePropertyNikonData#get(CGImagePropertyNikon,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyNikon, type Class<T>) : T extracted from public getString(property CGImagePropertyNikon) : String in class org.robovm.apple.imageio.CGImagePropertyNikonData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyNikonData#getNumber(CGImagePropertyNikon)`\
target: `org.robovm.apple.imageio.CGImagePropertyNikonData#get(CGImagePropertyNikon,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyNikon, type Class<T>) : T extracted from public getNumber(property CGImagePropertyNikon) : double in class org.robovm.apple.imageio.CGImagePropertyNikonData`

