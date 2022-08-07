<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.bitcoinj.protocols.channels.StoredPaymentChannelClientStates#removeChannel(StoredClientChannel)`\
target: `org.bitcoinj.protocols.channels.StoredPaymentChannelClientStates#updatedChannel(StoredClientChannel)`\
type: `EXTRACT`\
commit: [1d96e1ad1](https://github.com/bitcoinj/bitcoinj/commit/1d96e1ad1dca6e2151603e10515bb04f0c2730fc)\
description: `Extract Method package updatedChannel(channel StoredClientChannel) : void extracted from package removeChannel(channel StoredClientChannel) : void in class org.bitcoinj.protocols.channels.StoredPaymentChannelClientStates`

id: `1`\
source `org.bitcoinj.protocols.channels.StoredPaymentChannelClientStates#putChannel(StoredClientChannel,boolean)`\
target: `org.bitcoinj.protocols.channels.StoredPaymentChannelClientStates#updatedChannel(StoredClientChannel)`\
type: `EXTRACT`\
commit: [1d96e1ad1](https://github.com/bitcoinj/bitcoinj/commit/1d96e1ad1dca6e2151603e10515bb04f0c2730fc)\
description: `Extract Method package updatedChannel(channel StoredClientChannel) : void extracted from private putChannel(channel StoredClientChannel, updateWallet boolean) : void in class org.bitcoinj.protocols.channels.StoredPaymentChannelClientStates`

