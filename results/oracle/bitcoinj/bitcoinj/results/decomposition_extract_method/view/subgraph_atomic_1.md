<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.FullBlockTestGenerator#getBlocksToTest(boolean,boolean,File)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[],int)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[], length int) : Block extracted from public getBlocksToTest(runBarelyExpensiveTests boolean, runExpensiveTests boolean, blockStorageFile File) : RuleList in class org.bitcoinj.core.FullBlockTestGenerator & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `1`\
source `org.bitcoinj.core.FullBlockTestGenerator#getBlocksToTest(boolean,boolean,File)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[])`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[]) : Block extracted from public getBlocksToTest(runBarelyExpensiveTests boolean, runExpensiveTests boolean, blockStorageFile File) : RuleList in class org.bitcoinj.core.FullBlockTestGenerator & moved to class org.bitcoinj.core.BitcoinSerializer`

