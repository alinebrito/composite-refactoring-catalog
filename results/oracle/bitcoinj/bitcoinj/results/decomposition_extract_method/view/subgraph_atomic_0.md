<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeInventoryMessage(byte[],int)`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeInventoryMessage(payloadBytes byte[], length int) : InventoryMessage extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `1`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeAddressMessage(byte[],int)`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeAddressMessage(payloadBytes byte[], length int) : AddressMessage extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `2`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeTransaction(byte[],int,int,byte[])`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeTransaction(payloadBytes byte[], offset int, length int, hash byte[]) : Transaction extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `3`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBlock(byte[],int)`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeBlock(payloadBytes byte[], length int) : Block extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `4`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeBloomFilter(byte[])`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeBloomFilter(payloadBytes byte[]) : Message extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `5`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeAlertMessage(byte[])`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeAlertMessage(payloadBytes byte[]) : Message extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

id: `6`\
source `org.bitcoinj.core.BitcoinSerializer#makeMessage(String,int,byte[],byte[],byte[])`\
target: `org.bitcoinj.core.BitcoinSerializer#makeFilteredBlock(byte[])`\
type: `EXTRACT`\
commit: [12602650c](https://github.com/bitcoinj/bitcoinj/commit/12602650ce99f34cb530fc24266c23e39733b0bb)\
description: `Extract Method public makeFilteredBlock(payloadBytes byte[]) : FilteredBlock extracted from private makeMessage(command String, length int, payloadBytes byte[], hash byte[], checksum byte[]) : Message in class org.bitcoinj.core.BitcoinSerializer`

