<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.orientechnologies.orient.server.network.protocol.binary.ONetworkProtocolBinary#indexGet()`\
target: `com.orientechnologies.orient.server.network.protocol.binary.ONetworkProtocolBinary#serializeValue(OAbstractCommandResultListener,Object)`\
type: `EXTRACT`\
commit: [b40adc250](https://github.com/orientechnologies/orientdb/commit/b40adc25008b6f608ee3eb3422c8884fff987337)\
description: `Extract Method public serializeValue(listener OAbstractCommandResultListener, result Object) : void extracted from private indexGet() : void in class com.orientechnologies.orient.server.network.protocol.binary.ONetworkProtocolBinary`

id: `1`\
source `com.orientechnologies.orient.server.network.protocol.binary.ONetworkProtocolBinary#command()`\
target: `com.orientechnologies.orient.server.network.protocol.binary.ONetworkProtocolBinary#serializeValue(OAbstractCommandResultListener,Object)`\
type: `EXTRACT`\
commit: [b40adc250](https://github.com/orientechnologies/orientdb/commit/b40adc25008b6f608ee3eb3422c8884fff987337)\
description: `Extract Method public serializeValue(listener OAbstractCommandResultListener, result Object) : void extracted from protected command() : void in class com.orientechnologies.orient.server.network.protocol.binary.ONetworkProtocolBinary`

