<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.deeplearning4j.plot.ListenerTest`\
target: `org.deeplearning4j.optimize.solver.BackTrackLineSearchTest#testBackTrackLine()`\
type: `MOVE`\
commit: [91cdfa1ff](https://github.com/deeplearning4j/deeplearning4j/commit/91cdfa1ffd937a4cb01cdc0052874ef7831955e2)\
description: `Move Method public testBackTrackLine() : void from class org.deeplearning4j.plot.ListenerTest to public testBackTrackLine() : void from class org.deeplearning4j.optimize.solver.BackTrackLineSearchTest`

id: `1`\
source `org.deeplearning4j.plot.ListenerTest`\
target: `org.deeplearning4j.optimize.solver.BackTrackLineSearchTest#getIrisMultiLayerConfig(int[],String,int)`\
type: `MOVE_RENAME`\
commit: [91cdfa1ff](https://github.com/deeplearning4j/deeplearning4j/commit/91cdfa1ffd937a4cb01cdc0052874ef7831955e2)\
description: `Move And Rename Method private getIris1ItConfig(hiddenLayerSizes int[], activationFunction String, iterations int) : MultiLayerConfiguration from class org.deeplearning4j.plot.ListenerTest to private getIrisMultiLayerConfig(hiddenLayerSizes int[], activationFunction String, iterations int) : MultiLayerConfiguration from class org.deeplearning4j.optimize.solver.BackTrackLineSearchTest`

