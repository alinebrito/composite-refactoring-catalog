<img src=subgraph_atomic_0.svg width=25%>

## Refactorings:

id: `0`\
source `org.thymeleaf.templateparser.markup.ThymeleafMarkupTemplateReader#read(char[],int,int)`\
target: `org.thymeleaf.templateparser.markup.ThymeleafMarkupTemplateReader#fillUpOverflow()`\
type: `EXTRACT`\
commit: [aed371dac](https://github.com/thymeleaf/thymeleaf/commit/aed371dac5e1248880e869930c636994c3d0f8dc)\
description: `Extract Method private fillUpOverflow() : void extracted from public read(cbuf char[], off int, len int) : int in class org.thymeleaf.templateparser.markup.ThymeleafMarkupTemplateReader`

id: `1`\
source `org.thymeleaf.templateparser.markup.ThymeleafMarkupTemplateReader#read(char[],int,int)`\
target: `org.thymeleaf.templateparser.markup.ThymeleafMarkupTemplateReader#processReadBuffer(char[],int,int)`\
type: `EXTRACT`\
commit: [aed371dac](https://github.com/thymeleaf/thymeleaf/commit/aed371dac5e1248880e869930c636994c3d0f8dc)\
description: `Extract Method private processReadBuffer(buffer char[], off int, len int) : int extracted from public read(cbuf char[], off int, len int) : int in class org.thymeleaf.templateparser.markup.ThymeleafMarkupTemplateReader`

