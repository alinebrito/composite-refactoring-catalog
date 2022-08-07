<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.testing.TestExceptionInjection`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#createExceptionOnBit(DrillbitEndpoint,String,int,int,String)`\
type: `MOVE`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Move Method private createExceptionOnBit(endpoint DrillbitEndpoint, desc String, nSkip int, nFire int, exceptionClass String) : String from class org.apache.drill.exec.testing.TestExceptionInjection to public createExceptionOnBit(siteClass Class<?>, desc String, nSkip int, nFire int, exceptionClass Class<? extends Throwable>, endpoint DrillbitEndpoint) : String from class org.apache.drill.exec.testing.ControlsInjectionUtil`

id: `1`\
source `org.apache.drill.exec.testing.TestExceptionInjection`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#createException(String,int,int,String)`\
type: `MOVE`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Move Method private createException(desc String, nSkip int, nFire int, exceptionClass String) : String from class org.apache.drill.exec.testing.TestExceptionInjection to public createException(siteClass Class<?>, desc String, nSkip int, nFire int, exceptionClass Class<? extends Throwable>) : String from class org.apache.drill.exec.testing.ControlsInjectionUtil`

