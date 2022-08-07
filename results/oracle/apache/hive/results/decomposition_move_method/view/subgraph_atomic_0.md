<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.hive.beeline.BeeLine`\
target: `org.apache.hive.beeline.Commands#getFirstCmd(String,int)`\
type: `MOVE`\
commit: [102b23b16](https://github.com/apache/hive/commit/102b23b16bf26cbf439009b4b95542490a082710)\
description: `Move Method private getFirstCmd(cmd String, length int) : String from class org.apache.hive.beeline.BeeLine to private getFirstCmd(cmd String, length int) : String from class org.apache.hive.beeline.Commands`

id: `1`\
source `org.apache.hive.beeline.BeeLine`\
target: `org.apache.hive.beeline.Commands#sourceFile(String)`\
type: `MOVE`\
commit: [102b23b16](https://github.com/apache/hive/commit/102b23b16bf26cbf439009b4b95542490a082710)\
description: `Move Method private sourceFile(cmd String) : boolean from class org.apache.hive.beeline.BeeLine to private sourceFile(cmd String) : boolean from class org.apache.hive.beeline.Commands`

id: `2`\
source `org.apache.hive.beeline.BeeLine`\
target: `org.apache.hive.beeline.Commands#cliToBeelineCmd(String)`\
type: `MOVE`\
commit: [102b23b16](https://github.com/apache/hive/commit/102b23b16bf26cbf439009b4b95542490a082710)\
description: `Move Method private cliToBeelineCmd(cmd String) : String from class org.apache.hive.beeline.BeeLine to private cliToBeelineCmd(cmd String) : String from class org.apache.hive.beeline.Commands`

id: `3`\
source `org.apache.hive.beeline.BeeLine`\
target: `org.apache.hive.beeline.Commands#isSourceCMD(String)`\
type: `MOVE`\
commit: [102b23b16](https://github.com/apache/hive/commit/102b23b16bf26cbf439009b4b95542490a082710)\
description: `Move Method private isSourceCMD(cmd String) : boolean from class org.apache.hive.beeline.BeeLine to private isSourceCMD(cmd String) : boolean from class org.apache.hive.beeline.Commands`

