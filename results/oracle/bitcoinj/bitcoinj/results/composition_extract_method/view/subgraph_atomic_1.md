<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.core.Utils#sha256hash160(byte[])`\
target: `org.bitcoinj.core.Utils#newSha256Digest()`\
type: `EXTRACT`\
commit: [2fd96c777](https://github.com/bitcoinj/bitcoinj/commit/2fd96c777164dd812e8b5a4294b162889601df1d)\
description: `Extract Method public newSha256Digest() : MessageDigest extracted from public sha256hash160(input byte[]) : byte[] in class org.bitcoinj.core.Utils`

id: `1`\
source `org.bitcoinj.core.Sha256Hash#hash(byte[])`\
target: `org.bitcoinj.core.Utils#newSha256Digest()`\
type: `EXTRACT_MOVE`\
commit: [2fd96c777](https://github.com/bitcoinj/bitcoinj/commit/2fd96c777164dd812e8b5a4294b162889601df1d)\
description: `Extract And Move Method public newSha256Digest() : MessageDigest extracted from public hash(contents byte[]) : Sha256Hash in class org.bitcoinj.core.Sha256Hash & moved to class org.bitcoinj.core.Utils`

id: `2`\
source `org.bitcoinj.core.CheckpointManager#readBinary(InputStream)`\
target: `org.bitcoinj.core.Utils#newSha256Digest()`\
type: `EXTRACT_MOVE`\
commit: [2fd96c777](https://github.com/bitcoinj/bitcoinj/commit/2fd96c777164dd812e8b5a4294b162889601df1d)\
description: `Extract And Move Method public newSha256Digest() : MessageDigest extracted from private readBinary(inputStream InputStream) : Sha256Hash in class org.bitcoinj.core.CheckpointManager & moved to class org.bitcoinj.core.Utils`

id: `3`\
source `org.bitcoinj.script.Script#executeScript(Transaction,long,Script,LinkedList<byte[]>,boolean)`\
target: `org.bitcoinj.core.Utils#newSha256Digest()`\
type: `EXTRACT_MOVE`\
commit: [2fd96c777](https://github.com/bitcoinj/bitcoinj/commit/2fd96c777164dd812e8b5a4294b162889601df1d)\
description: `Extract And Move Method public newSha256Digest() : MessageDigest extracted from public executeScript(txContainingThis Transaction, index long, script Script, stack LinkedList<byte[]>, enforceNullDummy boolean) : void in class org.bitcoinj.script.Script & moved to class org.bitcoinj.core.Utils`

id: `4`\
source `org.bitcoinj.crypto.MnemonicCode#MnemonicCode(InputStream,String)`\
target: `org.bitcoinj.core.Utils#newSha256Digest()`\
type: `EXTRACT_MOVE`\
commit: [2fd96c777](https://github.com/bitcoinj/bitcoinj/commit/2fd96c777164dd812e8b5a4294b162889601df1d)\
description: `Extract And Move Method public newSha256Digest() : MessageDigest extracted from public MnemonicCode(wordstream InputStream, wordListDigest String) in class org.bitcoinj.crypto.MnemonicCode & moved to class org.bitcoinj.core.Utils`

id: `5`\
source `org.bitcoinj.tools.BuildCheckpoints#writeBinaryCheckpoints(TreeMap<Integer,StoredBlock>,File)`\
target: `org.bitcoinj.core.Utils#newSha256Digest()`\
type: `EXTRACT_MOVE`\
commit: [2fd96c777](https://github.com/bitcoinj/bitcoinj/commit/2fd96c777164dd812e8b5a4294b162889601df1d)\
description: `Extract And Move Method public newSha256Digest() : MessageDigest extracted from private writeBinaryCheckpoints(checkpoints TreeMap<Integer,StoredBlock>, file File) : void in class org.bitcoinj.tools.BuildCheckpoints & moved to class org.bitcoinj.core.Utils`

