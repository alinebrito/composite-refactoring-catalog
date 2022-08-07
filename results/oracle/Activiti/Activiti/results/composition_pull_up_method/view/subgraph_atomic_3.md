<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.activiti.bpmn.model.Activity#setNotExclusive(boolean)`\
target: `org.activiti.bpmn.model.FlowNode#setNotExclusive(boolean)`\
type: `PULL_UP`\
commit: [53036cece](https://github.com/Activiti/Activiti/commit/53036cece662f9c796d2a187b0077059c3d9088a)\
description: `Pull Up Method public setNotExclusive(notExclusive boolean) : void from class org.activiti.bpmn.model.Activity to public setNotExclusive(notExclusive boolean) : void from class org.activiti.bpmn.model.FlowNode`

id: `1`\
source `org.activiti.bpmn.model.Gateway#setNotExclusive(boolean)`\
target: `org.activiti.bpmn.model.FlowNode#setNotExclusive(boolean)`\
type: `PULL_UP`\
commit: [53036cece](https://github.com/Activiti/Activiti/commit/53036cece662f9c796d2a187b0077059c3d9088a)\
description: `Pull Up Method public setNotExclusive(notExclusive boolean) : void from class org.activiti.bpmn.model.Gateway to public setNotExclusive(notExclusive boolean) : void from class org.activiti.bpmn.model.FlowNode`

