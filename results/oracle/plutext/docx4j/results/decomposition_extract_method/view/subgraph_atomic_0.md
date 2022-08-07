<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.docx4j.org.apache.poi.poifs.storage.SmallBlockTableReader#getSmallDocumentBlocks(POIFSBigBlockSize,RawDataBlockList,RootProperty,int)`\
target: `org.docx4j.org.apache.poi.poifs.storage.SmallBlockTableReader#prepareSmallDocumentBlocks(POIFSBigBlockSize,RawDataBlockList,RootProperty,int)`\
type: `EXTRACT`\
commit: [e29924b33](https://github.com/plutext/docx4j/commit/e29924b33ec0c0298ba4fc3f7a8c218c8e6cfa0c)\
description: `Extract Method private prepareSmallDocumentBlocks(bigBlockSize POIFSBigBlockSize, blockList RawDataBlockList, root RootProperty, sbatStart int) : BlockList extracted from public getSmallDocumentBlocks(bigBlockSize POIFSBigBlockSize, blockList RawDataBlockList, root RootProperty, sbatStart int) : BlockList in class org.docx4j.org.apache.poi.poifs.storage.SmallBlockTableReader`

id: `1`\
source `org.docx4j.org.apache.poi.poifs.storage.SmallBlockTableReader#getSmallDocumentBlocks(POIFSBigBlockSize,RawDataBlockList,RootProperty,int)`\
target: `org.docx4j.org.apache.poi.poifs.storage.SmallBlockTableReader#prepareReader(POIFSBigBlockSize,RawDataBlockList,BlockList,RootProperty,int)`\
type: `EXTRACT`\
commit: [e29924b33](https://github.com/plutext/docx4j/commit/e29924b33ec0c0298ba4fc3f7a8c218c8e6cfa0c)\
description: `Extract Method private prepareReader(bigBlockSize POIFSBigBlockSize, blockList RawDataBlockList, list BlockList, root RootProperty, sbatStart int) : BlockAllocationTableReader extracted from public getSmallDocumentBlocks(bigBlockSize POIFSBigBlockSize, blockList RawDataBlockList, root RootProperty, sbatStart int) : BlockList in class org.docx4j.org.apache.poi.poifs.storage.SmallBlockTableReader`

