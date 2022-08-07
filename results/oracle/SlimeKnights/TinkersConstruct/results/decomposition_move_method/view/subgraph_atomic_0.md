<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `tconstruct.library.modifiers.Modifier`\
target: `tconstruct.library.mantle.RecipeMatchRegistry#addItem(String,int)`\
type: `MOVE`\
commit: [71820e573](https://github.com/SlimeKnights/TinkersConstruct/commit/71820e573134be3fad3935035249cd77c4412f4e)\
description: `Move Method public addItem(oredictItem String, count int) : void from class tconstruct.library.modifiers.Modifier to public addItem(oredictItem String, amountNeeded int, amountMatched int) : void from class tconstruct.library.mantle.RecipeMatchRegistry`

id: `1`\
source `tconstruct.library.modifiers.Modifier`\
target: `tconstruct.library.mantle.RecipeMatchRegistry#addItem(Item,int)`\
type: `MOVE`\
commit: [71820e573](https://github.com/SlimeKnights/TinkersConstruct/commit/71820e573134be3fad3935035249cd77c4412f4e)\
description: `Move Method public addItem(item Item, count int) : void from class tconstruct.library.modifiers.Modifier to public addItem(item Item, amountNeeded int, amountMatched int) : void from class tconstruct.library.mantle.RecipeMatchRegistry`

