<img src=subgraph_atomic_4.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#overridePidFileWithSpring()`\
target: `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#createEnvironment(String,String)`\
type: `EXTRACT`\
commit: [becced5f0](https://github.com/spring-projects/spring-boot/commit/becced5f0b7bac8200df7a5706b568687b517b90)\
description: `Extract Method private createEnvironment(propName String, propValue String) : ConfigurableEnvironment extracted from public overridePidFileWithSpring() : void in class org.springframework.boot.actuate.system.ApplicationPidFileWriterTests`

id: `1`\
source `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#differentEventTypes()`\
target: `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#createEnvironment(String,String)`\
type: `EXTRACT`\
commit: [becced5f0](https://github.com/spring-projects/spring-boot/commit/becced5f0b7bac8200df7a5706b568687b517b90)\
description: `Extract Method private createEnvironment(propName String, propValue String) : ConfigurableEnvironment extracted from public differentEventTypes() : void in class org.springframework.boot.actuate.system.ApplicationPidFileWriterTests`

