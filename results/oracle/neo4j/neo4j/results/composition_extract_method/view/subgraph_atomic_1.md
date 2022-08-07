<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.neo4j.index.impl.lucene.IndexCreationTest#verifyThatIndexCreationTransactionIsTheFirstOne()`\
target: `org.neo4j.kernel.impl.transaction.log.LogPosition#start(long)`\
type: `EXTRACT_MOVE`\
commit: [001de3074](https://github.com/neo4j/neo4j/commit/001de307492df8f84ad15f6aaa0bd1e748d4ce27)\
description: `Extract And Move Method public start(logVersion long) : LogPosition extracted from private verifyThatIndexCreationTransactionIsTheFirstOne() : void in class org.neo4j.index.impl.lucene.IndexCreationTest & moved to class org.neo4j.kernel.impl.transaction.log.LogPosition`

id: `1`\
source `org.neo4j.kernel.impl.transaction.log.PhysicalLogFile#accept(LogHeaderVisitor)`\
target: `org.neo4j.kernel.impl.transaction.log.LogPosition#start(long)`\
type: `EXTRACT_MOVE`\
commit: [001de3074](https://github.com/neo4j/neo4j/commit/001de307492df8f84ad15f6aaa0bd1e748d4ce27)\
description: `Extract And Move Method public start(logVersion long) : LogPosition extracted from public accept(visitor LogHeaderVisitor) : void in class org.neo4j.kernel.impl.transaction.log.PhysicalLogFile & moved to class org.neo4j.kernel.impl.transaction.log.LogPosition`

id: `2`\
source `org.neo4j.kernel.NeoStoreDataSource#buildTransactionLogs(File,Config,LogProvider,LabelScanStore,FileSystemAbstraction,NeoStore,CacheAccessBackDoor,IndexingService,Iterable<IndexImplementation>)`\
target: `org.neo4j.kernel.impl.transaction.log.LogPosition#start(long)`\
type: `EXTRACT_MOVE`\
commit: [001de3074](https://github.com/neo4j/neo4j/commit/001de307492df8f84ad15f6aaa0bd1e748d4ce27)\
description: `Extract And Move Method public start(logVersion long) : LogPosition extracted from private buildTransactionLogs(storeDir File, config Config, logProvider LogProvider, labelScanStore LabelScanStore, fileSystemAbstraction FileSystemAbstraction, neoStore NeoStore, cacheAccess CacheAccessBackDoor, indexingService IndexingService, indexProviders Iterable<IndexImplementation>) : TransactionLogModule in class org.neo4j.kernel.NeoStoreDataSource & moved to class org.neo4j.kernel.impl.transaction.log.LogPosition`

