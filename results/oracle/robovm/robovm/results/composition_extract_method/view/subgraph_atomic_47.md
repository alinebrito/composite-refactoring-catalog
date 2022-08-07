<img src=subgraph_atomic_47.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageProperties#getDNGData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getDNGData() : CGImagePropertyDNGData in class org.robovm.apple.imageio.CGImageProperties`

id: `1`\
source `org.robovm.apple.imageio.CGImageProperties#hasAlphaChannel()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public hasAlphaChannel() : boolean in class org.robovm.apple.imageio.CGImageProperties`

id: `2`\
source `org.robovm.apple.imageio.CGImageProperties#getMakerPentaxData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getMakerPentaxData() : CFDictionary in class org.robovm.apple.imageio.CGImageProperties`

id: `3`\
source `org.robovm.apple.imageio.CGImageProperties#getIPTCData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getIPTCData() : CGImagePropertyIPTCData in class org.robovm.apple.imageio.CGImageProperties`

id: `4`\
source `org.robovm.apple.imageio.CGImageProperties#getRawData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getRawData() : CFDictionary in class org.robovm.apple.imageio.CGImageProperties`

id: `5`\
source `org.robovm.apple.imageio.CGImageProperties#getICCProfile()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getICCProfile() : String in class org.robovm.apple.imageio.CGImageProperties`

id: `6`\
source `org.robovm.apple.imageio.CGImageProperties#getPNGData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getPNGData() : CGImagePropertyPNGData in class org.robovm.apple.imageio.CGImageProperties`

id: `7`\
source `org.robovm.apple.imageio.CGImageProperties#getGIFData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getGIFData() : CGImagePropertyGIFData in class org.robovm.apple.imageio.CGImageProperties`

id: `8`\
source `org.robovm.apple.imageio.CGImageProperties#getMakerOlympusData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getMakerOlympusData() : CFDictionary in class org.robovm.apple.imageio.CGImageProperties`

id: `9`\
source `org.robovm.apple.imageio.CGImageProperties#getExifData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getExifData() : CGImagePropertyExifData in class org.robovm.apple.imageio.CGImageProperties`

id: `10`\
source `org.robovm.apple.imageio.CGImageProperties#get8BIMData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public get8BIMData() : CGImageProperty8BIMData in class org.robovm.apple.imageio.CGImageProperties`

id: `11`\
source `org.robovm.apple.imageio.CGImageProperties#getDPIHeight()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getDPIHeight() : long in class org.robovm.apple.imageio.CGImageProperties`

id: `12`\
source `org.robovm.apple.imageio.CGImageProperties#getMakerFujiData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getMakerFujiData() : CFDictionary in class org.robovm.apple.imageio.CGImageProperties`

id: `13`\
source `org.robovm.apple.imageio.CGImageProperties#getPixelHeight()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getPixelHeight() : long in class org.robovm.apple.imageio.CGImageProperties`

id: `14`\
source `org.robovm.apple.imageio.CGImageProperties#getDepth()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getDepth() : int in class org.robovm.apple.imageio.CGImageProperties`

id: `15`\
source `org.robovm.apple.imageio.CGImageProperties#getGPSData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getGPSData() : CGImagePropertyGPSData in class org.robovm.apple.imageio.CGImageProperties`

id: `16`\
source `org.robovm.apple.imageio.CGImageProperties#getMakerCanonData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getMakerCanonData() : CGImagePropertyCanonData in class org.robovm.apple.imageio.CGImageProperties`

id: `17`\
source `org.robovm.apple.imageio.CGImageProperties#getDPIWidth()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getDPIWidth() : long in class org.robovm.apple.imageio.CGImageProperties`

id: `18`\
source `org.robovm.apple.imageio.CGImageProperties#isContainingFloatingPointPixels()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public isContainingFloatingPointPixels() : boolean in class org.robovm.apple.imageio.CGImageProperties`

id: `19`\
source `org.robovm.apple.imageio.CGImageProperties#getCIFFData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getCIFFData() : CGImagePropertyCIFFData in class org.robovm.apple.imageio.CGImageProperties`

id: `20`\
source `org.robovm.apple.imageio.CGImageProperties#getTIFFData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getTIFFData() : CGImagePropertyTIFFData in class org.robovm.apple.imageio.CGImageProperties`

id: `21`\
source `org.robovm.apple.imageio.CGImageProperties#getMakerMinoltaData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getMakerMinoltaData() : CFDictionary in class org.robovm.apple.imageio.CGImageProperties`

id: `22`\
source `org.robovm.apple.imageio.CGImageProperties#getPixelWidth()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getPixelWidth() : long in class org.robovm.apple.imageio.CGImageProperties`

id: `23`\
source `org.robovm.apple.imageio.CGImageProperties#getExifAuxData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getExifAuxData() : CGImagePropertyExifAuxData in class org.robovm.apple.imageio.CGImageProperties`

id: `24`\
source `org.robovm.apple.imageio.CGImageProperties#getJFIFData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getJFIFData() : CGImagePropertyJFIFData in class org.robovm.apple.imageio.CGImageProperties`

id: `25`\
source `org.robovm.apple.imageio.CGImageProperties#isIndexed()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public isIndexed() : boolean in class org.robovm.apple.imageio.CGImageProperties`

id: `26`\
source `org.robovm.apple.imageio.CGImageProperties#getColorModel()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getColorModel() : CGImagePropertyColorModel in class org.robovm.apple.imageio.CGImageProperties`

id: `27`\
source `org.robovm.apple.imageio.CGImageProperties#getFileSize()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getFileSize() : long in class org.robovm.apple.imageio.CGImageProperties`

id: `28`\
source `org.robovm.apple.imageio.CGImageProperties#getOrientation()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getOrientation() : CGImagePropertyOrientation in class org.robovm.apple.imageio.CGImageProperties`

id: `29`\
source `org.robovm.apple.imageio.CGImageProperties#getMakerNikonData()`\
target: `org.robovm.apple.imageio.CGImageProperties#get(CFString,Class<T>)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key CFString, type Class<T>) : T extracted from public getMakerNikonData() : CGImagePropertyNikonData in class org.robovm.apple.imageio.CGImageProperties`

