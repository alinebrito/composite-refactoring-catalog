<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.jgroups.auth.FixedMembershipToken#authenticate(AuthToken,Message)`\
target: `org.jgroups.auth.FixedMembershipToken#isInMembersList(IpAddress)`\
type: `EXTRACT`\
commit: [f15337561](https://github.com/belaban/JGroups/commit/f1533756133dec84ce8218202585ac85904da7c9)\
description: `Extract Method public isInMembersList(sender IpAddress) : boolean extracted from public authenticate(token AuthToken, msg Message) : boolean in class org.jgroups.auth.FixedMembershipToken`

id: `1`\
source `org.jgroups.auth.FixedMembershipToken#authenticate(AuthToken,Message)`\
target: `org.jgroups.auth.FixedMembershipToken#match(IpAddress,InetSocketAddress)`\
type: `EXTRACT`\
commit: [f15337561](https://github.com/belaban/JGroups/commit/f1533756133dec84ce8218202585ac85904da7c9)\
description: `Extract Method public match(sender IpAddress, addr InetSocketAddress) : boolean extracted from public authenticate(token AuthToken, msg Message) : boolean in class org.jgroups.auth.FixedMembershipToken`

