<img src=subgraph_atomic_49.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#isAllowingDuplicates()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public isAllowingDuplicates() : boolean in class org.robovm.apple.corebluetooth.CBCentralManagerScanOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#getSolicitedServiceUUIDs()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getSolicitedServiceUUIDs() : NSArray<CBUUID> in class org.robovm.apple.corebluetooth.CBCentralManagerScanOptions`
