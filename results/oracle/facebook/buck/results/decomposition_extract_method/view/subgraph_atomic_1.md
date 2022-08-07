<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.buck.js.ReactNativeBundle#ReactNativeBundle(BuildRuleParams,SourcePathResolver,SourcePath,boolean,String,SourcePath,ReactNativePlatform,ReactNativeDeps)`\
target: `com.facebook.buck.js.ReactNativeBundle#getPathToJSBundleDir(BuildTarget)`\
type: `EXTRACT`\
commit: [cfea606b1](https://github.com/facebook/buck/commit/cfea606b129dbfc5703eb279d4803185afc99c58)\
description: `Extract Method public getPathToJSBundleDir(target BuildTarget) : Path extracted from protected ReactNativeBundle(ruleParams BuildRuleParams, resolver SourcePathResolver, entryPath SourcePath, isDevMode boolean, bundleName String, jsPackager SourcePath, platform ReactNativePlatform, depsFinder ReactNativeDeps) in class com.facebook.buck.js.ReactNativeBundle`

id: `1`\
source `com.facebook.buck.js.ReactNativeBundle#ReactNativeBundle(BuildRuleParams,SourcePathResolver,SourcePath,boolean,String,SourcePath,ReactNativePlatform,ReactNativeDeps)`\
target: `com.facebook.buck.js.ReactNativeBundle#getPathToResources(BuildTarget)`\
type: `EXTRACT`\
commit: [cfea606b1](https://github.com/facebook/buck/commit/cfea606b129dbfc5703eb279d4803185afc99c58)\
description: `Extract Method public getPathToResources(target BuildTarget) : Path extracted from protected ReactNativeBundle(ruleParams BuildRuleParams, resolver SourcePathResolver, entryPath SourcePath, isDevMode boolean, bundleName String, jsPackager SourcePath, platform ReactNativePlatform, depsFinder ReactNativeDeps) in class com.facebook.buck.js.ReactNativeBundle`

