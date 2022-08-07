<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.android.internal.os.BatteryStatsImpl#parseProcWakelocks(byte[],int,boolean)`\
target: `com.android.internal.os.BatteryStatsImpl#getKernelWakelockUpdateVersion()`\
type: `EXTRACT`\
commit: [910397f23](https://github.com/CyanogenMod/android_frameworks_base/commit/910397f2390d6821a006991ed6035c76cbc74897)\
description: `Extract Method protected getKernelWakelockUpdateVersion() : int extracted from private parseProcWakelocks(wlBuffer byte[], len int, wakeup_sources boolean) : Map<String,KernelWakelockStats> in class com.android.internal.os.BatteryStatsImpl`

id: `1`\
source `com.android.internal.os.BatteryStatsImpl#parseProcWakelocks(byte[],int,boolean)`\
target: `com.android.internal.os.BatteryStatsImpl#setKernelWakelockUpdateVersion(int)`\
type: `EXTRACT`\
commit: [910397f23](https://github.com/CyanogenMod/android_frameworks_base/commit/910397f2390d6821a006991ed6035c76cbc74897)\
description: `Extract Method protected setKernelWakelockUpdateVersion(kernelWakelockUpdateVersion int) : void extracted from private parseProcWakelocks(wlBuffer byte[], len int, wakeup_sources boolean) : Map<String,KernelWakelockStats> in class com.android.internal.os.BatteryStatsImpl`

