<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder#visitTag(Tag,IParseDictionary)`\
target: `org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder#visitTagParse(Tag,IParseDictionary)`\
type: `EXTRACT`\
commit: [3b1f4e56f](https://github.com/AdoptOpenJDK/jitwatch/commit/3b1f4e56fea289860b31ef83ccfe96a3a003cc8b)\
description: `Extract Method private visitTagParse(tag Tag, parseDictionary IParseDictionary) : void extracted from public visitTag(tag Tag, parseDictionary IParseDictionary) : void in class org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder`

id: `1`\
source `org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder#visitTag(Tag,IParseDictionary)`\
target: `org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder#visitTagEliminateAllocation(Tag,IParseDictionary)`\
type: `EXTRACT`\
commit: [3b1f4e56f](https://github.com/AdoptOpenJDK/jitwatch/commit/3b1f4e56fea289860b31ef83ccfe96a3a003cc8b)\
description: `Extract Method private visitTagEliminateAllocation(tag Tag, parseDictionary IParseDictionary) : void extracted from public visitTag(tag Tag, parseDictionary IParseDictionary) : void in class org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder`

id: `2`\
source `org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder#visitTag(Tag,IParseDictionary)`\
target: `org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder#visitTagEliminateLock(Tag,IParseDictionary)`\
type: `EXTRACT`\
commit: [3b1f4e56f](https://github.com/AdoptOpenJDK/jitwatch/commit/3b1f4e56fea289860b31ef83ccfe96a3a003cc8b)\
description: `Extract Method private visitTagEliminateLock(tag Tag, parseDictionary IParseDictionary) : void extracted from public visitTag(tag Tag, parseDictionary IParseDictionary) : void in class org.adoptopenjdk.jitwatch.model.bytecode.BytecodeAnnotationBuilder`

