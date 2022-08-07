<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase#testSubsystemReadWriteOperations()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testSubsystemReadWriteOperations() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `1`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase#testProtocolStackAddRemoveAddSequence()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testProtocolStackAddRemoveAddSequence() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `2`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase#testTransportReadWriteOperation()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testTransportReadWriteOperation() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `3`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase#testProtocolStackRemoveRemoveSequence()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testProtocolStackRemoveRemoveSequence() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `4`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase#testTransportReadWriteWithParameters()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testTransportReadWriteWithParameters() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `5`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase#testProtocolStackAddRemoveSequenceWithParameters()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testProtocolStackAddRemoveSequenceWithParameters() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `6`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase#testProtocolStackRemoveRollback()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testProtocolStackRemoveRollback() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationSequencesTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

id: `7`\
source `org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase#testProtocolReadWriteOperation()`\
target: `org.infinispan.server.jgroups.subsystem.OperationTestCaseBase#buildKernelServices()`\
type: `EXTRACT_MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Extract And Move Method protected buildKernelServices() : KernelServices extracted from public testProtocolReadWriteOperation() : void in class org.jboss.as.clustering.jgroups.subsystem.OperationsTestCase & moved to class org.infinispan.server.jgroups.subsystem.OperationTestCaseBase`

