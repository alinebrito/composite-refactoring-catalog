<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.auto.common.BasicAnnotationProcessor#process(Set<?,RoundEnvironment)`\
target: `com.google.auto.common.BasicAnnotationProcessor#deferredElements()`\
type: `EXTRACT`\
commit: [8fc60d81f](https://github.com/google/auto/commit/8fc60d81fe0e46e7e5c96e71d4a93fcadc6bde4f)\
description: `Extract Method private deferredElements() : ImmutableMap<String,Optional<? extends Element>> extracted from public process(annotations Set<? extends TypeElement>, roundEnv RoundEnvironment) : boolean in class com.google.auto.common.BasicAnnotationProcessor`

id: `1`\
source `com.google.auto.common.BasicAnnotationProcessor#process(Set<?,RoundEnvironment)`\
target: `com.google.auto.common.BasicAnnotationProcessor#validElements(ImmutableMap<String,Optional<?,RoundEnvironment)`\
type: `EXTRACT`\
commit: [8fc60d81f](https://github.com/google/auto/commit/8fc60d81fe0e46e7e5c96e71d4a93fcadc6bde4f)\
description: `Extract Method private validElements(deferredElements ImmutableMap<String,Optional<? extends Element>>, roundEnv RoundEnvironment) : ImmutableSetMultimap<Class<? extends Annotation>,Element> extracted from public process(annotations Set<? extends TypeElement>, roundEnv RoundEnvironment) : boolean in class com.google.auto.common.BasicAnnotationProcessor`

id: `2`\
source `com.google.auto.common.BasicAnnotationProcessor#process(Set<?,RoundEnvironment)`\
target: `com.google.auto.common.BasicAnnotationProcessor#process(ImmutableSetMultimap<Class<?)`\
type: `EXTRACT`\
commit: [8fc60d81f](https://github.com/google/auto/commit/8fc60d81fe0e46e7e5c96e71d4a93fcadc6bde4f)\
description: `Extract Method private process(validElements ImmutableSetMultimap<Class<? extends Annotation>,Element>) : void extracted from public process(annotations Set<? extends TypeElement>, roundEnv RoundEnvironment) : boolean in class com.google.auto.common.BasicAnnotationProcessor`

