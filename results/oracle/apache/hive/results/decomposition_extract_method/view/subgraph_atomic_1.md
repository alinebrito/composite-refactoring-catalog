<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.hive.beeline.Commands#execute(String,boolean,boolean)`\
target: `org.apache.hive.beeline.Commands#executeInternal(String,boolean)`\
type: `EXTRACT`\
commit: [102b23b16](https://github.com/apache/hive/commit/102b23b16bf26cbf439009b4b95542490a082710)\
description: `Extract Method private executeInternal(sql String, call boolean) : boolean extracted from private execute(line String, call boolean, entireLineAsCommand boolean) : boolean in class org.apache.hive.beeline.Commands`

id: `1`\
source `org.apache.hive.beeline.Commands#execute(String,boolean,boolean)`\
target: `org.apache.hive.beeline.Commands#handleMultiLineCmd(String)`\
type: `EXTRACT`\
commit: [102b23b16](https://github.com/apache/hive/commit/102b23b16bf26cbf439009b4b95542490a082710)\
description: `Extract Method public handleMultiLineCmd(line String) : String extracted from private execute(line String, call boolean, entireLineAsCommand boolean) : boolean in class org.apache.hive.beeline.Commands`

