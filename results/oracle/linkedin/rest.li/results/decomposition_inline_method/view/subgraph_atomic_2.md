<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `com.linkedin.restli.examples.RestLiIntTestServer#createServer(Engine,int,String,boolean,int,List<?,List<?)`\
target: `com.linkedin.restli.examples.RestLiIntTestServer#createServer(Engine,int,String,boolean,int)`\
type: `INLINE`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Inline Method public createServer(engine Engine, port int, supportedCompression String, useAsyncServletApi boolean, asyncTimeOut int, requestFilters List<? extends RequestFilter>, responseFilters List<? extends ResponseFilter>) : HttpServer inlined to public createServer(engine Engine, port int, supportedCompression String, useAsyncServletApi boolean, asyncTimeOut int) : HttpServer in class com.linkedin.restli.examples.RestLiIntTestServer`

id: `1`\
source `com.linkedin.restli.examples.RestLiIntTestServer#createServer(Engine,int,String,boolean,int,List<?,List<?)`\
target: `com.linkedin.restli.examples.RestLiIntegrationTest#init(List<?,List<?)`\
type: `INLINE`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Move And Inline Method public createServer(engine Engine, port int, supportedCompression String, useAsyncServletApi boolean, asyncTimeOut int, requestFilters List<? extends RequestFilter>, responseFilters List<? extends ResponseFilter>) : HttpServer moved from class com.linkedin.restli.examples.RestLiIntTestServer to class com.linkedin.restli.examples.RestLiIntegrationTest & inlined to public init(requestFilters List<? extends RequestFilter>, responseFilters List<? extends ResponseFilter>) : void`

