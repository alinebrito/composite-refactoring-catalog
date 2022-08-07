<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.languagetool.gui.ConfigurationDialog#show(List<Rule>)`\
target: `org.languagetool.gui.ConfigurationDialog#getMouseAdapter()`\
type: `EXTRACT`\
commit: [01cddc5af](https://github.com/languagetool-org/languagetool/commit/01cddc5afb590b4d36cb784637a8ea8aa31d3561)\
description: `Extract Method private getMouseAdapter() : MouseAdapter extracted from public show(rules List<Rule>) : void in class org.languagetool.gui.ConfigurationDialog`

id: `1`\
source `org.languagetool.gui.ConfigurationDialog#show(List<Rule>)`\
target: `org.languagetool.gui.ConfigurationDialog#createNonOfficeElements(GridBagConstraints,JPanel)`\
type: `EXTRACT`\
commit: [01cddc5af](https://github.com/languagetool-org/languagetool/commit/01cddc5afb590b4d36cb784637a8ea8aa31d3561)\
description: `Extract Method private createNonOfficeElements(cons GridBagConstraints, portPanel JPanel) : void extracted from public show(rules List<Rule>) : void in class org.languagetool.gui.ConfigurationDialog`

id: `2`\
source `org.languagetool.gui.ConfigurationDialog#show(List<Rule>)`\
target: `org.languagetool.gui.ConfigurationDialog#getMotherTonguePanel(GridBagConstraints)`\
type: `EXTRACT`\
commit: [01cddc5af](https://github.com/languagetool-org/languagetool/commit/01cddc5afb590b4d36cb784637a8ea8aa31d3561)\
description: `Extract Method private getMotherTonguePanel(cons GridBagConstraints) : JPanel extracted from public show(rules List<Rule>) : void in class org.languagetool.gui.ConfigurationDialog`

id: `3`\
source `org.languagetool.gui.ConfigurationDialog#show(List<Rule>)`\
target: `org.languagetool.gui.ConfigurationDialog#getTreeModel(DefaultMutableTreeNode)`\
type: `EXTRACT`\
commit: [01cddc5af](https://github.com/languagetool-org/languagetool/commit/01cddc5afb590b4d36cb784637a8ea8aa31d3561)\
description: `Extract Method private getTreeModel(rootNode DefaultMutableTreeNode) : DefaultTreeModel extracted from public show(rules List<Rule>) : void in class org.languagetool.gui.ConfigurationDialog`

id: `4`\
source `org.languagetool.gui.ConfigurationDialog#show(List<Rule>)`\
target: `org.languagetool.gui.ConfigurationDialog#getTreeButtonPanel()`\
type: `EXTRACT`\
commit: [01cddc5af](https://github.com/languagetool-org/languagetool/commit/01cddc5afb590b4d36cb784637a8ea8aa31d3561)\
description: `Extract Method private getTreeButtonPanel() : JPanel extracted from public show(rules List<Rule>) : void in class org.languagetool.gui.ConfigurationDialog`

