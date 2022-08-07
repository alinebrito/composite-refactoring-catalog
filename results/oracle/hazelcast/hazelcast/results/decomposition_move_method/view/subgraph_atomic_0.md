<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#setup()`\
type: `MOVE`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move Method public setup() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public setup() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

id: `1`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#getName()`\
type: `MOVE`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move Method public getName() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public getName() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `2`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#whenDoubleProbeField()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readLong_whenDoubleGaugeField() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenDoubleProbeField() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `3`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#whenLongProbeField()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readLong_whenLongGaugeField() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenLongProbeField() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `4`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#whenLongProbe()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readLong_whenLongGauge() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenLongProbe() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `5`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#whenProbeThrowsException()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readLong_whenExceptionalInput() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenProbeThrowsException() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `6`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#whenNoProbeAvailable()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readDouble_whenNoMetricInput() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenNoProbeAvailable() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

id: `7`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#whenProbeThrowsException()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readDouble_whenExceptionalInput() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenProbeThrowsException() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

id: `8`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#whenLongGaugeField()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readDouble_whenLongGaugeField() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenLongGaugeField() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

id: `9`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#whenDoubleGaugeField()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readDouble_whenDoubleGaugeField() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenDoubleGaugeField() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

id: `10`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#whenDoubleProbe()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readLong_whenDoubleGauge() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenDoubleProbe() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `11`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.LongGaugeImplTest#whenNoProbeSet()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readLong_whenNoInput() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenNoProbeSet() : void from class com.hazelcast.internal.metrics.impl.LongGaugeImplTest`

id: `12`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#whenDoubleProbe()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readDouble_whenDoubleGauge() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenDoubleProbe() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

id: `13`\
source `com.hazelcast.internal.metrics.impl.GaugeImplTest`\
target: `com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest#whenLongProbe()`\
type: `MOVE_RENAME`\
commit: [30c4ae097](https://github.com/hazelcast/hazelcast/commit/30c4ae09745d6062077925a54f27205b7401d8df)\
description: `Move And Rename Method public readDouble_whenLongGauge() : void from class com.hazelcast.internal.metrics.impl.GaugeImplTest to public whenLongProbe() : void from class com.hazelcast.internal.metrics.impl.DoubleGaugeImplTest`

