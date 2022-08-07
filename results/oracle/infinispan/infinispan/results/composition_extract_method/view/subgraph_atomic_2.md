<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.jboss.as.clustering.jgroups.subsystem.JGroupsSubsystemXMLWriter#writeRelay(XMLExtendedStreamWriter,ModelNode,Element)`\
target: `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLWriter#writeAttribute(XMLExtendedStreamWriter,ModelNode,AttributeDefinition)`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method private writeAttribute(writer XMLExtendedStreamWriter, model ModelNode, attribute AttributeDefinition) : void extracted from private writeRelay(writer XMLExtendedStreamWriter, relay ModelNode, element Element) : void in class org.jboss.as.clustering.jgroups.subsystem.JGroupsSubsystemXMLWriter & moved to class org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLWriter`

id: `1`\
source `org.jboss.as.clustering.jgroups.subsystem.JGroupsSubsystemXMLWriter#writeSasl(XMLExtendedStreamWriter,ModelNode,Element)`\
target: `org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLWriter#writeAttribute(XMLExtendedStreamWriter,ModelNode,AttributeDefinition)`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method private writeAttribute(writer XMLExtendedStreamWriter, model ModelNode, attribute AttributeDefinition) : void extracted from private writeSasl(writer XMLExtendedStreamWriter, sasl ModelNode, element Element) : void in class org.jboss.as.clustering.jgroups.subsystem.JGroupsSubsystemXMLWriter & moved to class org.infinispan.server.jgroups.subsystem.JGroupsSubsystemXMLWriter`

