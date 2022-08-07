<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#resourceHandlerMappingDisabled()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public resourceHandlerMappingDisabled() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `1`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#faviconMappingDisabled()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public faviconMappingDisabled() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `2`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#customAsyncRequestTimeout()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public customAsyncRequestTimeout() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `3`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#ignoreDefaultModelOnRedirectIsTrue()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public ignoreDefaultModelOnRedirectIsTrue() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `4`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#handerAdaptersCreated()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public handerAdaptersCreated() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `5`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#handerMappingsCreated()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public handerMappingsCreated() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `6`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#resourceHandlerMapping()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public resourceHandlerMapping() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `7`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#faviconMapping()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public faviconMapping() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `8`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#defaultAsyncRequestTimeout()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(environment String...) : void extracted from public defaultAsyncRequestTimeout() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

