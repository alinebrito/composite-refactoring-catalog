<img src=subgraph_atomic_7.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.server.jgroups.subsystem.SubsystemParsingTestCase#testDescribeHandler()`\
target: `org.infinispan.server.jgroups.subsystem.SubsystemParsingTestCase#buildKernelServices()`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method private buildKernelServices() : KernelServices extracted from public testDescribeHandler() : void in class org.infinispan.server.jgroups.subsystem.SubsystemParsingTestCase`

id: `1`\
source `org.infinispan.server.jgroups.subsystem.SubsystemParsingTestCase#testParseAndMarshalModel()`\
target: `org.infinispan.server.jgroups.subsystem.SubsystemParsingTestCase#buildKernelServices()`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method private buildKernelServices() : KernelServices extracted from public testParseAndMarshalModel() : void in class org.infinispan.server.jgroups.subsystem.SubsystemParsingTestCase`

