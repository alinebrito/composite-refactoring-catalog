<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.quantumbadger.redreader.activities.CommentListingActivity#onDestroy()`\
target: `org.quantumbadger.redreader.activities.BaseActivity#onDestroy()`\
type: `PULL_UP`\
commit: [51b8b0e1a](https://github.com/QuantumBadger/RedReader/commit/51b8b0e1ad4be1b137d67774eab28dc0ef52cb0a)\
description: `Pull Up Method protected onDestroy() : void from class org.quantumbadger.redreader.activities.CommentListingActivity to protected onDestroy() : void from class org.quantumbadger.redreader.activities.BaseActivity`

id: `1`\
source `org.quantumbadger.redreader.activities.MoreCommentsListingActivity#onDestroy()`\
target: `org.quantumbadger.redreader.activities.BaseActivity#onDestroy()`\
type: `PULL_UP`\
commit: [51b8b0e1a](https://github.com/QuantumBadger/RedReader/commit/51b8b0e1ad4be1b137d67774eab28dc0ef52cb0a)\
description: `Pull Up Method protected onDestroy() : void from class org.quantumbadger.redreader.activities.MoreCommentsListingActivity to protected onDestroy() : void from class org.quantumbadger.redreader.activities.BaseActivity`

id: `2`\
source `org.quantumbadger.redreader.activities.MainActivity#onDestroy()`\
target: `org.quantumbadger.redreader.activities.BaseActivity#onDestroy()`\
type: `PULL_UP`\
commit: [51b8b0e1a](https://github.com/QuantumBadger/RedReader/commit/51b8b0e1ad4be1b137d67774eab28dc0ef52cb0a)\
description: `Pull Up Method protected onDestroy() : void from class org.quantumbadger.redreader.activities.MainActivity to protected onDestroy() : void from class org.quantumbadger.redreader.activities.BaseActivity`

id: `3`\
source `org.quantumbadger.redreader.activities.PostListingActivity#onDestroy()`\
target: `org.quantumbadger.redreader.activities.BaseActivity#onDestroy()`\
type: `PULL_UP`\
commit: [51b8b0e1a](https://github.com/QuantumBadger/RedReader/commit/51b8b0e1ad4be1b137d67774eab28dc0ef52cb0a)\
description: `Pull Up Method protected onDestroy() : void from class org.quantumbadger.redreader.activities.PostListingActivity to protected onDestroy() : void from class org.quantumbadger.redreader.activities.BaseActivity`

