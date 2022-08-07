<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.QueryProcessor.MigrationSubscriber#onDropAggregate(String,String,List<AbstractType<?>>)`\
target: `org.apache.cassandra.cql3.QueryProcessor.MigrationSubscriber#onDropFunctionInternal(String,String,List<AbstractType<?>>)`\
type: `EXTRACT`\
commit: [356684350](https://github.com/apache/cassandra/commit/35668435090eb47cf8c5e704243510b6cee35a7b)\
description: `Extract Method private onDropFunctionInternal(ksName String, functionName String, argTypes List<AbstractType<?>>) : void extracted from public onDropAggregate(ksName String, aggregateName String, argTypes List<AbstractType<?>>) : void in class org.apache.cassandra.cql3.QueryProcessor.MigrationSubscriber`

id: `1`\
source `org.apache.cassandra.cql3.QueryProcessor.MigrationSubscriber#onDropFunction(String,String,List<AbstractType<?>>)`\
target: `org.apache.cassandra.cql3.QueryProcessor.MigrationSubscriber#onDropFunctionInternal(String,String,List<AbstractType<?>>)`\
type: `EXTRACT`\
commit: [356684350](https://github.com/apache/cassandra/commit/35668435090eb47cf8c5e704243510b6cee35a7b)\
description: `Extract Method private onDropFunctionInternal(ksName String, functionName String, argTypes List<AbstractType<?>>) : void extracted from public onDropFunction(ksName String, functionName String, argTypes List<AbstractType<?>>) : void in class org.apache.cassandra.cql3.QueryProcessor.MigrationSubscriber`

