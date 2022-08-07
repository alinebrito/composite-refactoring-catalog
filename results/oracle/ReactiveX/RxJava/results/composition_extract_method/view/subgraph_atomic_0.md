<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `rx.observables.BlockingObservable#blockForSingle(Observable<?)`\
target: `rx.observables.BlockingObservable#awaitForComplete(CountDownLatch,Subscription)`\
type: `EXTRACT`\
commit: [8ad226067](https://github.com/ReactiveX/RxJava/commit/8ad226067434cd39ce493b336bd0659778625959)\
description: `Extract Method private awaitForComplete(latch CountDownLatch, subscription Subscription) : void extracted from private blockForSingle(observable Observable<? extends T>) : T in class rx.observables.BlockingObservable`

id: `1`\
source `rx.observables.BlockingObservable#forEach(Action1<?)`\
target: `rx.observables.BlockingObservable#awaitForComplete(CountDownLatch,Subscription)`\
type: `EXTRACT`\
commit: [8ad226067](https://github.com/ReactiveX/RxJava/commit/8ad226067434cd39ce493b336bd0659778625959)\
description: `Extract Method private awaitForComplete(latch CountDownLatch, subscription Subscription) : void extracted from public forEach(onNext Action1<? super T>) : void in class rx.observables.BlockingObservable`

