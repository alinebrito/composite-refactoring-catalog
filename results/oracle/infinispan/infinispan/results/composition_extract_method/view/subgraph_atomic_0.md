<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.interceptors.distribution.VersionedDistributionInterceptor#prepareOnAffectedNodes(TxInvocationContext<?>,PrepareCommand,Collection<Address>,boolean)`\
target: `org.infinispan.interceptors.distribution.TxDistributionInterceptor#createPrepareRpcOptions()`\
type: `EXTRACT_MOVE`\
commit: [ce4f6292d](https://github.com/infinispan/infinispan/commit/ce4f6292d6350a2c6b82d995352fdf6d07042c9c)\
description: `Extract And Move Method protected createPrepareRpcOptions() : RpcOptions extracted from protected prepareOnAffectedNodes(ctx TxInvocationContext<?>, command PrepareCommand, recipients Collection<Address>, ignored boolean) : void in class org.infinispan.interceptors.distribution.VersionedDistributionInterceptor & moved to class org.infinispan.interceptors.distribution.TxDistributionInterceptor`

id: `1`\
source `org.infinispan.interceptors.distribution.TxDistributionInterceptor#prepareOnAffectedNodes(TxInvocationContext<?>,PrepareCommand,Collection<Address>,boolean)`\
target: `org.infinispan.interceptors.distribution.TxDistributionInterceptor#createPrepareRpcOptions()`\
type: `EXTRACT`\
commit: [ce4f6292d](https://github.com/infinispan/infinispan/commit/ce4f6292d6350a2c6b82d995352fdf6d07042c9c)\
description: `Extract Method protected createPrepareRpcOptions() : RpcOptions extracted from protected prepareOnAffectedNodes(ctx TxInvocationContext<?>, command PrepareCommand, recipients Collection<Address>, sync boolean) : void in class org.infinispan.interceptors.distribution.TxDistributionInterceptor`

