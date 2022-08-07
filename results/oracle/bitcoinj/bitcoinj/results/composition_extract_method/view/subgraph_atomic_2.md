<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[],int)`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeBlock(payloadBytes byte[], length int) : Block extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `1`\
source `org.bitcoinj.core.FullBlockTestGenerator#getBlocksToTest(boolean,boolean,File)`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[],int)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[], length int) : Block extracted from public getBlocksToTest(runBarelyExpensiveTests boolean, runExpensiveTests boolean, blockStorageFile File) : RuleList in class org.bitcoinj.core.FullBlockTestGenerator & moved to class org.bitcoinj.core.BitcoinSerializer`

id: `2`\
source `org.bitcoinj.core.HeadersMessage#parse()`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[],int)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public makeBlock(payloadBytes byte[], length int) : Block extracted from package parse() : void in class org.bitcoinj.core.HeadersMessage & moved to class org.bitcoinj.core.BitcoinSerializer`

