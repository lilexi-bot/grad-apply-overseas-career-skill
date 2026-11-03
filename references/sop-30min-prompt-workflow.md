# 半小时出一篇可提交 SOP：提示词模板与执行顺序

> **When to load:** 用户要写 SOP/PS/Statement of Purpose、要把已有文书迁移到新项目、要控制"GPT 味"、需要先对齐文书要点再成文时。
> **Trigger:** SOP, Statement of Purpose, 目的陈述, 个人陈述, PS, 文书, 半小时写SOP, 文书提示词, 提示词模板, 迁移文书, 改文书, GPT味, AI味, 文书要点对齐, research interest, why program
> **Source:** 用户分享《半小时出一篇能直接提交的 sop》方法（2026-11-03）
> **Keywords:** SOP, statement of purpose, essay prompt, essay migration, AI-writing voice, outline-first workflow, program fit

---

## 中文原文

半小时出一篇能直接提交的 sop。

把自己的故事讲好、把自己的特点体现出来 & 跟项目 match 上，然后 gpt 味儿别太冲，就不会有问题。

我正在申请 xx 学校的 xx program，现在我要写 sop，我给你的参考信息有：xx 学校 xx program 的课程，我的简历，我申请其他学校 xx 专业相关项目的 sop，这些基本能构成所有要求的内容，你只需要在表述上适当修改以满足 xx 学校 xx program 的 sop 的 instructions 即可。我的 primary research interest 是 xxxx。接下来你先整理 sop 要求，然后规划一下行文，我们先对齐一下文书的要点，先不成文。

---

## 这套提示词为什么有效（本仓库拆解）

表面上是一段话，实际上同时做了四件事，缺一件都会退化成"通用模板生成器"：

| 要素 | 原文对应 | 作用 |
|---|---|---|
| **给参考材料，而不是让 AI 编** | 课程清单 + 简历 + 其他学校同类 SOP | 内容有出处，避免幻觉和空话 |
| **给迁移任务，而不是从零创作** | "你只需要在表述上适当修改" | 大幅压缩时间，且保住真实经历 |
| **给锚点** | primary research interest | 全文有主轴，不会写散 |
| **给顺序 + 给闸门** | 先整理要求 → 再规划行文 → 先对齐要点，先不成文 | 防止一上来就成文，改到第 5 版才发现结构错 |

**关键在最后那句"先不成文"。** 直接生成一篇 800 词的 SOP，你只能在成品上反复涂抹；先出要求和结构，你能在 20 分钟内确认"这个角度对不对"，再让它落笔。这就是半小时能交付的真正原因——**时间不是省在写，是省在不返工。**

---

## 四步执行顺序（可直接照做）

### 第一步：整理 SOP 要求（让 AI 只做提取，不做创作）

把项目官网的 SOP/PS instructions 原文粘进去，要求输出：

- 字数上限与页数限制
- 必须回答的问题（通常 3–5 个）
- 明确禁止的内容（有些项目禁止写个人童年故事、禁止重复 CV）
- 是否有固定结构或提示问题（prompt-based）
- 提交格式要求

> 这一步的价值：多数人写崩不是文笔问题，是**没回答项目真正问的那几个问题**。先把"评分问题清单"列出来，后面每段都要能对应上一条。

### 第二步：规划行文（先定骨架，再定素材）

要求输出一份**段落级大纲**，每段标注：这一段回答哪个问题、用简历里哪条经历做证据、和项目哪个资源挂钩。

推荐骨架（多数研究型项目通用）：

1. **钩子 + 定位**：我是谁、要做什么方向（primary research interest 一句话落地）
2. **已有基础 → 能力缺口**：做过什么、在哪一步发现不够（不要罗列技能）
3. **项目资源如何补上缺口**：具体课程名、实验室、教授、capstone（点名，不泛泛）
4. **我能带来什么**：diversity/贡献，用行为证据而非标签
5. **next steps**：读完这个项目后要做什么，可验证

### 第三步：对齐要点（人审，这一步不要交给 AI）

对着大纲逐段问三个问题：

- 这段是**我的**故事，还是任何人都能写的？（换个人名还成立 → 删或改）
- 这段有**具体证据**吗？（简历里的项目、数字、产出）
- 这段和这个项目**唯一匹配**吗？（换成隔壁学校也成立 → 说明 why program 没写到位）

### 第四步：成文 + 去 GPT 味

只在大纲通过后再让它写。写完后按下面清单过一遍（见下节）。

---

## "GPT 味"的具体识别与改写（本仓库补充）

不要求助"降低 AI 率"工具，先看文本里有没有这些特征：

| GPT 味特征 | 典型写法 | 改写方向 |
|---|---|---|
| 三段式排比 | "不仅…而且…更重要的是…" | 砍成两句，保留最有信息量的那句 |
| 万能形容词 | "深厚的兴趣""强烈的热情""卓越的能力" | 换成具体事实或直接删 |
| 抽象升华结尾 | "我期待为人类社会的进步贡献力量" | 换成可验证的下一步动作 |
| 每段开头都是连接词 | "首先/其次/此外/最后" | 用内容推进，不用序号推进 |
| 没有数字和时间 | 全篇没有年份、规模、结果 | 补具体数字与时间点 |
| 完美但无瑕疵的叙事 | 没有一次失败、没有一次改变想法 | 加一处真实的犹豫或修正 |
| 术语堆砌 | 连续三个以上模型名 | 只留你真用过的那一个 |

**一个快速自检：** 把 SOP 里所有形容词和"passion/interest"类词删掉，如果句子还成立，说明它们本来就没在承重；如果不成立，说明那才是你真正的论点——用事实把它撑起来。

---

## 一个容易被忽略的点：为什么"迁移已有 SOP"比"重新写"更安全

你申请同一专业的多个项目时，**research interest 和经历是不变的，变的只是"为什么是这个项目"**。所以正确的做法是：

- 保留：研究兴趣、经历叙述、能力缺口的逻辑链（这些是你的资产，重写只会损失细节）
- 重写：why program 段（课程名、教授、实验室、capstone 必须换成目标项目的）
- 调整：篇幅与语气（英式项目偏克制，美式项目可更直接）
- 删除：上一版里提到其他学校名字的任何残留（这是最常见的致命错误）

> 提交前必做：全文搜索其他学校名、教授名、项目缩写。迁移文书最容易翻车的地方就在这里。

---

## English Key Takeaways

1. **The prompt works because it does four things at once:** supplies source material (course list, CV, a SOP for a sibling programme), frames the task as migration rather than creation, gives a single anchor (primary research interest), and imposes an order with a gate ("outline first, don't write yet").
2. **"Don't write yet" is the whole trick.** Generating 800 words immediately means you can only polish the finished product; getting requirements + outline first lets you validate the angle in 20 minutes. **The half hour is saved on rework, not on writing.**
3. **Step 1 is extraction, not creation:** turn the programme's SOP instructions into a checklist of questions that must be answered, plus explicit prohibitions (many programmes forbid childhood narratives or CV repetition).
4. **Step 2 is a paragraph-level outline** where each paragraph declares which question it answers, which CV item is its evidence, and which programme resource it connects to.
5. **Step 3 is human-only:** for each paragraph ask — is this *my* story (would it survive a name swap?), is there concrete evidence, and is it uniquely matched to *this* programme?
6. **Kill the GPT voice structurally, not with detectors:** cut triadic parallelisms, delete universal adjectives ("deep passion", "outstanding ability"), replace abstract uplift endings with verifiable next steps, add real numbers and dates, and include one genuine hesitation or reversal.
7. **Stress test:** delete every adjective and every "passion/interest" word — if the sentence still stands, those words were never load-bearing.
8. **Migrating an existing SOP is safer than rewriting**, because research interest and experience are constant while "why this programme" must change; the most common fatal error is a leftover mention of another university.

---

## Connection to Repo Themes

- **`student-profiles-research-method.md`** (`/student-profiles`) — the "why program" paragraph should be built from the programme's own Meet-the-Class question framework; that file tells you what admissions actually rewards.
- **`cold-email-networking-template.md`** — naming a specific professor in the SOP is stronger when you have already emailed them; the two should be sequenced, not independent.
- **`cv-review.md`** (`/cv-review`) — the SOP's evidence layer is the CV; if the CV only lists tools and models without stating the problem solved, the SOP has nothing to cite.
- **`interview-prep.md`** — the SOP outline doubles as interview prep: every claim you make must be defensible in a 30-minute conversation.
- **`leadership-stories.md`** — the "what I bring to the community" paragraph needs behavioural evidence; the STAR stories are the source.
- **`phd-advisor-fit.md`** (`/phd-advisor`) — for research programmes, the professor-fit paragraph is the highest-weight section; use that file's fit criteria instead of generic praise.
- **`summer-research-practical-guide.md`** — research experience is the strongest evidence for "已有基础 → 能力缺口" and should be written as a problem, not a task list.
- **`us-ai-masters-30-programs.md`** (`/ai-masters`) — when applying to multiple AI programmes, the type taxonomy tells you which "why program" angle fits (algorithm-track vs product-track vs research-track).
- **`essmote-ai-writing-platform.md`** (`/essmote`) — a tool option for the drafting stage, but the outline-first gate still applies; never let a platform write before the requirements checklist exists.
