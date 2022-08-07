<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.kernel.api.impl.index.LuceneIndexAccessorReader#lookup(Object)`\
target: `org.neo4j.kernel.api.impl.index.LuceneIndexAccessorReader#query(Query)`\
type: `EXTRACT`\
commit: [b83e6a535](https://github.com/neo4j/neo4j/commit/b83e6a535cbca21d5ea764b0c49bfca8a9ff9db4)\
description: `Extract Method protected query(query Query) : PrimitiveLongIterator extracted from public lookup(value Object) : PrimitiveLongIterator in class org.neo4j.kernel.api.impl.index.LuceneIndexAccessorReader`

id: `1`\
source `org.neo4j.kernel.api.impl.index.LuceneIndexAccessorReader#scan()`\
target: `org.neo4j.kernel.api.impl.index.LuceneIndexAccessorReader#query(Query)`\
type: `EXTRACT`\
commit: [b83e6a535](https://github.com/neo4j/neo4j/commit/b83e6a535cbca21d5ea764b0c49bfca8a9ff9db4)\
description: `Extract Method protected query(query Query) : PrimitiveLongIterator extracted from public scan() : PrimitiveLongIterator in class org.neo4j.kernel.api.impl.index.LuceneIndexAccessorReader`

