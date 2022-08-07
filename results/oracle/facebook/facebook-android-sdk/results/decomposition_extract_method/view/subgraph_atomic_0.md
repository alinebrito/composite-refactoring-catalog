<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.login.KatanaProxyLoginMethodHandler#handleResultOk(LoginClient.Request,Intent)`\
target: `com.facebook.login.KatanaProxyLoginMethodHandler#getErrorMessage(Bundle)`\
type: `EXTRACT`\
commit: [19d1936c3](https://github.com/facebook/facebook-android-sdk/commit/19d1936c3b07d97d88646aeae30de747715e3248)\
description: `Extract Method private getErrorMessage(extras Bundle) : String extracted from private handleResultOk(request LoginClient.Request, data Intent) : LoginClient.Result in class com.facebook.login.KatanaProxyLoginMethodHandler`

id: `1`\
source `com.facebook.login.KatanaProxyLoginMethodHandler#handleResultOk(LoginClient.Request,Intent)`\
target: `com.facebook.login.KatanaProxyLoginMethodHandler#getError(Bundle)`\
type: `EXTRACT`\
commit: [19d1936c3](https://github.com/facebook/facebook-android-sdk/commit/19d1936c3b07d97d88646aeae30de747715e3248)\
description: `Extract Method private getError(extras Bundle) : String extracted from private handleResultOk(request LoginClient.Request, data Intent) : LoginClient.Result in class com.facebook.login.KatanaProxyLoginMethodHandler`

