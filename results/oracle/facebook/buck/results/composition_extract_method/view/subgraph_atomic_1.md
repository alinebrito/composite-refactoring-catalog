<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.buck.cxx.CxxSourceRuleFactory#createPreprocessBuildRule(BuildRuleResolver,String,CxxSource,PicType)`\
target: `com.facebook.buck.cxx.CxxSourceRuleFactory#computeSourcePreprocessorAndToolDeps(Optional<Tool>,CxxSource)`\
type: `EXTRACT`\
commit: [ecd0ad5ab](https://github.com/facebook/buck/commit/ecd0ad5ab99b8d14f28881cf4f49ec01f2221776)\
description: `Extract Method private computeSourcePreprocessorAndToolDeps(toolOptional Optional<Tool>, source CxxSource) : ImmutableSortedSet<BuildRule> extracted from public createPreprocessBuildRule(resolver BuildRuleResolver, name String, source CxxSource, pic PicType) : CxxPreprocessAndCompile in class com.facebook.buck.cxx.CxxSourceRuleFactory`

id: `1`\
source `com.facebook.buck.cxx.CxxSourceRuleFactory#createPreprocessAndCompileBuildRule(BuildRuleResolver,String,CxxSource,PicType,CxxPreprocessMode)`\
target: `com.facebook.buck.cxx.CxxSourceRuleFactory#computeSourcePreprocessorAndToolDeps(Optional<Tool>,CxxSource)`\
type: `EXTRACT`\
commit: [ecd0ad5ab](https://github.com/facebook/buck/commit/ecd0ad5ab99b8d14f28881cf4f49ec01f2221776)\
description: `Extract Method private computeSourcePreprocessorAndToolDeps(toolOptional Optional<Tool>, source CxxSource) : ImmutableSortedSet<BuildRule> extracted from public createPreprocessAndCompileBuildRule(resolver BuildRuleResolver, name String, source CxxSource, pic PicType, strategy CxxPreprocessMode) : CxxPreprocessAndCompile in class com.facebook.buck.cxx.CxxSourceRuleFactory`

