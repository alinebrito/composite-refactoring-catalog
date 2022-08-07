<img src=subgraph_atomic_41.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#getString(CGImagePropertyIPTCContactInfo)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#get(CGImagePropertyIPTCContactInfo,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyIPTCContactInfo, type Class<T>) : T extracted from public getString(property CGImagePropertyIPTCContactInfo) : String in class org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#getNumber(CGImagePropertyIPTCContactInfo)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData#get(CGImagePropertyIPTCContactInfo,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyIPTCContactInfo, type Class<T>) : T extracted from public getNumber(property CGImagePropertyIPTCContactInfo) : double in class org.robovm.apple.imageio.CGImagePropertyIPTCContactInfoData`

