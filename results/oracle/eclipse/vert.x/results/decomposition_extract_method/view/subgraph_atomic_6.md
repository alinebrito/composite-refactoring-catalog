<img src=subgraph_atomic_6.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.http.HttpClientOptions#HttpClientOptions(JsonObject)`\
target: `io.vertx.core.http.HttpClientOptions#init()`\
type: `EXTRACT`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract Method private init() : void extracted from public HttpClientOptions(json JsonObject) in class io.vertx.core.http.HttpClientOptions`

id: `1`\
source `io.vertx.core.http.HttpClientOptions#HttpClientOptions(JsonObject)`\
target: `io.vertx.core.http.HttpClientOptionsHelper#fromJson(JsonObject,HttpClientOptions)`\
type: `EXTRACT_MOVE`\
commit: [0ef66582f](https://github.com/eclipse/vert.x/commit/0ef66582ffaba9a8df1cad846880df2074d34505)\
description: `Extract And Move Method public fromJson(json JsonObject, obj HttpClientOptions) : void extracted from public HttpClientOptions(json JsonObject) in class io.vertx.core.http.HttpClientOptions & moved to class io.vertx.core.http.HttpClientOptionsHelper`

