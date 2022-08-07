<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.CreateTriggerStatementTest`\
target: `org.apache.cassandra.cql3.validation.operations.CreateTest#assertTriggerExists(String,Class<?>)`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method private assertTriggerExists(name String, clazz Class<?>) : void from class org.apache.cassandra.cql3.CreateTriggerStatementTest to private assertTriggerExists(name String, clazz Class<?>) : void from class org.apache.cassandra.cql3.validation.operations.CreateTest`

id: `1`\
source `org.apache.cassandra.cql3.CreateTriggerStatementTest`\
target: `org.apache.cassandra.cql3.validation.operations.CreateTest#testCreateTrigger()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testCreateTrigger() : void from class org.apache.cassandra.cql3.CreateTriggerStatementTest to public testCreateTrigger() : void from class org.apache.cassandra.cql3.validation.operations.CreateTest`

id: `2`\
source `org.apache.cassandra.cql3.CreateTriggerStatementTest`\
target: `org.apache.cassandra.cql3.validation.operations.CreateTest#testCreateTriggerIfNotExists()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testCreateTriggerIfNotExists() : void from class org.apache.cassandra.cql3.CreateTriggerStatementTest to public testCreateTriggerIfNotExists() : void from class org.apache.cassandra.cql3.validation.operations.CreateTest`

id: `3`\
source `org.apache.cassandra.cql3.CreateTriggerStatementTest`\
target: `org.apache.cassandra.cql3.validation.operations.CreateTest#testDropTrigger()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testDropTrigger() : void from class org.apache.cassandra.cql3.CreateTriggerStatementTest to public testDropTrigger() : void from class org.apache.cassandra.cql3.validation.operations.CreateTest`

id: `4`\
source `org.apache.cassandra.cql3.CreateTriggerStatementTest`\
target: `org.apache.cassandra.cql3.validation.operations.CreateTest#testDropTriggerIfExists()`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method public testDropTriggerIfExists() : void from class org.apache.cassandra.cql3.CreateTriggerStatementTest to public testDropTriggerIfExists() : void from class org.apache.cassandra.cql3.validation.operations.CreateTest`

id: `5`\
source `org.apache.cassandra.cql3.CreateTriggerStatementTest`\
target: `org.apache.cassandra.cql3.validation.operations.CreateTest#assertTriggerDoesNotExists(String,Class<?>)`\
type: `MOVE`\
commit: [f797bfa4d](https://github.com/apache/cassandra/commit/f797bfa4da53315b49f8d97b784047f33ba1bf5f)\
description: `Move Method private assertTriggerDoesNotExists(name String, clazz Class<?>) : void from class org.apache.cassandra.cql3.CreateTriggerStatementTest to private assertTriggerDoesNotExists(name String, clazz Class<?>) : void from class org.apache.cassandra.cql3.validation.operations.CreateTest`

