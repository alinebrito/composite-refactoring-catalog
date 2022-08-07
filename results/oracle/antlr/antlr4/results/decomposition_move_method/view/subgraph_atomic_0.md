<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.antlr.v4.runtime.tree.Trees`\
target: `org.antlr.v4.gui.Trees#getPS(Tree,List<String>)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public getPS(t Tree, ruleNames List<String>) : String from class org.antlr.v4.runtime.tree.Trees to public getPS(t Tree, ruleNames List<String>) : String from class org.antlr.v4.gui.Trees`

id: `1`\
source `org.antlr.v4.runtime.tree.Trees`\
target: `org.antlr.v4.gui.Trees#writePS(Tree,List<String>,String)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public writePS(t Tree, ruleNames List<String>, fileName String) : void from class org.antlr.v4.runtime.tree.Trees to public writePS(t Tree, ruleNames List<String>, fileName String) : void from class org.antlr.v4.gui.Trees`

id: `2`\
source `org.antlr.v4.runtime.tree.Trees`\
target: `org.antlr.v4.gui.Trees#writePS(Tree,List<String>,String,String,int)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public writePS(t Tree, ruleNames List<String>, fileName String, fontName String, fontSize int) : void from class org.antlr.v4.runtime.tree.Trees to public writePS(t Tree, ruleNames List<String>, fileName String, fontName String, fontSize int) : void from class org.antlr.v4.gui.Trees`

id: `3`\
source `org.antlr.v4.runtime.tree.Trees`\
target: `org.antlr.v4.gui.Trees#getPS(Tree,List<String>,String,int)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public getPS(t Tree, ruleNames List<String>, fontName String, fontSize int) : String from class org.antlr.v4.runtime.tree.Trees to public getPS(t Tree, ruleNames List<String>, fontName String, fontSize int) : String from class org.antlr.v4.gui.Trees`

