<img src=subgraph_atomic_47.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBPeripheralManagerRestoredState#getAdvertisementData()`\
target: `org.robovm.apple.corebluetooth.CBPeripheralManagerRestoredState#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public getAdvertisementData() : CBAdvertisementData in class org.robovm.apple.corebluetooth.CBPeripheralManagerRestoredState`

id: `1`\
source `org.robovm.apple.corebluetooth.CBPeripheralManagerRestoredState#getAdvertisementData()`\
target: `org.robovm.apple.corebluetooth.CBPeripheralManagerRestoredState#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getAdvertisementData() : CBAdvertisementData in class org.robovm.apple.corebluetooth.CBPeripheralManagerRestoredState`

