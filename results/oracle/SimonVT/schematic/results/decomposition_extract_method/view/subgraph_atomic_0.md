<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `net.simonvt.schematic.compiler.ContentProviderWriter#write(Filer)`\
target: `net.simonvt.schematic.compiler.ContentProviderWriter#printNotifyInsert(JavaWriter,UriContract)`\
type: `EXTRACT`\
commit: [c1a9dd63a](https://github.com/SimonVT/schematic/commit/c1a9dd63aca8bf488f9a671aa6281538540397f8)\
description: `Extract Method private printNotifyInsert(writer JavaWriter, uri UriContract) : void extracted from public write(filer Filer) : void in class net.simonvt.schematic.compiler.ContentProviderWriter`

id: `1`\
source `net.simonvt.schematic.compiler.ContentProviderWriter#write(Filer)`\
target: `net.simonvt.schematic.compiler.ContentProviderWriter#printNotifyBulkInsert(JavaWriter,UriContract)`\
type: `EXTRACT`\
commit: [c1a9dd63a](https://github.com/SimonVT/schematic/commit/c1a9dd63aca8bf488f9a671aa6281538540397f8)\
description: `Extract Method private printNotifyBulkInsert(writer JavaWriter, uri UriContract) : void extracted from public write(filer Filer) : void in class net.simonvt.schematic.compiler.ContentProviderWriter`

