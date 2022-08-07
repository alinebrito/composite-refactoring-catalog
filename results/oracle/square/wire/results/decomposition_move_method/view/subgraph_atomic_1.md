<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.squareup.wire.model.Linker`\
target: `com.squareup.wire.model.Options#resolveFieldPath(String,Set<String>)`\
type: `MOVE`\
commit: [85a690e3c](https://github.com/square/wire/commit/85a690e3cdbbb8447342eefdf690e22ad1b33e02)\
description: `Move Method package resolveFieldPath(name String, fullyQualifiedNames Set<String>) : String[] from class com.squareup.wire.model.Linker to package resolveFieldPath(name String, fullyQualifiedNames Set<String>) : String[] from class com.squareup.wire.model.Options`

id: `1`\
source `com.squareup.wire.model.Linker`\
target: `com.squareup.wire.model.Options#canonicalizeOption(Linker,ProtoTypeName,OptionElement)`\
type: `MOVE_RENAME`\
commit: [85a690e3c](https://github.com/square/wire/commit/85a690e3cdbbb8447342eefdf690e22ad1b33e02)\
description: `Move And Rename Method package fieldPath(packageName String, extensionType ProtoTypeName, fieldPath String) : List<WireField> from class com.squareup.wire.model.Linker to package canonicalizeOption(linker Linker, extensionType ProtoTypeName, option OptionElement) : Map<WireField,Object> from class com.squareup.wire.model.Options`

