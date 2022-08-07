<img src=subgraph_atomic_26.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.imageio.CGImageProperties#setGIFData(CGImagePropertyGIFData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setGIFData(metadata CGImagePropertyGIFData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `1`\
source `org.robovm.apple.imageio.CGImageProperties#setDepth(int)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setDepth(depth int) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `2`\
source `org.robovm.apple.imageio.CGImageProperties#setExifAuxData(CGImagePropertyExifAuxData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setExifAuxData(metadata CGImagePropertyExifAuxData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `3`\
source `org.robovm.apple.imageio.CGImageProperties#setHasAlphaChannel(boolean)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setHasAlphaChannel(alphaChannel boolean) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `4`\
source `org.robovm.apple.imageio.CGImageProperties#setMakerMinoltaData(CFDictionary)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setMakerMinoltaData(metadata CFDictionary) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `5`\
source `org.robovm.apple.imageio.CGImageProperties#setMakerOlympusData(CFDictionary)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setMakerOlympusData(metadata CFDictionary) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `6`\
source `org.robovm.apple.imageio.CGImageProperties#setCIFFData(CGImagePropertyCIFFData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setCIFFData(metadata CGImagePropertyCIFFData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `7`\
source `org.robovm.apple.imageio.CGImageProperties#setColorModel(CGImagePropertyColorModel)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setColorModel(colorModel CGImagePropertyColorModel) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `8`\
source `org.robovm.apple.imageio.CGImageProperties#set8BIMData(CGImageProperty8BIMData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public set8BIMData(metadata CGImageProperty8BIMData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `9`\
source `org.robovm.apple.imageio.CGImageProperties#setDPIWidth(long)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setDPIWidth(dpi long) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `10`\
source `org.robovm.apple.imageio.CGImageProperties#setIPTCData(CGImagePropertyIPTCData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setIPTCData(metadata CGImagePropertyIPTCData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `11`\
source `org.robovm.apple.imageio.CGImageProperties#setMakerFujiData(CFDictionary)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setMakerFujiData(metadata CFDictionary) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `12`\
source `org.robovm.apple.imageio.CGImageProperties#setGPSData(CGImagePropertyGPSData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setGPSData(metadata CGImagePropertyGPSData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `13`\
source `org.robovm.apple.imageio.CGImageProperties#setIndexed(boolean)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setIndexed(isIndexed boolean) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `14`\
source `org.robovm.apple.imageio.CGImageProperties#setContainsFloatingPointPixels(boolean)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setContainsFloatingPointPixels(isFloat boolean) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `15`\
source `org.robovm.apple.imageio.CGImageProperties#setMakerNikonData(CGImagePropertyNikonData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setMakerNikonData(metadata CGImagePropertyNikonData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `16`\
source `org.robovm.apple.imageio.CGImageProperties#setRawData(CFDictionary)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setRawData(metadata CFDictionary) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `17`\
source `org.robovm.apple.imageio.CGImageProperties#setMakerPentaxData(CFDictionary)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setMakerPentaxData(metadata CFDictionary) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `18`\
source `org.robovm.apple.imageio.CGImageProperties#setJFIFData(CGImagePropertyJFIFData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setJFIFData(metadata CGImagePropertyJFIFData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `19`\
source `org.robovm.apple.imageio.CGImageProperties#setFileSize(long)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setFileSize(fileSize long) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `20`\
source `org.robovm.apple.imageio.CGImageProperties#setTIFFData(CGImagePropertyTIFFData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setTIFFData(metadata CGImagePropertyTIFFData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `21`\
source `org.robovm.apple.imageio.CGImageProperties#setDNGData(CGImagePropertyDNGData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setDNGData(metadata CGImagePropertyDNGData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `22`\
source `org.robovm.apple.imageio.CGImageProperties#setDPIHeight(long)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setDPIHeight(dpi long) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `23`\
source `org.robovm.apple.imageio.CGImageProperties#setOrientation(CGImagePropertyOrientation)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setOrientation(orientation CGImagePropertyOrientation) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `24`\
source `org.robovm.apple.imageio.CGImageProperties#setICCProfile(String)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setICCProfile(profile String) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `25`\
source `org.robovm.apple.imageio.CGImageProperties#setPNGData(CGImagePropertyPNGData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setPNGData(metadata CGImagePropertyPNGData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `26`\
source `org.robovm.apple.imageio.CGImageProperties#setExifData(CGImagePropertyExifData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setExifData(metadata CGImagePropertyExifData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `27`\
source `org.robovm.apple.imageio.CGImageProperties#setMakerCanonData(CGImagePropertyCanonData)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setMakerCanonData(metadata CGImagePropertyCanonData) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `28`\
source `org.robovm.apple.imageio.CGImageProperties#setPixelHeight(long)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setPixelHeight(height long) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

id: `29`\
source `org.robovm.apple.imageio.CGImageProperties#setPixelWidth(long)`\
target: `org.robovm.apple.imageio.CGImageProperties#set(CFString,NativeObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key CFString, value NativeObject) : CGImageProperties extracted from public setPixelWidth(width long) : CGImageProperties in class org.robovm.apple.imageio.CGImageProperties`

