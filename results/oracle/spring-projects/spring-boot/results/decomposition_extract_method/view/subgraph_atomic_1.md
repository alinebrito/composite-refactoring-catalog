<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#differentEventTypes()`\
target: `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#createEnvironmentPreparedEvent(String,String)`\
type: `EXTRACT`\
commit: [becced5f0](https://github.com/spring-projects/spring-boot/commit/becced5f0b7bac8200df7a5706b568687b517b90)\
description: `Extract Method private createEnvironmentPreparedEvent(propName String, propValue String) : SpringApplicationEvent extracted from public differentEventTypes() : void in class org.springframework.boot.actuate.system.ApplicationPidFileWriterTests`

id: `1`\
source `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#differentEventTypes()`\
target: `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#mockPropertySource(String,String)`\
type: `EXTRACT`\
commit: [becced5f0](https://github.com/spring-projects/spring-boot/commit/becced5f0b7bac8200df7a5706b568687b517b90)\
description: `Extract Method private mockPropertySource(name String, value String) : MockPropertySource extracted from public differentEventTypes() : void in class org.springframework.boot.actuate.system.ApplicationPidFileWriterTests`

id: `2`\
source `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#differentEventTypes()`\
target: `org.springframework.boot.actuate.system.ApplicationPidFileWriterTests#createEnvironment(String,String)`\
type: `EXTRACT`\
commit: [becced5f0](https://github.com/spring-projects/spring-boot/commit/becced5f0b7bac8200df7a5706b568687b517b90)\
description: `Extract Method private createEnvironment(propName String, propValue String) : ConfigurableEnvironment extracted from public differentEventTypes() : void in class org.springframework.boot.actuate.system.ApplicationPidFileWriterTests`

