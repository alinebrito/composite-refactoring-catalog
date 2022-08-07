<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.tomcat.util.net.SSLHostConfig`\
target: `org.apache.tomcat.util.net.SSLHostConfigCertificate#getCertificateKeyAlias()`\
type: `MOVE`\
commit: [40f00732b](https://github.com/apache/tomcat/commit/40f00732b9652350ac11830367fd32db67987fc7)\
description: `Move Method public getCertificateKeyAlias() : String from class org.apache.tomcat.util.net.SSLHostConfig to public getCertificateKeyAlias() : String from class org.apache.tomcat.util.net.SSLHostConfigCertificate`

id: `1`\
source `org.apache.tomcat.util.net.SSLHostConfig`\
target: `org.apache.tomcat.util.net.SSLHostConfigCertificate#getCertificateKeystoreFile()`\
type: `MOVE`\
commit: [40f00732b](https://github.com/apache/tomcat/commit/40f00732b9652350ac11830367fd32db67987fc7)\
description: `Move Method public getCertificateKeystoreFile() : String from class org.apache.tomcat.util.net.SSLHostConfig to public getCertificateKeystoreFile() : String from class org.apache.tomcat.util.net.SSLHostConfigCertificate`

id: `2`\
source `org.apache.tomcat.util.net.SSLHostConfig`\
target: `org.apache.tomcat.util.net.SSLHostConfigCertificate#getCertificateKeystorePassword()`\
type: `MOVE`\
commit: [40f00732b](https://github.com/apache/tomcat/commit/40f00732b9652350ac11830367fd32db67987fc7)\
description: `Move Method public getCertificateKeystorePassword() : String from class org.apache.tomcat.util.net.SSLHostConfig to public getCertificateKeystorePassword() : String from class org.apache.tomcat.util.net.SSLHostConfigCertificate`

id: `3`\
source `org.apache.tomcat.util.net.SSLHostConfig`\
target: `org.apache.tomcat.util.net.SSLHostConfigCertificate#getCertificateKeystoreType()`\
type: `MOVE`\
commit: [40f00732b](https://github.com/apache/tomcat/commit/40f00732b9652350ac11830367fd32db67987fc7)\
description: `Move Method public getCertificateKeystoreType() : String from class org.apache.tomcat.util.net.SSLHostConfig to public getCertificateKeystoreType() : String from class org.apache.tomcat.util.net.SSLHostConfigCertificate`

id: `4`\
source `org.apache.tomcat.util.net.SSLHostConfig`\
target: `org.apache.tomcat.util.net.SSLHostConfigCertificate#getCertificateKeystoreProvider()`\
type: `MOVE`\
commit: [40f00732b](https://github.com/apache/tomcat/commit/40f00732b9652350ac11830367fd32db67987fc7)\
description: `Move Method public getCertificateKeystoreProvider() : String from class org.apache.tomcat.util.net.SSLHostConfig to public getCertificateKeystoreProvider() : String from class org.apache.tomcat.util.net.SSLHostConfigCertificate`

