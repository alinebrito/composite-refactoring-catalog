<img src=subgraph_atomic_48.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getOverflowServiceUUIDs()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getOverflowServiceUUIDs() : NSArray<CBUUID> in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `1`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#isConnectable()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public isConnectable() : boolean in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `2`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getSolicitedServiceUUIDs()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getSolicitedServiceUUIDs() : NSArray<CBUUID> in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `3`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getLocalName()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getLocalName() : String in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `4`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getTxPowerLevel()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getTxPowerLevel() : double in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `5`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getManufacturerData()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getManufacturerData() : NSData in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `6`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getServiceUUIDs()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getServiceUUIDs() : NSArray<CBUUID> in class org.robovm.apple.corebluetooth.CBAdvertisementData`

