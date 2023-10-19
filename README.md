# LangChain 之路：12个范例带你快速上手 LangChain（包含完整代码和数据集）


本文通过演示 LangChain 12 个最具有代表性的应用范例，带你快速上手 LangChain 各个使用场景。这些范例大都简洁易懂，非常具有实操价值。

- [x] 1. 文本总结(Summarization): 对文本/聊天内容的重点内容总结。

- [x] 2. 文档问答(QA over Documents): 使用文档作为上下文信息，基于文档内容进行问答。

- [x] 3. 信息抽取(Extraction): 从文本内容中抽取结构化的内容。

- [x] 4，结果评估(Evaluation): 分析并评估LLM输出的结果的好坏。

- [x] 5，数据库问答(QA over Database): 从数据库/类数据库内容中抽取数据信息。

- [x] 6. 代码理解(Code Understanding): 分析代码，并从代码中获取逻辑，同时也支持QA。

- [x] 7. API交互(Interacting with APIs): 通过对API文档的阅读，理解API文档并向真实世界调用API获取真实数据。

- [x] 8. 聊天机器人(Chatbots): 具备记忆能力的聊天机器人框架（有UI交互能力)。

- [x] 9. RAG(Retrieval-Augmented Generation)：除了 llm 本身已经学到的知识之外，通过外挂其他数据源的方式来增强 LLM 的能力。

- [x] 10. 智能体(Agents): 使用LLMs进行任务分析和决策，并调用工具执行决策。

- [ ] 11. 打标签(Tagging):

- [ ] 12. 分类(Classification):


---

## 准备


### notebook 配置

```python
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
# 帮助你的ipynb看起来更舒服
```

### 依赖
```python
!pip install langchain
!pip install openai
```