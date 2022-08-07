<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `tachyon.client.BlockOutStreamIntegrationTest#disableLocalWriteTest()`\
target: `tachyon.client.BlockOutStreamIntegrationTest#getBlockOutStream(String,boolean)`\
type: `EXTRACT`\
commit: [b0938501f](https://github.com/Alluxio/alluxio/commit/b0938501f1014cf663e33b44ed5bb9b24d19a358)\
description: `Extract Method private getBlockOutStream(filename String, isLocalWrite boolean) : BlockOutStream extracted from public disableLocalWriteTest() : void in class tachyon.client.BlockOutStreamIntegrationTest`

id: `1`\
source `tachyon.client.BlockOutStreamIntegrationTest#enableLocalWriteTest()`\
target: `tachyon.client.BlockOutStreamIntegrationTest#getBlockOutStream(String,boolean)`\
type: `EXTRACT`\
commit: [b0938501f](https://github.com/Alluxio/alluxio/commit/b0938501f1014cf663e33b44ed5bb9b24d19a358)\
description: `Extract Method private getBlockOutStream(filename String, isLocalWrite boolean) : BlockOutStream extracted from public enableLocalWriteTest() : void in class tachyon.client.BlockOutStreamIntegrationTest`

