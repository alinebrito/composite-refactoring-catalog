<img src=subgraph_atomic_50.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#isShowingPowerAlert()`\
target: `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public isShowingPowerAlert() : boolean in class org.robovm.apple.corebluetooth.CBPeripheralManagerOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#getRestoreIdentifier()`\
target: `org.robovm.apple.corebluetooth.CBPeripheralManagerOptions#get(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public get(key NSString) : NSObject extracted from public getRestoreIdentifier() : String in class org.robovm.apple.corebluetooth.CBPeripheralManagerOptions`
