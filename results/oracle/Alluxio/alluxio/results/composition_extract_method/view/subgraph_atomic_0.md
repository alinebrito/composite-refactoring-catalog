<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `tachyon.worker.block.meta.StorageDir#addBlockMeta(BlockMeta)`\
target: `tachyon.worker.block.meta.StorageDir#reserveSpace(long)`\
type: `EXTRACT`\
commit: [ed966510c](https://github.com/Alluxio/alluxio/commit/ed966510ccf8441115614e2258aea61df0ea55f5)\
description: `Extract Method private reserveSpace(size long) : void extracted from public addBlockMeta(block BlockMeta) : Optional<BlockMeta> in class tachyon.worker.block.meta.StorageDir`

id: `1`\
source `tachyon.worker.block.meta.StorageDir#addTempBlockMeta(TempBlockMeta)`\
target: `tachyon.worker.block.meta.StorageDir#reserveSpace(long)`\
type: `EXTRACT`\
commit: [ed966510c](https://github.com/Alluxio/alluxio/commit/ed966510ccf8441115614e2258aea61df0ea55f5)\
description: `Extract Method private reserveSpace(size long) : void extracted from public addTempBlockMeta(tempBlockMeta TempBlockMeta) : boolean in class tachyon.worker.block.meta.StorageDir`

