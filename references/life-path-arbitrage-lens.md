# 人生路径套利：一个透镜，以及这个仓库不该变成什么

> 来源：用户 2026-11-20 上传的 `思考了 1m 15s.txt`（另一模型对本仓库的战略重构提案，共五节，文件在第五节「存量资产改造」表格第二行处截断）。
> 提案主张：把本仓库从「留学申请工具」重新定义为「人生路径套利系统」，用七种套利维度作顶层分类，引入人生选择权（Option Value）与六维评分模型，新增 `strategy/`、`engines/`、`databases/`、`models/`、`simulations/` 五个目录约 35 个文件，并建议用 NetworkX / OR-Tools / Monte Carlo / PostgreSQL 实现路径组合引擎。
> 本文件是**采纳决定**，不是转述。采纳四条，驳回四条，并给出最小可行改造。
> 核心判断：**这份提案的诊断是对的，处方是错的。它准确指出了仓库缺少战略层，但把「缺一层思考」误诊成了「缺一套系统」。**
>
> **Last verified: 2026-11**（本文件为方法论，半衰期 5 年+；但第二节映射表中的项目/政策类文件各自另有衰减周期，引用前按 SKILL.md §0.5 第 4 条处理）

**English abstract**: A strategy-redesign proposal for this repository, arguing it should be redefined from an application tool into a "life path arbitrage system" with seven arbitrage dimensions, an option-value term, a six-dimension scoring model, and ~35 new files across five new directories. This file records the adoption decision. **Adopted**: (1) the seven-dimension lens, because the repo already contains all seven dimensions scattered across 69 reference files but is organized by topic, which makes it unaddressable by strategic question; (2) the option-value concept, reframed as three decision questions rather than a formula, because every term in the proposed formula is unmeasurable and stating it would manufacture false precision; (3) feasibility-before-scoring, which independently converges with the eligibility-versus-difficulty distinction established in `us-grad-program-difficulty-tiers-6-majors.md`; (4) the opportunity-lifecycle discipline, which is the most operationally valuable idea in the proposal and is already an unsolved problem in this repo — every policy fact here is date-stamped and decaying. **Rejected**: a static `databases/` directory (policy facts decay faster than any static repo can be maintained — a repo can store methods and dated snapshots, not a database); seven separate `engines/` files (one protocol is stronger than seven thin ones); JSON schemas before any data exists; and the proposed weights and formula, which would present invented parameters as measurements. Also rejected: a user-profile schema in a public repository, which directly violates this project's privacy rule.

---

## When to load

- 用户问「我该不该出国」「该先工作还是先读研」「哪条路长期更好」这类**没有单一正解的结构性选择**
- 用户拿到了多个 offer / 多个方向，需要比较而不是挑选
- 用户问「这个仓库到底在解决什么问题」「怎么用这套东西」
- 用户在规划**跨制度组合**：海外学分 → 低学费硕士 → 当地实习 → 工签 → 移民
- 需要把散落在 69 个 reference 里的碎片，按一个战略问题重新组织
- 有人提出要把本仓库「升级成系统 / 加数据库 / 加评分模型」时，先用本文件的采纳/驳回清单对齐

## Trigger

人生路径、套利、路径设计、该不该出国、先工作还是先读研、长期规划、十年、选择权、option value、反事实、路径组合、制度差、信息差、机会窗口、值不值、战略层、重构仓库

## Keywords

`life path arbitrage` `option value` `path combination` `counterfactual` `feasibility filter` `opportunity decay`

---

## 一、这份提案说对了什么

### 说对的第一件事：本仓库缺的不是内容，是**可寻址性**

提案的核心指控成立——但这个指控比它自己以为的更精确。

本仓库现在有 69 个 reference 文件，覆盖了从丹麦工签、EU 平台路由、36 国跑签手册，到 HUST 飞跃手册、七源选校尽调、六专业难度分档、SOP 框架、创始人叙事、冷邮件、量化面试。**内容密度不低。**

但它现在是**按主题组织的**：`denmark-siri`、`eu-platforms`、`scholarships`、`visa-policy-links`、`study-roi`……

按主题组织的知识库有一个致命特性：**只有知道该问什么的人才能用。**

- 一个已经在想丹麦的人，会去读 `denmark-siri`
- 一个已经在想奖学金的人，会去读 `niche-scholarships-12-channels`
- 但一个只知道「我想出国，但不知道从哪下手」的人，面对这 69 个文件是**失语的**——因为他的问题不是任何一个文件名

**战略问题的形式是「在什么约束下、下一步做什么、能改善什么」，而本仓库的回答形式是「某个主题的全部信息」。这两种形式之间没有桥。**

所以真正缺的不是新内容，是**一个把主题索引变成问题索引的透镜**。这是本文件存在的唯一理由。

### 说对的第二件事：纯 ROI 会系统性低估保留选择权的路径

本仓库已有 `study-abroad-roi-and-internship-playbook.md`，它算的是成本、回报、回本周期。这是必要的，但**不充分**，而且它的偏差方向是确定的：

| 路径 | 花费 | 毕业后可进入 | 起薪 |
| --- | --- | --- | --- |
| A | 50 万 | 1 个国家的 1 个行业 | 更高 |
| B | 30 万 | 3 个国家的 4 个行业 | 略低 |

纯 ROI 会选 A。但如果把「三年后想换赛道」这个真实概率算进去，B 可能更优——**因为 B 的失败模式是「换个方向」，A 的失败模式是「重新读一个学位」。**

这不是玄学。它有一个可操作的形式，见第三节。

### 说对的第三件事：必须先筛资格，再谈打分

提案提出「任何一个关键条件不满足，都应该标记为 `INFEASIBLE`，而不是让高分掩盖不可执行性」。

**这条与本仓库刚刚确立的「资格 ≠ 难度」是同一个原理**（见 `us-grad-program-difficulty-tiers-6-majors.md`：MIT/Harvard 不招 CS 硕士却被列进第一档、Princeton EE 主录本校、Stanford EE 不收雅思——这些不是「难」，是「门没开」）。

两条独立路径收敛到同一个结论，说明这个结论是对的：**任何评分模型，只要允许不可行的选项参与排序，就一定会在某个时刻推荐一个走不通的路径。** 而人生路径的试错成本，比选校高一个数量级。

### 说对的第四件事：机会会衰减，而本仓库没有衰减管理

这是提案里**最有操作价值**的一条，而且它指出的正是本仓库现在最真实的一个隐患。

看本仓库里已有的这些事实：

- 丹麦：学签求职期从 3 年缩到 1 年、家属随行关闭、2027 集体协议工签 DKK322,000、**认证 2026-12-01**
- 美国：签证费 185 美元、SEVIS 350 美元、PERM 暂停
- HUST 飞跃手册 2023：里面的签证费、SEVIS 数字已经过期
- EU：VPD 不转送、6–8 周按校开具；瑞典单 offer + 1/15 锁排序

**这些全部是会过期的事实，而本仓库没有任何机制标记它们什么时候过期。** 一个 2026-11 写的文件，到 2027-11 会被一个用户当作现状来用。

提案提出的 `last_verified_at` / `expected_expiration` / `arbitrage_window` 字段，方向完全正确。**但落地方式必须改**——见第七节。

---

## 二、七维套利透镜：让 69 个文件可以被战略问题寻址

这是本文件的主要产出。**七维不是七个新目录，是七个提问角度。**每个角度下挂的，是仓库里**已经有**的文件。

### 01 教育套利 Education Arbitrage
> 利用不同教育体系的学费、学制、录取门槛、学分互认、奖学金和学历认可差异。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `top30-us-1-1.5yr-programs-2027fall.md` | 学制差：一年制 vs 两年制，总成本差近一倍 |
| `us-ai-masters-30-programs.md` | 项目结构差：同样叫 AI 硕士，课程与就业通道完全不同 |
| `us-grad-program-difficulty-tiers-6-majors.md` | 门槛差：同校不同项目差三档；名校洼地 |
| `niche-scholarships-12-channels.md` | 资助差：12 条非主流奖学金通道 |
| `us-phd-fee-waiver-guide.md` | 申请成本差：申请费可豁免，多数人不知道 |
| `industry-phd-programs-guide.md` | 学制差：产业博士 vs 学术博士，资助结构不同 |
| `yale-m2m-application-review.md` | 学分互认：双学位/跨校衔接 |
| `study-abroad-roi-and-internship-playbook.md` | 成本-回报计算底座 |
| `data/` `school-programs.csv` | 结构化项目底表 |

**典型的跨维组合**：中国本科 → 低成本获取美国大学正式学分 → 申请欧洲低学费硕士 → 当地科研/实习 → 人才短缺行业 → 毕业后工作资格。**这条路径的每一环都在仓库里，但没有任何一个文件把它串起来。**

### 02 劳动力市场套利 Labor Market Arbitrage
> 利用国家之间的人才供需错配、薪资差异、专业短缺和国际招聘制度。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `dinq-ai-job-map.md` | 岗位地图：AI 岗位的真实技能要求分布 |
| `returnee-employment-market-2025.md` | 回流侧的供需错配 |
| `career-global-capability-system.md` | 可迁移能力：什么能力跨市场保值 |
| `job-search-and-immigration-tools-stack.md` | 求职工具与身份工具的组合 |
| `perm-suspension-tech-impact.md` | 政策冲击：单一市场的劳动力通道可能瞬间关闭 |

### 03 地理套利 Geographic Arbitrage
> 在收入来源、居住成本、税负、购买力和生活质量之间寻找最优组合。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `run-manual-europe-36-countries.md` | 36 国 110 条路线的落地成本 |
| `letsmigrate-eu-residence-routes.md` | EU 居留路径的合法性差异 |
| `eures-eu-job-mobility-portal.md` | 31 国劳动力流动的官方入口 |
| `niche-overseas-routes-10.md` | 10 条非主流目的地路线 |
| `return-vs-stay-decision-framework.md` | 回流 vs 留下：决策框架 |
| `career-wealth-freedom-philosophy.md` | 收入、成本、自由的权衡 |

### 04 制度套利 Institutional Arbitrage
> 利用合法的教育签证、毕业后求职期、人才签证、创业签证、科研居留等制度衔接。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `denmark-siri-2026-2027-updates.md` | 求职期缩短、集体协议工签、认证时点 |
| `immigration-visa-resource-collection.md` | 签证资源总集 |
| `visa-policy-links.md` | 官方政策链接（必须带日期引用） |
| `eu-application-platform-routing.md` | 平台路由：VPD、单 offer 锁序、四国四种截止日 |
| `ai-business-three-tiers.md` | 身份路径：STEM-OPT、创业身份的分层 |
| `perm-suspension-tech-impact.md` | 制度风险：通道可能被行政性关闭 |

**这一维是全部七维里衰减最快的**，见第六节。

### 05 资本套利 Capital Arbitrage
> 利用不同市场的融资环境、资本成本、创业补贴、人才基金和资金来源差异。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `founder-fundraising-ecosystem.md` | 融资生态的地域差异 |
| `founder-fundraising-methodology.md` | 融资方法论 |
| `silicon-valley-incubator-guide.md` | 孵化器/加速器的准入与补贴 |
| `niche-scholarships-12-channels.md` | 非贷款型资金来源 |
| `us-phd-fee-waiver-guide.md` | 把成本侧压到零的具体做法 |
| `ai-investment-flywheel.md` | 资本流向的判断 |

### 06 网络套利 Network Arbitrage
> 利用大学校友网络、教授资源、产业集群、国际组织、投资人和跨国人脉之间的信息差。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `hust-alumni-professor-network.md` | 本校校友与教授网络的具体用法 |
| `cold-email-networking-template.md` | 冷启动触达模板 |
| `phd-advisor-sourcing.md` | 导师寻源：谁有钱、谁在招、谁带学生毕业 |
| `phd-cold-email-interview-tactics.md` | 套磁与面试的具体战术 |
| `program-intel-community-search.md` | 社区情报：官方口径之外的真相 |
| `founder-personal-profile-building.md` | 个人可被检索到的资产 |
| `student-profiles-research-method.md` | 反查真实录取画像的方法 |

### 07 技术套利 Technology Arbitrage
> 利用新技术扩散速度差、行业数字化程度差、AI 工具生产率差和技术人才供需差。

| 已有资产 | 它提供的套利差 |
| --- | --- |
| `career-what-ai-cannot-encode.md` | 技能保值：什么不会被自动化 |
| `career-ai-trapped-in-human-symbolic-system.md` | AI 落地的结构性瓶颈 |
| `sv-ai-industry-observations.md` | 硅谷一线的真实节奏差 |
| `sv-china-info-gap-fomo-bubble.md` | 信息差本身如何被定价 |
| `karpathy-llm-wiki-architecture.md` | 技术架构的认知差 |
| `deepseek-mhc-hyperconnections.md` | 前沿效率优化的方向 |
| `quant-weekly-compute-flow-hft.md` | 算力/低延迟方向的技能溢价 |
| `awesome-cyber-security-university.md` | 安全方向的教育资源差 |

### 这张映射表本身就是结论

**69 个文件，全部能被七维中的至少一维吸收。没有一个是多余的。**

所以提案说「需要建立一套新的顶层分类」——对的；但接着说「因此需要新建 `databases/` 等五个目录」——**不成立**。缺的是索引，不是仓库。

### 七维真正的用法：交叉处才是套利

**单维机会竞争充分、衰减快；跨维组合才是非对称收益的来源。**

一个单维机会长这样：「丹麦工签门槛低」——所有人都能查，所有人都知道，窗口在关闭。

一个跨维组合长这样：

> 用**教育套利**拿到欧洲低成本学分 → 用**网络套利**通过教授进入实验室 → 用**制度套利**利用该国的毕业后求职期 → 用**劳动力市场套利**进入当地短缺行业 → 用**地理套利**在低成本城市工作、在高购买力市场变现

这条路径的每一环都不稀奇，**但把它串起来需要同时持有五个维度的信息，而这正是单维机会搜索做不到的。**

所以提问的正确形式不是「有哪些机会」，而是：**「在我现有的约束下，哪两个维度之间的差，还没有被别人用掉？」**

---

## 三、人生选择权（Option Value）：不写公式，问三个问题

提案给出：

```
V(P) = E(R_P) − C_P − Risk_P + λ·O_P + μ·C*_P
```

**这个公式不该写进仓库。**理由很直接：`λ`、`μ` 没有取值来源，`O_P`（未来选择权）和 `C*_P`（长期复利）无法测量。写下来会制造一种「我们量化过了」的错觉，而这种错觉比不量化更危险——它会让一个本质上靠判断的决策，伪装成靠计算的决策。

但**这个概念是对的**，而且可以完全脱离公式落地。判断一条路径的选择权价值，只需要问三个问题：

### 问题一：失败之后，能不能回到原来的轨道？

| 路径类型 | 失败模式 | 可逆性 |
| --- | --- | --- |
| 一年制授课硕士 | 花掉一年和一笔钱，学历还在 | **高**。可回国就业、可再申、可换国家 |
| 直博（5–6 年） | 中途退出无硕士学位，年龄成本高 | **低**。退出成本是数年时间 |
| 先工作再出国 | 延迟 1–2 年，但保留了国内履历 | **高**。且随时可启动 |
| 依赖单一雇主的工签路径 | 雇主变故即失去身份 | **中低**。绑定在一个人/公司上 |
| 创业 | 资金与时间沉没，但技能与网络留存 | **中**。财务可逆性差、能力可逆性好 |

**规则：在预期收益接近时，优先可逆的那条。**不是因为保守，是因为可逆性本身就是一种可以兑现的资产——它让你在坏消息出现时还能换路。

### 问题二：成功之后，可选路径是变多了还是变少了？

这是最反直觉的一问。**有些「成功」会减少选择权。**

- 进入一个高度专业化、地域绑定强的岗位 → 起薪高，但三年后能去的地方只有同类岗位
- 读一个窄口径的硕士 → 学历有了，但换赛道要从零补先修课
- 拿一个绑定雇主的身份 → 留下了，但换工作要先解决身份

反过来：
- 一段带强推荐信的科研经历 → 申博、申硕、找工作三条路同时打开
- 一个可迁移的技能栈（如统计+编程+领域知识） → 行业可换、国家可换
- 一个真实的作品/论文 → 不依赖任何机构的背书

**规则：把「三年后的可选路径数量」当作一个显式指标去估，而不是只看起薪。**

### 问题三：这个选择锁死几年？

| 承诺期限 | 典型路径 | 决策含义 |
| --- | --- | --- |
| < 1 年 | 交换、短期项目、暑研 | 试错成本低，可以多试 |
| 1–2 年 | 一年制硕士、短期工作 | 主流区间，需认真算 |
| 3–5 年 | 两年制硕士+工作、部分工签路径 | 需要较高的确信度 |
| 5 年+ | 直博、移民、创业 | 需要接受「中途转向成本很高」 |

**规则：锁死时间越长，越应该先验证而不是先优化。**一个五年承诺不该建立在一份文档和几次搜索上，应该有至少一次低成本的实际接触（暑研、短期项目、和三个在读/在职的人聊过）。

### 三条问题的合并用法

不要算总分。**按顺序过：**

1. 如果一条路径**不可逆 + 减少选择权 + 锁死 5 年**，它需要在其他所有维度上压倒性更好才值得选
2. 如果一条路径**可逆 + 增加选择权 + 锁死 1 年**，它的容错空间很大，可以更激进
3. 两条路径在其他方面接近时，选**可逆性高**的那条

---

## 四、先筛资格，再谈打分

提案的 `INFEASIBLE` 机制要保留，但**落地成一个简短的检查表，不是一张评分卡**。

任何路径在进入比较之前，先过六道门。**任何一道门不过，直接标记 `INFEASIBLE`，不参与排序。**

| 门 | 要确认的 | 不过的典型情形 |
| --- | --- | --- |
| **身份资格** | 国籍、年龄、学历层次、现有居留状态 | 目标国项目不招该国籍；年龄上限；需要已有居留 |
| **学术资格** | GPA 口径、专业背景、语言、先修课 | 先修课缺失（最常见、最不可豁免）；WES 换算后不达标 |
| **财务资格** | 学费+生活费+资金证明+现金流断点 | 资金证明要求 12 个月流水；第一年缺口无来源 |
| **时间资格** | 申请窗口、毕业时间、签证审理期 | 毕业与入学时间对不上；签证审理期超过 gap |
| **法律资格** | 工作许可、兼职限制、移民倾向认定 | 学生签的兼职上限；某些表述触发拒签条款 |
| **机会资格** | 是否接受国际生、是否有实际开放名额 | 项目不招国际生；名额已被本校/合作项目占满 |

**这一步为什么必须前置？**

因为评分模型有一个结构性的失效模式：**它会用其他维度的高分，掩盖某一项为零。**

一个 GPA 3.9、GRE 330、三段实习的申请者，在六维评分里会得到很高的分数——但如果目标项目不招国际生，这个分数毫无意义。**分数越高，越不容易有人去检查那六道门。**

所以规则要写死：**先过门，再打分；门不过，分不算。**

---

## 五、反事实是强制项

提案最重视 `counterfactual-analysis.md`，这一点我完全同意，而且应该做成硬规则。

**任何路径建议，必须同时给出至少三条替代路径，其中一条必须是「现在什么都不做」。**

不是出于礼貌，是因为：

1. **没有反事实的建议无法被证伪。**「去读一年制硕士是个不错的选择」这句话，在什么情况下是错的？说不出来，就不是分析。
2. **反事实会暴露被忽略的低成本选项。**提案自己举的例子很到位——「直接申美硕」的替代方案里，有「先拿海外学分再申」「先暑研拿推荐信再申」「先国内跨国企业再外派」「直接申欧洲低学费」「本科毕业直接海外就业」。**这五条里至少有三条比原方案便宜。**
3. **「什么都不做」是必须出现的对照项。**因为很多焦虑驱动的决策，在明确写出「延迟一年的代价是 X」之后，会自动消解。

### 反事实的输出格式

对每条被考虑的路径，输出这张表：

| 路径 | 总成本 | 时间 | 成功概率（区间+依据） | 失败后能回到哪 | 三年后可选路径数 | 证据等级 |
| --- | --- | --- | --- | --- | --- | --- |
| 主方案 | | | | | | |
| 替代 1 | | | | | | |
| 替代 2 | | | | | | |
| 替代 3 | | | | | | |
| **什么都不做** | | | | | | |

**「证据等级」这一列不能省。**分三级：

- **A 级**：官方文件、项目页原文、法规条文（可引用）
- **B 级**：在读/在职者的第一手描述、多个独立来源一致（可参考，需交叉验证）
- **C 级**：单一论坛帖、中介宣传、模型推断（只能当线索，不能当依据）

**没有 A 级证据的单元格，必须留空或标 C，不能填一个看起来合理的数字。**这是防止整个分析变成一份精致的猜测的唯一办法。

---

## 六、机会生命周期与「事实会衰减」

提案提出的 Opportunity Lifecycle（Discovery → Validation → Execution → Competition → Compression → Expiration）是对的。**但它的落地方式必须是「日期纪律」，不是「数据库字段」。**

### 三类事实，三种衰减速度

| 事实类型 | 半衰期 | 本仓库里的例子 | 处理方式 |
| --- | --- | --- | --- |
| **身份/签证/政策** | 3–12 个月 | 丹麦求职期 3→1 年；PERM 暂停；签证费 185；SEVIS 350；认证 2026-12-01 | **每次引用都必须重新核实**，不允许直接复用文件里的数字 |
| **项目/学费/结构** | 1–2 年 | 一年制项目清单；录取门槛分档；cohort size；STEM CIP | 引用时标注 `as of` 年份，超过两年视为过期 |
| **方法/判断模式** | 5 年+ | 七源尽调流程；信息五级模型；SOP 框架；冷邮件结构；套利七维 | 可以稳定复用，但仍需检查例子是否过时 |

### 硬规则（写进 SKILL.md）

1. **每一条政策事实，必须带三样东西**：`as of YYYY-MM`、来源链接、预计失效点（或「不确定，需复核」）
2. **引用身份/签证类事实时，不允许直接复述文件里的数字**——必须先查当期官方页面，查到再引用；查不到就说明查不到，不要用旧数字
3. **每份 reference 的头部保留一个 `Last verified:` 行**，记录这份文件最近一次整体核实的时间
4. **当 `Last verified` 距今超过该类事实的半衰期，该文件的结论默认降级为「线索」而不是「依据」**

### 为什么不做 `databases/`

提案建议建九个 `databases/` 子目录存放国家、教育、奖学金、劳动力市场、移民、产业、资本、网络、机会。

**这个设计有一个结构性错误：它假设仓库能跑赢事实衰减。**

丹麦那条政策从「求职期 3 年」改成「1 年」，是一个部委网页的一次更新。仓库里对应的文件在下一次有人手动修改之前，会一直保持错误。**而没有人会定期回来修改——因为没有触发机制，也没有收益。**

所以正确的分工是：

| 谁 | 存什么 |
| --- | --- |
| **仓库** | 方法、判断模式、带日期的快照、来源链接、失效条件 |
| **实时查询** | 当前的政策数字、当前的名额、当前的学费 |

**仓库能存的是「怎么查」和「截至某日是什么」，不能存「现在是什么」。**把后者塞进仓库，只会造出一个看起来完整、实际上在持续腐烂的数据层——而它比没有更危险，因为它有权威的外观。

---

## 七、这份提案不该照做的四件事

### ① `databases/` 静态存储外部事实 —— 驳回

理由见第六节。核心是：**事实衰减速度快于维护速度，静态存储必然腐烂，且腐烂后仍有权威外观。**

替代：方法 + 带日期快照 + 来源链接 + 强制复核规则。

### ② `engines/` 拆成七个文件 —— 驳回

提案要建 `profile-engine`、`opportunity-discovery`、`path-combination`、`path-scoring`、`scenario-simulation`、`counterfactual-analysis`、`decision-engine` 七个文件。

**七个文件意味着每个都只有一两段实质内容。**而这个仓库的 reference 文件之所以有用，是因为每个都装满了具体事实（65,678 条 RMP 评价、19 个 CDS 因素、36 国 110 条路线）。

**拆得越细，每份越薄；越薄，越像目录而不像内容。**

替代：**一个决策协议文件**，把六步写成一个流程（见第八节）。一个写得好的协议，胜过七个写得空的模块。

### ③ 在还没有数据之前定义 `models/*.json` schema —— 驳回

`path-schema.json`、`opportunity-schema.json`、`country-schema.json`、`user-profile-schema.json`、`scoring-schema.json`。

**在没有 20 条真实记录之前定义 schema，是用结构代替思考。**你会定义一个字段集，然后发现真实的记录需要另外五个字段，然后改 schema，然后旧记录全部失效。

替代：先用 Markdown 表格记 10–20 条真实路径，看它们**实际**需要哪些字段，再抽 schema。**结构应该是数据的结果，不是数据的前提。**

### ④ 六维权重 25/20/20/10/10/15 与公式 V(P) —— 驳回（作为「测量」保留）

提案自己写了「这些权重只是初始假设，不是经过实证验证的普遍规律」——**这句免责声明本身就说明它不该以评分模型的形式出现。**

一旦写成一个带百分比的模型，它就会被当作测量结果使用：用户会问「我的路径多少分」，模型会回答「72 分」，然后「72 分」会取代「我该不该」这个真问题。**这是量化最典型的失败模式——用一个数字替换掉一个判断。**

替代：
- **选择权** → 三个问题（第三节），不定量
- **可逆性** → 五级分类（高/中高/中/中低/低），可判断
- **证据等级** → 三级（A/B/C），可标注
- **成本与时间** → 可以真的算，用代码算
- **成功概率** → 只给区间 + 依据 + 置信说明，不给点估计

**能算的算，不能算的说不能算。**这比一个 72 分诚实得多，也有用得多。

### 另外两件提案没注意到的事

**⑤ `user-profile-schema.json` 在 public 仓库里是隐私违规。**
本仓库是 public，且项目已确立规则：**GPA / CV / SOP / offer / 融资细节绝不入 public 仓库**。一个用户画像 schema 在这个仓库里，要么是空的（无用），要么是违规的。

**⑥ 提案没发现，七维里的大部分内容仓库已经有了。**
它把仓库当作「一个留学申请工具」，因此以为需要从零建七个维度。实际上 69 个文件已经覆盖了全部七维（见第二节映射表）。**真正的风险不是内容不足，是造出两套并行的体系互相打架**——一套按主题（现有），一套按维度（新建），然后同一件事有两个说法。

---

## 八、落地：最小可行改造清单

按「性价比」排序。前三条现在就做，后三条按需。

### 现在做（已完成 / 本文件即产出）

| # | 改动 | 状态 |
| --- | --- | --- |
| 1 | 七维透镜 + 69 文件映射表 | ✅ 本文件第二节 |
| 2 | 选择权三问（替代公式） | ✅ 本文件第三节 |
| 3 | 资格六门（`INFEASIBLE` 前置） | ✅ 本文件第四节 |
| 4 | 反事实强制项 + 证据三级 | ✅ 本文件第五节 |
| 5 | 日期纪律四条硬规则 | ✅ 本文件第六节，已写入 SKILL.md |

### 按需再做

| # | 改动 | 触发条件 |
| --- | --- | --- |
| 6 | 给高衰减文件补 `Last verified:` 行 | 下次任何文件被修改时顺手补，不专门做一轮 |
| 7 | 路径记录表（Markdown 表格，先记 10–20 条真实路径） | 有 10 条以上真实案例后，再考虑抽 schema |
| 8 | 情景模拟 / 多目标优化 / Monte Carlo | **不做**，除非这个仓库真的变成一个软件产品 |

### 一个六步决策协议（替代七个 engines 文件）

```
1. 现状约束     → 用户的六道门现在各是什么状态
2. 候选路径     → 七维透镜逐维过一遍，找出 3–6 条候选
3. 资格筛选     → 六门过滤，标记 INFEASIBLE，不参与后续
4. 反事实表     → 主方案 + ≥3 替代 + 什么都不做，五列 + 证据等级
5. 三问检验     → 可逆性 / 选择权增减 / 锁死年限
6. 最小下一步   → 只给一个动作，且必须是可在一周内完成的
```

**第 6 步是最容易被跳过、也最重要的一步。**

「你应该去欧洲」不是下一步。「这周去 EURES 查三个国家的岗位数量，记下雇主是否明确写 visa sponsorship」是下一步。

**判断一个路径分析有没有用，标准很简单：看完之后，你能不能在今天之内做一件具体的事。**

---

## 九、English Key Takeaways

1. **The diagnosis is right; the prescription is wrong.** The repository does lack a strategic layer — but what it lacks is *addressability*, not content. All 69 reference files map onto the seven proposed arbitrage dimensions; none is redundant. The repo is organized by topic, which means only someone who already knows what to ask can use it. A strategic question ("given my constraints, what is the next step that most expands my options?") has no filename here. The fix is a lens, not a new directory tree.

2. **The proposal's own internal contradiction is the tell.** It advises "start with JSON + CSV, don't over-engineer" and then specifies ~35 files across five directories plus NetworkX, OR-Tools, Monte Carlo, and PostgreSQL. That is not a repository modification; it is a different product.

3. **A static `databases/` directory cannot work, because policy facts decay faster than a repo can be maintained.** Denmark's post-study job-search period changed from three years to one; PERM was suspended; visa fees and SEVIS figures in a 2023 guide are already wrong. There is no trigger to update these and no reward for doing so — the directory would rot while retaining the appearance of authority, which is worse than having nothing. A repo can store methods, dated snapshots, source links, and expiry conditions. It cannot store "what is true now."

4. **Option value is real, but the proposed formula should not be written down.** Every term except cost is unmeasurable: λ, μ have no source, O_P and C*_P cannot be observed. Stating the formula manufactures false precision and lets a judgment problem masquerade as a calculation. Replace it with three questions: (a) if this fails, can I return to my previous track? (b) if this succeeds, do my available paths multiply or narrow? (c) how many years does this lock me in?

5. **Question (b) is the one people skip, and it is the one that matters most.** Some successes reduce optionality: a hyper-specialized, geography-bound role pays well but leads only to more of itself; a narrow master's leaves you needing prerequisites to switch; an employer-bound visa lets you stay but not move. Conversely, a strong research letter or a portable skill stack opens several tracks at once.

6. **Feasibility must precede scoring, and this conclusion was reached twice independently.** The six-professional difficulty tiers file established that Harvard/MIT admitting no CS master's students is an *eligibility* fact, not a *difficulty* fact. The proposal's `INFEASIBLE` flag is the same principle. Two independent paths converging is a good signal it is correct — and the failure mode it prevents is specific: a scoring model lets a high average conceal a zero. A 3.9 GPA with three internships scores well even when the program admits no international students, and the higher the score, the less likely anyone checks the gate.

7. **Counterfactuals should be mandatory, including "do nothing."** A recommendation without alternatives cannot be falsified — "a one-year master's is a good choice" has no conditions under which it is wrong, which means it is not analysis. The proposal's own example makes the case: among the alternatives to applying directly to a US master's are earning transferable credits first, doing a summer research stint for a letter, and taking a domestic multinational role with an eventual transfer — at least three of which are cheaper.

8. **Every cell in the comparison table needs an evidence grade.** A (official documents, program pages, statute), B (first-hand accounts, multiple independent sources agreeing), C (single forum post, agency marketing, model inference). Cells without A-grade evidence must be left blank or marked C rather than filled with a plausible-looking number. This is the only defense against the whole analysis becoming an elaborate guess.

9. **A user-profile schema in a public repository would violate this project's own privacy rule.** GPA, CV, SOP, offer details, and funding terms are explicitly excluded from the public repo. A profile schema here is either empty or a breach.

10. **The test of a path analysis is whether it produces one action you can complete this week.** "You should go to Europe" is not a next step. "Look up three countries' job counts on EURES this week and note whether each posting states visa sponsorship" is.

---

## 十、Connection to Repo Themes

- **`references/us-grad-program-difficulty-tiers-6-majors.md`** — the eligibility-versus-difficulty distinction there is the concrete instance of the `INFEASIBLE` principle in section four. Read together: one gives the school-level case, this file generalizes it to life paths.
- **`references/study-abroad-roi-and-internship-playbook.md`** — that file is the ROI engine; this file is the correction to it. ROI is necessary and insufficient, and its bias has a definite direction: it systematically undervalues paths that preserve optionality, because optionality does not appear in the numerator.
- **`references/return-vs-stay-decision-framework.md`** / **`references/niche-overseas-routes-10.md`** / **`references/letsmigrate-eu-residence-routes.md`** — these are the geographic and institutional dimensions' existing assets; section two's mapping table is what makes them addressable from a strategic question rather than a topic.
- **`references/denmark-siri-2026-2027-updates.md`** / **`references/visa-policy-links.md`** / **`references/immigration-visa-resource-collection.md`** — the highest-decay files in the repo. Under section six's rule, their numbers must be re-verified before every citation rather than quoted from the file.
- **`references/hust-oeises-feiyue-2023-guide.md`** — the clearest existing example of decay: a 2023 guide whose visa fee and SEVIS figures are already wrong. It is also the best available empirical check on any proposed path, because it records what HUST graduates actually did.
- **`references/founder-anti-hedging-principles.md`** — an interesting tension worth naming: that file argues against hedging, while option-value thinking argues for preserving it. The reconciliation is timing — hedging early (before commitment) is cheap and preserves optionality; hedging after commitment is what the anti-hedging file is warning about.
- **`references/career-wealth-freedom-philosophy.md`** — supplies the preference weights that section seven refuses to hard-code. The reason the six-dimension model was rejected is that its weights are personal, not universal; that file is where a person's actual weights live.
