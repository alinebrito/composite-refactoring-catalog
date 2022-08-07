<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createCellSignalTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createCellSignalTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

id: `1`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createOpenCellIDTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createOpenCellIDTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

id: `2`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createDefaultMCCTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createDefaultMCCTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

id: `3`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createLocationTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createLocationTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

id: `4`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createSilentSmsTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createSilentSmsTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

id: `5`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createCellTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createCellTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

id: `6`\
source `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#onCreate(SQLiteDatabase)`\
target: `com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper#createEventLogTable(SQLiteDatabase)`\
type: `EXTRACT`\
commit: [e235f884f](https://github.com/SecUpwN/Android-IMSI-Catcher-Detector/commit/e235f884f2e0bc258da77b9c80492ad33386fa86)\
description: `Extract Method private createEventLogTable(database SQLiteDatabase) : void extracted from public onCreate(database SQLiteDatabase) : void in class com.SecUpwN.AIMSICD.adapters.AIMSICDDbAdapter.DbHelper`

