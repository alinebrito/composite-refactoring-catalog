<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#notFound(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public notFound(resource String) : String from class org.jboss.as.clustering.jgroups.JGroupsMessages to public notFound(resource String) : String from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `1`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#duplicateNodeName(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public duplicateNodeName(name String) : IllegalStateException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public duplicateNodeName(name String) : IllegalStateException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `2`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#protocolNotDefined(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public protocolNotDefined(relativePath String) : OperationFailedException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public protocolNotDefined(relativePath String) : OperationFailedException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `3`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#protocolAlreadyDefined(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public protocolAlreadyDefined(relativePath String) : OperationFailedException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public protocolAlreadyDefined(relativePath String) : OperationFailedException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `4`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#transportNotDefined(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public transportNotDefined(stackName String) : OperationFailedException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public transportNotDefined(stackName String) : OperationFailedException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `5`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#unauthorizedNodeJoin(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public unauthorizedNodeJoin(nodeName String) : SecurityException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public unauthorizedNodeJoin(nodeName String) : SecurityException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `6`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#parserFailure(URL)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public parserFailure(url URL) : String from class org.jboss.as.clustering.jgroups.JGroupsMessages to public parserFailure(url URL) : String from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `7`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#protocolListNotDefined(String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public protocolListNotDefined(stackName String) : OperationFailedException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public protocolListNotDefined(stackName String) : OperationFailedException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

id: `8`\
source `org.jboss.as.clustering.jgroups.JGroupsMessages`\
target: `org.infinispan.server.jgroups.logging.JGroupsLogger#propertyNotDefined(String,String)`\
type: `MOVE`\
commit: [8f446b6dd](https://github.com/infinispan/infinispan/commit/8f446b6ddf540e1b1fefca34dd10f45ba7256095)\
description: `Move Method public propertyNotDefined(propertyName String, protocolRelativePath String) : OperationFailedException from class org.jboss.as.clustering.jgroups.JGroupsMessages to public propertyNotDefined(propertyName String, protocolRelativePath String) : OperationFailedException from class org.infinispan.server.jgroups.logging.JGroupsLogger`

