<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.jbpm.query.jpa.data.QueryWhere#getAppropriateQueryCriteria(String,int)`\
target: `org.jbpm.query.jpa.data.QueryWhere#addParameter(String,T...)`\
type: `INLINE`\
commit: [3815f293b](https://github.com/droolsjbpm/jbpm/commit/3815f293ba9338f423315d93a373608c95002b15)\
description: `Inline Method private getAppropriateQueryCriteria(listId String, valueListSize int) : QueryCriteria inlined to public addParameter(listId String, param T...) : QueryCriteria in class org.jbpm.query.jpa.data.QueryWhere`

id: `1`\
source `org.jbpm.query.jpa.data.QueryWhere#getAppropriateQueryCriteria(String,int)`\
target: `org.jbpm.query.jpa.data.QueryWhere#addRangeParameter(String,T,boolean)`\
type: `INLINE`\
commit: [3815f293b](https://github.com/droolsjbpm/jbpm/commit/3815f293ba9338f423315d93a373608c95002b15)\
description: `Inline Method private getAppropriateQueryCriteria(listId String, valueListSize int) : QueryCriteria inlined to public addRangeParameter(listId String, param T, start boolean) : void in class org.jbpm.query.jpa.data.QueryWhere`

