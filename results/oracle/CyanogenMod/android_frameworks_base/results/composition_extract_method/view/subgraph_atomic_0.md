<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.android.server.am.ActivityManagerService#removeLruProcessLocked(ProcessRecord)`\
target: `com.android.server.am.ActivityManagerService#killProcessGroup(int,int)`\
type: `EXTRACT`\
commit: [5d1a70a4d](https://github.com/CyanogenMod/android_frameworks_base/commit/5d1a70a4d32ac4c96a32535c68c69b20288d8968)\
description: `Extract Method public killProcessGroup(uid int, pid int) : void extracted from package removeLruProcessLocked(app ProcessRecord) : void in class com.android.server.am.ActivityManagerService`

id: `1`\
source `com.android.server.am.ActivityManagerService#appDiedLocked(ProcessRecord,int,IApplicationThread,boolean)`\
target: `com.android.server.am.ActivityManagerService#killProcessGroup(int,int)`\
type: `EXTRACT`\
commit: [5d1a70a4d](https://github.com/CyanogenMod/android_frameworks_base/commit/5d1a70a4d32ac4c96a32535c68c69b20288d8968)\
description: `Extract Method public killProcessGroup(uid int, pid int) : void extracted from package appDiedLocked(app ProcessRecord, pid int, thread IApplicationThread, fromBinderDied boolean) : void in class com.android.server.am.ActivityManagerService`

id: `2`\
source `com.android.server.am.ActivityManagerService#startProcessLocked(String,ApplicationInfo,boolean,int,String,ComponentName,boolean,boolean,int,boolean,String,String,String[],Runnable)`\
target: `com.android.server.am.ActivityManagerService#killProcessGroup(int,int)`\
type: `EXTRACT`\
commit: [5d1a70a4d](https://github.com/CyanogenMod/android_frameworks_base/commit/5d1a70a4d32ac4c96a32535c68c69b20288d8968)\
description: `Extract Method public killProcessGroup(uid int, pid int) : void extracted from package startProcessLocked(processName String, info ApplicationInfo, knownToBeDead boolean, intentFlags int, hostingType String, hostingName ComponentName, allowWhileBooting boolean, isolated boolean, isolatedUid int, keepIfLarge boolean, abiOverride String, entryPoint String, entryPointArgs String[], crashHandler Runnable) : ProcessRecord in class com.android.server.am.ActivityManagerService`

id: `3`\
source `com.android.server.am.ActivityManagerService#crashApplication(ProcessRecord,ApplicationErrorReport.CrashInfo)`\
target: `com.android.server.am.ActivityManagerService#killProcessGroup(int,int)`\
type: `EXTRACT`\
commit: [5d1a70a4d](https://github.com/CyanogenMod/android_frameworks_base/commit/5d1a70a4d32ac4c96a32535c68c69b20288d8968)\
description: `Extract Method public killProcessGroup(uid int, pid int) : void extracted from private crashApplication(r ProcessRecord, crashInfo ApplicationErrorReport.CrashInfo) : void in class com.android.server.am.ActivityManagerService`

id: `4`\
source `com.android.server.am.ProcessRecord#kill(String,boolean)`\
target: `com.android.server.am.ActivityManagerService#killProcessGroup(int,int)`\
type: `EXTRACT_MOVE`\
commit: [5d1a70a4d](https://github.com/CyanogenMod/android_frameworks_base/commit/5d1a70a4d32ac4c96a32535c68c69b20288d8968)\
description: `Extract And Move Method public killProcessGroup(uid int, pid int) : void extracted from package kill(reason String, noisy boolean) : void in class com.android.server.am.ProcessRecord & moved to class com.android.server.am.ActivityManagerService`

