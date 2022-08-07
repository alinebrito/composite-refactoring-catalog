<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.ansj.app.crf.model.WapitiCRFModel`\
target: `org.ansj.app.crf.WapitiCRFModelParser#parseWapitiCRFModel(String,String,int)`\
type: `MOVE_RENAME`\
commit: [9.137040000000003e+88](https://github.com/NLPchina/ansj_seg/commit/913704e835169255530c7408cad11ce9a714d4ec)\
description: `Move And Rename Method private parseFile(path String, templatePath String) : void from class org.ansj.app.crf.model.WapitiCRFModel to public parseWapitiCRFModel(modelFile String, templateFile String, maxSize int) : Model from class org.ansj.app.crf.WapitiCRFModelParser`

id: `1`\
source `org.ansj.app.crf.model.WapitiCRFModel`\
target: `org.ansj.app.crf.WapitiCRFModelParser#parseGrad(String,int)`\
type: `MOVE`\
commit: [9.137040000000003e+88](https://github.com/NLPchina/ansj_seg/commit/913704e835169255530c7408cad11ce9a714d4ec)\
description: `Move Method private parseGrad(temp String, featureNum int) : void from class org.ansj.app.crf.model.WapitiCRFModel to private parseGrad(statusMap Map<String,Integer>, myGrad Map<String,Feature>, temp String, featureNum int, tagNum int) : void from class org.ansj.app.crf.WapitiCRFModelParser`

