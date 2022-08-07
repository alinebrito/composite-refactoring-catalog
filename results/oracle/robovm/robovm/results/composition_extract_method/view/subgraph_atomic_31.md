<img src=subgraph_atomic_31.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBCentralManagerOptions#setRestoreIdentifier(String)`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBCentralManagerOptions extracted from public setRestoreIdentifier(identifier String) : CBCentralManagerOptions in class org.robovm.apple.corebluetooth.CBCentralManagerOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBCentralManagerOptions#setShowPowerAlert(boolean)`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBCentralManagerOptions extracted from public setShowPowerAlert(showAlert boolean) : CBCentralManagerOptions in class org.robovm.apple.corebluetooth.CBCentralManagerOptions`

