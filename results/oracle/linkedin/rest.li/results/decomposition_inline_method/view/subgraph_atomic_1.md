<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.linkedin.pegasus.generator.TemplateSpecGenerator#generate(DataSchema)`\
target: `com.linkedin.pegasus.generator.TemplateSpecGenerator#generateRecord(RecordDataSchema)`\
type: `INLINE`\
commit: [f61db44ca](https://github.com/linkedin/rest.li/commit/f61db44ca4a862f1a84450643d92f85449016cfa)\
description: `Inline Method public generate(schema DataSchema) : ClassTemplateSpec inlined to private generateRecord(schema RecordDataSchema) : RecordTemplateSpec in class com.linkedin.pegasus.generator.TemplateSpecGenerator`

id: `1`\
source `com.linkedin.pegasus.generator.TemplateSpecGenerator#generate(DataSchema)`\
target: `com.linkedin.pegasus.generator.TemplateSpecGenerator#generate(DataSchema,DataSchemaLocation)`\
type: `INLINE`\
commit: [f61db44ca](https://github.com/linkedin/rest.li/commit/f61db44ca4a862f1a84450643d92f85449016cfa)\
description: `Inline Method public generate(schema DataSchema) : ClassTemplateSpec inlined to public generate(schema DataSchema, location DataSchemaLocation) : ClassTemplateSpec in class com.linkedin.pegasus.generator.TemplateSpecGenerator`

