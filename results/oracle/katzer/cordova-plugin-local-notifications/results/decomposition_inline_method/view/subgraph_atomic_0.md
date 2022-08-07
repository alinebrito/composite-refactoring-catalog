<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cordova.CordovaActivity#postMessage(String,Object)`\
target: `org.apache.cordova.CordovaActivity#onCreateOptionsMenu(Menu)`\
type: `INLINE`\
commit: [51f498a96](https://github.com/katzer/cordova-plugin-local-notifications/commit/51f498a96b2fa1822e392027982c20e950535fd1)\
description: `Inline Method public postMessage(id String, data Object) : void inlined to public onCreateOptionsMenu(menu Menu) : boolean in class org.apache.cordova.CordovaActivity`

id: `1`\
source `org.apache.cordova.CordovaActivity#postMessage(String,Object)`\
target: `org.apache.cordova.CordovaActivity#onOptionsItemSelected(MenuItem)`\
type: `INLINE`\
commit: [51f498a96](https://github.com/katzer/cordova-plugin-local-notifications/commit/51f498a96b2fa1822e392027982c20e950535fd1)\
description: `Inline Method public postMessage(id String, data Object) : void inlined to public onOptionsItemSelected(item MenuItem) : boolean in class org.apache.cordova.CordovaActivity`

id: `2`\
source `org.apache.cordova.CordovaActivity#postMessage(String,Object)`\
target: `org.apache.cordova.CordovaActivity#onPrepareOptionsMenu(Menu)`\
type: `INLINE`\
commit: [51f498a96](https://github.com/katzer/cordova-plugin-local-notifications/commit/51f498a96b2fa1822e392027982c20e950535fd1)\
description: `Inline Method public postMessage(id String, data Object) : void inlined to public onPrepareOptionsMenu(menu Menu) : boolean in class org.apache.cordova.CordovaActivity`

