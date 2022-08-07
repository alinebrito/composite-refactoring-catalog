<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `net.bytebuddy.description.method.ParameterList.Explicit#wrap(List<ParameterDescription>)`\
target: `net.bytebuddy.description.method.ParameterList.AbstractBase#wrap(List<ParameterDescription>)`\
type: `PULL_UP`\
commit: [f1dfb66a3](https://github.com/raphw/byte-buddy/commit/f1dfb66a368760e77094ac1e3860b332cf0e4eb5)\
description: `Pull Up Method protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.Explicit to protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.AbstractBase`

id: `1`\
source `net.bytebuddy.description.method.ParameterList.ForLoadedExecutable#wrap(List<ParameterDescription>)`\
target: `net.bytebuddy.description.method.ParameterList.AbstractBase#wrap(List<ParameterDescription>)`\
type: `PULL_UP`\
commit: [f1dfb66a3](https://github.com/raphw/byte-buddy/commit/f1dfb66a368760e77094ac1e3860b332cf0e4eb5)\
description: `Pull Up Method protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.ForLoadedExecutable to protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.AbstractBase`

id: `2`\
source `net.bytebuddy.description.method.ParameterList.ForLoadedExecutable.OfLegacyVmMethod#wrap(List<ParameterDescription>)`\
target: `net.bytebuddy.description.method.ParameterList.AbstractBase#wrap(List<ParameterDescription>)`\
type: `PULL_UP`\
commit: [f1dfb66a3](https://github.com/raphw/byte-buddy/commit/f1dfb66a368760e77094ac1e3860b332cf0e4eb5)\
description: `Pull Up Method protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.ForLoadedExecutable.OfLegacyVmMethod to protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.AbstractBase`

id: `3`\
source `net.bytebuddy.description.method.ParameterList.ForLoadedExecutable.OfLegacyVmConstructor#wrap(List<ParameterDescription>)`\
target: `net.bytebuddy.description.method.ParameterList.AbstractBase#wrap(List<ParameterDescription>)`\
type: `PULL_UP`\
commit: [f1dfb66a3](https://github.com/raphw/byte-buddy/commit/f1dfb66a368760e77094ac1e3860b332cf0e4eb5)\
description: `Pull Up Method protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.ForLoadedExecutable.OfLegacyVmConstructor to protected wrap(values List<ParameterDescription>) : ParameterList from class net.bytebuddy.description.method.ParameterList.AbstractBase`

