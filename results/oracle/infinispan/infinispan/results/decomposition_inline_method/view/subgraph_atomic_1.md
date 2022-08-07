<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.infinispan.client.hotrod.marshall.EmbeddedCompatTest#createAccountPB()`\
target: `org.infinispan.client.hotrod.marshall.EmbeddedCompatTest#testRemoteQuery()`\
type: `INLINE`\
commit: [35b6c8695](https://github.com/infinispan/infinispan/commit/35b6c869546a7968b6fd2f640add6eea87e03c22)\
description: `Inline Method private createAccountPB() : AccountPB inlined to public testRemoteQuery() : void in class org.infinispan.client.hotrod.marshall.EmbeddedCompatTest`

id: `1`\
source `org.infinispan.client.hotrod.marshall.EmbeddedCompatTest#createAccountPB()`\
target: `org.infinispan.client.hotrod.marshall.EmbeddedCompatTest#testPutAndGet()`\
type: `INLINE`\
commit: [35b6c8695](https://github.com/infinispan/infinispan/commit/35b6c869546a7968b6fd2f640add6eea87e03c22)\
description: `Inline Method private createAccountPB() : AccountPB inlined to public testPutAndGet() : void in class org.infinispan.client.hotrod.marshall.EmbeddedCompatTest`

id: `2`\
source `org.infinispan.client.hotrod.marshall.EmbeddedCompatTest#createAccountPB()`\
target: `org.infinispan.client.hotrod.marshall.EmbeddedCompatTest#testEmbeddedLuceneQuery()`\
type: `INLINE`\
commit: [35b6c8695](https://github.com/infinispan/infinispan/commit/35b6c869546a7968b6fd2f640add6eea87e03c22)\
description: `Inline Method private createAccountPB() : AccountPB inlined to public testEmbeddedLuceneQuery() : void in class org.infinispan.client.hotrod.marshall.EmbeddedCompatTest`

