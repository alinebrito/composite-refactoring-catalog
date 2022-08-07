<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#shouldExcludeXMP()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldExcludeXMP() : boolean in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `1`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#shouldExcludeGPS()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldExcludeGPS() : boolean in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `2`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#getOrientation()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public getOrientation() : CGImagePropertyOrientation in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `3`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#getDateTime()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public getDateTime() : String in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `4`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#getMetadata()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public getMetadata() : CGImageMetadata in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `5`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#isMergingMetadata()`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public isMergingMetadata() : boolean in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

