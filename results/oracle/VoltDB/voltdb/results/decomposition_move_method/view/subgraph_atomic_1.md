<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.voltdb.importer.ChannelChangeNotifier`\
target: `org.voltdb.importer.ChannelDistributer#registerCallback(String,ChannelChangeCallback)`\
type: `MOVE`\
commit: [7527cfc74](https://github.com/VoltDB/voltdb/commit/7527cfc746dc20ddb78002c7b3a65d55026a334e)\
description: `Move Method public registerCallback(importer String, callback ChannelChangeCallback) : void from class org.voltdb.importer.ChannelChangeNotifier to public registerCallback(importer String, callback ChannelChangeCallback) : void from class org.voltdb.importer.ChannelDistributer`

id: `1`\
source `org.voltdb.importer.ChannelChangeNotifier`\
target: `org.voltdb.importer.ChannelAssignment#mapByImporter(Set<ChannelSpec>)`\
type: `MOVE`\
commit: [7527cfc74](https://github.com/VoltDB/voltdb/commit/7527cfc746dc20ddb78002c7b3a65d55026a334e)\
description: `Move Method package mapByImporter(specs Set<ChannelSpec>) : SetMultimap<String,URI> from class org.voltdb.importer.ChannelChangeNotifier to private mapByImporter(specs Set<ChannelSpec>) : SetMultimap<String,URI> from class org.voltdb.importer.ChannelAssignment`

