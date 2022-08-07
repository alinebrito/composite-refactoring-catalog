<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.buck.maven.Resolver#resolve(String...)`\
target: `com.facebook.buck.maven.Resolver#downloadArtifact(Artifact,RepositorySystem,RepositorySystemSession,Map<Path,SortedSet<Prebuilt>>,MutableDirectedGraph<Artifact>)`\
type: `EXTRACT`\
commit: [7e104c3ed](https://github.com/facebook/buck/commit/7e104c3ed4b80ec8e9b72356396f879d1067cc40)\
description: `Extract Method private downloadArtifact(artifactToDownload Artifact, repoSys RepositorySystem, session RepositorySystemSession, buckFiles Map<Path,SortedSet<Prebuilt>>, graph MutableDirectedGraph<Artifact>) : void extracted from public resolve(mavenCoords String...) : void in class com.facebook.buck.maven.Resolver`

id: `1`\
source `com.facebook.buck.maven.Resolver#resolve(String...)`\
target: `com.facebook.buck.maven.Resolver#createBuckFiles(Map<Path,SortedSet<Prebuilt>>)`\
type: `EXTRACT`\
commit: [7e104c3ed](https://github.com/facebook/buck/commit/7e104c3ed4b80ec8e9b72356396f879d1067cc40)\
description: `Extract Method private createBuckFiles(buckFilesData Map<Path,SortedSet<Prebuilt>>) : void extracted from public resolve(mavenCoords String...) : void in class com.facebook.buck.maven.Resolver`

id: `2`\
source `com.facebook.buck.maven.Resolver#resolve(String...)`\
target: `com.facebook.buck.maven.Resolver#resolveLib(Artifact,RepositorySystem,RepositorySystemSession,Path)`\
type: `EXTRACT`\
commit: [7e104c3ed](https://github.com/facebook/buck/commit/7e104c3ed4b80ec8e9b72356396f879d1067cc40)\
description: `Extract Method private resolveLib(artifact Artifact, repoSys RepositorySystem, session RepositorySystemSession, project Path) : Prebuilt extracted from public resolve(mavenCoords String...) : void in class com.facebook.buck.maven.Resolver`

id: `3`\
source `com.facebook.buck.maven.Resolver#resolve(String...)`\
target: `com.facebook.buck.maven.Resolver#downloadSources(Artifact,RepositorySystem,RepositorySystemSession,Path,Prebuilt)`\
type: `EXTRACT`\
commit: [7e104c3ed](https://github.com/facebook/buck/commit/7e104c3ed4b80ec8e9b72356396f879d1067cc40)\
description: `Extract Method private downloadSources(artifact Artifact, repoSys RepositorySystem, session RepositorySystemSession, project Path, library Prebuilt) : void extracted from public resolve(mavenCoords String...) : void in class com.facebook.buck.maven.Resolver`

id: `4`\
source `com.facebook.buck.maven.Resolver#resolve(String...)`\
target: `com.facebook.buck.maven.Resolver#resolveArtifact(Artifact,RepositorySystem,RepositorySystemSession,Path)`\
type: `EXTRACT`\
commit: [7e104c3ed](https://github.com/facebook/buck/commit/7e104c3ed4b80ec8e9b72356396f879d1067cc40)\
description: `Extract Method private resolveArtifact(artifact Artifact, repoSys RepositorySystem, session RepositorySystemSession, project Path) : Path extracted from public resolve(mavenCoords String...) : void in class com.facebook.buck.maven.Resolver`

id: `5`\
source `com.facebook.buck.maven.Resolver#resolve(String...)`\
target: `com.facebook.buck.maven.Resolver#getProjectName(Artifact)`\
type: `EXTRACT`\
commit: [7e104c3ed](https://github.com/facebook/buck/commit/7e104c3ed4b80ec8e9b72356396f879d1067cc40)\
description: `Extract Method private getProjectName(artifact Artifact) : String extracted from public resolve(mavenCoords String...) : void in class com.facebook.buck.maven.Resolver`

