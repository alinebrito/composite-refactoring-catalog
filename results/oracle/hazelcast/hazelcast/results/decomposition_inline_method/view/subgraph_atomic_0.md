<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.hazelcast.cluster.impl.ClusterServiceImpl#sendHearBeatIfRequired(long,MemberImpl)`\
target: `com.hazelcast.cluster.impl.ClusterServiceImpl#heartBeaterSlave(long,long)`\
type: `INLINE`\
commit: [204bf49cb](https://github.com/hazelcast/hazelcast/commit/204bf49cba03fe5d581a35ff82dd22587a681f46)\
description: `Inline Method private sendHearBeatIfRequired(now long, member MemberImpl) : void inlined to private heartBeaterSlave(now long, clockJump long) : void in class com.hazelcast.cluster.impl.ClusterServiceImpl`

id: `1`\
source `com.hazelcast.cluster.impl.ClusterServiceImpl#sendHearBeatIfRequired(long,MemberImpl)`\
target: `com.hazelcast.cluster.impl.ClusterServiceImpl#heartBeaterMaster(long,long)`\
type: `INLINE`\
commit: [204bf49cb](https://github.com/hazelcast/hazelcast/commit/204bf49cba03fe5d581a35ff82dd22587a681f46)\
description: `Inline Method private sendHearBeatIfRequired(now long, member MemberImpl) : void inlined to private heartBeaterMaster(now long, clockJump long) : void in class com.hazelcast.cluster.impl.ClusterServiceImpl`

