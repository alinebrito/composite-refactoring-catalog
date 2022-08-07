<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cassandra.cql3.functions.UDFunction#create(FunctionName,List<ColumnIdentifier>,List<AbstractType<?>>,AbstractType<?>,boolean,String,String)`\
target: `org.apache.cassandra.cql3.functions.UDFunction#assertUdfsEnabled(String)`\
type: `EXTRACT`\
commit: [e37d577b6](https://github.com/apache/cassandra/commit/e37d577b6cfc2d3e11252cef87ab9ebba72e1d52)\
description: `Extract Method public assertUdfsEnabled(language String) : void extracted from public create(name FunctionName, argNames List<ColumnIdentifier>, argTypes List<AbstractType<?>>, returnType AbstractType<?>, calledOnNullInput boolean, language String, body String) : UDFunction in class org.apache.cassandra.cql3.functions.UDFunction`

id: `1`\
source `org.apache.cassandra.cql3.functions.UDFunction#execute(int,List<ByteBuffer>)`\
target: `org.apache.cassandra.cql3.functions.UDFunction#assertUdfsEnabled(String)`\
type: `EXTRACT`\
commit: [e37d577b6](https://github.com/apache/cassandra/commit/e37d577b6cfc2d3e11252cef87ab9ebba72e1d52)\
description: `Extract Method public assertUdfsEnabled(language String) : void extracted from public execute(protocolVersion int, parameters List<ByteBuffer>) : ByteBuffer in class org.apache.cassandra.cql3.functions.UDFunction`

