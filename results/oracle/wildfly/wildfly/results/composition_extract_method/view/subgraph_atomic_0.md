<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.wildfly.extension.batch.jberet.deployment.BatchEnvironmentProcessor#deploy(DeploymentPhaseContext)`\
target: `org.wildfly.extension.batch.jberet.deployment.WildFlyJobXmlResolver#of(ClassLoader,DeploymentUnit)`\
type: `EXTRACT_MOVE`\
commit: [bf35b533f](https://github.com/wildfly/wildfly/commit/bf35b533f067b51d4c373c5e5124d88525db99f3)\
description: `Extract And Move Method public of(classLoader ClassLoader, deploymentUnit DeploymentUnit) : WildFlyJobXmlResolver extracted from public deploy(phaseContext DeploymentPhaseContext) : void in class org.wildfly.extension.batch.jberet.deployment.BatchEnvironmentProcessor & moved to class org.wildfly.extension.batch.jberet.deployment.WildFlyJobXmlResolver`

id: `1`\
source `org.wildfly.extension.batch.deployment.BatchEnvironmentProcessor#deploy(DeploymentPhaseContext)`\
target: `org.wildfly.extension.batch.jberet.deployment.WildFlyJobXmlResolver#of(ClassLoader,DeploymentUnit)`\
type: `EXTRACT_MOVE`\
commit: [bf35b533f](https://github.com/wildfly/wildfly/commit/bf35b533f067b51d4c373c5e5124d88525db99f3)\
description: `Extract And Move Method public of(classLoader ClassLoader, deploymentUnit DeploymentUnit) : WildFlyJobXmlResolver extracted from public deploy(phaseContext DeploymentPhaseContext) : void in class org.wildfly.extension.batch.deployment.BatchEnvironmentProcessor & moved to class org.wildfly.extension.batch.jberet.deployment.WildFlyJobXmlResolver`

