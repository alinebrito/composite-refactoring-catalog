<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#isOperator(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private isOperator(op String) : boolean from class io.undertow.server.handlers.builder.HandlerParser to private isOperator(op String) : boolean from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `1`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#tokenize(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method package tokenize(string String) : Deque<Token> from class io.undertow.server.handlers.builder.HandlerParser to public tokenize(string String) : Deque<Token> from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `2`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#coerceToType(String,Token,Class<?>,ExchangeAttributeParser)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private coerceToType(string String, token Token, type Class<?>, attributeParser ExchangeAttributeParser) : Object from class io.undertow.server.handlers.builder.HandlerParser to private coerceToType(string String, token Token, type Class<?>, attributeParser ExchangeAttributeParser) : Object from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `3`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#precedence(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private precedence(operator String) : int from class io.undertow.server.handlers.builder.HandlerParser to private precedence(operator String) : int from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `4`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#isSpecialChar(String)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private isSpecialChar(token String) : boolean from class io.undertow.server.handlers.builder.HandlerParser to private isSpecialChar(token String) : boolean from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `5`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#handleSingleArrayValue(String,HandlerBuilder,Deque<Token>,Token,ExchangeAttributeParser,String,Token)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private handleSingleArrayValue(string String, builder HandlerBuilder, tokens Deque<Token>, token Token, attributeParser ExchangeAttributeParser, endChar String, last Token) : HandlerWrapper from class io.undertow.server.handlers.builder.HandlerParser to private handleSingleArrayValue(string String, builder Token, tokens Deque<Token>, endChar String) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `6`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#readArrayType(String,Deque<Token>,Token,HandlerBuilder,ExchangeAttributeParser,String,Token)`\
type: `MOVE`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move Method private readArrayType(string String, tokens Deque<Token>, paramName Token, builder HandlerBuilder, attributeParser ExchangeAttributeParser, expectedEndToken String, last Token) : Object from class io.undertow.server.handlers.builder.HandlerParser to private readArrayType(string String, paramName String, value ArrayNode, parser ExchangeAttributeParser, type Class) : Object from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `7`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#loadHandlerBuilders(ClassLoader)`\
type: `MOVE_RENAME`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move And Rename Method private loadBuilders(classLoader ClassLoader) : Map<String,HandlerBuilder> from class io.undertow.server.handlers.builder.HandlerParser to private loadHandlerBuilders(classLoader ClassLoader) : Map<String,HandlerBuilder> from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

id: `8`\
source `io.undertow.server.handlers.builder.HandlerParser`\
target: `io.undertow.server.handlers.builder.PredicatedHandlersParser#parseExpression(String,Token,Deque<Token>)`\
type: `MOVE_RENAME`\
commit: [d5b2bb8cd](https://github.com/undertow-io/undertow/commit/d5b2bb8cd1393f1c5a5bb623e3d8906cd57e53c4)\
description: `Move And Rename Method private parseBuilder(string String, token Token, tokens Deque<Token>, builders Map<String,HandlerBuilder>, attributeParser ExchangeAttributeParser) : HandlerWrapper from class io.undertow.server.handlers.builder.HandlerParser to private parseExpression(string String, token Token, tokens Deque<Token>) : Node from class io.undertow.server.handlers.builder.PredicatedHandlersParser`

