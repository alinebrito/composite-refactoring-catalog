<img src=subgraph_atomic_56.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCreateThumbnailFromImageIfAbsent()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public shouldCreateThumbnailFromImageIfAbsent() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `1`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldAllowFloat()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public shouldAllowFloat() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `2`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCreateThumbnailWithTransform()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public shouldCreateThumbnailWithTransform() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `3`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCacheImmediately()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public shouldCacheImmediately() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `4`\
source `org.robovm.apple.imageio.CGImageSourceOptions#getThumbnailMaxPixelSize()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getThumbnailMaxPixelSize() : long in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `5`\
source `org.robovm.apple.imageio.CGImageSourceOptions#getTypeIdentifierHint()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getTypeIdentifierHint() : String in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `6`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCache()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public shouldCache() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

