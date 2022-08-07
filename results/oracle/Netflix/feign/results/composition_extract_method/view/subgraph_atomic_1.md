<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `feign.jaxrs.JAXRSContractTest#httpMethods()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public httpMethods() : void in class feign.jaxrs.JAXRSContractTest`

id: `1`\
source `feign.jaxrs.JAXRSContractTest#customMethodWithoutPath()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public customMethodWithoutPath() : void in class feign.jaxrs.JAXRSContractTest`

id: `2`\
source `feign.jaxrs.JAXRSContractTest#queryParamsInPathExtract()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public queryParamsInPathExtract() : void in class feign.jaxrs.JAXRSContractTest`

id: `3`\
source `feign.jaxrs.JAXRSContractTest#producesAddsAcceptHeader()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public producesAddsAcceptHeader() : void in class feign.jaxrs.JAXRSContractTest`

id: `4`\
source `feign.jaxrs.JAXRSContractTest#producesNada()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public producesNada() : void in class feign.jaxrs.JAXRSContractTest`

id: `5`\
source `feign.jaxrs.JAXRSContractTest#producesEmpty()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public producesEmpty() : void in class feign.jaxrs.JAXRSContractTest`

id: `6`\
source `feign.jaxrs.JAXRSContractTest#consumesAddsContentTypeHeader()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public consumesAddsContentTypeHeader() : void in class feign.jaxrs.JAXRSContractTest`

id: `7`\
source `feign.jaxrs.JAXRSContractTest#consumesNada()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public consumesNada() : void in class feign.jaxrs.JAXRSContractTest`

id: `8`\
source `feign.jaxrs.JAXRSContractTest#consumesEmpty()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public consumesEmpty() : void in class feign.jaxrs.JAXRSContractTest`

id: `9`\
source `feign.jaxrs.JAXRSContractTest#bodyParamIsGeneric()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public bodyParamIsGeneric() : void in class feign.jaxrs.JAXRSContractTest`

id: `10`\
source `feign.jaxrs.JAXRSContractTest#tooManyBodies()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public tooManyBodies() : void in class feign.jaxrs.JAXRSContractTest`

id: `11`\
source `feign.jaxrs.JAXRSContractTest#emptyPathOnType()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public emptyPathOnType() : void in class feign.jaxrs.JAXRSContractTest`

id: `12`\
source `feign.jaxrs.JAXRSContractTest#emptyPathParam()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public emptyPathParam() : void in class feign.jaxrs.JAXRSContractTest`

id: `13`\
source `feign.jaxrs.JAXRSContractTest#pathParamWithSpaces()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public pathParamWithSpaces() : void in class feign.jaxrs.JAXRSContractTest`

id: `14`\
source `feign.jaxrs.JAXRSContractTest#regexPathOnMethod()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public regexPathOnMethod() : void in class feign.jaxrs.JAXRSContractTest`

id: `15`\
source `feign.jaxrs.JAXRSContractTest#withPathAndURIParams()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public withPathAndURIParams() : void in class feign.jaxrs.JAXRSContractTest`

id: `16`\
source `feign.jaxrs.JAXRSContractTest#pathAndQueryParams()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public pathAndQueryParams() : void in class feign.jaxrs.JAXRSContractTest`

id: `17`\
source `feign.jaxrs.JAXRSContractTest#emptyQueryParam()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public emptyQueryParam() : void in class feign.jaxrs.JAXRSContractTest`

id: `18`\
source `feign.jaxrs.JAXRSContractTest#formParamsParseIntoIndexToName()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public formParamsParseIntoIndexToName() : void in class feign.jaxrs.JAXRSContractTest`

id: `19`\
source `feign.jaxrs.JAXRSContractTest#formParamsDoesNotSetBodyType()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public formParamsDoesNotSetBodyType() : void in class feign.jaxrs.JAXRSContractTest`

id: `20`\
source `feign.jaxrs.JAXRSContractTest#emptyFormParam()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public emptyFormParam() : void in class feign.jaxrs.JAXRSContractTest`

id: `21`\
source `feign.jaxrs.JAXRSContractTest#headerParamsParseIntoIndexToName()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public headerParamsParseIntoIndexToName() : void in class feign.jaxrs.JAXRSContractTest`

id: `22`\
source `feign.jaxrs.JAXRSContractTest#emptyHeaderParam()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public emptyHeaderParam() : void in class feign.jaxrs.JAXRSContractTest`

id: `23`\
source `feign.jaxrs.JAXRSContractTest#pathsWithoutSlashesParseCorrectly()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public pathsWithoutSlashesParseCorrectly() : void in class feign.jaxrs.JAXRSContractTest`

id: `24`\
source `feign.jaxrs.JAXRSContractTest#pathsWithSomeSlashesParseCorrectly()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public pathsWithSomeSlashesParseCorrectly() : void in class feign.jaxrs.JAXRSContractTest`

id: `25`\
source `feign.jaxrs.JAXRSContractTest#pathsWithSomeOtherSlashesParseCorrectly()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public pathsWithSomeOtherSlashesParseCorrectly() : void in class feign.jaxrs.JAXRSContractTest`

id: `26`\
source `feign.jaxrs.JAXRSContractTest#classWithRootPathParsesCorrectly()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public classWithRootPathParsesCorrectly() : void in class feign.jaxrs.JAXRSContractTest`

id: `27`\
source `feign.jaxrs.JAXRSContractTest#classPathWithTrailingSlashParsesCorrectly()`\
target: `feign.jaxrs.JAXRSContractTest#parseAndValidateMetadata(Class<?>,String,Class<?>...)`\
type: `EXTRACT`\
commit: [b2b408534](https://github.com/Netflix/feign/commit/b2b4085348de32f10903970dded99fdf0376a43c)\
description: `Extract Method private parseAndValidateMetadata(targetType Class<?>, method String, parameterTypes Class<?>...) : MethodMetadata extracted from public classPathWithTrailingSlashParsesCorrectly() : void in class feign.jaxrs.JAXRSContractTest`

