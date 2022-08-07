<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `cgeo.geocaching.connector.WaymarkingConnectorTest#testCanHandle()`\
target: `cgeo.geocaching.connector.WaymarkingConnectorTest#getWaymarkingConnector()`\
type: `EXTRACT`\
commit: [c142b8ca3](https://github.com/cgeo/cgeo/commit/c142b8ca3e9f9467931987ee16805cf53e6bc5d2)\
description: `Extract Method private getWaymarkingConnector() : IConnector extracted from public testCanHandle() : void in class cgeo.geocaching.connector.WaymarkingConnectorTest`

id: `1`\
source `cgeo.geocaching.connector.WaymarkingConnectorTest#testGetGeocodeFromUrl()`\
target: `cgeo.geocaching.connector.WaymarkingConnectorTest#getWaymarkingConnector()`\
type: `EXTRACT`\
commit: [c142b8ca3](https://github.com/cgeo/cgeo/commit/c142b8ca3e9f9467931987ee16805cf53e6bc5d2)\
description: `Extract Method private getWaymarkingConnector() : IConnector extracted from public testGetGeocodeFromUrl() : void in class cgeo.geocaching.connector.WaymarkingConnectorTest`

