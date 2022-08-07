<img src=subgraph_atomic_33.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageProperty8BIMData#getString(CGImageProperty8BIM)`\
target: `org.robovm.apple.imageio.CGImageProperty8BIMData#get(CGImageProperty8BIM,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImageProperty8BIM, type Class<T>) : T extracted from public getString(property CGImageProperty8BIM) : String in class org.robovm.apple.imageio.CGImageProperty8BIMData`

id: `1`\
source `org.robovm.apple.imageio.CGImageProperty8BIMData#getNumber(CGImageProperty8BIM)`\
target: `org.robovm.apple.imageio.CGImageProperty8BIMData#get(CGImageProperty8BIM,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImageProperty8BIM, type Class<T>) : T extracted from public getNumber(property CGImageProperty8BIM) : double in class org.robovm.apple.imageio.CGImageProperty8BIMData`

