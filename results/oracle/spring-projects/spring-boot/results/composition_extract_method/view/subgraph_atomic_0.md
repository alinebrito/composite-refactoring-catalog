<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#overrideMessageCodesFormat()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public overrideMessageCodesFormat() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `1`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#overrideLocale()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public overrideLocale() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `2`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#overrideDateFormat()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public overrideDateFormat() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `3`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#noLocaleResolver()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public noLocaleResolver() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `4`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#resourceHandlerMappingOverrideAll()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public resourceHandlerMappingOverrideAll() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `5`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#noDateFormat()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public noDateFormat() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `6`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#customContentNegotiatingViewResolver()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public customContentNegotiatingViewResolver() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `7`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#customViewResolver()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public customViewResolver() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `8`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#resourceHandlerMappingOverrideWebjars()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public resourceHandlerMappingOverrideWebjars() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

id: `9`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#noMessageCodesResolver()`\
target: `org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests#load(Class<?>,String...)`\
type: `EXTRACT`\
commit: [cb98ee25f](https://github.com/spring-projects/spring-boot/commit/cb98ee25ff52bf97faebe3f45cdef0ced9b4416e)\
description: `Extract Method private load(config Class<?>, environment String...) : void extracted from public noMessageCodesResolver() : void in class org.springframework.boot.autoconfigure.web.WebMvcAutoConfigurationTests`

