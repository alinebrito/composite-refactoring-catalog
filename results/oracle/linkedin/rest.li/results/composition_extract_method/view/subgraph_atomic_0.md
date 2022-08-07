<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.linkedin.restli.examples.TestCompressionServer#testCompressionBetter(Compressor)`\
target: `com.linkedin.restli.examples.TestCompressionServer#addCompressionHeaders(HttpGet,String)`\
type: `EXTRACT`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Extract Method public addCompressionHeaders(getMessage HttpGet, acceptEncoding String) : void extracted from public testCompressionBetter(compressor Compressor) : void in class com.linkedin.restli.examples.TestCompressionServer`

id: `1`\
source `com.linkedin.restli.examples.TestCompressionServer#testAcceptEncoding(String,String)`\
target: `com.linkedin.restli.examples.TestCompressionServer#addCompressionHeaders(HttpGet,String)`\
type: `EXTRACT`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Extract Method public addCompressionHeaders(getMessage HttpGet, acceptEncoding String) : void extracted from public testAcceptEncoding(acceptedEncoding String, contentEncoding String) : void in class com.linkedin.restli.examples.TestCompressionServer`

id: `2`\
source `com.linkedin.restli.examples.TestCompressionServer#testCompressionWorse(Compressor)`\
target: `com.linkedin.restli.examples.TestCompressionServer#addCompressionHeaders(HttpGet,String)`\
type: `EXTRACT`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Extract Method public addCompressionHeaders(getMessage HttpGet, acceptEncoding String) : void extracted from public testCompressionWorse(compressor Compressor) : void in class com.linkedin.restli.examples.TestCompressionServer`

id: `3`\
source `com.linkedin.restli.examples.TestCompressionServer#testCompatibleDefault(String,String)`\
target: `com.linkedin.restli.examples.TestCompressionServer#addCompressionHeaders(HttpGet,String)`\
type: `EXTRACT`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Extract Method public addCompressionHeaders(getMessage HttpGet, acceptEncoding String) : void extracted from public testCompatibleDefault(acceptEncoding String, contentEncoding String) : void in class com.linkedin.restli.examples.TestCompressionServer`

id: `4`\
source `com.linkedin.restli.examples.TestCompressionServer#test406Error(String)`\
target: `com.linkedin.restli.examples.TestCompressionServer#addCompressionHeaders(HttpGet,String)`\
type: `EXTRACT`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Extract Method public addCompressionHeaders(getMessage HttpGet, acceptEncoding String) : void extracted from public test406Error(acceptContent String) : void in class com.linkedin.restli.examples.TestCompressionServer`

