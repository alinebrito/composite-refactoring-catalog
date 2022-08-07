<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.graphhopper.routing.AbstractRoutingAlgorithmTester#testTwoWeightsPerEdge2()`\
target: `com.graphhopper.routing.AbstractRoutingAlgorithmTester#getGraph(GraphHopperStorage)`\
type: `EXTRACT`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Extract Method protected getGraph(ghStorage GraphHopperStorage) : Graph extracted from public testTwoWeightsPerEdge2() : void in class com.graphhopper.routing.AbstractRoutingAlgorithmTester`

id: `1`\
source `com.graphhopper.routing.AbstractRoutingAlgorithmTester#testWithCoordinates()`\
target: `com.graphhopper.routing.AbstractRoutingAlgorithmTester#getGraph(GraphHopperStorage)`\
type: `EXTRACT`\
commit: [7f80425b6](https://github.com/graphhopper/graphhopper/commit/7f80425b6a0af9bdfef12c8a873676e39e0a04a6)\
description: `Extract Method protected getGraph(ghStorage GraphHopperStorage) : Graph extracted from public testWithCoordinates() : void in class com.graphhopper.routing.AbstractRoutingAlgorithmTester`

