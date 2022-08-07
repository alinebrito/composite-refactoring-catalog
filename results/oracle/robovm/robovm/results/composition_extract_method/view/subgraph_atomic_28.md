<img src=subgraph_atomic_28.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#setAllowsDuplicates(boolean)`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBCentralManagerScanOptions extracted from public setAllowsDuplicates(allowDuplicates boolean) : CBCentralManagerScanOptions in class org.robovm.apple.corebluetooth.CBCentralManagerScanOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#setSolicitedServiceUUIDs(NSArray<CBUUID>)`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerScanOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBCentralManagerScanOptions extracted from public setSolicitedServiceUUIDs(uuids NSArray<CBUUID>) : CBCentralManagerScanOptions in class org.robovm.apple.corebluetooth.CBCentralManagerScanOptions`

