<img src=subgraph_atomic_6.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getTransportAddOperationWithProperties(String,String)`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getProtocolPropertyAddOperation(String,String,String,String)`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method protected getProtocolPropertyAddOperation(stackName String, protocolName String, propertyName String, propertyValue String) : ModelNode extracted from protected getTransportAddOperationWithProperties(stackName String, protocolType String) : ModelNode in class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `1`\
source `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getProtocolAddOperationWithProperties(String,String)`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#getProtocolPropertyAddOperation(String,String,String,String)`\
type: `EXTRACT`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract Method protected getProtocolPropertyAddOperation(stackName String, protocolName String, propertyName String, propertyValue String) : ModelNode extracted from protected getProtocolAddOperationWithProperties(stackName String, protocolType String) : ModelNode in class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

