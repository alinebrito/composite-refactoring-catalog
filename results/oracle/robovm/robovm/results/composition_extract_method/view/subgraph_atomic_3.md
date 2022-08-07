<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCreateThumbnailFromImageIfAbsent()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldCreateThumbnailFromImageIfAbsent() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `1`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCacheImmediately()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldCacheImmediately() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `2`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCreateThumbnailWithTransform()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldCreateThumbnailWithTransform() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `3`\
source `org.robovm.apple.imageio.CGImageSourceOptions#getThumbnailMaxPixelSize()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public getThumbnailMaxPixelSize() : long in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `4`\
source `org.robovm.apple.imageio.CGImageSourceOptions#getTypeIdentifierHint()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public getTypeIdentifierHint() : String in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `5`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldCache()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldCache() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

id: `6`\
source `org.robovm.apple.imageio.CGImageSourceOptions#shouldAllowFloat()`\
target: `org.robovm.apple.imageio.CGImageSourceOptions#has(CFString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key CFString) : boolean extracted from public shouldAllowFloat() : boolean in class org.robovm.apple.imageio.CGImageSourceOptions`

