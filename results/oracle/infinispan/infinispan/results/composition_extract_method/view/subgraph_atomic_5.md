<img src=subgraph_atomic_5.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader#parseRemoteSite(XMLExtendedStreamReader,PathAddress,List<ModelNode>)`\
target: `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader#require(XMLExtendedStreamReader,Attribute)`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method private require(reader XMLExtendedStreamReader, attribute Attribute) : String extracted from private parseRemoteSite(reader XMLExtendedStreamReader, relayAddress PathAddress, operations List<ModelNode>) : void in class org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader`

id: `1`\
source `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader#readElement(XMLExtendedStreamReader,List<ModelNode>)`\
target: `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader#require(XMLExtendedStreamReader,Attribute)`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method private require(reader XMLExtendedStreamReader, attribute Attribute) : String extracted from public readElement(reader XMLExtendedStreamReader, operations List<ModelNode>) : void in class org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader`

id: `2`\
source `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader#parseProperty(XMLExtendedStreamReader,PathAddress,List<ModelNode>)`\
target: `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader#require(XMLExtendedStreamReader,Attribute)`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method private require(reader XMLExtendedStreamReader, attribute Attribute) : String extracted from private parseProperty(reader XMLExtendedStreamReader, address PathAddress, operations List<ModelNode>) : void in class org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLReader`

