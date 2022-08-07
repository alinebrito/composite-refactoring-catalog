<img src=subgraph_atomic_41.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#getDateTime()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public getDateTime() : String in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `1`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#getDateTime()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getDateTime() : String in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

