<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.server.TestDrillbitResilience`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#createException(Class<?>,String,int,int,Class<?)`\
type: `MOVE_RENAME`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Move And Rename Method private createSingleException(siteClass Class<?>, desc String, exceptionClass Class<? extends Throwable>) : String from class org.apache.drill.exec.server.TestDrillbitResilience to public createException(siteClass Class<?>, desc String, nSkip int, nFire int, exceptionClass Class<? extends Throwable>) : String from class org.apache.drill.exec.testing.ControlsInjectionUtil`

id: `1`\
source `org.apache.drill.exec.server.TestDrillbitResilience`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#createExceptionOnBit(Class<?>,String,int,int,Class<?,DrillbitEndpoint)`\
type: `MOVE_RENAME`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Move And Rename Method private createSingleExceptionOnBit(siteClass Class<?>, desc String, exceptionClass Class<? extends Throwable>, bitName String) : String from class org.apache.drill.exec.server.TestDrillbitResilience to public createExceptionOnBit(siteClass Class<?>, desc String, nSkip int, nFire int, exceptionClass Class<? extends Throwable>, endpoint DrillbitEndpoint) : String from class org.apache.drill.exec.testing.ControlsInjectionUtil`

id: `2`\
source `org.apache.drill.exec.server.TestDrillbitResilience`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#createPause(Class,String,int)`\
type: `MOVE_RENAME`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Move And Rename Method private createPauseInjection(siteClass Class, siteDesc String, nSkip int) : String from class org.apache.drill.exec.server.TestDrillbitResilience to public createPause(siteClass Class, desc String, nSkip int) : String from class org.apache.drill.exec.testing.ControlsInjectionUtil`

