<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.activiti.bpmn.model.Activity#isAsynchronous()`\
target: `org.activiti.bpmn.model.FlowNode#isAsynchronous()`\
type: `PULL_UP`\
commit: [53036cece](https://github.com/Activiti/Activiti/commit/53036cece662f9c796d2a187b0077059c3d9088a)\
description: `Pull Up Method public isAsynchronous() : boolean from class org.activiti.bpmn.model.Activity to public isAsynchronous() : boolean from class org.activiti.bpmn.model.FlowNode`

id: `1`\
source `org.activiti.bpmn.model.Gateway#isAsynchronous()`\
target: `org.activiti.bpmn.model.FlowNode#isAsynchronous()`\
type: `PULL_UP`\
commit: [53036cece](https://github.com/Activiti/Activiti/commit/53036cece662f9c796d2a187b0077059c3d9088a)\
description: `Pull Up Method public isAsynchronous() : boolean from class org.activiti.bpmn.model.Gateway to public isAsynchronous() : boolean from class org.activiti.bpmn.model.FlowNode`

