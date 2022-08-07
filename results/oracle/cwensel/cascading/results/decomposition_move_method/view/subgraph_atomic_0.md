<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `cascading.stats.tez.TezNodeStats`\
target: `cascading.stats.CascadingStats#logInfo(String,Object...)`\
type: `MOVE`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Move Method protected logInfo(message String, arguments Object...) : void from class cascading.stats.tez.TezNodeStats to protected logInfo(message String, arguments Object...) : void from class cascading.stats.CascadingStats`

id: `1`\
source `cascading.stats.tez.TezNodeStats`\
target: `cascading.stats.CascadingStats#logWarn(String,Object...)`\
type: `MOVE`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Move Method protected logWarn(message String, arguments Object...) : void from class cascading.stats.tez.TezNodeStats to protected logWarn(message String, arguments Object...) : void from class cascading.stats.CascadingStats`

id: `2`\
source `cascading.stats.tez.TezNodeStats`\
target: `cascading.stats.CascadingStats#logDebug(String,Object...)`\
type: `MOVE`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Move Method protected logDebug(message String, arguments Object...) : void from class cascading.stats.tez.TezNodeStats to protected logDebug(message String, arguments Object...) : void from class cascading.stats.CascadingStats`

id: `3`\
source `cascading.stats.tez.TezNodeStats`\
target: `cascading.stats.CascadingStats#getPrefix()`\
type: `MOVE`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Move Method private getPrefix() : String from class cascading.stats.tez.TezNodeStats to private getPrefix() : String from class cascading.stats.CascadingStats`

