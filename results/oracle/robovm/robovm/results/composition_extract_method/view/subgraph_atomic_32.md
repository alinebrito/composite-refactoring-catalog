<img src=subgraph_atomic_32.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#setShowPowerAlert(boolean)`\
target: `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBPeripheralManagerOptions extracted from public setShowPowerAlert(showAlert boolean) : CBPeripheralManagerOptions in class org.robovm.apple.corebluetooth.CBPeripheralManagerOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#setRestoreIdentifier(String)`\
target: `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBPeripheralManagerOptions extracted from public setRestoreIdentifier(identifier String) : CBPeripheralManagerOptions in class org.robovm.apple.corebluetooth.CBPeripheralManagerOptions`

