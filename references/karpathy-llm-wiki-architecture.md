# Karpathy's LLM Wiki Architecture — raw sources / wiki / schema + 4 meta-insights

> Field synthesis (Chinese original verbatim at the bottom). Load when: the user is thinking about
> knowledge management architecture, LLM-obsidian workflows, or how to build a personal wiki that
> *compounds*. This file articulates the three-layer architecture (raw sources / wiki / schema) and
> the four meta-insights (compound interest / raw-vs-synthesised / LLM-as-bookkeeper-not-oracle /
> lint-as-health-mechanism), plus three practical best practices.
> （Karpathy LLM wiki， 知识管理， raw sources / wiki / schema， 复利， bookkeeping， lint，
> obsidian IDE， raw truth vs synthesized knowledge， 双随机约束）。

## The three-layer architecture (Karpathy)

| Layer | Role | Mutable? |
|---|---|---|
| **Raw sources** | 原始材料，不可修改 | Immutable |
| **Wiki** | LLM 持续维护的"知识编译结果"，真正服务问答的是这一层 | Mutable, evolved |
| **Schema** | 规范 LLM 怎么读写这个 wiki | Meta-layer |

### The reasoning
Knowledge management's hardest part is not *understanding* the knowledge; it is **bookkeeping**.
Reading a source is not the hard part — the hard part is afterwards: whether to update a bunch of
related pages, add bi-directional links, mark conflicts, rewrite the index, update the timeline.
Karpathy defines this bookkeeping layer as the one **most suitable for LLM takeover**.

## Four meta-insights

### 1. Treat knowledge accumulation as a *compound interest* process
LLM wiki emphasises "continuous" and "iterative" — each new material ingested is not just "adding
a record", but *adding new connections to the existing knowledge structure, repairing existing
pages, making every future query more efficient*. This is much stronger than traditional RAG,
where each query round is almost a one-time consumption.

### 2. Strictly separate raw truth from synthesised knowledge
Prior memory systems gave both the same weight, making errors harder to trace. Karpathy's design:
**raw sources are immutable; what evolves is the wiki.**

### 3. LLM is for wiki-layer maintenance, not for being the oracle of truth
LLM should not be responsible for judging everything; it is better suited to tedious bookkeeping.
This is an accurate positioning of LLM: LLM is good at cross-document integration, writing
summaries, filling in cross-references, finding gaps — but it should not *create facts* outside
the raw sources.

### 4. Introduce *lint* as a knowledge-base health mechanism
> （Karpathy 简直是天才）

Most knowledge systems only care "can we write it in" and "can we query it out". Karpathy adds a
concern: **will the knowledge base become dirtier over time?** The thinking behind lint is turning
the knowledge base from a *static repository* into a *maintainable system* — because knowledge is
not forever correct; it must be periodically checked for: inconsistent data, missing data,
interesting connections.

## Three practical best practices

1. **Use Obsidian as the IDE front-end UI** — to view raw data, compiled wiki, and derived
   visualisations.
2. **Let LLM output more than plain text / terminal.** Markdown files, PPT, matplotlib images —
   these outputs can themselves be archived back into the wiki, reinforcing the whole system.
3. **Build a small search engine running on this wiki**, also callable as a CLI for LLM to handle
   larger queries.

## Cross-reference
- `career-oak-high-level-state-transition.md` — Oak's "high-level state transition" framing is
  the *epistemological* analogue of the wiki layer: both privilege the *compiled* description over
  the micro-physical sequence.
- `career-ai-trapped-in-human-symbolic-system.md` — the raw-truth / wiki distinction maps onto the
  "symbolic system" argument: raw sources are closer to the universe; wiki is the human-layer
  encoding. LLM operates entirely in the wiki layer.

---

## 中文原稿（verbatim）

Karpathy给的架构是： raw sources：原始材料，不可修改 wiki：llm持续维护的"知识编译结果"，真正服务问答的是这一层 schema：规范llm怎么读写这个wiki 这种架构设计背后的reasoning是，知识管理最费劲的不是理解知识本身，而是bookkeeping。换句话说，读一篇资料本身不是最难的，难的是之后要不要更新一大堆相关页面、加双向链接（原来飞书搁这儿呢[笑哭R]）、标注冲突、改index、改timeline。Karpathy 把这一层定义为最适合让 LLM 接管的工作。 主包认为，llm wiki最有价值的思想有四点： 1️⃣ 把知识沉淀看成复利过程 llm wiki强调"持续""更迭"，也就是每次摄入新材料时，不只是添加一条记录，而是在已有的知识结构上增加新的连接、修正已有页面、让未来所有查询都更高效。这一点比传统RAG强很多，因为RAG的每轮查询几乎都是一次性消费 2️⃣ 严格区分raw truth和synthesized knowledge 此前很多memory系统赋予两者同样的权重，导致错误更难溯源。Karpathy的设计里，raw sources是不可变的，可演化的是wiki 3️⃣ LLM用于wiki层的维护，而不是直接拿来充当真理机器 llm不应该负责判断一切，而是更适合做tedious bookkeeping。这种对llm的定位还是比较准确的，因为llm擅长跨文档整合、写摘要、补交叉引用、查缺漏，但不该脱离raw sources创造事实。 4️⃣ 引入lint作为知识库健康机制（karpathy简直是天才[惊恐R]） 大多数knowledge system只关心"能不能写进去"和"能不能查出来"，而Karpathy加了一个concern：知识库会不会越来越脏？lint背后的thinking是把知识库从静态仓库变成一个可维护的系统，因为知识不是永远正确的，必须定期检查：inconsistent data、数据缺失、有意思的connections... Karpathy的best practice： 1️⃣ 把obsidian当成IDE的前端UI，用来看raw data，complied wiki，以及衍生出来的各种visualization 2️⃣ 除了让它输出纯文本/在terminal中看输出，还可以让它输出md文件、ppt、数学图表（matplotlib images），这些输出还可以继续归档，增强整个wiki 3️⃣ 做一个小型search engine，专门跑在这个wiki上，也可以做成cli给llm来处理更大的查询
