<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.interceptors.distribution.TxDistributionInterceptor#lockAndWrap(InvocationContext,Object,InternalCacheEntry,FlagAffectedCommand)`\
target: `org.infinispan.interceptors.distribution.TxDistributionInterceptor#localGet(InvocationContext,Object,boolean,FlagAffectedCommand,boolean)`\
type: `INLINE`\
commit: [ce4f6292d](https://github.com/infinispan/infinispan/commit/ce4f6292d6350a2c6b82d995352fdf6d07042c9c)\
description: `Inline Method protected lockAndWrap(ctx InvocationContext, key Object, ice InternalCacheEntry, command FlagAffectedCommand) : void inlined to private localGet(ctx InvocationContext, key Object, isWrite boolean, command FlagAffectedCommand, isGetCacheEntry boolean) : Object in class org.infinispan.interceptors.distribution.TxDistributionInterceptor`

id: `1`\
source `org.infinispan.interceptors.distribution.TxDistributionInterceptor#lockAndWrap(InvocationContext,Object,InternalCacheEntry,FlagAffectedCommand)`\
target: `org.infinispan.interceptors.distribution.TxDistributionInterceptor#remoteGet(InvocationContext,Object,boolean,FlagAffectedCommand)`\
type: `INLINE`\
commit: [ce4f6292d](https://github.com/infinispan/infinispan/commit/ce4f6292d6350a2c6b82d995352fdf6d07042c9c)\
description: `Inline Method protected lockAndWrap(ctx InvocationContext, key Object, ice InternalCacheEntry, command FlagAffectedCommand) : void inlined to private remoteGet(ctx InvocationContext, key Object, isWrite boolean, command FlagAffectedCommand) : InternalCacheEntry in class org.infinispan.interceptors.distribution.TxDistributionInterceptor`

