<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `cascading.stats.CascadingStats#fireListeners(CascadingStats.Status,CascadingStats.Status)`\
target: `cascading.stats.CascadingStats#logWarn(String,Object...)`\
type: `EXTRACT`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Extract Method protected logWarn(message String, arguments Object...) : void extracted from protected fireListeners(fromStatus CascadingStats.Status, toStatus CascadingStats.Status) : void in class cascading.stats.CascadingStats`

id: `1`\
source `cascading.stats.hadoop.HadoopNodeStats#captureChildDetailInternal()`\
target: `cascading.stats.CascadingStats#logWarn(String,Object...)`\
type: `EXTRACT_MOVE`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Extract And Move Method protected logWarn(message String, arguments Object...) : void extracted from protected captureChildDetailInternal() : boolean in class cascading.stats.hadoop.HadoopNodeStats & moved to class cascading.stats.CascadingStats`

id: `2`\
source `cascading.stats.hadoop.HadoopNodeStats#addTaskStats(TaskReport[],boolean)`\
target: `cascading.stats.CascadingStats#logWarn(String,Object...)`\
type: `EXTRACT_MOVE`\
commit: [f9d3171f5](https://github.com/cwensel/cascading/commit/f9d3171f5020da5c359cdda28ef05172e858c464)\
description: `Extract And Move Method protected logWarn(message String, arguments Object...) : void extracted from protected addTaskStats(taskReports TaskReport[], skipLast boolean) : void in class cascading.stats.hadoop.HadoopNodeStats & moved to class cascading.stats.CascadingStats`

