<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.facebook.share.internal.ShareInternalUtility`\
target: `com.facebook.GraphRequest#newUploadPhotoRequest(String,AccessToken,Uri,String,Bundle,Callback)`\
type: `MOVE`\
commit: [19d1936c3](https://github.com/facebook/facebook-android-sdk/commit/19d1936c3b07d97d88646aeae30de747715e3248)\
description: `Move Method public newUploadPhotoRequest(graphPath String, accessToken AccessToken, photoUri Uri, caption String, params Bundle, callback Callback) : GraphRequest from class com.facebook.share.internal.ShareInternalUtility to public newUploadPhotoRequest(accessToken AccessToken, graphPath String, photoUri Uri, caption String, params Bundle, callback Callback) : GraphRequest from class com.facebook.GraphRequest`

id: `1`\
source `com.facebook.share.internal.ShareInternalUtility`\
target: `com.facebook.GraphRequest#newUploadPhotoRequest(String,AccessToken,Bitmap,String,Bundle,Callback)`\
type: `MOVE`\
commit: [19d1936c3](https://github.com/facebook/facebook-android-sdk/commit/19d1936c3b07d97d88646aeae30de747715e3248)\
description: `Move Method public newUploadPhotoRequest(graphPath String, accessToken AccessToken, image Bitmap, caption String, params Bundle, callback Callback) : GraphRequest from class com.facebook.share.internal.ShareInternalUtility to public newUploadPhotoRequest(accessToken AccessToken, graphPath String, image Bitmap, caption String, params Bundle, callback Callback) : GraphRequest from class com.facebook.GraphRequest`

id: `2`\
source `com.facebook.share.internal.ShareInternalUtility`\
target: `com.facebook.GraphRequest#newUploadPhotoRequest(String,AccessToken,File,String,Bundle,Callback)`\
type: `MOVE`\
commit: [19d1936c3](https://github.com/facebook/facebook-android-sdk/commit/19d1936c3b07d97d88646aeae30de747715e3248)\
description: `Move Method public newUploadPhotoRequest(graphPath String, accessToken AccessToken, file File, caption String, params Bundle, callback Callback) : GraphRequest from class com.facebook.share.internal.ShareInternalUtility to public newUploadPhotoRequest(accessToken AccessToken, graphPath String, file File, caption String, params Bundle, callback Callback) : GraphRequest from class com.facebook.GraphRequest`

