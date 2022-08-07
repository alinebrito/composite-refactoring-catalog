<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.lealone.command.ddl.AlterUser#update()`\
target: `org.lealone.command.ddl.CreateUser#setPassword(User,Session,Expression)`\
type: `EXTRACT_MOVE`\
commit: [7a2e0ae5f](https://github.com/codefollower/Lealone/commit/7a2e0ae5f6172cbe34f9bc4a5cde666314ff75dd)\
description: `Extract And Move Method package setPassword(user User, session Session, password Expression) : void extracted from public update() : int in class org.lealone.command.ddl.AlterUser & moved to class org.lealone.command.ddl.CreateUser`

id: `1`\
source `org.lealone.command.ddl.AlterUser#update()`\
target: `org.lealone.command.ddl.CreateUser#setSaltAndHash(User,Session,Expression,Expression)`\
type: `EXTRACT_MOVE`\
commit: [7a2e0ae5f](https://github.com/codefollower/Lealone/commit/7a2e0ae5f6172cbe34f9bc4a5cde666314ff75dd)\
description: `Extract And Move Method package setSaltAndHash(user User, session Session, salt Expression, hash Expression) : void extracted from public update() : int in class org.lealone.command.ddl.AlterUser & moved to class org.lealone.command.ddl.CreateUser`

