<img src=subgraph_atomic_4.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.BlockTest#testHeaderParse()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testHeaderParse() : void in class org.bitcoinj.core.BlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `1`\
source `org.bitcoinj.core.FullBlockTestGenerator#getBlocksToTest(boolean,boolean,File)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public getBlocksToTest(runBarelyExpensiveTests boolean, runExpensiveTests boolean, blockStorageFile File) : RuleList in class org.bitcoinj.core.FullBlockTestGenerator & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `2`\
source `org.bitcoinj.core.StoredBlock#deserializeCompact(NetworkParameters,ByteBuffer)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public deserializeCompact(params NetworkParameters, buffer ByteBuffer) : StoredBlock in class org.bitcoinj.core.StoredBlock & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `3`\
source `org.bitcoinj.core.BlockTest#testBitcoinSerialization()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testBitcoinSerialization() : void in class org.bitcoinj.core.BlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `4`\
source `org.bitcoinj.core.BlockTest#testDate()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testDate() : void in class org.bitcoinj.core.BlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `5`\
source `org.bitcoinj.store.WalletProtobufSerializerTest#testLastBlockSeenHash()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testLastBlockSeenHash() : void in class org.bitcoinj.store.WalletProtobufSerializerTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `6`\
source `org.bitcoinj.core.FilteredBlock#parse()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from package parse() : void in class org.bitcoinj.core.FilteredBlock & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `7`\
source `org.bitcoinj.core.BlockTest#testBadTransactions()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testBadTransactions() : void in class org.bitcoinj.core.BlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `8`\
source `org.bitcoinj.core.BlockTest#testBlockVerification()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testBlockVerification() : void in class org.bitcoinj.core.BlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `9`\
source `org.bitcoinj.core.BlockTest#testProofOfWork()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testProofOfWork() : void in class org.bitcoinj.core.BlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `10`\
source `org.bitcoinj.store.DatabaseFullPrunedBlockStore#get(Sha256Hash,boolean)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public get(hash Sha256Hash, wasUndoableOnly boolean) : StoredBlock in class org.bitcoinj.store.DatabaseFullPrunedBlockStore & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `11`\
source `org.bitcoinj.utils.BlockFileLoader#loadNextBlock()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from private loadNextBlock() : void in class org.bitcoinj.utils.BlockFileLoader & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `12`\
source `org.bitcoinj.core.CoinbaseBlockTest#testReceiveCoinbaseTransaction()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public testReceiveCoinbaseTransaction() : void in class org.bitcoinj.core.CoinbaseBlockTest & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `13`\
source `org.bitcoinj.core.ChainSplitTest#roundtrip(Block)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from private roundtrip(b2 Block) : Block in class org.bitcoinj.core.ChainSplitTest & moved to class org.bitcoinj.core.BitcoinSerializer`

