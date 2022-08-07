<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.jbpm.services.task.wih.HTWorkItemHandlerBaseTest#testTaskWithVariables()`\
target: `org.jbpm.services.task.wih.HTWorkItemHandlerBaseTest#prepareWorkItemWithTaskVariables(String)`\
type: `EXTRACT`\
commit: [83cfa2157](https://github.com/droolsjbpm/jbpm/commit/83cfa21578e63956bca0715eefee2860c3b6d39a)\
description: `Extract Method private prepareWorkItemWithTaskVariables(taskDescriptionParam String) : WorkItemImpl extracted from public testTaskWithVariables() : void in class org.jbpm.services.task.wih.HTWorkItemHandlerBaseTest`

id: `1`\
source `org.jbpm.services.task.wih.HTWorkItemHandlerBaseTest#testTaskWithVariables()`\
target: `org.jbpm.services.task.wih.HTWorkItemHandlerBaseTest#testTaskWithExpectedDescription(Task,String)`\
type: `EXTRACT`\
commit: [83cfa2157](https://github.com/droolsjbpm/jbpm/commit/83cfa21578e63956bca0715eefee2860c3b6d39a)\
description: `Extract Method private testTaskWithExpectedDescription(task Task, expectedDescription String) : void extracted from public testTaskWithVariables() : void in class org.jbpm.services.task.wih.HTWorkItemHandlerBaseTest`

