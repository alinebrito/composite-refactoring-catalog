<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.hibernate.jpa.test.callbacks.CallbacksTest`\
target: `org.hibernate.jpa.test.instrument.cases.TestLazyPropertyOnPreUpdateExecutable#checkLazyField(EntityWithLazyProperty,EntityManager,byte[])`\
type: `MOVE`\
commit: [0b6ea757e](https://github.com/hibernate/hibernate-orm/commit/0b6ea757e34a63b1421b77ed5fbb61398377aab1)\
description: `Move Method private checkLazyField(entity EntityWithLazyProperty, em EntityManager, expected byte[]) : void from class org.hibernate.jpa.test.callbacks.CallbacksTest to private checkLazyField(entity EntityWithLazyProperty, em EntityManager, expected byte[]) : void from class org.hibernate.jpa.test.instrument.cases.TestLazyPropertyOnPreUpdateExecutable`

id: `1`\
source `org.hibernate.jpa.test.callbacks.CallbacksTest`\
target: `org.hibernate.jpa.test.instrument.cases.TestLazyPropertyOnPreUpdateExecutable#execute()`\
type: `MOVE_RENAME`\
commit: [0b6ea757e](https://github.com/hibernate/hibernate-orm/commit/0b6ea757e34a63b1421b77ed5fbb61398377aab1)\
description: `Move And Rename Method public testJpaFlushEntityEventListener() : void from class org.hibernate.jpa.test.callbacks.CallbacksTest to public execute() : void from class org.hibernate.jpa.test.instrument.cases.TestLazyPropertyOnPreUpdateExecutable`

