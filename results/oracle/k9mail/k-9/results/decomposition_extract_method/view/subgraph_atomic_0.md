<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.fsck.k9.controller.MessagingController#notifyAccountWithDataLocked(Context,Account,LocalMessage,NotificationData)`\
target: `com.fsck.k9.controller.MessagingController#setNotificationContent(Context,Message,CharSequence,CharSequence,NotificationCompat.Builder,String)`\
type: `EXTRACT`\
commit: [23c49d834](https://github.com/k9mail/k-9/commit/23c49d834d3859fc76a604da32d1789d2e863303)\
description: `Extract Method private setNotificationContent(context Context, message Message, sender CharSequence, subject CharSequence, builder NotificationCompat.Builder, accountDescr String) : NotificationCompat.Builder extracted from private notifyAccountWithDataLocked(context Context, account Account, message LocalMessage, data NotificationData) : void in class com.fsck.k9.controller.MessagingController`

id: `1`\
source `com.fsck.k9.controller.MessagingController#notifyAccountWithDataLocked(Context,Account,LocalMessage,NotificationData)`\
target: `com.fsck.k9.controller.MessagingController#buildNotificationNavigationStack(Context,Account,LocalMessage,int,int,ArrayList<MessageReference>)`\
type: `EXTRACT`\
commit: [23c49d834](https://github.com/k9mail/k-9/commit/23c49d834d3859fc76a604da32d1789d2e863303)\
description: `Extract Method private buildNotificationNavigationStack(context Context, account Account, message LocalMessage, newMessages int, unreadCount int, allRefs ArrayList<MessageReference>) : TaskStackBuilder extracted from private notifyAccountWithDataLocked(context Context, account Account, message LocalMessage, data NotificationData) : void in class com.fsck.k9.controller.MessagingController`

id: `2`\
source `com.fsck.k9.controller.MessagingController#notifyAccountWithDataLocked(Context,Account,LocalMessage,NotificationData)`\
target: `com.fsck.k9.controller.MessagingController#addWearActions(NotificationCompat.Builder,int,int,Account,ArrayList<MessageReference>,List<?,int)`\
type: `EXTRACT`\
commit: [23c49d834](https://github.com/k9mail/k-9/commit/23c49d834d3859fc76a604da32d1789d2e863303)\
description: `Extract Method private addWearActions(builder NotificationCompat.Builder, totalMsgCount int, msgCount int, account Account, allRefs ArrayList<MessageReference>, messages List<? extends Message>, notificationID int) : void extracted from private notifyAccountWithDataLocked(context Context, account Account, message LocalMessage, data NotificationData) : void in class com.fsck.k9.controller.MessagingController`

