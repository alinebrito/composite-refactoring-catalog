<img src=subgraph_atomic_3.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.buck.cxx.CxxSourceRuleFactory#createPreprocessAndCompileBuildRule(BuildRuleResolver,String,CxxSource,PicType,CxxPreprocessMode)`\
target: `com.facebook.buck.cxx.CxxSourceRuleFactory#computePlatformCompilerFlags(PicType,CxxSource)`\
type: `EXTRACT`\
commit: [ecd0ad5ab](https://github.com/facebook/buck/commit/ecd0ad5ab99b8d14f28881cf4f49ec01f2221776)\
description: `Extract Method private computePlatformCompilerFlags(pic PicType, source CxxSource) : ImmutableList<String> extracted from public createPreprocessAndCompileBuildRule(resolver BuildRuleResolver, name String, source CxxSource, pic PicType, strategy CxxPreprocessMode) : CxxPreprocessAndCompile in class com.facebook.buck.cxx.CxxSourceRuleFactory`

id: `1`\
source `com.facebook.buck.cxx.CxxSourceRuleFactory#createPreprocessAndCompileBuildRule(BuildRuleResolver,String,CxxSource,PicType,CxxPreprocessMode)`\
target: `com.facebook.buck.cxx.CxxSourceRuleFactory#computeRuleCompilerFlags(CxxSource)`\
type: `EXTRACT`\
commit: [ecd0ad5ab](https://github.com/facebook/buck/commit/ecd0ad5ab99b8d14f28881cf4f49ec01f2221776)\
description: `Extract Method private computeRuleCompilerFlags(source CxxSource) : ImmutableList<String> extracted from public createPreprocessAndCompileBuildRule(resolver BuildRuleResolver, name String, source CxxSource, pic PicType, strategy CxxPreprocessMode) : CxxPreprocessAndCompile in class com.facebook.buck.cxx.CxxSourceRuleFactory`

id: `2`\
source `com.facebook.buck.cxx.CxxSourceRuleFactory#createPreprocessAndCompileBuildRule(BuildRuleResolver,String,CxxSource,PicType,CxxPreprocessMode)`\
target: `com.facebook.buck.cxx.CxxSourceRuleFactory#computeSourcePreprocessorAndToolDeps(Optional<Tool>,CxxSource)`\
type: `EXTRACT`\
commit: [ecd0ad5ab](https://github.com/facebook/buck/commit/ecd0ad5ab99b8d14f28881cf4f49ec01f2221776)\
description: `Extract Method private computeSourcePreprocessorAndToolDeps(toolOptional Optional<Tool>, source CxxSource) : ImmutableSortedSet<BuildRule> extracted from public createPreprocessAndCompileBuildRule(resolver BuildRuleResolver, name String, source CxxSource, pic PicType, strategy CxxPreprocessMode) : CxxPreprocessAndCompile in class com.facebook.buck.cxx.CxxSourceRuleFactory`

