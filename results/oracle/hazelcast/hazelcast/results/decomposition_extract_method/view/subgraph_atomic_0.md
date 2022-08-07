<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderConnection()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderConnection() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `1`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderThread()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderThread() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `2`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderOperationService()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderOperationService() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `3`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderEvents()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderEvents() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `4`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderNativeMemory()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderNativeMemory() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `5`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderHeap()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderHeap() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `6`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderClient()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderClient() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `7`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderPhysicalMemory()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderPhysicalMemory() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `8`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderProcessors()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderProcessors() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `9`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderSwap()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderSwap() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `10`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderCluster()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderCluster() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `11`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderExecutors()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderExecutors() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `12`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderProxy()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderProxy() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `13`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderGc()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderGc() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

id: `14`\
source `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#toString()`\
target: `com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics#renderLoad()`\
type: `EXTRACT`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Extract Method private renderLoad() : void extracted from public toString() : String in class com.hazelcast.internal.monitors.HealthMonitor.HealthMetrics`

