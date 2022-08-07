<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.gh4a.utils.StringUtils`\
target: `com.gh4a.activities.FileViewerActivity#highlightImage(String)`\
type: `MOVE`\
commit: [b8fffb706](https://github.com/slapperwan/gh4a/commit/b8fffb706258db4c4d2f608d8e8dad9312e2230d)\
description: `Move Method public highlightImage(imageUrl String) : String from class com.gh4a.utils.StringUtils to private highlightImage(imageUrl String) : String from class com.gh4a.activities.FileViewerActivity`

id: `1`\
source `com.gh4a.utils.StringUtils`\
target: `com.gh4a.activities.WebViewerActivity#writeCssInclude(StringBuilder,String)`\
type: `MOVE`\
commit: [b8fffb706](https://github.com/slapperwan/gh4a/commit/b8fffb706258db4c4d2f608d8e8dad9312e2230d)\
description: `Move Method private writeCssInclude(builder StringBuilder, cssType String) : void from class com.gh4a.utils.StringUtils to protected writeCssInclude(builder StringBuilder, cssType String) : void from class com.gh4a.activities.WebViewerActivity`

id: `2`\
source `com.gh4a.utils.StringUtils`\
target: `com.gh4a.activities.WebViewerActivity#writeScriptInclude(StringBuilder,String)`\
type: `MOVE`\
commit: [b8fffb706](https://github.com/slapperwan/gh4a/commit/b8fffb706258db4c4d2f608d8e8dad9312e2230d)\
description: `Move Method private writeScriptInclude(builder StringBuilder, scriptName String) : void from class com.gh4a.utils.StringUtils to protected writeScriptInclude(builder StringBuilder, scriptName String) : void from class com.gh4a.activities.WebViewerActivity`

id: `3`\
source `com.gh4a.utils.StringUtils`\
target: `com.gh4a.activities.WebViewerActivity#loadCode(String,String,String,String,String)`\
type: `MOVE_RENAME`\
commit: [b8fffb706](https://github.com/slapperwan/gh4a/commit/b8fffb706258db4c4d2f608d8e8dad9312e2230d)\
description: `Move And Rename Method public highlightSyntax(data String, fileName String, repoOwner String, repoName String, ref String) : String from class com.gh4a.utils.StringUtils to protected loadCode(data String, fileName String, repoOwner String, repoName String, ref String) : void from class com.gh4a.activities.WebViewerActivity`

