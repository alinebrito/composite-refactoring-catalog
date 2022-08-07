<img src=subgraph_atomic_7.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.http.HttpServerOptions#HttpServerOptions(JsonObject)`\
target: `io.vertx.core.http.HttpServerOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public HttpServerOptions(json JsonObject) in class io.vertx.core.http.HttpServerOptions`

id: `1`\
source `io.vertx.core.http.HttpServerOptions#HttpServerOptions()`\
target: `io.vertx.core.http.HttpServerOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public HttpServerOptions() in class io.vertx.core.http.HttpServerOptions`

