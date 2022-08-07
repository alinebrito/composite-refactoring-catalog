<img src=subgraph_atomic_37.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImagePropertyExifAuxData#getNumber(CGImagePropertyExifAux)`\
target: `org.robovm.apple.imageio.CGImagePropertyExifAuxData#get(CGImagePropertyExifAux,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyExifAux, type Class<T>) : T extracted from public getNumber(property CGImagePropertyExifAux) : double in class org.robovm.apple.imageio.CGImagePropertyExifAuxData`

id: `1`\
source `org.robovm.apple.imageio.CGImagePropertyExifAuxData#getString(CGImagePropertyExifAux)`\
target: `org.robovm.apple.imageio.CGImagePropertyExifAuxData#get(CGImagePropertyExifAux,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CGImagePropertyExifAux, type Class<T>) : T extracted from public getString(property CGImagePropertyExifAux) : String in class org.robovm.apple.imageio.CGImagePropertyExifAuxData`

