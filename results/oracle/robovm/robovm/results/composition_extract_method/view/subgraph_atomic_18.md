<img src=subgraph_atomic_18.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#set(CGImagePropertyIPTCContactInfo,String)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#set(CGImagePropertyIPTCContactInfo,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyIPTCContactInfo, value NativeObject) : CGImagePropertyIPTCContactInfoData extracted from public set(property CGImagePropertyIPTCContactInfo, value String) : CGImagePropertyIPTCContactInfoData in class org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#set(CGImagePropertyIPTCContactInfo,double)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#set(CGImagePropertyIPTCContactInfo,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CGImagePropertyIPTCContactInfo, value NativeObject) : CGImagePropertyIPTCContactInfoData extracted from public set(property CGImagePropertyIPTCContactInfo, value double) : CGImagePropertyIPTCContactInfoData in class org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData`

