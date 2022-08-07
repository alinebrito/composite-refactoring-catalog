<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.common.primitives.Longs#tryParse(String)`\
target: `com.google.common.primitives.Longs#tryParse(String,int)`\
type: `EXTRACT`\
commit: [31fc19200](https://github.com/google/guava/commit/31fc19200207ccadc45328037d8a2a62b617c029)\
description: `Extract Method public tryParse(string String, radix int) : Long extracted from public tryParse(string String) : Long in class com.google.common.primitives.Longs`

id: `1`\
source `com.google.common.primitives.Ints#tryParse(String,int)`\
target: `com.google.common.primitives.Longs#tryParse(String,int)`\
type: `EXTRACT_MOVE`\
commit: [31fc19200](https://github.com/google/guava/commit/31fc19200207ccadc45328037d8a2a62b617c029)\
description: `Extract And Move Method public tryParse(string String, radix int) : Long extracted from package tryParse(string String, radix int) : Integer in class com.google.common.primitives.Ints & moved to class com.google.common.primitives.Longs`

