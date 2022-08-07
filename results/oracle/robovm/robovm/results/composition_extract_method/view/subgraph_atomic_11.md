<img src=subgraph_atomic_11.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageProperty8BIMData#set(CGImageProperty8BIM,String)`\
target: `org.robovm.apple.imageio.CGImageProperty8BIMData#set(CGImageProperty8BIM,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImageProperty8BIM, value NativeObject) : CGImageProperty8BIMData extracted from public set(property CGImageProperty8BIM, value String) : CGImageProperty8BIMData in class org.robovm.apple.imageio.CGImageProperty8BIMData`

id: `1`\
source `org.robovm.apple.imageio.CGImageProperty8BIMData#set(CGImageProperty8BIM,double)`\
target: `org.robovm.apple.imageio.CGImageProperty8BIMData#set(CGImageProperty8BIM,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImageProperty8BIM, value NativeObject) : CGImageProperty8BIMData extracted from public set(property CGImageProperty8BIM, value double) : CGImageProperty8BIMData in class org.robovm.apple.imageio.CGImageProperty8BIMData`

