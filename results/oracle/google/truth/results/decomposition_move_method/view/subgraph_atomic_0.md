<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#isOrderedFailure()`\
type: `MOVE`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move Method public isOrderedFailure() : void from class com.google.common.truth.ListTest to public isOrderedFailure() : void from class com.google.common.truth.IterableTest`

id: `1`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#isStrictlyOrderedFailure()`\
type: `MOVE`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move Method public isStrictlyOrderedFailure() : void from class com.google.common.truth.ListTest to public isStrictlyOrderedFailure() : void from class com.google.common.truth.IterableTest`

id: `2`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#isOrderedWithNonComparableElementsFailure()`\
type: `MOVE`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move Method public isOrderedWithNonComparableElementsFailure() : void from class com.google.common.truth.ListTest to public isOrderedWithNonComparableElementsFailure() : void from class com.google.common.truth.IterableTest`

id: `3`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#isStrictlyOrderedWithNonComparableElementsFailure()`\
type: `MOVE`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move Method public isStrictlyOrderedWithNonComparableElementsFailure() : void from class com.google.common.truth.ListTest to public isStrictlyOrderedWithNonComparableElementsFailure() : void from class com.google.common.truth.IterableTest`

id: `4`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableIsStrictlyOrdered()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listIsStrictlyOrdered() : void from class com.google.common.truth.ListTest to public iterableIsStrictlyOrdered() : void from class com.google.common.truth.IterableTest`

id: `5`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableIsOrdered()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listIsOrdered() : void from class com.google.common.truth.ListTest to public iterableIsOrdered() : void from class com.google.common.truth.IterableTest`

id: `6`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableIsStrictlyOrderedWithComparator()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listIsStrictlyOrderedWithComparator() : void from class com.google.common.truth.ListTest to public iterableIsStrictlyOrderedWithComparator() : void from class com.google.common.truth.IterableTest`

id: `7`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableIsStrictlyOrderedWithComparatorFailure()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listIsStrictlyOrderedWithComparatorFailure() : void from class com.google.common.truth.ListTest to public iterableIsStrictlyOrderedWithComparatorFailure() : void from class com.google.common.truth.IterableTest`

id: `8`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableIsOrderedWithComparator()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listIsOrderedWithComparator() : void from class com.google.common.truth.ListTest to public iterableIsOrderedWithComparator() : void from class com.google.common.truth.IterableTest`

id: `9`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableIsOrderedWithComparatorFailure()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listIsOrderedWithComparatorFailure() : void from class com.google.common.truth.ListTest to public iterableIsOrderedWithComparatorFailure() : void from class com.google.common.truth.IterableTest`

id: `10`\
source `com.google.common.truth.ListTest`\
target: `com.google.common.truth.IterableTest#iterableOrderedByBaseClassComparator()`\
type: `MOVE_RENAME`\
commit: [1768840bf](https://github.com/google/truth/commit/1768840bf1e69892fd2a23776817f620edfed536)\
description: `Move And Rename Method public listOrderedByBaseClassComparator() : void from class com.google.common.truth.ListTest to public iterableOrderedByBaseClassComparator() : void from class com.google.common.truth.IterableTest`

