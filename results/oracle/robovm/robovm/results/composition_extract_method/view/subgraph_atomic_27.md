<img src=subgraph_atomic_27.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setShouldCache(boolean)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setShouldCache(cache boolean) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `1`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setShouldAllowFloat(boolean)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setShouldAllowFloat(allowFloat boolean) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `2`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setTypeIdentifierHint(String)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setTypeIdentifierHint(typeIdentifier String) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `3`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setShouldCreateThumbnailWithTransform(boolean)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setShouldCreateThumbnailWithTransform(transform boolean) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `4`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setThumbnailMaxPixelSize(long)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setThumbnailMaxPixelSize(maxSize long) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `5`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setShouldCacheImmediately(boolean)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setShouldCacheImmediately(cache boolean) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `6`\
source `org.robovm.apple.imageio.CGImageSourceOptions#setShouldCreateThumbnailFromImageIfAbsent(boolean)`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageSourceOptions extracted from public setShouldCreateThumbnailFromImageIfAbsent(createThumbnail boolean) : CGImageSourceOptions in class org.robovm.apple.imageio.CGImageSourceOptions`

