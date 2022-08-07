<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.android.internal.os.BatteryStatsImpl#readSummaryFromParcel(Parcel)`\
target: `com.android.internal.os.BatteryStatsImpl#setCpuSpeedSteps(int)`\
type: `EXTRACT`\
commit: [910397f23](https://github.com/CyanogenMod/android_frameworks_base/commit/910397f2390d6821a006991ed6035c76cbc74897)\
description: `Extract Method protected setCpuSpeedSteps(numSpeedSteps int) : void extracted from public readSummaryFromParcel(in Parcel) : void in class com.android.internal.os.BatteryStatsImpl`

id: `1`\
source `com.android.internal.os.BatteryStatsImpl#setNumSpeedSteps(int)`\
target: `com.android.internal.os.BatteryStatsImpl#setCpuSpeedSteps(int)`\
type: `EXTRACT`\
commit: [910397f23](https://github.com/CyanogenMod/android_frameworks_base/commit/910397f2390d6821a006991ed6035c76cbc74897)\
description: `Extract Method protected setCpuSpeedSteps(numSpeedSteps int) : void extracted from public setNumSpeedSteps(steps int) : void in class com.android.internal.os.BatteryStatsImpl`

id: `2`\
source `com.android.internal.os.BatteryStatsImpl#readFromParcelLocked(Parcel)`\
target: `com.android.internal.os.BatteryStatsImpl#setCpuSpeedSteps(int)`\
type: `EXTRACT`\
commit: [910397f23](https://github.com/CyanogenMod/android_frameworks_base/commit/910397f2390d6821a006991ed6035c76cbc74897)\
description: `Extract Method protected setCpuSpeedSteps(numSpeedSteps int) : void extracted from package readFromParcelLocked(in Parcel) : void in class com.android.internal.os.BatteryStatsImpl`

