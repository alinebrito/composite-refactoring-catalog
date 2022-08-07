<img src=subgraph_atomic_5.svg width=25%>

## Refactorings:

id: `0`\
source `uk.co.real_logic.aeron.driver.DriverConductorTest#verifyReceiverSubscribes()`\
target: `uk.co.real_logic.aeron.driver.DriverConductorTest#shouldNotTimeoutSubscriptionOnKeepAlive()`\
type: `INLINE`\
commit: [35893c115](https://github.com/real-logic/Aeron/commit/35893c115ba23bd62a7036a33390420f074ce660)\
description: `Inline Method private verifyReceiverSubscribes() : void inlined to public shouldNotTimeoutSubscriptionOnKeepAlive() : void in class uk.co.real_logic.aeron.driver.DriverConductorTest`

id: `1`\
source `uk.co.real_logic.aeron.driver.DriverConductorTest#verifyReceiverSubscribes()`\
target: `uk.co.real_logic.aeron.driver.DriverConductorTest#shouldTimeoutSubscription()`\
type: `INLINE`\
commit: [35893c115](https://github.com/real-logic/Aeron/commit/35893c115ba23bd62a7036a33390420f074ce660)\
description: `Inline Method private verifyReceiverSubscribes() : void inlined to public shouldTimeoutSubscription() : void in class uk.co.real_logic.aeron.driver.DriverConductorTest`

