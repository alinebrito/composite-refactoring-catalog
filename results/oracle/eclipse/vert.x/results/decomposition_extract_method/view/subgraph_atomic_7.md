<img src=subgraph_atomic_7.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.http.HttpServerOptions#HttpServerOptions(JsonObject)`\
target: `io.vertx.core.http.HttpServerOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public HttpServerOptions(json JsonObject) in class io.vertx.core.http.HttpServerOptions`

id: `1`\
source `io.vertx.core.http.HttpServerOptions#HttpServerOptions(JsonObject)`\
target: `io.vertx.core.http.HttpServerOptionsHelper#fromJson(JsonObject,HttpServerOptions)`\
type: `EXTRACT_MOVE`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract And Move Method public fromJson(json JsonObject, obj HttpServerOptions) : void extracted from public HttpServerOptions(json JsonObject) in class io.vertx.core.http.HttpServerOptions & moved to class io.vertx.core.http.HttpServerOptionsHelper`

