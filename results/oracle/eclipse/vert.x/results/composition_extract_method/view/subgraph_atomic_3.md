<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.net.TCPSSLOptions#TCPSSLOptions(JsonObject)`\
target: `io.vertx.core.net.TCPSSLOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public TCPSSLOptions(json JsonObject) in class io.vertx.core.net.TCPSSLOptions`

id: `1`\
source `io.vertx.core.net.TCPSSLOptions#TCPSSLOptions()`\
target: `io.vertx.core.net.TCPSSLOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public TCPSSLOptions() in class io.vertx.core.net.TCPSSLOptions`

