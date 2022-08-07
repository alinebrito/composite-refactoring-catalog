<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#isOperator(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private isOperator(op String) : boolean from class io.undertow.predicate.PredicateParser to private isOperator(op String) : boolean from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `1`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#coerceToType(String,Token,Class<?>,ExchangeAttributeParser)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private coerceToType(string String, token Token, type Class<?>, attributeParser ExchangeAttributeParser) : Object from class io.undertow.predicate.PredicateParser to private coerceToType(string String, token Token, type Class<?>, attributeParser ExchangeAttributeParser) : Object from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `2`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#isSpecialChar(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private isSpecialChar(token String) : boolean from class io.undertow.predicate.PredicateParser to private isSpecialChar(token String) : boolean from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `3`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#precedence(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private precedence(operator String) : int from class io.undertow.predicate.PredicateParser to private precedence(operator String) : int from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `4`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#handleSingleArrayValue(String,PredicateBuilder,Deque<Token>,Token,ExchangeAttributeParser,String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private handleSingleArrayValue(string String, builder PredicateBuilder, tokens Deque<Token>, token Token, attributeParser ExchangeAttributeParser, endChar String) : Node from class io.undertow.predicate.PredicateParser to private handleSingleArrayValue(string String, builder Token, tokens Deque<Token>, endChar String) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `5`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#collapseOutput(Object,Deque<Object>)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private collapseOutput(token Object, tokens Deque<Object>) : Node from class io.undertow.predicate.PredicateParser to private collapseOutput(token Node, tokens Deque<Node>) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `6`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#parse(String,Deque<Token>,Map<String,PredicateBuilder>,ExchangeAttributeParser)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method package parse(string String, tokens Deque<Token>, builders Map<String,PredicateBuilder>, attributeParser ExchangeAttributeParser) : Predicate from class io.undertow.predicate.PredicateParser to package parse(string String, tokens Deque<Token>, topLevel boolean) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `7`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#readArrayType(String,Deque<Token>,Token,PredicateBuilder,ExchangeAttributeParser,String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private readArrayType(string String, tokens Deque<Token>, paramName Token, builder PredicateBuilder, attributeParser ExchangeAttributeParser, expectedEndToken String) : Object from class io.undertow.predicate.PredicateParser to private readArrayType(string String, paramName String, value ArrayNode, parser ExchangeAttributeParser, type Class) : Object from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `8`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#handleSingleVarArgsValue(String,PredicateBuilder,Deque<Token>,Token,ExchangeAttributeParser,String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private handleSingleVarArgsValue(string String, builder PredicateBuilder, tokens Deque<Token>, token Token, attributeParser ExchangeAttributeParser, endChar String) : Node from class io.undertow.predicate.PredicateParser to private handleSingleVarArgsValue(string String, expressionName Token, tokens Deque<Token>, endChar String) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `9`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#loadPredicateBuilders(ClassLoader)`\
type: `MOVE_RENAME`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move And Rename Method private loadBuilders(classLoader ClassLoader) : Map<String,PredicateBuilder> from class io.undertow.predicate.PredicateParser to private loadPredicateBuilders(classLoader ClassLoader) : Map<String,PredicateBuilder> from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `10`\
source `io.undertow.predicate.PredicateParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#parseExpression(String,Token,Deque<Token>)`\
type: `MOVE_RENAME`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move And Rename Method private parsePredicate(string String, token Token, tokens Deque<Token>, builders Map<String,PredicateBuilder>, attributeParser ExchangeAttributeParser) : Object from class io.undertow.predicate.PredicateParser to private parseExpression(string String, token Token, tokens Deque<Token>) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

