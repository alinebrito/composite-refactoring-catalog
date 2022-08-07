<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.linkedin.restli.internal.server.methods.response.BatchResponseUtil#populateErrors(Map<K,RestLiServiceException>,RoutingResult,ErrorResponseBuilder)`\
target: `com.linkedin.restli.internal.server.methods.response.BatchUpdateResponseBuilder#buildRestLiResponseData(RestRequest,RoutingResult,Object,Map<String,String>)`\
type: `INLINE`\
commit: [ec5ea36fa](https://github.com/linkedin/rest.li/commit/ec5ea36faa3dd74585bb339beabdba6149ed63be)\
description: `Move And Inline Method package populateErrors(serviceErrors Map<K,RestLiServiceException>, routingResult RoutingResult, builder ErrorResponseBuilder) : Map<K,ErrorResponse> moved from class com.linkedin.restli.internal.server.methods.response.BatchResponseUtil to class com.linkedin.restli.internal.server.methods.response.BatchUpdateResponseBuilder & inlined to public buildRestLiResponseData(request RestRequest, routingResult RoutingResult, result Object, headers Map<String,String>) : RestLiResponseEnvelope`

id: `1`\
source `com.linkedin.restli.internal.server.methods.response.BatchResponseUtil#populateErrors(Map<K,RestLiServiceException>,RoutingResult,ErrorResponseBuilder)`\
target: `com.linkedin.restli.internal.server.methods.response.BatchGetResponseBuilder#buildRestLiResponseData(RestRequest,RoutingResult,Object,Map<String,String>)`\
type: `INLINE`\
commit: [ec5ea36fa](https://github.com/linkedin/rest.li/commit/ec5ea36faa3dd74585bb339beabdba6149ed63be)\
description: `Move And Inline Method package populateErrors(serviceErrors Map<K,RestLiServiceException>, routingResult RoutingResult, builder ErrorResponseBuilder) : Map<K,ErrorResponse> moved from class com.linkedin.restli.internal.server.methods.response.BatchResponseUtil to class com.linkedin.restli.internal.server.methods.response.BatchGetResponseBuilder & inlined to public buildRestLiResponseData(request RestRequest, routingResult RoutingResult, result Object, headers Map<String,String>) : RestLiResponseEnvelope`

