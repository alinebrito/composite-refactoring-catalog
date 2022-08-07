<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.core.annotation.AnnotationUtilsTests#synthesizeAnnotationFromMapWithMissingAttributeValue()`\
target: `org.springframework.core.annotation.AnnotationUtilsTests#assertMissingTextAttribute(Map<String,Object>)`\
type: `EXTRACT`\
commit: [ece12f9d3](https://github.com/spring-projects/spring-framework/commit/ece12f9d370108549fffac105e4bcb7faeaaf124)\
description: `Extract Method private assertMissingTextAttribute(attributes Map<String,Object>) : void extracted from public synthesizeAnnotationFromMapWithMissingAttributeValue() : void in class org.springframework.core.annotation.AnnotationUtilsTests`

id: `1`\
source `org.springframework.core.annotation.AnnotationUtilsTests#synthesizeAnnotationFromMapWithNullAttributeValue()`\
target: `org.springframework.core.annotation.AnnotationUtilsTests#assertMissingTextAttribute(Map<String,Object>)`\
type: `EXTRACT`\
commit: [ece12f9d3](https://github.com/spring-projects/spring-framework/commit/ece12f9d370108549fffac105e4bcb7faeaaf124)\
description: `Extract Method private assertMissingTextAttribute(attributes Map<String,Object>) : void extracted from public synthesizeAnnotationFromMapWithNullAttributeValue() : void in class org.springframework.core.annotation.AnnotationUtilsTests`

