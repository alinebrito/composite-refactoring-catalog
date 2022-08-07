<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.testing.ControlsInjectionUtil#setControls(DrillClient,String)`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#setSessionOption(DrillClient,String,String)`\
type: `EXTRACT`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Extract Method public setSessionOption(drillClient DrillClient, option String, value String) : void extracted from public setControls(drillClient DrillClient, controls String) : void in class org.apache.drill.exec.testing.ControlsInjectionUtil`

id: `1`\
source `org.apache.drill.exec.server.TestDrillbitResilience#setSessionOption(String,String)`\
target: `org.apache.drill.exec.testing.ControlsInjectionUtil#setSessionOption(DrillClient,String,String)`\
type: `EXTRACT_MOVE`\
commit: [00aa01fb9](https://github.com/apache/drill/commit/00aa01fb90f3210d1e3027d7f759fb1085b814bd)\
description: `Extract And Move Method public setSessionOption(drillClient DrillClient, option String, value String) : void extracted from private setSessionOption(option String, value String) : void in class org.apache.drill.exec.server.TestDrillbitResilience & moved to class org.apache.drill.exec.testing.ControlsInjectionUtil`

