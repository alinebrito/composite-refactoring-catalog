<img src=subgraph_atomic_6.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityPower#runIterations(int)`\
target: `org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityBase#incrementTotalIterations()`\
type: `EXTRACT_MOVE`\
commit: [4712de476](https://github.com/neo4j/neo4j/commit/4712de476aabe69cd762233c9641dd3cf9f8361b)\
description: `Extract And Move Method protected incrementTotalIterations() : void extracted from public runIterations(maxNrIterations int) : int in class org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityPower & moved to class org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityBase`

id: `1`\
source `org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityArnoldi#runInternalArnoldi(int)`\
target: `org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityBase#incrementTotalIterations()`\
type: `EXTRACT_MOVE`\
commit: [4712de476](https://github.com/neo4j/neo4j/commit/4712de476aabe69cd762233c9641dd3cf9f8361b)\
description: `Extract And Move Method protected incrementTotalIterations() : void extracted from protected runInternalArnoldi(iterations int) : int in class org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityArnoldi & moved to class org.neo4j.graphalgo.impl.centrality.EigenvectorCentralityBase`

