<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `jline.console.WCWidth`\
target: `jline.console.ConsoleReader#wcwidth(CharSequence)`\
type: `MOVE`\
commit: [1eb3b624b](https://github.com/jline/jline2/commit/1eb3b624b288a4b1a054420d3efb05b8f1d28517)\
description: `Move Method public wcwidth(cs CharSequence) : int from class jline.console.WCWidth to package wcwidth(str CharSequence, pos int) : int from class jline.console.ConsoleReader`

id: `1`\
source `jline.console.WCWidth`\
target: `jline.console.ConsoleReader#wcwidth(CharSequence,int,int)`\
type: `MOVE`\
commit: [1eb3b624b](https://github.com/jline/jline2/commit/1eb3b624b288a4b1a054420d3efb05b8f1d28517)\
description: `Move Method public wcwidth(cs CharSequence, start int, end int) : int from class jline.console.WCWidth to package wcwidth(str CharSequence, start int, end int, pos int) : int from class jline.console.ConsoleReader`

