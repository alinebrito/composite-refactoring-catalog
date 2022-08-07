<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.BitcoinSerializerTest#testLazyParsing()`\
target: `org.bitcoinj.params.AbstractBitcoinNetParams#getSerializer(boolean,boolean)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public getSerializer(parseLazy boolean, parseRetain boolean) : BitcoinSerializer extracted from public testLazyParsing() : void in class org.bitcoinj.core.BitcoinSerializerTest & moved to class org.bitcoinj.params.AbstractBitcoinNetParams`

id: `1`\
source `org.bitcoinj.core.BitcoinSerializerTest#testCachedParsing(boolean)`\
target: `org.bitcoinj.params.AbstractBitcoinNetParams#getSerializer(boolean,boolean)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public getSerializer(parseLazy boolean, parseRetain boolean) : BitcoinSerializer extracted from private testCachedParsing(lazy boolean) : void in class org.bitcoinj.core.BitcoinSerializerTest & moved to class org.bitcoinj.params.AbstractBitcoinNetParams`

id: `2`\
source `org.bitcoinj.core.LazyParseByteCacheTest#testTransaction(NetworkParameters,byte[],boolean,boolean,boolean)`\
target: `org.bitcoinj.params.AbstractBitcoinNetParams#getSerializer(boolean,boolean)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public getSerializer(parseLazy boolean, parseRetain boolean) : BitcoinSerializer extracted from public testTransaction(params NetworkParameters, txBytes byte[], isChild boolean, lazy boolean, retain boolean) : void in class org.bitcoinj.core.LazyParseByteCacheTest & moved to class org.bitcoinj.params.AbstractBitcoinNetParams`

id: `3`\
source `org.bitcoinj.core.LazyParseByteCacheTest#testBlock(byte[],boolean,boolean,boolean)`\
target: `org.bitcoinj.params.AbstractBitcoinNetParams#getSerializer(boolean,boolean)`\
type: `EXTRACT_MOVE`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract And Move Method public getSerializer(parseLazy boolean, parseRetain boolean) : BitcoinSerializer extracted from public testBlock(blockBytes byte[], isChild boolean, lazy boolean, retain boolean) : void in class org.bitcoinj.core.LazyParseByteCacheTest & moved to class org.bitcoinj.params.AbstractBitcoinNetParams`

