<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.hazelcast.spi.impl.operationservice.impl.InvocationNetworkSplitTest#testWaitNotifyService_whenNodeSplitFromCluster(SplitAction)`\
target: `com.hazelcast.spi.impl.operationservice.impl.InvocationNetworkSplitTest#createConfig()`\
type: `EXTRACT`\
commit: [204bf49cb](https://github.com/hazelcast/hazelcast/commit/204bf49cba03fe5d581a35ff82dd22587a681f46)\
description: `Extract Method private createConfig() : Config extracted from private testWaitNotifyService_whenNodeSplitFromCluster(action SplitAction) : void in class com.hazelcast.spi.impl.operationservice.impl.InvocationNetworkSplitTest`

id: `1`\
source `com.hazelcast.spi.impl.operationservice.impl.InvocationNetworkSplitTest#testWaitingInvocations_whenNodeSplitFromCluster(SplitAction)`\
target: `com.hazelcast.spi.impl.operationservice.impl.InvocationNetworkSplitTest#createConfig()`\
type: `EXTRACT`\
commit: [204bf49cb](https://github.com/hazelcast/hazelcast/commit/204bf49cba03fe5d581a35ff82dd22587a681f46)\
description: `Extract Method private createConfig() : Config extracted from private testWaitingInvocations_whenNodeSplitFromCluster(splitAction SplitAction) : void in class com.hazelcast.spi.impl.operationservice.impl.InvocationNetworkSplitTest`

