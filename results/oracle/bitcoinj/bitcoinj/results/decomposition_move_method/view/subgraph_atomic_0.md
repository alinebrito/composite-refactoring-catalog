<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.Utils`\
target: `org.bitcoinj.core.Sha256Hash#newDigest()`\
type: `MOVE_RENAME`\
commit: [a6601066d](https://github.com/bitcoinj/bitcoinj/commit/a6601066ddc72ef8e71c46c5a51e1252ea0a1af5)\
description: `Move And Rename Method public newSha256Digest() : MessageDigest from class org.bitcoinj.core.Utils to public newDigest() : MessageDigest from class org.bitcoinj.core.Sha256Hash`

id: `1`\
source `org.bitcoinj.core.Utils`\
target: `org.bitcoinj.core.Sha256Hash#calcHashBytes(byte[],int,int)`\
type: `MOVE_RENAME`\
commit: [a6601066d](https://github.com/bitcoinj/bitcoinj/commit/a6601066ddc72ef8e71c46c5a51e1252ea0a1af5)\
description: `Move And Rename Method public singleDigest(input byte[], offset int, length int) : byte[] from class org.bitcoinj.core.Utils to public calcHashBytes(input byte[], offset int, length int) : byte[] from class org.bitcoinj.core.Sha256Hash`

id: `2`\
source `org.bitcoinj.core.Utils`\
target: `org.bitcoinj.core.Sha256Hash#calcDoubleHashBytes(byte[],int,int)`\
type: `MOVE_RENAME`\
commit: [a6601066d](https://github.com/bitcoinj/bitcoinj/commit/a6601066ddc72ef8e71c46c5a51e1252ea0a1af5)\
description: `Move And Rename Method public doubleDigest(input byte[], offset int, length int) : byte[] from class org.bitcoinj.core.Utils to public calcDoubleHashBytes(input byte[], offset int, length int) : byte[] from class org.bitcoinj.core.Sha256Hash`

id: `3`\
source `org.bitcoinj.core.Utils`\
target: `org.bitcoinj.core.Sha256Hash#calcDoubleHashBytes(byte[],int,int,byte[],int,int)`\
type: `MOVE_RENAME`\
commit: [a6601066d](https://github.com/bitcoinj/bitcoinj/commit/a6601066ddc72ef8e71c46c5a51e1252ea0a1af5)\
description: `Move And Rename Method public doubleDigestTwoBuffers(input1 byte[], offset1 int, length1 int, input2 byte[], offset2 int, length2 int) : byte[] from class org.bitcoinj.core.Utils to public calcDoubleHashBytes(input1 byte[], offset1 int, length1 int, input2 byte[], offset2 int, length2 int) : byte[] from class org.bitcoinj.core.Sha256Hash`

id: `4`\
source `org.bitcoinj.core.Utils`\
target: `org.bitcoinj.core.Sha256Hash#calcDoubleHashBytes(byte[])`\
type: `MOVE_RENAME`\
commit: [a6601066d](https://github.com/bitcoinj/bitcoinj/commit/a6601066ddc72ef8e71c46c5a51e1252ea0a1af5)\
description: `Move And Rename Method public doubleDigest(input byte[]) : byte[] from class org.bitcoinj.core.Utils to public calcDoubleHashBytes(input byte[]) : byte[] from class org.bitcoinj.core.Sha256Hash`

id: `5`\
source `org.bitcoinj.core.Utils`\
target: `org.bitcoinj.core.Sha256Hash#calcHashBytes(byte[])`\
type: `MOVE_RENAME`\
commit: [a6601066d](https://github.com/bitcoinj/bitcoinj/commit/a6601066ddc72ef8e71c46c5a51e1252ea0a1af5)\
description: `Move And Rename Method public singleDigest(input byte[]) : byte[] from class org.bitcoinj.core.Utils to public calcHashBytes(input byte[]) : byte[] from class org.bitcoinj.core.Sha256Hash`

