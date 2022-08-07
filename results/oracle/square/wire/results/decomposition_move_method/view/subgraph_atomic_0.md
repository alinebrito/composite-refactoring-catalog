<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.squareup.wire.internal.Util`\
target: `com.squareup.wire.model.Options#optionMatches(List<WireOption>,String,String)`\
type: `MOVE`\
commit: [85a690e3c](https://github.com/square/wire/commit/85a690e3cdbbb8447342eefdf690e22ad1b33e02)\
description: `Move Method public optionMatches(options List<WireOption>, namePattern String, valuePattern String) : boolean from class com.squareup.wire.internal.Util to public optionMatches(namePattern String, valuePattern String) : boolean from class com.squareup.wire.model.Options`

id: `1`\
source `com.squareup.wire.internal.Util`\
target: `com.squareup.wire.model.Options#get(String)`\
type: `MOVE_RENAME`\
commit: [85a690e3c](https://github.com/square/wire/commit/85a690e3cdbbb8447342eefdf690e22ad1b33e02)\
description: `Move And Rename Method public findOption(options List<WireOption>, name String) : WireOption from class com.squareup.wire.internal.Util to public get(name String) : Object from class com.squareup.wire.model.Options`

