<img src=subgraph_atomic_6.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBCentralManagerRestoredState#getPeripherals()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerRestoredState#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public getPeripherals() : NSArray<CBPeripheral> in class org.robovm.apple.corebluetooth.CBCentralManagerRestoredState`

id: `1`\
source `org.robovm.apple.corebluetooth.CBCentralManagerRestoredState#getScanOptions()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerRestoredState#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public getScanOptions() : CBCentralManagerScanOptions in class org.robovm.apple.corebluetooth.CBCentralManagerRestoredState`

id: `2`\
source `org.robovm.apple.corebluetooth.CBCentralManagerRestoredState#getScanServices()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerRestoredState#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public getScanServices() : NSArray<CBUUID> in class org.robovm.apple.corebluetooth.CBCentralManagerRestoredState`

