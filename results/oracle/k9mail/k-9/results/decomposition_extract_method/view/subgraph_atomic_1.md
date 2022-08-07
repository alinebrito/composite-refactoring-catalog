<img src=subgraph_atomic_1.svg width=25%>

## Refactorings:

id: `0`\
source `com.fsck.k9.controller.MessagingController#sendPendingMessagesSynchronous(Account)`\
target: `com.fsck.k9.controller.MessagingController#handleSendFailure(Account,Store,Folder,Message,Exception,boolean)`\
type: `EXTRACT`\
commit: [9d44f0e06](https://github.com/k9mail/k-9/commit/9d44f0e06232661259681d64002dd53c7c43099d)\
description: `Extract Method private handleSendFailure(account Account, localStore Store, localFolder Folder, message Message, exception Exception, permanentFailure boolean) : void extracted from public sendPendingMessagesSynchronous(account Account) : void in class com.fsck.k9.controller.MessagingController`

id: `1`\
source `com.fsck.k9.controller.MessagingController#sendPendingMessagesSynchronous(Account)`\
target: `com.fsck.k9.controller.MessagingController#notifySynchronizeMailboxFailed(Account,Folder,Exception)`\
type: `EXTRACT`\
commit: [9d44f0e06](https://github.com/k9mail/k-9/commit/9d44f0e06232661259681d64002dd53c7c43099d)\
description: `Extract Method private notifySynchronizeMailboxFailed(account Account, localFolder Folder, exception Exception) : void extracted from public sendPendingMessagesSynchronous(account Account) : void in class com.fsck.k9.controller.MessagingController`

