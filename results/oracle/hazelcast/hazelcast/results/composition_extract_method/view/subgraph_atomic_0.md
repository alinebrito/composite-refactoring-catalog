<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.hazelcast.test.TestHazelcastInstanceFactory#createAddresses(int)`\
target: `com.hazelcast.test.TestHazelcastInstanceFactory#createAddress(String,int)`\
type: `EXTRACT`\
commit: [76d7f5e3f](https://github.com/hazelcast/hazelcast/commit/76d7f5e3fe4eb41b383c1d884bc1217b9fa7192e)\
description: `Extract Method protected createAddress(host String, port int) : Address extracted from private createAddresses(count int) : Address[] in class com.hazelcast.test.TestHazelcastInstanceFactory`

id: `1`\
source `com.hazelcast.test.TestHazelcastInstanceFactory#createAddresses(String...)`\
target: `com.hazelcast.test.TestHazelcastInstanceFactory#createAddress(String,int)`\
type: `EXTRACT`\
commit: [76d7f5e3f](https://github.com/hazelcast/hazelcast/commit/76d7f5e3fe4eb41b383c1d884bc1217b9fa7192e)\
description: `Extract Method protected createAddress(host String, port int) : Address extracted from private createAddresses(addressArray String...) : Address[] in class com.hazelcast.test.TestHazelcastInstanceFactory`

