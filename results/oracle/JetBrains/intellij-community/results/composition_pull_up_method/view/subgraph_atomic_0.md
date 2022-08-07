<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.jetbrains.idea.maven.server.Maven30ServerEmbedderImpl#retrieveAvailableVersions(String,String,String)`\
target: `org.jetbrains.idea.maven.server.Maven3ServerEmbedder#retrieveAvailableVersions(String,String,String)`\
type: `PULL_UP`\
commit: [6ff3fe00d](https://github.com/JetBrains/intellij-community/commit/6ff3fe00d7ffe04dbe0904b8bad98285b6988d6d)\
description: `Pull Up Method public retrieveAvailableVersions(groupId String, artifactId String, remoteRepositoryUrl String) : List<String> from class org.jetbrains.idea.maven.server.Maven30ServerEmbedderImpl to public retrieveAvailableVersions(groupId String, artifactId String, remoteRepositoryUrl String) : List<String> from class org.jetbrains.idea.maven.server.Maven3ServerEmbedder`

id: `1`\
source `org.jetbrains.idea.maven.server.Maven32ServerEmbedderImpl#retrieveAvailableVersions(String,String,String)`\
target: `org.jetbrains.idea.maven.server.Maven3ServerEmbedder#retrieveAvailableVersions(String,String,String)`\
type: `PULL_UP`\
commit: [6ff3fe00d](https://github.com/JetBrains/intellij-community/commit/6ff3fe00d7ffe04dbe0904b8bad98285b6988d6d)\
description: `Pull Up Method public retrieveAvailableVersions(groupId String, artifactId String, remoteRepositoryUrl String) : List<String> from class org.jetbrains.idea.maven.server.Maven32ServerEmbedderImpl to public retrieveAvailableVersions(groupId String, artifactId String, remoteRepositoryUrl String) : List<String> from class org.jetbrains.idea.maven.server.Maven3ServerEmbedder`

