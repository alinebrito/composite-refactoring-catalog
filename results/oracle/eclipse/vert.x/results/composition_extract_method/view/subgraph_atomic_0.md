<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.net.impl.VertxHandler#channelWritabilityChanged(ChannelHandlerContext)`\
target: `io.vertx.core.http.impl.VertxHttpHandler#getConnection(Channel)`\
type: `EXTRACT_MOVE`\
commit: [718782014](https://github.com/eclipse/vert.x/commit/718782014519034b28f6d3182fd9d340b7b31a74)\
description: `Extract And Move Method protected getConnection(channel Channel) : C extracted from public channelWritabilityChanged(ctx ChannelHandlerContext) : void in class io.vertx.core.net.impl.VertxHandler & moved to class io.vertx.core.http.impl.VertxHttpHandler`

id: `1`\
source `io.vertx.core.net.impl.VertxHandler#channelReadComplete(ChannelHandlerContext)`\
target: `io.vertx.core.http.impl.VertxHttpHandler#getConnection(Channel)`\
type: `EXTRACT_MOVE`\
commit: [718782014](https://github.com/eclipse/vert.x/commit/718782014519034b28f6d3182fd9d340b7b31a74)\
description: `Extract And Move Method protected getConnection(channel Channel) : C extracted from public channelReadComplete(ctx ChannelHandlerContext) : void in class io.vertx.core.net.impl.VertxHandler & moved to class io.vertx.core.http.impl.VertxHttpHandler`

