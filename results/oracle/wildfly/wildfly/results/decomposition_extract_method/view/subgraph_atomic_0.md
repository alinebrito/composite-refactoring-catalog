<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.jboss.as.ejb3.deployment.processors.merging.MethodPermissionsMergingProcessor#handleDeploymentDescriptor(DeploymentUnit,DeploymentReflectionIndex,Class<?>,EJBComponentDescription)`\
target: `org.jboss.as.ejb3.deployment.processors.merging.MethodPermissionsMergingProcessor#handleExcludeMethods(EJBComponentDescription,ExcludeListMetaData)`\
type: `EXTRACT`\
commit: [d7675fb0b](https://github.com/wildfly/wildfly/commit/d7675fb0b19d3d22978e79954f441eeefd74a3b2)\
description: `Extract Method private handleExcludeMethods(componentDescription EJBComponentDescription, excludeList ExcludeListMetaData) : void extracted from protected handleDeploymentDescriptor(deploymentUnit DeploymentUnit, deploymentReflectionIndex DeploymentReflectionIndex, componentClass Class<?>, componentDescription EJBComponentDescription) : void in class org.jboss.as.ejb3.deployment.processors.merging.MethodPermissionsMergingProcessor`

id: `1`\
source `org.jboss.as.ejb3.deployment.processors.merging.MethodPermissionsMergingProcessor#handleDeploymentDescriptor(DeploymentUnit,DeploymentReflectionIndex,Class<?>,EJBComponentDescription)`\
target: `org.jboss.as.ejb3.deployment.processors.merging.MethodPermissionsMergingProcessor#handleMethodPermissions(EJBComponentDescription,MethodPermissionsMetaData)`\
type: `EXTRACT`\
commit: [d7675fb0b](https://github.com/wildfly/wildfly/commit/d7675fb0b19d3d22978e79954f441eeefd74a3b2)\
description: `Extract Method private handleMethodPermissions(componentDescription EJBComponentDescription, methodPermissions MethodPermissionsMetaData) : void extracted from protected handleDeploymentDescriptor(deploymentUnit DeploymentUnit, deploymentReflectionIndex DeploymentReflectionIndex, componentClass Class<?>, componentDescription EJBComponentDescription) : void in class org.jboss.as.ejb3.deployment.processors.merging.MethodPermissionsMergingProcessor`

