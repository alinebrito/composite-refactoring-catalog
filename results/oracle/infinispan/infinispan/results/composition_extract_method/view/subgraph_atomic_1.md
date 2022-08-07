<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.jboss.as.clustering.jgroups.JChannelFactory#getProtocolStack()`\
target: `org.infinispan.server.jgroups.JChannelFactory#createProtocols(ProtocolStackConfiguration,boolean)`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method package createProtocols(stack ProtocolStackConfiguration, multicastCapable boolean) : List<org.jgroups.conf.ProtocolConfiguration> extracted from public getProtocolStack() : List<org.jgroups.conf.ProtocolConfiguration> in class org.jboss.as.clustering.jgroups.JChannelFactory & moved to class org.infinispan.server.jgroups.JChannelFactory`

id: `1`\
source `org.infinispan.server.jgroups.JChannelFactory#getProtocolStack()`\
target: `org.infinispan.server.jgroups.JChannelFactory#createProtocols(ProtocolStackConfiguration,boolean)`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method package createProtocols(stack ProtocolStackConfiguration, multicastCapable boolean) : List<org.jgroups.conf.ProtocolConfiguration> extracted from public getProtocolStack() : List<org.jgroups.conf.ProtocolConfiguration> in class org.infinispan.server.jgroups.JChannelFactory`

