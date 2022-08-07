<img src=subgraph_atomic_7.svg width=25%>

## Refactorings:

id: `0`\
source `org.robovm.apple.corebluetooth.CBCentralManagerOptions#getRestoreIdentifier()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerOptions#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public getRestoreIdentifier() : String in class org.robovm.apple.corebluetooth.CBCentralManagerOptions`

id: `1`\
source `org.robovm.apple.corebluetooth.CBCentralManagerOptions#isShowingPowerAlert()`\
target: `org.robovm.apple.corebluetooth.CBCentralManagerOptions#has(NSString)`\
type: `EXTRACT`\
commit: [bf5ee44b3](https://github.com/robovm/robovm/commit/bf5ee44b3b576e01ab09cae9f50300417b01dc07)\
description: `Extract Method public has(key NSString) : boolean extracted from public isShowingPowerAlert() : boolean in class org.robovm.apple.corebluetooth.CBCentralManagerOptions`

