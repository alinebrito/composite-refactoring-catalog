<img src=subgraph_atomic_5.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.net.NetServerOptions#NetServerOptions(JsonObject)`\
target: `io.vertx.core.net.NetServerOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public NetServerOptions(json JsonObject) in class io.vertx.core.net.NetServerOptions`

id: `1`\
source `io.vertx.core.net.NetServerOptions#NetServerOptions(JsonObject)`\
target: `io.vertx.core.net.NetServerOptionsHelper#fromJson(JsonObject,NetServerOptions)`\
type: `EXTRACT_MOVE`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract And Move Method public fromJson(json JsonObject, obj NetServerOptions) : void extracted from public NetServerOptions(json JsonObject) in class io.vertx.core.net.NetServerOptions & moved to class io.vertx.core.net.NetServerOptionsHelper`

