<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.apache.drill.exec.impersonation.TestImpersonationMetadata#addMiniDfsBasedStorage()`\
target: `org.apache.drill.exec.impersonation.BaseTestImpersonation#addMiniDfsBasedStorage()`\
type: `PULL_UP`\
commit: [c1b847acd](https://github.com/apache/drill/commit/c1b847acdc8cb90a1498b236b3bb5c81ca75c044)\
description: `Pull Up Method public addMiniDfsBasedStorage() : void from class org.apache.drill.exec.impersonation.TestImpersonationMetadata to protected addMiniDfsBasedStorage(workspaces Map<String,WorkspaceConfig>) : void from class org.apache.drill.exec.impersonation.BaseTestImpersonation`

id: `1`\
source `org.apache.drill.exec.impersonation.TestImpersonationDisabledWithMiniDFS#addMiniDfsBasedStorage()`\
target: `org.apache.drill.exec.impersonation.BaseTestImpersonation#addMiniDfsBasedStorage()`\
type: `PULL_UP`\
commit: [c1b847acd](https://github.com/apache/drill/commit/c1b847acdc8cb90a1498b236b3bb5c81ca75c044)\
description: `Pull Up Method public addMiniDfsBasedStorage() : void from class org.apache.drill.exec.impersonation.TestImpersonationDisabledWithMiniDFS to protected addMiniDfsBasedStorage(workspaces Map<String,WorkspaceConfig>) : void from class org.apache.drill.exec.impersonation.BaseTestImpersonation`

