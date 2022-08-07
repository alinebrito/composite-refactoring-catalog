<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.linkedin.restli.examples.TestCompressionServer`\
target: `com.linkedin.r2.filter.compression.TestClientCompressionFilter#contentEncodingGeneratorDataProvider()`\
type: `MOVE`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Move Method public contentEncodingGeneratorDataProvider() : Object[][] from class com.linkedin.restli.examples.TestCompressionServer to public contentEncodingGeneratorDataProvider() : Object[][] from class com.linkedin.r2.filter.compression.TestClientCompressionFilter`

id: `1`\
source `com.linkedin.restli.examples.TestCompressionServer`\
target: `com.linkedin.r2.filter.compression.TestClientCompressionFilter#testEncodingGeneration(EncodingType[],String)`\
type: `MOVE`\
commit: [54fa890a6](https://github.com/linkedin/rest.li/commit/54fa890a6af4ccf564fb481d3e1b6ad4d084de9e)\
description: `Move Method public testEncodingGeneration(encoding EncodingType[], acceptEncoding String) : void from class com.linkedin.restli.examples.TestCompressionServer to public testEncodingGeneration(encoding EncodingType[], acceptEncoding String) : void from class com.linkedin.r2.filter.compression.TestClientCompressionFilter`

