<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.common.collect.HashBiMap.Itr#checkForConcurrentModification()`\
target: `com.google.common.collect.HashBiMap.Itr#hasNext()`\
type: `INLINE`\
commit: [5bab9e837](https://github.com/google/guava/commit/5bab9e837cf273250aa26702204f139fdcfd9e7a)\
description: `Inline Method private checkForConcurrentModification() : void inlined to public hasNext() : boolean in class com.google.common.collect.HashBiMap.Itr`

id: `1`\
source `com.google.common.collect.HashBiMap.Itr#checkForConcurrentModification()`\
target: `com.google.common.collect.HashBiMap.Itr#remove()`\
type: `INLINE`\
commit: [5bab9e837](https://github.com/google/guava/commit/5bab9e837cf273250aa26702204f139fdcfd9e7a)\
description: `Inline Method private checkForConcurrentModification() : void inlined to public remove() : void in class com.google.common.collect.HashBiMap.Itr`

