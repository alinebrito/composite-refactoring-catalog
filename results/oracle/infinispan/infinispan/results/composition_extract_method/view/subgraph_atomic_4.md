<img src=subgraph_atomic_4.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getProtocolStackAddress(String)`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getSubsystemAddress()`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method protected getSubsystemAddress() : PathAddress extracted from protected getProtocolStackAddress(stackName String) : PathAddress in class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `1`\
source `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getSubsystemReadOperation(String)`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getSubsystemAddress()`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method protected getSubsystemAddress() : PathAddress extracted from protected getSubsystemReadOperation(name String) : ModelNode in class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `2`\
source `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getSubsystemWriteOperation(String,String)`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getSubsystemAddress()`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method protected getSubsystemAddress() : PathAddress extracted from protected getSubsystemWriteOperation(name String, value String) : ModelNode in class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

