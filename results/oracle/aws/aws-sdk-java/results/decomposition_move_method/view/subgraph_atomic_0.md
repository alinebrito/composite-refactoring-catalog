<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.amazonaws.util.EC2MetadataUtilsTest`\
target: `com.amazonaws.util.EC2MetadataUtilsServer#startServer()`\
type: `MOVE_RENAME`\
commit: [4baf0a4de](https://github.com/aws/aws-sdk-java/commit/4baf0a4de8d03022df48d696d210cc8b3117d38a)\
description: `Move And Rename Method private runServer() : void from class com.amazonaws.util.EC2MetadataUtilsTest to private startServer() : void from class com.amazonaws.util.EC2MetadataUtilsServer`

id: `1`\
source `com.amazonaws.util.EC2MetadataUtilsTest`\
target: `com.amazonaws.util.EC2MetadataUtilsServer#stop()`\
type: `MOVE_RENAME`\
commit: [4baf0a4de](https://github.com/aws/aws-sdk-java/commit/4baf0a4de8d03022df48d696d210cc8b3117d38a)\
description: `Move And Rename Method private killServer() : void from class com.amazonaws.util.EC2MetadataUtilsTest to public stop() : void from class com.amazonaws.util.EC2MetadataUtilsServer`

