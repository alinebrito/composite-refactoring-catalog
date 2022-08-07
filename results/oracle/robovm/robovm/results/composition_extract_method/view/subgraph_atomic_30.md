<img src=subgraph_atomic_30.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageDestinationProperties#setMaxPixelSize(long)`\
target: `org.robovm.apple.imageio.CGImageDestinationProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationProperties extracted from public setMaxPixelSize(size long) : CGImageDestinationProperties in class org.robovm.apple.imageio.CGImageDestinationProperties`

id: `1`\
source `org.robovm.apple.imageio.CGImageDestinationProperties#setLossyCompressionQuality(double)`\
target: `org.robovm.apple.imageio.CGImageDestinationProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationProperties extracted from public setLossyCompressionQuality(quality double) : CGImageDestinationProperties in class org.robovm.apple.imageio.CGImageDestinationProperties`

id: `2`\
source `org.robovm.apple.imageio.CGImageDestinationProperties#setEmbedThumbnail(boolean)`\
target: `org.robovm.apple.imageio.CGImageDestinationProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationProperties extracted from public setEmbedThumbnail(embed boolean) : CGImageDestinationProperties in class org.robovm.apple.imageio.CGImageDestinationProperties`

id: `3`\
source `org.robovm.apple.imageio.CGImageDestinationProperties#setBackgroundColor(CGColor)`\
target: `org.robovm.apple.imageio.CGImageDestinationProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageDestinationProperties extracted from public setBackgroundColor(color CGColor) : CGImageDestinationProperties in class org.robovm.apple.imageio.CGImageDestinationProperties`

