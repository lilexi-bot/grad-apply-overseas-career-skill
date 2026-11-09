# RUN · 润 — 海外移居手册（GitHub: BryceYuuu/RUN）

> 来源：用户 2026-11-10 分享的仓库链接 <https://github.com/BryceYuuu/RUN>
> 本文件为**该手册的结构化导读 + 可靠边界判定**，不复制其正文。原文内容以 CC BY-SA 4.0 授权，本仓库为 MIT，因此只做引用与归纳，不搬运原文与数据表。
> 手册自身标注：**最新更新 2026-11-03**；欧洲 36 国 / 110 条路线 / 13 个全球目的地 / 380+ 官方来源链接。

---

## When to load

- 用户在比较**欧洲各国**的居留路径（数字游民 / 蓝卡 / 创业自雇 / 被动收入 / 投资）
- 用户问「我这条路上还有没有可能」「这个签证是不是已经关了」
- 用户想知道**毕业后能留多久找工作**（欧洲 12 国 + 美加澳新日港对比）
- 用户是中国大陆护照，需要知道**哪些路线对自己直接不可用**
- 用户在评估「欧洲 vs 美加澳新」的横比，或想找一个能横向比较门槛的单一数据源
- 用户提到 RUN / 润 / 润手册 / 移民手册 / BryceYuuu

## Trigger

RUN、润、润手册、海外移居手册、BryceYuuu、欧洲移民、欧洲36国、数字游民签证、欧盟蓝卡、蓝卡门槛、创业自雇、被动收入居留、投资居留、黄金签证、毕业后找工作签证、找工作居留、永居年限对比、入籍年限、双重国籍、中国护照不适用、programmes.csv

## Keywords

`RUN manual` `Europe residency routes` `digital nomad visa` `EU Blue Card threshold` `post-study work visa` `permanent residence years` `golden visa closed` `China passport exclusions`

---

## 一、这份手册是什么

| 维度 | 事实 |
| --- | --- |
| 定位 | 中文开源移居手册，按「你的收入从哪来」分六类路线：数字游民 / 技术工作·蓝卡 / 留学转工作 / 创业自雇 / 被动收入 / 投资居留 |
| 规模 | 欧洲 **36 国**、**110 条**路线、欧洲以外 **13 个**目的地（美加澳新、日韩新港、泰马、阿联酋、拉美）、**380+** 条官方来源链接 |
| 结构 | `docs/europe/` 36 国各一页（脚本自动生成）· `docs/routes/` 按路线 · `docs/global/` 非欧洲 · `docs/practical/` 文件准备/税务居民/落地 90 天清单 |
| 数据 | `data/programmes.csv` — **99 条路线的结构化数据**，12 个字段，可直接用 Excel 打开 |
| 更新机制 | `src/details/<国家>.json` + `src/notes/<国家>.md` 手写，`scripts/build_docs.py` 生成文档与图表 |
| 许可 | 内容 CC BY-SA 4.0，脚本 MIT |

### 数据血缘（决定它能信到什么程度）

- **欧洲 99 条**：来自 [LetsMigrate.org](https://letsmigrate.org/zh-hans/countries/) 的公开项目记录，本项目改写并补充细节
- **另外 11 条 RUN 补充**：西班牙非营利居留、葡萄牙 D7、德国机会卡与技术工人签证、希腊 FIP、意大利选择性居留、马耳他 GRP、爱沙尼亚创业签证、英国技术工作/全球人才/HPI
- **生活与身份档案**：Numbeo（生活成本/房租/安全，2026 年中）、Eurostat（平均工资）、Tax Foundation（个税 2026）、Henley（护照 2026）、各国移民局（永居/入籍/双重国籍）

**关键判断：这是一个二手聚合项目，不是官方源。** 它的价值不在「比官方更权威」，而在三件官方做不到的事：① 把 110 条路线放在同一张表里可横向比；② 把门槛统一折算成欧元月收入；③ 把散在 36 个国家的规则变化收进一张时间表。

作者自己在 README 里写得很清楚：**欧洲以外（美加澳新日韩等）的核查深度低于欧洲篇。** 这句话要当真——全球篇只能当线索，不能当依据。

---

## 二、最值得读的部分：2025–2026 政策变化表

这是全篇最高密度的资产。**移民信息最大的风险不是「不知道有什么路」，是「知道的那条路已经没了」。** 17 条变化里，5 条关闭、4 条收紧：

### ⛔ 已关闭（5 条）

| 时间 | 国家 | 关了什么 |
| --- | --- | --- |
| 2025-04-03 | 🇪🇸 西班牙 | 黄金签证**全部投资类别**停止受理新申请 |
| 2025-07 | 🇲🇹 马耳他 | 投资入籍（护照项目）被欧盟法院判决后**废止**，只剩功绩入籍 |
| 2026-05 | 🇮🇸 冰岛 | 远程工作长期签证**废止**，目前无可用数字游民路线 |
| 2026-06-30 | 🇨🇦 加拿大 | 联邦创业签证 **SUV 完全暂停** |
| 2026-09-15 | 🇱🇻 拉脱维亚 | 新《移民法》关闭**买房居留**和银行次级债居留 |

另有 2022-02-17 关闭、仅剩历史案件的 🇬🇧 英国 Tier 1 投资移民（永居申请截止 2028-02-17）。

### 🔺 已收紧（4 条）

| 时间 | 国家 | 变化 |
| --- | --- | --- |
| 2025-10-16 | 🇯🇵 日本 | 经营管理签证资本金 **500 万 → 3,000 万日元**，并须雇员和日语 |
| 2026 | 🇵🇹 葡萄牙 | 国籍法改革：入籍从 5 年改为**一般 10 年** |
| 2026 | 🇦🇩 安道尔 | 被动居留投资门槛涨到 **100 万欧元 + 年度配额** |
| 2026 | 🇸🇪 瑞典 | 工作许可须达**中位工资 90%**（SEK 34,470/月） |
| 2026-11-02 | 🇬🇧 英国 | 永居标准 **5 年 → 10 年**（详见第四节） |

### 🆕 新开 / 🔄 变化（8 条）

| 时间 | 国家 | 变化 |
| --- | --- | --- |
| 2025-11-21 | 🇸🇮 斯洛文尼亚 | 新开数字游民许可；蓝卡门槛降至平均工资 1 倍 |
| 2026-01-01 | 🇧🇬 保加利亚 | 改用欧元（2025 年已完整加入申根） |
| 2026-01-08 | 🇫🇮 芬兰 | 永居新规：年收入 ≥ €40,000 可 **4 年**申请 |
| 2026-04-27 | 🇵🇱 波兰 | 居留申请全部改为 **MOS 线上递交** |
| 2026-06-30 | 🇰🇷 韩国 | F-1-D 数字游民签证**转为正式签证**，最长 3 年 |
| 2026-09-30 | 🇺🇸 美国 | 法院**阻止执行** H-1B 10 万美元附加费；抽签改为**按工资加权** |
| 2026-11-03 | 🇨🇦 加拿大 | Express Entry 新规：加拿大工作经验、高薪职业 offer 加分，**offer 不再需要 LMIA** |
| 2026-11 | 🇧🇪 比利时 | 蓝卡审理时限缩短为 **90 天** |

---

## 三、被低估的一页：中国大陆护照直接不适用的路线

这是整份手册最实用的一个栏目，也是最容易被其他清单误导的地方——**很多「欧洲数字游民签证清单」会把这几条列进去，但不标注国籍排除。**

| 路线 | 排除原因 |
| --- | --- |
| 🇨🇿 捷克 Digital Nomad Program | 计划本身不含中国大陆护照 |
| 🇯🇵 日本数字游民签证 | 对象国名单不含中国大陆 |
| 🇱🇻 拉脱维亚远程工作签证 | 雇主须为 OECD 国家企业 |
| 🇵🇦 巴拿马友好国家签证 | 对象国名单不含中国大陆 |
| 🇺🇸 美国 E-2 条约投资者 | 中国不是条约国 |

**用法：** 看到任何「某国有数字游民签证，月入 €X 即可」的信息，第一件事是查**国籍适用范围**，不是查收入门槛。

---

## 四、英国 Earned Settlement：手册给的档位表比公告更细

这是本仓库第二次核这个政策（第一次见 `job-search-and-immigration-tools-stack.md`）。手册的版本比 GOV.UK 新闻稿更细，且**关键数字与官方一致**：

| 档位 | 条件 |
| --- | --- |
| **3 年** | 最近 4 年中有 3 年收入 ≥ **£125,141**，或属于「最高人才组」（如全球人才签证） |
| **5 年** | 最近 5 年中有 3 年收入 ≥ **£50,271**；或在指定公共服务岗位工作 5 年；或与英国有特定联系（如英国公民配偶） |
| **10 年（标准）** | 最近 7 年中有 5 年收入 ≥ **£12,571**，并满足全部基本要求 |
| **20 年** | 违反移民规定，或近 5 年领取过公共福利 |

**所有人的基本要求**：英语 B2（永居英语要求 **2027-03-26** 起升到 B2）、无犯罪记录、不欠政府债务、至少 **3 年 NI 缴费**、通过 Life in the UK。夫妻可合并收入，家庭门槛 **£25,142**（个人门槛两倍）。

**算 / 不算永居年限**：
- ✅ 技术工作、全球人才、扩张、创新创业、英国祖籍、国际体育人员等「核心路线」；家庭类签证；部分保护类身份
- ❌ 学生签证、毕业生签证、HPI、访客、全球商务流动、临时工作、青年交流、季节工、海外家政工

**过渡与例外**：2025 年 5 月白皮书发布前已入境的**护理工作者**（年薪 £25,000、满足担保条件）保留 5 年路径；BN(O)、英国军人海外成员、Windrush 等历史路线持有人保留原路径；**原咨询方案中低于 RQF 6 级岗位的 15 年路径已取消**，并入 10 年标准路径。

**时间表**：2026-12 起移民规则修订陆续写入 → 2027 年内分批实施 → 2027-01-01 毕业生签证缩短为 18 个月（博士 3 年）→ 2027-03-26 永居英语升到 B2。

### 本仓库的补充判断（与手册的差异）

手册反复表述「**十年长居路线关闭**」。这个说法需要加一个时间限定：

- 截至 2026-11-10，**Immigration Rules Appendix Long Residence 仍然有效**（2026-10-29 更新），LR 3.1 仍要求 10 年合法连续居住，LR 13.1 甚至给出了 2027-03-26 之后 B1→B2 的过渡条款。
- 所以「关闭」目前是**已宣布、待写入**的状态，不是已生效的规则。手册自己也写了「2026 年 12 月起陆续写入规则」——两句话放在一起读才是完整的。
- **这个差别对个人决策是决定性的**：如果按现行规则已经满足十年长居，现在仍可递交；等规则写入后就未必。手册文末那句「已满足十年长居条件的人，应在新规写入法规前尽快咨询持牌律师」，其实比标题里的「路线关闭」更准确。

**使用规则：英国永居一律以 GOV.UK 与 Appendix 原文为准，手册用于预警和读懂方向，不用于判断「我现在还能不能交」。**

---

## 五、本仓库归纳：怎么读这份手册

### 1. 先读「关闭」，再读「开放」

一份移民清单最容易过时的是「开放列表」，最不容易过时的是「关闭记录」——关掉的项目基本不会重开。所以正确的阅读顺序是：**变化表 → 排除清单 → 门槛排行 → 具体国家页**。

### 2. 它的 `pr` 字段是刻意保守的，这是优点

`programmes.csv` 里永居列只有三档：`可能通向永居` / `通常偏临时` / 空。它**不假装能给出确定的永居年限**——因为多数路线转永居的年限取决于后续换成什么签证、在哪个州/大区、工资是否达标。这种保守比给出一个漂亮但错的数字更有用。

### 3. `income_eur_month` 是它真正的护城河

把 110 条路线的收入门槛统一折算成欧元月收入，才使得「阿尔巴尼亚 €330 / 斯洛伐克蓝卡 €1,944 / 西班牙数字游民 €2,442 / 葡萄牙 €3,680 / 罗马尼亚 €5,500」这一串能直接比较。**没有这一列，这 110 条就只是一堆不可比的数字。**

### 4. 欧洲篇可作决策起点，全球篇只能作线索

作者明确说欧洲以外「核查深度低于欧洲篇」。据此分工：
- **欧洲 36 国** → 可以用来做初筛和横向比较，结论仍需回官方页确认
- **美加澳新日韩新港** → 只用来「知道有哪些类型」，不能用来判断门槛

### 5. 它是 LetsMigrate 的二次加工，两者要一起用

本仓库 `/letsmigrate` 命令用的就是 LetsMigrate 原始数据。RUN 在其上做了三件 LetsMigrate 没做的事：**政策变化时间表、国籍排除清单、生活成本与税负档案**。所以不是「二选一」，而是：**用 LetsMigrate 查单条路线的原始字段，用 RUN 查这条路线最近有没有变、中国人能不能用、过去生活要多少钱。**

---

## 六、和本仓库其他命令的关系

| 命令 / 文件 | 关系 |
| --- | --- |
| `/letsmigrate` | **上游数据源**。RUN 的欧洲 99 条来自 LetsMigrate。查单条路线的官方链接和原始字段用它 |
| `/niche-routes` | 那份是「冷门国家/冷门路径」的深度叙述，RUN 是「广度 + 时效」。互补：先用 RUN 扫出候选，再用 niche-routes 深挖 |
| `/study-to-work`（见 `study-to-work` 相关章节） | RUN 的 `docs/routes/study-to-work.md` 有 12 国毕业后找工作签证期限对比，可直接用于选校阶段判断「读完能不能留下」 |
| `/scholarships` | 资助侧。RUN 不管钱，只管身份；两者拼起来才是完整的「能不能去 + 去了怎么活」 |
| `/tool-stack` | 那份把 RUN 定位为「五层移民工具」中的第 4 层（时效手册）。本文件是它的展开版 |
| `/top30-short-programs` | 选校看学制，RUN 看学制结束后的居留窗口。1–1.5 年制项目要特别核对毕业后的找工作签证长度 |
| `/study-roi` | ROI 的分母是成本，分子是「留下来之后的收入」。RUN 提供的永居年限直接决定分子的时间跨度 |

---

## 七、可执行清单

1. **先查排除清单**：捷克数字游民、日本数字游民、拉脱维亚远程、巴拿马友好国家、美国 E-2——这五条对中国大陆护照不可用，别在它们上面花时间。
2. **按收入来源定位**：目的国雇主 offer → 蓝卡/技术工作；境外雇主或客户 → 数字游民；自己当老板 → 创业自雇；一笔闲置资金 → 投资居留；养老金/租金/存款 → 被动收入。**这一步决定你能看哪 1/6 的内容。**
3. **用 `programmes.csv` 做初筛**：按 `income_eur_month` 排序，先看自己够不够门槛，再看 `pr` 字段判断是不是死路。
4. **只看 2026 年之后核查过的条目**：CSV 的 `verified` 字段标了核查日期，2025 年及更早的要重新核。
5. **回国别只看门槛**：同时看该国是否允许双重国籍（中国不承认）、入籍年限、以及「居留 ≠ 税务居民」的 183 天规则（见其 `docs/practical/tax-residency.md`）。
6. **落地前看 90 天清单**：住址登记、居留卡、税号、银行开户、续签时间点——这些漏一项就会影响后续永居年限的连续性。
7. **任何结论回官方页**：手册每条都附官方链接（共 380+），点进去核一遍，尤其是金额门槛（每年调整）和国籍适用范围。

---

## 八、English Key Takeaways

1. **RUN is a secondary aggregator, not a primary source.** Its 99 European routes derive from LetsMigrate.org, plus 11 self-added routes; living-cost and tax data come from Numbeo, Eurostat, Tax Foundation and Henley. The author states explicitly that non-European coverage is verified less deeply than the European section.
2. **Its unique value is three things official sources cannot give you:** a single comparable table across 110 routes, thresholds normalised to EUR/month, and a dated timeline of 2025–2026 policy changes.
3. **Read the closures first.** Of 17 tracked changes, five routes closed and four tightened. A closed route essentially never reopens, so that table ages far better than any "open routes" list.
4. **The most underrated section is the China-passport exclusion list:** Czech digital nomad, Japan digital nomad, Latvia remote work (OECD employer required), Panama Friendly Nations, and US E-2 are all unavailable to mainland Chinese passports — yet they routinely appear on generic "digital nomad visa" lists without that caveat.
5. **Its PR field is deliberately conservative** — only "possibly leads to PR" / "usually temporary" / blank. That honesty is more useful than a confident but wrong number of years, because the actual path depends on which visa you convert into later.
6. **The UK "10-year long residence is closed" claim is announced-but-not-yet-in-force.** Appendix Long Residence was still valid as of 2026-10-29; rules are to be laid from December 2026. Anyone who already qualifies should act before the rules are written — which is what the manual itself advises at the end, and is more accurate than its own headline.
7. **Use LetsMigrate and RUN together, not either/or:** LetsMigrate for a single route's original fields and official links, RUN for whether it recently changed, whether a Chinese passport can use it, and what living there costs.
