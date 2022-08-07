<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.net.ClientOptionsBase#ClientOptionsBase(JsonObject)`\
target: `io.vertx.core.net.ClientOptionsBase#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public ClientOptionsBase(json JsonObject) in class io.vertx.core.net.ClientOptionsBase`

id: `1`\
source `io.vertx.core.net.ClientOptionsBase#ClientOptionsBase(JsonObject)`\
target: `io.vertx.core.net.ClientOptionsBaseHelper#fromJson(JsonObject,ClientOptionsBase)`\
type: `EXTRACT_MOVE`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract And Move Method public fromJson(json JsonObject, obj ClientOptionsBase) : void extracted from public ClientOptionsBase(json JsonObject) in class io.vertx.core.net.ClientOptionsBase & moved to class io.vertx.core.net.ClientOptionsBaseHelper`

