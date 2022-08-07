<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `io.vertx.core.net.impl.VertxHandler#exceptionCaught(ChannelHandlerContext,Throwable)`\
target: `io.vertx.core.net.impl.VertxNetHandler#getConnection(Channel)`\
type: `EXTRACT_MOVE`\
commit: [718782014](https://github.com/eclipse/vert.x/commit/718782014519034b28f6d3182fd9d340b7b31a74)\
description: `Extract And Move Method protected getConnection(channel Channel) : NetSocketImpl extracted from public exceptionCaught(chctx ChannelHandlerContext, t Throwable) : void in class io.vertx.core.net.impl.VertxHandler & moved to class io.vertx.core.net.impl.VertxNetHandler`

id: `1`\
source `io.vertx.core.net.impl.VertxHandler#channelWritabilityChanged(ChannelHandlerContext)`\
target: `io.vertx.core.net.impl.VertxNetHandler#getConnection(Channel)`\
type: `EXTRACT_MOVE`\
commit: [718782014](https://github.com/eclipse/vert.x/commit/718782014519034b28f6d3182fd9d340b7b31a74)\
description: `Extract And Move Method protected getConnection(channel Channel) : NetSocketImpl extracted from public channelWritabilityChanged(ctx ChannelHandlerContext) : void in class io.vertx.core.net.impl.VertxHandler & moved to class io.vertx.core.net.impl.VertxNetHandler`

id: `2`\
source `io.vertx.core.net.impl.VertxHandler#channelRead(ChannelHandlerContext,Object)`\
target: `io.vertx.core.net.impl.VertxNetHandler#getConnection(Channel)`\
type: `EXTRACT_MOVE`\
commit: [718782014](https://github.com/eclipse/vert.x/commit/718782014519034b28f6d3182fd9d340b7b31a74)\
description: `Extract And Move Method protected getConnection(channel Channel) : NetSocketImpl extracted from public channelRead(chctx ChannelHandlerContext, msg Object) : void in class io.vertx.core.net.impl.VertxHandler & moved to class io.vertx.core.net.impl.VertxNetHandler`

id: `3`\
source `io.vertx.core.net.impl.VertxHandler#channelReadComplete(ChannelHandlerContext)`\
target: `io.vertx.core.net.impl.VertxNetHandler#getConnection(Channel)`\
type: `EXTRACT_MOVE`\
commit: [718782014](https://github.com/eclipse/vert.x/commit/718782014519034b28f6d3182fd9d340b7b31a74)\
description: `Extract And Move Method protected getConnection(channel Channel) : NetSocketImpl extracted from public channelReadComplete(ctx ChannelHandlerContext) : void in class io.vertx.core.net.impl.VertxHandler & moved to class io.vertx.core.net.impl.VertxNetHandler`

