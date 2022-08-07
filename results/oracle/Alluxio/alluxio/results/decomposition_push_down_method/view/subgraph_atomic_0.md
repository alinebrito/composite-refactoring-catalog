<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `tachyon.worker.block.meta.BlockMetaBase#getBlockSize()`\
target: `tachyon.worker.block.meta.BlockMeta#getBlockSize()`\
type: `PUSH_DOWN`\
commit: [6d1062146](https://github.com/Alluxio/alluxio/commit/6d10621465c0e6ae81ad8d240d70a55c72caeea6)\
description: `Push Down Method public getBlockSize() : long from class tachyon.worker.block.meta.BlockMetaBase to public getBlockSize() : long from class tachyon.worker.block.meta.BlockMeta`

id: `1`\
source `tachyon.worker.block.meta.BlockMetaBase#getBlockSize()`\
target: `tachyon.worker.block.meta.TempBlockMeta#getBlockSize()`\
type: `PUSH_DOWN`\
commit: [6d1062146](https://github.com/Alluxio/alluxio/commit/6d10621465c0e6ae81ad8d240d70a55c72caeea6)\
description: `Push Down Method public getBlockSize() : long from class tachyon.worker.block.meta.BlockMetaBase to public getBlockSize() : long from class tachyon.worker.block.meta.TempBlockMeta`

