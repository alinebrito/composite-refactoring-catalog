<img src=subgraph_atomic_12.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCData#set(CGImagePropertyIPTC,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCData#set(CGImagePropertyIPTC,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyIPTC, value NativeObject) : CGImagePropertyIPTCData extracted from public set(property CGImagePropertyIPTC, value double) : CGImagePropertyIPTCData in class org.robovm.apple.imageio.CGImagePropertyIPTCData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCData#set(CGImagePropertyIPTC,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCData#set(CGImagePropertyIPTC,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyIPTC, value NativeObject) : CGImagePropertyIPTCData extracted from public set(property CGImagePropertyIPTC, value String) : CGImagePropertyIPTCData in class org.robovm.apple.imageio.CGImagePropertyIPTCData`

id: `2`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCData#setContactInfo(CGImagePropertyIPTCContactInfoData)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCData#set(CGImagePropertyIPTC,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyIPTC, value NativeObject) : CGImagePropertyIPTCData extracted from public setContactInfo(contactInfo CGImagePropertyIPTCContactInfoData) : CGImagePropertyIPTCData in class org.robovm.apple.imageio.CGImagePropertyIPTCData`

