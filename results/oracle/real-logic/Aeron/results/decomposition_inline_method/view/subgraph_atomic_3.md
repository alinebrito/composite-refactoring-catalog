<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `uk.co.real_logic.aeron.driver.DriverConductorTest#verifySenderNotifiedOfNewPublication()`\
target: `uk.co.real_logic.aeron.driver.DriverConductorTest#shouldBeAbleToAddSinglePublication()`\
type: `INLINE`\
commit: [35893c115](https://github.com/real-logic/Aeron/commit/35893c115ba23bd62a7036a33390420f074ce660)\
description: `Inline Method private verifySenderNotifiedOfNewPublication() : void inlined to public shouldBeAbleToAddSinglePublication() : void in class uk.co.real_logic.aeron.driver.DriverConductorTest`

id: `1`\
source `uk.co.real_logic.aeron.driver.DriverConductorTest#verifySenderNotifiedOfNewPublication()`\
target: `uk.co.real_logic.aeron.driver.DriverConductorTest#shouldNotTimeoutPublicationOnKeepAlive()`\
type: `INLINE`\
commit: [35893c115](https://github.com/real-logic/Aeron/commit/35893c115ba23bd62a7036a33390420f074ce660)\
description: `Inline Method private verifySenderNotifiedOfNewPublication() : void inlined to public shouldNotTimeoutPublicationOnKeepAlive() : void in class uk.co.real_logic.aeron.driver.DriverConductorTest`

id: `2`\
source `uk.co.real_logic.aeron.driver.DriverConductorTest#verifySenderNotifiedOfNewPublication()`\
target: `uk.co.real_logic.aeron.driver.DriverConductorTest#shouldTimeoutPublication()`\
type: `INLINE`\
commit: [35893c115](https://github.com/real-logic/Aeron/commit/35893c115ba23bd62a7036a33390420f074ce660)\
description: `Inline Method private verifySenderNotifiedOfNewPublication() : void inlined to public shouldTimeoutPublication() : void in class uk.co.real_logic.aeron.driver.DriverConductorTest`

