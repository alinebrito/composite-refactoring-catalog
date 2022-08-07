<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.cordova.ConfigXmlParser#parse(XmlResourceParser)`\
target: `org.apache.cordova.ConfigXmlParser#handleEndTag(XmlPullParser)`\
type: `EXTRACT`\
commit: [51f498a96](https://github.com/katzer/cordova-plugin-local-notifications/commit/51f498a96b2fa1822e392027982c20e950535fd1)\
description: `Extract Method public handleEndTag(xml XmlPullParser) : void extracted from public parse(xml XmlResourceParser) : void in class org.apache.cordova.ConfigXmlParser`

id: `1`\
source `org.apache.cordova.ConfigXmlParser#parse(XmlResourceParser)`\
target: `org.apache.cordova.ConfigXmlParser#handleStartTag(XmlPullParser)`\
type: `EXTRACT`\
commit: [51f498a96](https://github.com/katzer/cordova-plugin-local-notifications/commit/51f498a96b2fa1822e392027982c20e950535fd1)\
description: `Extract Method public handleStartTag(xml XmlPullParser) : void extracted from public parse(xml XmlResourceParser) : void in class org.apache.cordova.ConfigXmlParser`

