<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.cli.compiler.grape.SettingsXmlRepositorySystemSessionAutoConfiguration`\
target: `org.springframework.boot.cli.compiler.MavenSettingsReader#MavenSettingsReader()`\
type: `MOVE_RENAME`\
commit: [849375517](https://github.com/spring-projects/spring-boot/commit/84937551787072a4befac29fb48436b3187ac4c6)\
description: `Move And Rename Method public SettingsXmlRepositorySystemSessionAutoConfiguration() from class org.springframework.boot.cli.compiler.grape.SettingsXmlRepositorySystemSessionAutoConfiguration to public MavenSettingsReader() from class org.springframework.boot.cli.compiler.MavenSettingsReader`

id: `1`\
source `org.springframework.boot.cli.compiler.grape.SettingsXmlRepositorySystemSessionAutoConfiguration`\
target: `org.springframework.boot.cli.compiler.MavenSettingsReader#MavenSettingsReader(String)`\
type: `MOVE_RENAME`\
commit: [849375517](https://github.com/spring-projects/spring-boot/commit/84937551787072a4befac29fb48436b3187ac4c6)\
description: `Move And Rename Method package SettingsXmlRepositorySystemSessionAutoConfiguration(homeDir String) from class org.springframework.boot.cli.compiler.grape.SettingsXmlRepositorySystemSessionAutoConfiguration to public MavenSettingsReader(homeDir String) from class org.springframework.boot.cli.compiler.MavenSettingsReader`

