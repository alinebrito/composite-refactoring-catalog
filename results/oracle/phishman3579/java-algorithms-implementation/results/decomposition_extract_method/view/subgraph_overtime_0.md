<img src=subgraph_overtime_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.jwetherell.algorithms.sorts.timing.SortsTiming#main(String[])`\
target: `com.jwetherell.algorithms.sorts.timing.SortsTiming#putOutTheGarbage()`\
type: `EXTRACT`\
commit: [f2385a56e](https://github.com/phishman3579/java-algorithms-implementation/commit/f2385a56e6aa040ea4ff18a23ce5b63a4eeacf29)\
description: `Extract Method private putOutTheGarbage() : void extracted from public main(args String[]) : void in class com.jwetherell.algorithms.sorts.timing.SortsTiming`

id: `1`\
source `com.jwetherell.algorithms.sorts.timing.SortsTiming#main(String[])`\
target: `com.jwetherell.algorithms.sorts.timing.SortsTiming#collectGarbage()`\
type: `EXTRACT`\
commit: [4ffcb5a65](https://github.com/phishman3579/java-algorithms-implementation/commit/4ffcb5a65e6d24c58ef75a5cd7692e875619548d)\
description: `Extract Method private collectGarbage() : void extracted from public main(args String[]) : void in class com.jwetherell.algorithms.sorts.timing.SortsTiming`

id: `2`\
source `com.jwetherell.algorithms.sorts.timing.SortsTiming#main(String[])`\
target: `com.jwetherell.algorithms.sorts.timing.SortsTiming#runTest(Testable,Integer[],Integer[],double[],int)`\
type: `EXTRACT`\
commit: [ab98bcacf](https://github.com/phishman3579/java-algorithms-implementation/commit/ab98bcacf6e5bf1c3a06f6bcca68f178f880ffc9)\
description: `Extract Method private runTest(testable Testable, unsorted Integer[], sorted Integer[], results double[], count int) : int extracted from public main(args String[]) : void in class com.jwetherell.algorithms.sorts.timing.SortsTiming`

