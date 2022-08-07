<img src=subgraph_atomic_25.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setOrientation(CGImagePropertyOrientation)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setOrientation(orientation CGImagePropertyOrientation) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `1`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setDateTime(String)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setDateTime(dateTime String) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `2`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setShouldExcludeGPS(boolean)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setShouldExcludeGPS(exclude boolean) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `3`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setShouldExcludeXMP(boolean)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setShouldExcludeXMP(exclude boolean) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `4`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setMergeMetadata(boolean)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setMergeMetadata(merge boolean) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `5`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setMetadata(CGImageMetadata)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setMetadata(metadata CGImageMetadata) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

id: `6`\
source `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#setDateTime(NSDate)`\
target: `org.robovm.apple.imageio.CGImageDestinationCopySourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationCopySourceOptions extracted from public setDateTime(dateTime NSDate) : CGImageDestinationCopySourceOptions in class org.robovm.apple.imageio.CGImageDestinationCopySourceOptions`

