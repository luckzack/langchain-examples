# 十几个范例带你快速上手 LangChain（包含完整代码和数据集，持续更新~）

<p align="center">
<img alt="Fiber" height="125" src="langchain.png">
</p>

通过演示 LangChain 最具有代表性的应用范例，带你快速上手 LangChain 各个使用场景。这些范例大都简洁易懂，非常具有实操价值。

- [x] 1. 文本总结(Summarization): 对文本/聊天内容的重点内容总结。

- [x] 2. 文档问答(QA over Documents): 使用文档作为上下文信息，基于文档内容进行问答。

- [x] 3. 信息抽取(Extraction): 从文本内容中抽取结构化的内容。

- [x] 4. 结果评估(Evaluation): 分析并评估 LLM 输出的结果的好坏。

- [x] 5. 数据库问答(QA over Database): 从数据库/类数据库内容中抽取数据信息。

- [x] 6. 代码理解(Code Understanding): 分析代码，并从代码中获取逻辑，同时也支持QA。

- [x] 7. API交互(Interacting with APIs): 通过对 API 文档的阅读，理解 API 文档并向真实世界调用API获取真实数据。

- [x] 8. 聊天机器人(Chatbots): 具备记忆能力的聊天机器人框架（有 UI 交互能力)。

- [x] 9. RAG(Retrieval-Augmented Generation)：除了 LLM 本身已经学到的知识之外，通过外挂其他数据源和主动检索互联网数据的方式来增强 LLM 的能力。

- [x] 10. 智能体(Agents): 使用 LLMs 进行任务分析和决策，并调用工具执行决策。

- [x] 11. 标注(Tagging):  让 LLM 使用不同类别/维度的 tags 来标注文档。

- [x] 12. 分类(Classification): 使用 prompt engineering 基于某个方向对文档进行分类。

- [x] 13. 结构化输出(Structured Output): 按要求输出结构化的JSON数据，快速交付给下游使用。

- [x] 14. 网页爬取(Web Scraper): 让 LLM 爬取指定 URL 的网页内容，提取并输出关键信息。

- [x] 15. 缓存(Cache): 以合适的方式缓存LLM返回结果，不仅能大大提高应答效率，也能节省token花费，提升程序健壮性。

- [x] 16. 向量存储索引(Vectorstore-Index): 用 QA Chain 实现文档问答步骤有点多，有没有更简单快速的方式？


---

## 准备


### Notebook 配置

```python
from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
# 帮助你的ipynb看起来更舒服
```

### 必备依赖
```python
!pip install langchain
!pip install openai
!pip install dotenv
```

### 环境变量
Rename `.env.template` to `.env` and fill environment variables as below:
```toml
# openai
OPENAI_API_KEY="xxx"

# azure
AZURE_OPENAI_BASE_URL = "xxx"
AZURE_OPENAI_API_KEY = "xxx"
AZURE_DEPLOYMENT_NAME_COMPLETE="xxx"
AZURE_DEPLOYMENT_NAME_CHAT="xxx"
AZURE_DEPLOYMENT_NAME_EMBEDDING="xxx"

# minimax
MINIMAX_GROUP_ID = "xxx"
MINIMAX_API_KEY = "xxx"
```

---

<p align="center">
&nbsp;<b>I</b>&nbsp;&#160;❤️ 
<br>
🦜⛓️
</p>