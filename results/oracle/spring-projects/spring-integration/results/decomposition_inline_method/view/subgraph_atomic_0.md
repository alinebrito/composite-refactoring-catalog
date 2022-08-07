<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.integration.ip.tcp.connection.TcpConnectionSupport#afterSend(Message<?>)`\
target: `org.springframework.integration.ip.tcp.connection.TcpNioConnection#send(Message<?>)`\
type: `INLINE`\
commit: [ec5230abc](https://github.com/spring-projects/spring-integration/commit/ec5230abc7500734d7b78a176c291378e100a927)\
description: `Move And Inline Method public afterSend(message Message<?>) : void moved from class org.springframework.integration.ip.tcp.connection.TcpConnectionSupport to class org.springframework.integration.ip.tcp.connection.TcpNioConnection & inlined to public send(message Message<?>) : void`

id: `1`\
source `org.springframework.integration.ip.tcp.connection.TcpConnectionSupport#afterSend(Message<?>)`\
target: `org.springframework.integration.ip.tcp.connection.TcpNetConnection#send(Message<?>)`\
type: `INLINE`\
commit: [ec5230abc](https://github.com/spring-projects/spring-integration/commit/ec5230abc7500734d7b78a176c291378e100a927)\
description: `Move And Inline Method public afterSend(message Message<?>) : void moved from class org.springframework.integration.ip.tcp.connection.TcpConnectionSupport to class org.springframework.integration.ip.tcp.connection.TcpNetConnection & inlined to public send(message Message<?>) : void`

