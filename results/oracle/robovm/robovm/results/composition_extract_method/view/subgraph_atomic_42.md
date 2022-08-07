<img src=subgraph_atomic_42.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCData#getString(CGImagePropertyIPTC)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCData#get(CGImagePropertyIPTC,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyIPTC, type Class<T>) : T extracted from public getString(property CGImagePropertyIPTC) : String in class org.robovm.apple.imageio.CGImagePropertyIPTCData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCData#getNumber(CGImagePropertyIPTC)`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCData#get(CGImagePropertyIPTC,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyIPTC, type Class<T>) : T extracted from public getNumber(property CGImagePropertyIPTC) : double in class org.robovm.apple.imageio.CGImagePropertyIPTCData`

id: `2`\
source `org.robovm.apple.imageio.CGImagePropertyIPTCData#getContactInfo()`\
target: `org.robovm.apple.imageio.CGImagePropertyIPTCData#get(CGImagePropertyIPTC,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyIPTC, type Class<T>) : T extracted from public getContactInfo() : CGImagePropertyIPTCContactInfoData in class org.robovm.apple.imageio.CGImagePropertyIPTCData`

