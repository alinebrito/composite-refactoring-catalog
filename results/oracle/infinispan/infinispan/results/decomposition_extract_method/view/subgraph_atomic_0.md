<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.stream.impl.DistributedCacheStream#remoteIterator()`\
target: `org.infinispan.stream.impl.DistributedCacheStream#rehashAwareIteration(AtomicBoolean,Consumer<R>,IteratorSupplier<R>,boolean)`\
type: `EXTRACT`\
commit: [043030723](https://github.com/infinispan/infinispan/commit/043030723632627b0908dca6b24dae91d3dfd938)\
description: `Extract Method private rehashAwareIteration(complete AtomicBoolean, consumer Consumer<R>, supplier IteratorSupplier<R>, iteratorParallelDistribute boolean) : void extracted from package remoteIterator() : Iterator<R> in class org.infinispan.stream.impl.DistributedCacheStream`

id: `1`\
source `org.infinispan.stream.impl.DistributedCacheStream#remoteIterator()`\
target: `org.infinispan.stream.impl.DistributedCacheStream#ignoreRehashIteration(Consumer<R>,IteratorSupplier<R>,boolean)`\
type: `EXTRACT`\
commit: [043030723](https://github.com/infinispan/infinispan/commit/043030723632627b0908dca6b24dae91d3dfd938)\
description: `Extract Method private ignoreRehashIteration(consumer Consumer<R>, supplier IteratorSupplier<R>, iteratorParallelDistribute boolean) : void extracted from package remoteIterator() : Iterator<R> in class org.infinispan.stream.impl.DistributedCacheStream`

id: `2`\
source `org.infinispan.stream.impl.DistributedCacheStream#remoteIterator()`\
target: `org.infinispan.stream.impl.DistributedCacheStream#segmentsToProcess(IteratorSupplier<R>,KeyTrackingConsumer<Object,R>,Set<Integer>,UUID)`\
type: `EXTRACT`\
commit: [043030723](https://github.com/infinispan/infinispan/commit/043030723632627b0908dca6b24dae91d3dfd938)\
description: `Extract Method private segmentsToProcess(supplier IteratorSupplier<R>, results KeyTrackingConsumer<Object,R>, segmentsToProcess Set<Integer>, id UUID) : Set<Integer> extracted from package remoteIterator() : Iterator<R> in class org.infinispan.stream.impl.DistributedCacheStream`

id: `3`\
source `org.infinispan.stream.impl.DistributedCacheStream#remoteIterator()`\
target: `org.infinispan.stream.impl.DistributedCacheStream#performLocalRehashAwareOperation(KeyTrackingConsumer<Object,R>,Set<Integer>,ConsistentHash,Set<Integer>,KeyTrackingTerminalOperation<Object,R,Object>,Supplier<Set<Integer>>,UUID)`\
type: `EXTRACT`\
commit: [043030723](https://github.com/infinispan/infinispan/commit/043030723632627b0908dca6b24dae91d3dfd938)\
description: `Extract Method private performLocalRehashAwareOperation(results KeyTrackingConsumer<Object,R>, segmentsToProcess Set<Integer>, ch ConsistentHash, segments Set<Integer>, op KeyTrackingTerminalOperation<Object,R,Object>, ownedSegmentsSupplier Supplier<Set<Integer>>, id UUID) : void extracted from package remoteIterator() : Iterator<R> in class org.infinispan.stream.impl.DistributedCacheStream`

