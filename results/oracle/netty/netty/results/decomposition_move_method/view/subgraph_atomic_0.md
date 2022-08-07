<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `io.netty.handler.codec.http.DefaultHttpHeaders.HttpHeadersValidationConverter`\
target: `io.netty.handler.codec.http.DefaultHttpHeaders.HeaderValueConverterAndValidator#validateValueChar(int,char,CharSequence)`\
type: `MOVE`\
commit: [d31fa31cd](https://github.com/netty/netty/commit/d31fa31cdcc5ea2fa96116e3b1265baa180df58a)\
description: `Move Method private validateValueChar(state int, c char, seq CharSequence) : int from class io.netty.handler.codec.http.DefaultHttpHeaders.HttpHeadersValidationConverter to private validateValueChar(seq CharSequence, state int, character char) : int from class io.netty.handler.codec.http.DefaultHttpHeaders.HeaderValueConverterAndValidator`

id: `1`\
source `io.netty.handler.codec.http.DefaultHttpHeaders.HttpHeadersValidationConverter`\
target: `io.netty.handler.codec.http.DefaultHttpHeaders.HeaderValueConverter#convertObject(Object)`\
type: `MOVE`\
commit: [d31fa31cd](https://github.com/netty/netty/commit/d31fa31cdcc5ea2fa96116e3b1265baa180df58a)\
description: `Move Method public convertObject(value Object) : CharSequence from class io.netty.handler.codec.http.DefaultHttpHeaders.HttpHeadersValidationConverter to public convertObject(value Object) : CharSequence from class io.netty.handler.codec.http.DefaultHttpHeaders.HeaderValueConverter`

id: `2`\
source `io.netty.handler.codec.http.DefaultHttpHeaders.HttpHeadersValidationConverter`\
target: `io.netty.handler.codec.http.DefaultHttpHeaders.HeaderValueConverterAndValidator#convertObject(Object)`\
type: `MOVE_RENAME`\
commit: [d31fa31cd](https://github.com/netty/netty/commit/d31fa31cdcc5ea2fa96116e3b1265baa180df58a)\
description: `Move And Rename Method private validateValue(seq CharSequence) : void from class io.netty.handler.codec.http.DefaultHttpHeaders.HttpHeadersValidationConverter to public convertObject(value Object) : CharSequence from class io.netty.handler.codec.http.DefaultHttpHeaders.HeaderValueConverterAndValidator`

