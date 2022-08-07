<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration.WebMvcAutoConfigurationAdapter.FaviconConfiguration`\
target: `org.springframework.boot.autoconfigure.web.ResourceProperties#setResourceLoader(ResourceLoader)`\
type: `MOVE`\
commit: [1e464da24](https://github.com/spring-projects/spring-boot/commit/1e464da2480568014a87dd0bac6febe63a76c889)\
description: `Move Method public setResourceLoader(resourceLoader ResourceLoader) : void from class org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration.WebMvcAutoConfigurationAdapter.FaviconConfiguration to public setResourceLoader(resourceLoader ResourceLoader) : void from class org.springframework.boot.autoconfigure.web.ResourceProperties`

id: `1`\
source `org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration.WebMvcAutoConfigurationAdapter.FaviconConfiguration`\
target: `org.springframework.boot.autoconfigure.web.ResourceProperties#getFaviconLocations()`\
type: `MOVE_RENAME`\
commit: [1e464da24](https://github.com/spring-projects/spring-boot/commit/1e464da2480568014a87dd0bac6febe63a76c889)\
description: `Move And Rename Method private getLocations() : List<Resource> from class org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration.WebMvcAutoConfigurationAdapter.FaviconConfiguration to public getFaviconLocations() : List<Resource> from class org.springframework.boot.autoconfigure.web.ResourceProperties`

