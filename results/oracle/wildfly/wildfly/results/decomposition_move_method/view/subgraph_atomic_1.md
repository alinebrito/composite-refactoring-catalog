<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.jboss.as.clustering.controller.BoottimeAddStepHandler`\
target: `org.jboss.as.clustering.controller.ResourceDescriptor#addAttributes(Attribute...)`\
type: `MOVE`\
commit: [4aa2e8746](https://github.com/wildfly/wildfly/commit/4aa2e8746b5492bbc1cf2b36af956cf3b01e40f5)\
description: `Move Method public addAttributes(attributes Attribute...) : BoottimeAddStepHandler from class org.jboss.as.clustering.controller.BoottimeAddStepHandler to public addAttributes(attributes Attribute...) : ResourceDescriptor from class org.jboss.as.clustering.controller.ResourceDescriptor`

id: `1`\
source `org.jboss.as.clustering.controller.BoottimeAddStepHandler`\
target: `org.jboss.as.clustering.controller.ResourceDescriptor#addAttributes(Class<E>)`\
type: `MOVE`\
commit: [4aa2e8746](https://github.com/wildfly/wildfly/commit/4aa2e8746b5492bbc1cf2b36af956cf3b01e40f5)\
description: `Move Method public addAttributes(enumClass Class<E>) : BoottimeAddStepHandler from class org.jboss.as.clustering.controller.BoottimeAddStepHandler to public addAttributes(enumClass Class<E>) : ResourceDescriptor from class org.jboss.as.clustering.controller.ResourceDescriptor`

