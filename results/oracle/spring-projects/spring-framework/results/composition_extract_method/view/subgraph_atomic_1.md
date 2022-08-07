<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.test.util.JsonPathExpectationsHelper#exists(String)`\
target: `org.springframework.test.util.JsonPathExpectationsHelper#assertExistsAndReturn(String)`\
type: `EXTRACT`\
commit: [fffdd1e9e](https://github.com/spring-projects/spring-framework/commit/fffdd1e9e9dc887c3e8973147904d47d9fffbb47)\
description: `Extract Method private assertExistsAndReturn(content String) : Object extracted from public exists(content String) : void in class org.springframework.test.util.JsonPathExpectationsHelper`

id: `1`\
source `org.springframework.test.util.JsonPathExpectationsHelper#assertValueIsArray(String)`\
target: `org.springframework.test.util.JsonPathExpectationsHelper#assertExistsAndReturn(String)`\
type: `EXTRACT`\
commit: [fffdd1e9e](https://github.com/spring-projects/spring-framework/commit/fffdd1e9e9dc887c3e8973147904d47d9fffbb47)\
description: `Extract Method private assertExistsAndReturn(content String) : Object extracted from public assertValueIsArray(responseContent String) : void in class org.springframework.test.util.JsonPathExpectationsHelper`

