<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.geoserver.wfs.response.Ogr2OgrOutputFormat#getMimeType(Object,Operation)`\
target: `org.geoserver.ogr.core.Format#isSingleFile()`\
type: `EXTRACT_MOVE`\
commit: [e78cda0fc](https://github.com/geoserver/geoserver/commit/e78cda0fcf23de3973b659bc54f58a4e9b1f3bd3)\
description: `Extract And Move Method public isSingleFile() : boolean extracted from public getMimeType(value Object, operation Operation) : String in class org.geoserver.wfs.response.Ogr2OgrOutputFormat & moved to class org.geoserver.ogr.core.Format`

id: `1`\
source `org.geoserver.wfs.response.Ogr2OgrOutputFormat#getAttachmentFileName(Object,Operation)`\
target: `org.geoserver.ogr.core.Format#isSingleFile()`\
type: `EXTRACT_MOVE`\
commit: [e78cda0fc](https://github.com/geoserver/geoserver/commit/e78cda0fcf23de3973b659bc54f58a4e9b1f3bd3)\
description: `Extract And Move Method public isSingleFile() : boolean extracted from public getAttachmentFileName(value Object, operation Operation) : String in class org.geoserver.wfs.response.Ogr2OgrOutputFormat & moved to class org.geoserver.ogr.core.Format`

