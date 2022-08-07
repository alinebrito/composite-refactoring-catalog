<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#internalEdgeDisconnect(int,long,int,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method package internalEdgeDisconnect(edgeToRemove int, edgeToUpdatePointer long, baseNode int, adjNode int) : long from class com.graphhopper.storage.GraphHopperStorage to package internalEdgeDisconnect(edgeToRemove int, edgeToUpdatePointer long, baseNode int, adjNode int) : long from class com.graphhopper.storage.BaseGraph`

id: `1`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#getDebugInfo(int,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method public getDebugInfo(node int, area int) : String from class com.graphhopper.storage.GraphHopperStorage to public getDebugInfo(node int, area int) : String from class com.graphhopper.storage.BaseGraph`

id: `2`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#createSingleEdge(int,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected createSingleEdge(edgeId int, nodeId int) : SingleEdge from class com.graphhopper.storage.GraphHopperStorage to protected createSingleEdge(edgeId int, nodeId int) : SingleEdge from class com.graphhopper.storage.BaseGraph`

id: `3`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#getDist(long)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private getDist(pointer long) : double from class com.graphhopper.storage.GraphHopperStorage to private getDist(pointer long) : double from class com.graphhopper.storage.BaseGraph`

id: `4`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#setNodesHeader()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected setNodesHeader() : int from class com.graphhopper.storage.GraphHopperStorage to protected setNodesHeader() : int from class com.graphhopper.storage.BaseGraph`

id: `5`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#loadNodesHeader()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected loadNodesHeader() : int from class com.graphhopper.storage.GraphHopperStorage to protected loadNodesHeader() : int from class com.graphhopper.storage.BaseGraph`

id: `6`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#nextEdge()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private nextEdge() : int from class com.graphhopper.storage.GraphHopperStorage to private nextEdge() : int from class com.graphhopper.storage.BaseGraph`

id: `7`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#initStorage()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected initStorage() : void from class com.graphhopper.storage.GraphHopperStorage to package initStorage() : void from class com.graphhopper.storage.BaseGraph`

id: `8`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#ensureEdgeIndex(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private ensureEdgeIndex(edgeIndex int) : void from class com.graphhopper.storage.GraphHopperStorage to private ensureEdgeIndex(edgeIndex int) : void from class com.graphhopper.storage.BaseGraph`

id: `9`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#ensureGeometry(long,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private ensureGeometry(bytePos long, byteLength int) : void from class com.graphhopper.storage.GraphHopperStorage to private ensureGeometry(bytePos long, byteLength int) : void from class com.graphhopper.storage.BaseGraph`

id: `10`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#setEdgesHeader()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected setEdgesHeader() : int from class com.graphhopper.storage.GraphHopperStorage to protected setEdgesHeader() : int from class com.graphhopper.storage.BaseGraph`

id: `11`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#nextGeoRef(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private nextGeoRef(arrayLength int) : int from class com.graphhopper.storage.GraphHopperStorage to private nextGeoRef(arrayLength int) : int from class com.graphhopper.storage.BaseGraph`

id: `12`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#setEdgeCount(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method package setEdgeCount(cnt int) : void from class com.graphhopper.storage.GraphHopperStorage to package setEdgeCount(cnt int) : void from class com.graphhopper.storage.BaseGraph`

id: `13`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#connectNewEdge(int,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private connectNewEdge(fromNode int, newOrExistingEdge int) : void from class com.graphhopper.storage.GraphHopperStorage to private connectNewEdge(fromNode int, newOrExistingEdge int) : void from class com.graphhopper.storage.BaseGraph`

id: `14`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#inPlaceNodeRemove(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private inPlaceNodeRemove(removeNodeCount int) : void from class com.graphhopper.storage.GraphHopperStorage to package inPlaceNodeRemove(removeNodeCount int) : void from class com.graphhopper.storage.BaseGraph`

id: `15`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#setWayGeometryHeader()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected setWayGeometryHeader() : int from class com.graphhopper.storage.GraphHopperStorage to protected setWayGeometryHeader() : int from class com.graphhopper.storage.BaseGraph`

id: `16`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#initNodeAndEdgeEntrySize()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected initNodeAndEdgeEntrySize() : void from class com.graphhopper.storage.GraphHopperStorage to protected initNodeAndEdgeEntrySize() : void from class com.graphhopper.storage.BaseGraph`

id: `17`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#getOtherNode(int,long)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private getOtherNode(nodeThis int, edgePointer long) : int from class com.graphhopper.storage.GraphHopperStorage to private getOtherNode(nodeThis int, edgePointer long) : int from class com.graphhopper.storage.BaseGraph`

id: `18`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#initNodeRefs(long,long)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private initNodeRefs(oldCapacity long, newCapacity long) : void from class com.graphhopper.storage.GraphHopperStorage to package initNodeRefs(oldCapacity long, newCapacity long) : void from class com.graphhopper.storage.BaseGraph`

id: `19`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#checkInit()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method package checkInit() : void from class com.graphhopper.storage.GraphHopperStorage to package checkInit() : void from class com.graphhopper.storage.BaseGraph`

id: `20`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#invalidateEdge(long)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private invalidateEdge(edgePointer long) : void from class com.graphhopper.storage.GraphHopperStorage to private invalidateEdge(edgePointer long) : void from class com.graphhopper.storage.BaseGraph`

id: `21`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#copyProperties(EdgeIteratorState,EdgeIteratorState)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method package copyProperties(from EdgeIteratorState, to EdgeIteratorState) : EdgeIteratorState from class com.graphhopper.storage.GraphHopperStorage to package copyProperties(from EdgeIteratorState, to EdgeIteratorState) : EdgeIteratorState from class com.graphhopper.storage.BaseGraph`

id: `22`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#getLinkPosInEdgeArea(int,int,long)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected getLinkPosInEdgeArea(nodeThis int, nodeOther int, edgePointer long) : long from class com.graphhopper.storage.GraphHopperStorage to protected getLinkPosInEdgeArea(nodeThis int, nodeOther int, edgePointer long) : long from class com.graphhopper.storage.BaseGraph`

id: `23`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#writeEdge(int,int,int,int,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private writeEdge(edge int, nodeThis int, nodeOther int, nextEdge int, nextEdgeOther int) : long from class com.graphhopper.storage.GraphHopperStorage to private writeEdge(edge int, nodeThis int, nodeOther int, nextEdge int, nextEdgeOther int) : long from class com.graphhopper.storage.BaseGraph`

id: `24`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#distToInt(double)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private distToInt(distance double) : int from class com.graphhopper.storage.GraphHopperStorage to private distToInt(distance double) : int from class com.graphhopper.storage.BaseGraph`

id: `25`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#getRemovedNodes()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private getRemovedNodes() : GHBitSet from class com.graphhopper.storage.GraphHopperStorage to package getRemovedNodes() : GHBitSet from class com.graphhopper.storage.BaseGraph`

id: `26`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#loadEdgesHeader()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected loadEdgesHeader() : int from class com.graphhopper.storage.GraphHopperStorage to protected loadEdgesHeader() : int from class com.graphhopper.storage.BaseGraph`

id: `27`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#isTestingEnabled()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private isTestingEnabled() : boolean from class com.graphhopper.storage.GraphHopperStorage to private isTestingEnabled() : boolean from class com.graphhopper.storage.BaseGraph`

id: `28`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#nextNodeEntryIndex(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected nextNodeEntryIndex(sizeInBytes int) : int from class com.graphhopper.storage.GraphHopperStorage to protected nextNodeEntryIndex(sizeInBytes int) : int from class com.graphhopper.storage.BaseGraph`

id: `29`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#trimToSize()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private trimToSize() : void from class com.graphhopper.storage.GraphHopperStorage to protected trimToSize() : void from class com.graphhopper.storage.BaseGraph`

id: `30`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#internalEdgeAdd(int,int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method package internalEdgeAdd(fromNodeId int, toNodeId int) : int from class com.graphhopper.storage.GraphHopperStorage to package internalEdgeAdd(fromNodeId int, toNodeId int) : int from class com.graphhopper.storage.BaseGraph`

id: `31`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#nextEdgeEntryIndex(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected nextEdgeEntryIndex(sizeInBytes int) : int from class com.graphhopper.storage.GraphHopperStorage to protected nextEdgeEntryIndex(sizeInBytes int) : int from class com.graphhopper.storage.BaseGraph`

id: `32`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#stringHashCode(String)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method private stringHashCode(str String) : int from class com.graphhopper.storage.GraphHopperStorage to private stringHashCode(str String) : int from class com.graphhopper.storage.BaseGraph`

id: `33`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#loadWayGeometryHeader()`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method protected loadWayGeometryHeader() : int from class com.graphhopper.storage.GraphHopperStorage to protected loadWayGeometryHeader() : int from class com.graphhopper.storage.BaseGraph`

id: `34`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#ensureNodeIndex(int)`\
type: `MOVE`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move Method package ensureNodeIndex(nodeIndex int) : void from class com.graphhopper.storage.GraphHopperStorage to package ensureNodeIndex(nodeIndex int) : void from class com.graphhopper.storage.BaseGraph`

id: `35`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#getFlags_(InternalGraphPropertyAccess,long,boolean)`\
type: `MOVE_RENAME`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move And Rename Method private getFlags(edgePointer long, reverse boolean) : long from class com.graphhopper.storage.GraphHopperStorage to package getFlags_(tmpPropAccess InternalGraphPropertyAccess, edgePointer long, reverse boolean) : long from class com.graphhopper.storage.BaseGraph`

id: `36`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#setFlags_(InternalGraphPropertyAccess,long,boolean,long)`\
type: `MOVE_RENAME`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move And Rename Method private setFlags(edgePointer long, reverse boolean, flags long) : void from class com.graphhopper.storage.GraphHopperStorage to package setFlags_(tmpPropAccess InternalGraphPropertyAccess, edgePointer long, reverse boolean, flags long) : void from class com.graphhopper.storage.BaseGraph`

id: `37`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#setWayGeometry_(PointList,long,boolean)`\
type: `MOVE_RENAME`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move And Rename Method private setWayGeometry(pillarNodes PointList, edgePointer long, reverse boolean) : void from class com.graphhopper.storage.GraphHopperStorage to private setWayGeometry_(pillarNodes PointList, edgePointer long, reverse boolean) : void from class com.graphhopper.storage.BaseGraph`

id: `38`\
source `com.graphhopper.storage.GraphHopperStorage`\
target: `com.graphhopper.storage.BaseGraph#fetchWayGeometry_(long,boolean,int,int,int)`\
type: `MOVE_RENAME`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Move And Rename Method private fetchWayGeometry(edgePointer long, reverse boolean, mode int, baseNode int, adjNode int) : PointList from class com.graphhopper.storage.GraphHopperStorage to private fetchWayGeometry_(edgePointer long, reverse boolean, mode int, baseNode int, adjNode int) : PointList from class com.graphhopper.storage.BaseGraph`

