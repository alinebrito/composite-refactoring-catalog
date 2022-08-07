<img src=subgraph_atomic_2.svg width=25%>

## Refactorings:

id: `0`\
source `org.springframework.boot.actuate.metrics.buffer.BufferMetricReader#findAll()`\
target: `org.springframework.boot.actuate.metrics.buffer.BufferMetricReader#findAll(Predicate<String>)`\
type: `EXTRACT`\
commit: [b47634176](https://github.com/spring-projects/spring-boot/commit/b47634176fa48ad925f79886c6aaca225cb9af64)\
description: `Extract Method private findAll(predicate Predicate<String>) : Iterable<Metric<?>> extracted from public findAll() : Iterable<Metric<?>> in class org.springframework.boot.actuate.metrics.buffer.BufferMetricReader`

id: `1`\
source `org.springframework.boot.actuate.metrics.buffer.BufferMetricReader#findAll(String)`\
target: `org.springframework.boot.actuate.metrics.buffer.BufferMetricReader#findAll(Predicate<String>)`\
type: `EXTRACT`\
commit: [b47634176](https://github.com/spring-projects/spring-boot/commit/b47634176fa48ad925f79886c6aaca225cb9af64)\
description: `Extract Method private findAll(predicate Predicate<String>) : Iterable<Metric<?>> extracted from public findAll(prefix String) : Iterable<Metric<?>> in class org.springframework.boot.actuate.metrics.buffer.BufferMetricReader`

