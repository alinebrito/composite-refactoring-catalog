<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `io.netty.handler.codec.http2.DefaultHttp2RemoteFlowControllerTest#windowUpdateAndFlushShouldTriggerWrite()`\
target: `io.netty.handler.codec.http2.DefaultHttp2RemoteFlowControllerTest#resetCtx()`\
type: `EXTRACT`\
commit: [9f422ed0f](https://github.com/netty/netty/commit/9f422ed0f44516bea8116ed7730203e4eb316252)\
description: `Extract Method private resetCtx() : void extracted from public windowUpdateAndFlushShouldTriggerWrite() : void in class io.netty.handler.codec.http2.DefaultHttp2RemoteFlowControllerTest`

id: `1`\
source `io.netty.handler.codec.http2.DefaultHttp2RemoteFlowControllerTest#setup()`\
target: `io.netty.handler.codec.http2.DefaultHttp2RemoteFlowControllerTest#resetCtx()`\
type: `EXTRACT`\
commit: [9f422ed0f](https://github.com/netty/netty/commit/9f422ed0f44516bea8116ed7730203e4eb316252)\
description: `Extract Method private resetCtx() : void extracted from public setup() : void in class io.netty.handler.codec.http2.DefaultHttp2RemoteFlowControllerTest`

