<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.buck.android.FilterResourcesStepTest#testFilterLocales()`\
target: `com.facebook.buck.android.FilterResourcesStepTest#getTestPathPredicate(boolean,ImmutableSet<Path>,ImmutableSet<String>)`\
type: `EXTRACT`\
commit: [d49765899](https://github.com/facebook/buck/commit/d49765899cb9df6781fff9773ffc244b5167351c)\
description: `Extract Method private getTestPathPredicate(enableStringWhitelisting boolean, whitelistedStringDirs ImmutableSet<Path>, locales ImmutableSet<String>) : Predicate<Path> extracted from public testFilterLocales() : void in class com.facebook.buck.android.FilterResourcesStepTest`

id: `1`\
source `com.facebook.buck.android.FilterResourcesStepTest#testFilterStrings()`\
target: `com.facebook.buck.android.FilterResourcesStepTest#getTestPathPredicate(boolean,ImmutableSet<Path>,ImmutableSet<String>)`\
type: `EXTRACT`\
commit: [d49765899](https://github.com/facebook/buck/commit/d49765899cb9df6781fff9773ffc244b5167351c)\
description: `Extract Method private getTestPathPredicate(enableStringWhitelisting boolean, whitelistedStringDirs ImmutableSet<Path>, locales ImmutableSet<String>) : Predicate<Path> extracted from public testFilterStrings() : void in class com.facebook.buck.android.FilterResourcesStepTest`

