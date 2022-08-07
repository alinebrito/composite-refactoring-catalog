<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `io.undertow.util.PredicateTokeniser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#error(String,int,String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method public error(string String, pos int, reason String) : IllegalStateException from class io.undertow.util.PredicateTokeniser to public error(string String, pos int, reason String) : IllegalStateException from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `1`\
source `io.undertow.util.PredicateTokeniser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#tokenize(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method public tokenize(string String) : Deque<Token> from class io.undertow.util.PredicateTokeniser to public tokenize(string String) : Deque<Token> from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

