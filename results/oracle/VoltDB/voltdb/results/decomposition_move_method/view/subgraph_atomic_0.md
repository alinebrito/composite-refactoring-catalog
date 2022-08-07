<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.voltdb.sqlparser.matchers.TypeAssert`\
target: `org.voltdb.sqlparser.symtab.TypeAssert#hasName(String)`\
type: `MOVE`\
commit: [e58c9c3ee](https://github.com/VoltDB/voltdb/commit/e58c9c3eef4c6e44b21a97cfbd2862bb2eb4627a)\
description: `Move Method public hasName(aTypeName String) : TypeAssert from class org.voltdb.sqlparser.matchers.TypeAssert to public hasName(aTypeName String) : TypeAssert from class org.voltdb.sqlparser.symtab.TypeAssert`

id: `1`\
source `org.voltdb.sqlparser.matchers.TypeAssert`\
target: `org.voltdb.sqlparser.symtab.TypeAssert#hasNominalSize(int)`\
type: `MOVE`\
commit: [e58c9c3ee](https://github.com/VoltDB/voltdb/commit/e58c9c3eef4c6e44b21a97cfbd2862bb2eb4627a)\
description: `Move Method public hasNominalSize(aNominalSize int) : TypeAssert from class org.voltdb.sqlparser.matchers.TypeAssert to public hasNominalSize(aNominalSize int) : TypeAssert from class org.voltdb.sqlparser.symtab.TypeAssert`

id: `2`\
source `org.voltdb.sqlparser.matchers.TypeAssert`\
target: `org.voltdb.sqlparser.symtab.TypeAssert#hasMaxSize(int)`\
type: `MOVE`\
commit: [e58c9c3ee](https://github.com/VoltDB/voltdb/commit/e58c9c3eef4c6e44b21a97cfbd2862bb2eb4627a)\
description: `Move Method public hasMaxSize(aMaxSize int) : TypeAssert from class org.voltdb.sqlparser.matchers.TypeAssert to public hasMaxSize(aMaxSize int) : TypeAssert from class org.voltdb.sqlparser.symtab.TypeAssert`

