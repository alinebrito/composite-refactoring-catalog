<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.vector.BitVector#allocateNew(int)`\
target: `org.apache.drill.exec.vector.BitVector#allocateBytes(long)`\
type: `EXTRACT`\
commit: [b2bbd9941](https://github.com/apache/drill/commit/b2bbd9941be6b132a83d27c0ae02c935e1dec5dd)\
description: `Extract Method private allocateBytes(size long) : void extracted from public allocateNew(valueCount int) : void in class org.apache.drill.exec.vector.BitVector`

id: `1`\
source `org.apache.drill.exec.vector.BitVector#allocateNewSafe()`\
target: `org.apache.drill.exec.vector.BitVector#allocateBytes(long)`\
type: `EXTRACT`\
commit: [b2bbd9941](https://github.com/apache/drill/commit/b2bbd9941be6b132a83d27c0ae02c935e1dec5dd)\
description: `Extract Method private allocateBytes(size long) : void extracted from public allocateNewSafe() : boolean in class org.apache.drill.exec.vector.BitVector`

