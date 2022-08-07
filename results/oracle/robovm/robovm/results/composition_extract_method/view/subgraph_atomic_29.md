<img src=subgraph_atomic_29.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#setNotifyOnConnection(boolean)`\
target: `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBConnectPeripheralOptions extracted from public setNotifyOnConnection(notify boolean) : CBConnectPeripheralOptions in class org.robovm.apple.corebluetooth.CBConnectPeripheralOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#setNotifyOnNotification(boolean)`\
target: `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBConnectPeripheralOptions extracted from public setNotifyOnNotification(notify boolean) : CBConnectPeripheralOptions in class org.robovm.apple.corebluetooth.CBConnectPeripheralOptions`

id: `2`\
source `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#setNotifyOnDisconnection(boolean)`\
target: `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#set(NSString,NSObject)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public set(key NSString, value NSObject) : CBConnectPeripheralOptions extracted from public setNotifyOnDisconnection(notify boolean) : CBConnectPeripheralOptions in class org.robovm.apple.corebluetooth.CBConnectPeripheralOptions`

