<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.antlr.v4.runtime.RuleContext`\
target: `org.antlr.v4.gui.Trees#save(Parser,String,String,int)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public save(parser Parser, fileName String, fontName String, fontSize int) : void from class org.antlr.v4.runtime.RuleContext to public save(t Tree, parser Parser, fileName String, fontName String, fontSize int) : void from class org.antlr.v4.gui.Trees`

id: `1`\
source `org.antlr.v4.runtime.RuleContext`\
target: `org.antlr.v4.gui.Trees#save(Parser,String)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public save(parser Parser, fileName String) : void from class org.antlr.v4.runtime.RuleContext to public save(t Tree, parser Parser, fileName String) : void from class org.antlr.v4.gui.Trees`

id: `2`\
source `org.antlr.v4.runtime.RuleContext`\
target: `org.antlr.v4.gui.Trees#inspect(List<String>)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public inspect(ruleNames List<String>) : Future<JDialog> from class org.antlr.v4.runtime.RuleContext to public inspect(t Tree, ruleNames List<String>) : Future<JDialog> from class org.antlr.v4.gui.Trees`

id: `3`\
source `org.antlr.v4.runtime.RuleContext`\
target: `org.antlr.v4.gui.Trees#inspect(Parser)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public inspect(parser Parser) : Future<JDialog> from class org.antlr.v4.runtime.RuleContext to public inspect(t Tree, parser Parser) : Future<JDialog> from class org.antlr.v4.gui.Trees`

id: `4`\
source `org.antlr.v4.runtime.RuleContext`\
target: `org.antlr.v4.gui.Trees#save(List<String>,String,String,int)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public save(ruleNames List<String>, fileName String, fontName String, fontSize int) : void from class org.antlr.v4.runtime.RuleContext to public save(t Tree, ruleNames List<String>, fileName String, fontName String, fontSize int) : void from class org.antlr.v4.gui.Trees`

id: `5`\
source `org.antlr.v4.runtime.RuleContext`\
target: `org.antlr.v4.gui.Trees#save(List<String>,String)`\
type: `MOVE`\
commit: [b395127e7](https://github.com/antlr/antlr4/commit/b395127e733b33c27f344695ebf155ecf5edeeab)\
description: `Move Method public save(ruleNames List<String>, fileName String) : void from class org.antlr.v4.runtime.RuleContext to public save(t Tree, ruleNames List<String>, fileName String) : void from class org.antlr.v4.gui.Trees`

