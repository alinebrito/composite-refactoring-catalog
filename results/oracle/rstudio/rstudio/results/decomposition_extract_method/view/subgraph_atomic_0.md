<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel#init(AceEditorWidget,Position)`\
target: `org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel#getBoolean(String)`\
type: `EXTRACT`\
commit: [9a581e07c](https://github.com/rstudio/rstudio/commit/9a581e07cb6381d70f3fd9bb2055e810e2a682a9)\
description: `Extract Method private getBoolean(key String) : boolean extracted from public init(widget AceEditorWidget, position Position) : void in class org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel`

id: `1`\
source `org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel#init(AceEditorWidget,Position)`\
target: `org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel#has(String)`\
type: `EXTRACT`\
commit: [9a581e07c](https://github.com/rstudio/rstudio/commit/9a581e07cb6381d70f3fd9bb2055e810e2a682a9)\
description: `Extract Method private has(key String) : boolean extracted from public init(widget AceEditorWidget, position Position) : void in class org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel`

id: `2`\
source `org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel#init(AceEditorWidget,Position)`\
target: `org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel#get(String)`\
type: `EXTRACT`\
commit: [9a581e07c](https://github.com/rstudio/rstudio/commit/9a581e07cb6381d70f3fd9bb2055e810e2a682a9)\
description: `Extract Method public get(key String) : String extracted from public init(widget AceEditorWidget, position Position) : void in class org.rstudio.studio.client.workbench.views.source.editors.text.ChunkOptionsPopupPanel`

