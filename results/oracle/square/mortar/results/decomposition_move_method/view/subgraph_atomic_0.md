<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `mortar.ObjectGraphServiceTest`\
target: `mortar.MortarScopeTest#cannotRegisterOnDestroyed()`\
type: `MOVE`\
commit: [72dda3404](https://github.com/square/mortar/commit/72dda3404820a82d53f1a16bb2ed9ad95f745d3c)\
description: `Move Method public cannotRegisterOnDestroyed() : void from class mortar.ObjectGraphServiceTest to public cannotRegisterOnDestroyed() : void from class mortar.MortarScopeTest`

id: `1`\
source `mortar.ObjectGraphServiceTest`\
target: `mortar.MortarScopeTest#isDestroyedGetsSet()`\
type: `MOVE`\
commit: [72dda3404](https://github.com/square/mortar/commit/72dda3404820a82d53f1a16bb2ed9ad95f745d3c)\
description: `Move Method public isDestroyedGetsSet() : void from class mortar.ObjectGraphServiceTest to public isDestroyedGetsSet() : void from class mortar.MortarScopeTest`

id: `2`\
source `mortar.ObjectGraphServiceTest`\
target: `mortar.MortarScopeTest#isDestroyedStartsFalse()`\
type: `MOVE`\
commit: [72dda3404](https://github.com/square/mortar/commit/72dda3404820a82d53f1a16bb2ed9ad95f745d3c)\
description: `Move Method public isDestroyedStartsFalse() : void from class mortar.ObjectGraphServiceTest to public isDestroyedStartsFalse() : void from class mortar.MortarScopeTest`

id: `3`\
source `mortar.ObjectGraphServiceTest`\
target: `mortar.MortarScopeTest#cannotFindChildFromDestroyed()`\
type: `MOVE`\
commit: [72dda3404](https://github.com/square/mortar/commit/72dda3404820a82d53f1a16bb2ed9ad95f745d3c)\
description: `Move Method public cannotFindChildFromDestroyed() : void from class mortar.ObjectGraphServiceTest to public cannotFindChildFromDestroyed() : void from class mortar.MortarScopeTest`

id: `4`\
source `mortar.ObjectGraphServiceTest`\
target: `mortar.MortarScopeTest#rootDestroyIsIdempotent()`\
type: `MOVE`\
commit: [72dda3404](https://github.com/square/mortar/commit/72dda3404820a82d53f1a16bb2ed9ad95f745d3c)\
description: `Move Method public rootDestroyIsIdempotent() : void from class mortar.ObjectGraphServiceTest to public rootDestroyIsIdempotent() : void from class mortar.MortarScopeTest`

id: `5`\
source `mortar.ObjectGraphServiceTest`\
target: `mortar.MortarScopeTest#destroyIsIdempotent()`\
type: `MOVE`\
commit: [72dda3404](https://github.com/square/mortar/commit/72dda3404820a82d53f1a16bb2ed9ad95f745d3c)\
description: `Move Method public destroyIsIdempotent() : void from class mortar.ObjectGraphServiceTest to public destroyIsIdempotent() : void from class mortar.MortarScopeTest`

