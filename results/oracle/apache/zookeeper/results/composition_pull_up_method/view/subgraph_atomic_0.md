<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.zookeeper.server.NIOServerCnxn#cleanupWriterSocket(PrintWriter)`\
target: `org.apache.zookeeper.server.ServerCnxn#cleanupWriterSocket(PrintWriter)`\
type: `PULL_UP`\
commit: [3fd77b419](https://github.com/apache/zookeeper/commit/3fd77b419673ce6ec41e06cdc27558b1d8f4ca06)\
description: `Pull Up Method private cleanupWriterSocket(pwriter PrintWriter) : void from class org.apache.zookeeper.server.NIOServerCnxn to public cleanupWriterSocket(pwriter PrintWriter) : void from class org.apache.zookeeper.server.ServerCnxn`

id: `1`\
source `org.apache.zookeeper.server.NettyServerCnxn#cleanupWriterSocket(PrintWriter)`\
target: `org.apache.zookeeper.server.ServerCnxn#cleanupWriterSocket(PrintWriter)`\
type: `PULL_UP`\
commit: [3fd77b419](https://github.com/apache/zookeeper/commit/3fd77b419673ce6ec41e06cdc27558b1d8f4ca06)\
description: `Pull Up Method private cleanupWriterSocket(pwriter PrintWriter) : void from class org.apache.zookeeper.server.NettyServerCnxn to public cleanupWriterSocket(pwriter PrintWriter) : void from class org.apache.zookeeper.server.ServerCnxn`

