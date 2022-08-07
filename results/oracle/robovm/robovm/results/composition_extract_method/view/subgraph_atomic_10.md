<img src=subgraph_atomic_10.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#isNotifyingOnConnection()`\
target: `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public isNotifyingOnConnection() : boolean in class org.robovm.apple.corebluetooth.CBConnectPeripheralOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#isNotifyingOnDisconnection()`\
target: `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public isNotifyingOnDisconnection() : boolean in class org.robovm.apple.corebluetooth.CBConnectPeripheralOptions`

id: `2`\
source `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#isNotifyingOnNotification()`\
target: `org.robovm.apple.corebluetooth.CBConnectPeripheralOptions#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public isNotifyingOnNotification() : boolean in class org.robovm.apple.corebluetooth.CBConnectPeripheralOptions`

