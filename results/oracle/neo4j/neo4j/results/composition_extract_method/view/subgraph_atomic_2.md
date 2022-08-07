<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.impl.factory.GraphDatabaseFacade#beginTx()`\
target: `org.neo4j.kernel.impl.factory.GraphDatabaseFacade#checkAvailability()`\
type: `EXTRACT`\
commit: [74d2cc420](https://github.com/neo4j/neo4j/commit/74d2cc420e5590ba3bc0ffcc15b30b76a9cbef0b)\
description: `Extract Method private checkAvailability() : void extracted from public beginTx() : Transaction in class org.neo4j.kernel.impl.factory.GraphDatabaseFacade`

id: `1`\
source `org.neo4j.kernel.impl.factory.GraphDatabaseFacade#execute(String,Map<String,Object>)`\
target: `org.neo4j.kernel.impl.factory.GraphDatabaseFacade#checkAvailability()`\
type: `EXTRACT`\
commit: [74d2cc420](https://github.com/neo4j/neo4j/commit/74d2cc420e5590ba3bc0ffcc15b30b76a9cbef0b)\
description: `Extract Method private checkAvailability() : void extracted from public execute(query String, parameters Map<String,Object>) : Result in class org.neo4j.kernel.impl.factory.GraphDatabaseFacade`

