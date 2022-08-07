<img src=subgraph_atomic_54.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getTxPowerLevel()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public getTxPowerLevel() : double in class org.robovm.apple.corebluetooth.CBAdvertisementData`

id: `1`\
source `org.robovm.apple.corebluetooth.CBAdvertisementData#getTxPowerLevel()`\
target: `org.robovm.apple.corebluetooth.CBAdvertisementData#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getTxPowerLevel() : double in class org.robovm.apple.corebluetooth.CBAdvertisementData`

