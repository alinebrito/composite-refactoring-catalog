<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `integration.BaseRestTest`\
target: `integration.RestAssuredSetupRule#before()`\
type: `MOVE_RENAME`\
commit: [2ef067fc7](https://github.com/Graylog2/graylog2-server/commit/2ef067fc70055fc4d55c75937303414ddcf07e0e)\
description: `Move And Rename Method public setupTestSuite() : void from class integration.BaseRestTest to protected before() : void from class integration.RestAssuredSetupRule`

id: `1`\
source `integration.BaseRestTest`\
target: `integration.RequiredVersionRule#apply(Statement,FrameworkMethod,Object)`\
type: `MOVE_RENAME`\
commit: [2ef067fc7](https://github.com/Graylog2/graylog2-server/commit/2ef067fc70055fc4d55c75937303414ddcf07e0e)\
description: `Move And Rename Method public run(callBack IHookCallBack, testResult ITestResult) : void from class integration.BaseRestTest to public apply(base Statement, method FrameworkMethod, target Object) : Statement from class integration.RequiredVersionRule`

