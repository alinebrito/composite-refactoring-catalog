<img src=subgraph_atomic_4.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.net.NetClientOptions#NetClientOptions(JsonObject)`\
target: `io.vertx.core.net.NetClientOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public NetClientOptions(json JsonObject) in class io.vertx.core.net.NetClientOptions`

id: `1`\
source `io.vertx.core.net.NetClientOptions#NetClientOptions(JsonObject)`\
target: `io.vertx.core.net.NetClientOptionsHelper#fromJson(JsonObject,NetClientOptions)`\
type: `EXTRACT_MOVE`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract And Move Method public fromJson(json JsonObject, obj NetClientOptions) : void extracted from public NetClientOptions(json JsonObject) in class io.vertx.core.net.NetClientOptions & moved to class io.vertx.core.net.NetClientOptionsHelper`

