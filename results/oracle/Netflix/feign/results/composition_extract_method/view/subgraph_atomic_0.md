<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `feign.DefaultContractTest#formParamsDoesNotSetBodyType()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public formParamsDoesNotSetBodyType() : void in class feign.DefaultContractTest`

id: `1`\
source `feign.DefaultContractTest#headerParamsParseIntoIndexToName()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public headerParamsParseIntoIndexToName() : void in class feign.DefaultContractTest`

id: `2`\
source `feign.DefaultContractTest#customExpander()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public customExpander() : void in class feign.DefaultContractTest`

id: `3`\
source `feign.DefaultContractTest#slashAreEncodedWhenNeeded()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public slashAreEncodedWhenNeeded() : void in class feign.DefaultContractTest`

id: `4`\
source `feign.DefaultContractTest#httpMethods()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public httpMethods() : void in class feign.DefaultContractTest`

id: `5`\
source `feign.DefaultContractTest#bodyParamIsGeneric()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public bodyParamIsGeneric() : void in class feign.DefaultContractTest`

id: `6`\
source `feign.DefaultContractTest#tooManyBodies()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public tooManyBodies() : void in class feign.DefaultContractTest`

id: `7`\
source `feign.DefaultContractTest#customMethodWithoutPath()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public customMethodWithoutPath() : void in class feign.DefaultContractTest`

id: `8`\
source `feign.DefaultContractTest#queryParamsInPathExtract()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public queryParamsInPathExtract() : void in class feign.DefaultContractTest`

id: `9`\
source `feign.DefaultContractTest#bodyWithoutParameters()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public bodyWithoutParameters() : void in class feign.DefaultContractTest`

id: `10`\
source `feign.DefaultContractTest#headersOnMethodAddsContentTypeHeader()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public headersOnMethodAddsContentTypeHeader() : void in class feign.DefaultContractTest`

id: `11`\
source `feign.DefaultContractTest#headersOnTypeAddsContentTypeHeader()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public headersOnTypeAddsContentTypeHeader() : void in class feign.DefaultContractTest`

id: `12`\
source `feign.DefaultContractTest#withPathAndURIParam()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public withPathAndURIParam() : void in class feign.DefaultContractTest`

id: `13`\
source `feign.DefaultContractTest#pathAndQueryParams()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public pathAndQueryParams() : void in class feign.DefaultContractTest`

id: `14`\
source `feign.DefaultContractTest#bodyWithTemplate()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public bodyWithTemplate() : void in class feign.DefaultContractTest`

id: `15`\
source `feign.DefaultContractTest#formParamsParseIntoIndexToName()`\
target: `feign.DefaultContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public formParamsParseIntoIndexToName() : void in class feign.DefaultContractTest`

