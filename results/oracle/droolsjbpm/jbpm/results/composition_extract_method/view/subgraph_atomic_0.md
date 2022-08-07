<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.jbpm.services.task.LifeCycleBaseTest#testActivateFromIncorrectStatus()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testActivateFromIncorrectStatus() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `1`\
source `org.jbpm.services.task.LifeCycleBaseTest#testNominateToUser()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testNominateToUser() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `2`\
source `org.jbpm.services.task.LifeCycleBaseTest#testCompleteWithComments()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testCompleteWithComments() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `3`\
source `org.jbpm.services.task.LifeCycleBaseTest#testForwardFromReserved()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testForwardFromReserved() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `4`\
source `org.jbpm.services.task.LifeCycleBaseTest#testDelegateFromReserved()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testDelegateFromReserved() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `5`\
source `org.jbpm.services.task.LifeCycleBaseTest#testNominateOnOtherThanCreated()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testNominateOnOtherThanCreated() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `6`\
source `org.jbpm.services.task.LifeCycleBaseTest#testForwardFromReservedWithIncorrectUser()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testForwardFromReservedWithIncorrectUser() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `7`\
source `org.jbpm.services.task.LifeCycleBaseTest#testRemoveNotInRecipientList()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testRemoveNotInRecipientList() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `8`\
source `org.jbpm.services.task.LifeCycleBaseTest#testNominateWithIncorrectUser()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testNominateWithIncorrectUser() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `9`\
source `org.jbpm.services.task.LifeCycleBaseTest#testDelegateFromReady()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testDelegateFromReady() : void in class org.jbpm.services.task.LifeCycleBaseTest`

id: `10`\
source `org.jbpm.services.task.LifeCycleBaseTest#testDelegateFromReservedWithIncorrectUser()`\
target: `org.jbpm.services.task.LifeCycleBaseTest#createUser(String)`\
type: `EXTRACT`\
commit: [a739d16d3](https://github.com/droolsjbpm/jbpm/commit/a739d16d301f0e89ab0b9dfa56b4585bbad6b793)\
description: `Extract Method private createUser(id String) : User extracted from public testDelegateFromReservedWithIncorrectUser() : void in class org.jbpm.services.task.LifeCycleBaseTest`

