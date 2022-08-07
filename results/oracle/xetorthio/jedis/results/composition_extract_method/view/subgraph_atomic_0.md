<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `redis.clients.util.Pool#getNumActive()`\
target: `redis.clients.util.Pool#poolInactive()`\
type: `EXTRACT`\
commit: [d4b4aecbc](https://github.com/xetorthio/jedis/commit/d4b4aecbc69bbd04ba87c4e32a52cff3d129906a)\
description: `Extract Method private poolInactive() : boolean extracted from public getNumActive() : int in class redis.clients.util.Pool`

id: `1`\
source `redis.clients.util.Pool#getNumWaiters()`\
target: `redis.clients.util.Pool#poolInactive()`\
type: `EXTRACT`\
commit: [d4b4aecbc](https://github.com/xetorthio/jedis/commit/d4b4aecbc69bbd04ba87c4e32a52cff3d129906a)\
description: `Extract Method private poolInactive() : boolean extracted from public getNumWaiters() : int in class redis.clients.util.Pool`

id: `2`\
source `redis.clients.util.Pool#getNumIdle()`\
target: `redis.clients.util.Pool#poolInactive()`\
type: `EXTRACT`\
commit: [d4b4aecbc](https://github.com/xetorthio/jedis/commit/d4b4aecbc69bbd04ba87c4e32a52cff3d129906a)\
description: `Extract Method private poolInactive() : boolean extracted from public getNumIdle() : int in class redis.clients.util.Pool`

