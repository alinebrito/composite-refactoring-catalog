<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `tachyon.worker.block.meta.StorageDir#removeTempBlockMeta(TempBlockMeta)`\
target: `tachyon.worker.block.meta.StorageDir#reclaimSpace(long)`\
type: `EXTRACT`\
commit: [ed966510c](https://github.com/Alluxio/alluxio/commit/ed966510ccf8441115614e2258aea61df0ea55f5)\
description: `Extract Method private reclaimSpace(size long) : void extracted from public removeTempBlockMeta(tempBlockMeta TempBlockMeta) : boolean in class tachyon.worker.block.meta.StorageDir`

id: `1`\
source `tachyon.worker.block.meta.StorageDir#removeBlockMeta(BlockMeta)`\
target: `tachyon.worker.block.meta.StorageDir#reclaimSpace(long)`\
type: `EXTRACT`\
commit: [ed966510c](https://github.com/Alluxio/alluxio/commit/ed966510ccf8441115614e2258aea61df0ea55f5)\
description: `Extract Method private reclaimSpace(size long) : void extracted from public removeBlockMeta(block BlockMeta) : boolean in class tachyon.worker.block.meta.StorageDir`
