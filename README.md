# Grad Apply & Overseas Career — Master Skill

**留学申请 + 海外工作 + 创业路径 一体化 AI Skill** · v2.13.51 · MIT

An end-to-end, Claude-Code/Codex-native skill for master's/PhD applications across 8 tracks
(FinEng · ECE · ME/Robotics · CS/AI · Data Science · Interdisciplinary · Tech Transfer · **Founder**),
plus overseas career and hard-tech founder visa/fundraising strategy.

> **⚠️ Read before using — three hard limits**
> 1. **AI hallucinates.** School tuition/deadlines and visa policies change often. Every factual figure
>    must be re-verified on the **official website link** the skill attaches. Never submit based on AI output alone.
> 2. **AI drafts are not final.** SOP/CV require your own deep rewrite, then a native-English proofread.
>    Plagiarism from sample essays is prohibited.
> 3. **Visa content is strategy reference, NOT legal advice.** Canada/UK/US rules shift (e.g. Canada SUV
>    paused 2026-01). Consult a licensed immigration lawyer before any filing.

## 🚀 Quick start (3 steps)

```bash
# 1. get the skill
git clone https://github.com/lilexi-bot/grad-apply-overseas-career-skill.git my-applications
cd my-applications

# 2. open in your agent (auto-loads CLAUDE.md / AGENTS.md → SKILL.md)
claude        # or: codex

# 3. type the first command
/profile-intake
```

That's it. Natural language also works — e.g. *"帮我开始准备美国CS硕士申请"* or
*"compare founder visa routes for Singapore vs UK"* — the skill metadata auto-triggers.
Follow-on flow: `/build-evidence-map` → `/school-match` → `/cv-generate cs` → `/sop-draft` → …
(see `examples/` for what good outputs look like).

## Repository structure

```
SKILL.md                     # router: YAML metadata (auto-trigger) + workflow + command routing
CLAUDE.md / AGENTS.md        # auto-load entry files (@-import SKILL.md)
templates/                   # fill-in templates (private data goes here, gitignored paths)
  evidence-map-template.md   #   reusable achievement library
  school-comparison-template.md
  cv-template.md / cv-template.tex
  cv-template-academic.md   # 学术/研究向英文CV（Education→Publication→Patent 前置）
  sop-outline-template.md
  founder-pack-template.md   #   venture brief + visa-evidence checklist
  lor-cold-email-template.md
  deadline-offer-templates.md
references/                  # external data loaded on demand
  school-programs.csv        #   45-programme seed DB (verify on official URLs!)
  visa-policy-links.md       #   official immigration source links (UK/US/CA/SG/FR/…)
  founder-fundraising-ecosystem.md  # YC/US/Middle East/China hard-tech investors + fundable-founder traits (Cambridge notes)
  career-mindset-adaptability.md    # 心态底座：应对世界变化的元能力（中文原文 + agent 导读）
  interview-communication-notes.md  # 面试表达：术语校准 jargon/plain-English + 前台角色气质
  leadership-ladder.md              # 领导力叙事五档阶梯（美硕/MBA/DMBA 文书 + 活动/晋升思路）
  phd-advisor-sourcing.md           # 博士导师挖掘法（官网/Scholar/套话在读生）+ CS/AI 红榜种子
  founder-coldstart-playbook.md     # 创始人冷启动四条渠道（X/Reddit/LinkedIn/UGC）+ 前100用户漏斗
  founder-anti-hedging-principles.md # 斯坦福GSB创业三反常识：阶梯式冒险/无中间地带/黑科技未必赢
  founder-infrastructure-migration.md # 链上支付案例（X/Meta/Visa/渣打）+ 用户假设/结算场景/合规原则
  founder-personal-profile-building.md # 创业者个人品牌建设：profile画圆 + details扎实；真实人设≠包装；身份层护城河
  founder-fundraising-methodology.md # 融资实战5大认知纠偏 + 7问自检 + 估值策略（Down Round/被估值锁死/5问压力测试）
  returnee-employment-market-2025.md # 2025海归就业现状：回国规模/生源地/学历行业/薪资/城市下沉（智联招聘数据）
  ecm-interview-prep-ms-hk.md      # MS香港ECM面试辅导：Placement技术面 + Why Move跳槽叙事 + Deal Experience讲述框架
  phd-cold-email-interview-tactics.md # PhD套磁信四条：match>interest/ability>passion/主动提问/follow up节奏
  yale-m2m-application-review.md    # Yale M2M申请复盘：candidate画像/ESG故事线/1+1捷径
  ai-investment-flywheel.md         # AI投资飞轮：LLM股票对冲token成本/正反馈循环/财富分化
  sequoia-cognitive-revolution.md   # 红杉认知革命：AI=工业革命押韵/Engels' pause/速度风险
  how-to-live-better-guide.md       # 高性价比人生指南入口：552条循证建议/32章索引/在线检索
  type-safe-jev-decision-model.md   # TypeSafe Jev判断模型：并行决策/RLCD校准/Agent高频检查降本
  silicon-valley-incubator-guide.md # 硅谷孵化器指南+Startup Compass匹配工具
  career-what-ai-cannot-encode.md     # AI无法编码的人类原生特质（信任/品味/审美/想象/情绪）+ Hassabis微观结构
  investment-codex-reverse-engineering.md # Codex逆向工程美股博主半公开指标（三步法：完整摄入/已知未知分离/假设空间限定）
  career-oak-high-level-state-transition.md # Oak架构/Sutton：世界用高层状态转移描述，agent取时间延展选项
  career-ai-trapped-in-human-symbolic-system.md # 姚期智-Sutton对话：AI被困在人类符号系统/数学范式内，仅人类自身或可跳出
  sv-ai-industry-observations.md               # 硅谷AI一线观察：中美AI格局/AI制药/泡沫预警/Google FDE
  cold-email-networking-template.md             # Cold Email Networking模板：4块结构回复率95%
  career-global-capability-system.md            # 年轻人版本答案：语言+专业技能+AI+互联网+全球化=能力系统
  grey-market-cognition-hedge.md                # 灰产认知对冲：非共识判断/钻空子思维/索罗斯反身性/庙堂与江湖
  quant-weekly-compute-flow-hft.md              # Quant周报：Jane Street算力军备/Systematic Flow/HFT扩张/大宗电子化/指数分化
  sv-china-info-gap-fomo-bubble.md     # 硅谷与国内两周信息差：VC FOMO/泡沫共识/应用vs模型ROI/positioning startup/RSI/OAI机器人数据
  essmote-ai-writing-platform.md       # Essmote AI 留学文书平台（PS/SOP/CV/推荐信生成 + 人工润色）
  founder-collaboration-postmortem.md   # 创业合作复盘：尽调缺失/先钱后干活/管理边界失守/止损信号/单向惩罚条款
  awesome-cyber-security-university.md # 免费网络安全自学课程体系：Red Team/Blue Team/CTF/OWASP/逆向/取证（TryHackMe）
  immigration-visa-resource-collection.md # 移民/签证/海外工作开源资源合集：awesome-immigration/H1B数据/高技能求职/Five Flags/DiasporaAI
  perm-suspension-tech-impact.md       # PERM暂停与科技行业留美影响：8家公司暂停、量化投行转型、加拿大香港替代
  return-vs-stay-decision-framework.md # 回国or留美10条决策框架：储蓄速度/家庭/身份/性格/躺平/子女教育/人生目标
  dinq-ai-job-map.md                  # 中国AI岗位地图：279家公司/12895+岗位、按城市区域分类（jobs.dinq.me）
  industry-phd-programs-guide.md      # 海外企业联培博士指南：CIFRE/MSCA/Industrial PhD、6国路径、12家目标企业
  student-profiles-research-method.md # 官网学生分享(Meet the Class)研究法：问题框架反推录取偏好、why program逻辑链、diversity贡献
  letsmigrate-eu-residence-routes.md  # LetsMigrate.org欧洲居留路线：蓝卡/数字游民/创业/投资93+项目、18国、中国材料准备(apostille)
  us-ms-engineering-fee-waivers-11-programs.md # 美国工科硕士免申请费11校：六种机制可靠性排序 + 协会会员资格陷阱 + 先定清单后找豁免 + 多申一所边际成本 + 跟踪表
  us-phd-fee-waiver-guide.md          # 美国PhD申请费fee waiver：四档学校机制、邮件模板、15申12中、申请季预算
  study-abroad-roi-and-internship-playbook.md  # 留学预算与回报率大表（10目的地/9专业组/五类画像）；海外实习全攻略（CPT/OPT/PGWP/485/IANG+PR路径）
  us-ai-masters-30-programs.md         # 全美Top50 AI硕士30项目：四类分型、首届项目风险、CMU MSAII/MSML差异
  ai-business-three-tiers.md           # AI生意三类分型：硬塞AI/chatbot补位/AI native、识别信号、去AI检验法
  sop-30min-prompt-workflow.md         # 半小时出可提交SOP：提示词模板、四步执行、去GPT味改写表
  niche-overseas-routes-10.md          # 10条冷门出国路径 + 逐条官方口径核查与人群匹配
  top30-us-1-1.5yr-programs-2027fall.md # Top30一年/一年半硕士292项目×2027 Fall截止日期总表（12月+1月占53%）、GRE三分格局、五种时长结构、置信度用法
  job-search-and-immigration-tools-stack.md # 求职五环节工具栈（LinkedIn Posts/Handshake/Glassdoor/JobWizard/Teal-Huntr/Levels.fyi）+ 移民检索五层工具 + 英国Earned Settlement官方核查
  niche-scholarships-12-channels.md # 冷门奖学金十二类（9类奖学金+3类低门槛渠道+介护兜底），按获取逻辑重排为四类，含提名制/叠加限制与逐条官方核查
  run-manual-europe-36-countries.md # RUN润手册导读：数据血缘与可靠边界 + 2025-26政策变化17条 + 中国护照排除5条 + 英国Earned Settlement档位表
  denmark-siri-2026-2027-updates.md # 丹麦SIRI 2026-2027：学签求职期3年→1年+家属关闭、集体协议工签DKK322,000含中国、雇主认证瓶颈
  product-sense-three-axes-and-missing-fourth.md # 产品sense三轴+缺失第四轴：基线（偏差方向才是判据）+ 舍弃判断学不到 + 前提清单 + 判断保鲜期分离
  ai-era-job-market-asymmetric-bets.md # AI时代求职不对称下注：竞争强度=价格镜像 + 缩HC三分类 + 岗位定价五问 + 回报分布五拆 + 签证过滤器正交
  ai-research-method-and-career-yao-shunyu.md # 大模型研究方法与职业选择：scaling ladder + 指标分工 + 不可量化工作靠人不靠 KPI + 生产方式 vs 判断力
  ai-era-scarcity-shift-and-positioning.md # AI 时代稀缺转移：benchmark 判据 + 衡量标准三档筛子 + 中间层五问 + 卖劳动力不卖软件 + Harness 四层
  life-path-arbitrage-lens.md # 人生路径套利透镜：七维映射 69 文件 + 选择权三问 + 资格六门 + 反事实强制 + 事实衰减纪律
  us-grad-program-difficulty-tiers-6-majors.md # 美研六专业难度分档（CS/EE/BA/DS/金融/MFE）：资格vs难度 + 跨表矩阵 + 名校洼地 + 缺失七维度
  us-college-due-diligence-7-sources.md # 选校尽调七源：CDS C7（仅本科）/ Scorecard 第4年口径 / Clery 四地理 / Niche / RMP + 信息五级模型 + 必补五源
  program-intel-community-search.md # 项目情报搜集：Rustle五平台扒风评/面经 + 搜索词构造 + 44篇之后的偏差处理 + 三层信息源分工
  eu-application-platform-routing.md # 欧洲申请平台路由：Studielink/uni-assist VPD/瑞典统招/EEF/Mon Master 走哪个 + 四种「截止日定义」+ 联盟校两列法
  silicon-valley-founder-storytelling.md # Lulu Cheng Meservey 叙事方法论全套（1–7节）：Go Direct / Narrative Arc / Underdog / 宁可被低估 / Message-Market Fit（主角位置·Schmidt 翻车·Shopify）/ 风险厌恶与独木舟 + 迁移到 SOP·套磁·面试
  hust-oeises-feiyue-2023-guide.md # HUST光电/工程科学飞跃手册2023：结构索引+七块方法论（转码/暑研/推荐信/面试/GPA套利）+去向表读法+五处过期修正
  eures-eu-job-mobility-portal.md # EURES欧盟官方招聘：31国岗位池 + 顾问/招聘会/落地指南三大用法 + B1四档门槛 + 语言选择杠杆差 + 中国护照打法
  data/top30-us-masters-1-1.5yr-2027fall.xlsx  # 原始数据表（排版/全 双工作表，292条项目记录）
  sop-meta-framework.md            # SOP 写作元框架：招生官三问（动机/计划/能力）+ 十拍写作骨架
  sop-8h-workflow.md               # 8小时文书初稿 7 步工作流（PS/CV/RL 三位一体 / BAR 模型 / 量化 / 推荐人沟通）
  sop-ps-regional-styles.md        # 区域 PS 风格：英国（学术）/ 香港（职业）/ 新加坡（混合）
  sop-ps-writing-principles.md     # 通用 PS 写作原则：真实感/细节/思想深度/5段式叙事
  sop-ai-era-writing-stance.md     # 26fall AI 文书立场：AI declaration / vibe coding / de-GPT 清单 / prompt 模板
  karpathy-llm-wiki-architecture.md # Karpathy LLM Wiki 架构：raw sources / wiki / schema + 4 条元洞察
  career-youngest-most-exhausted.md # 能力最强的年轻人为何最累：迭代速度 vs 社会公允速度的错位
  deepseek-mhc-hyperconnections.md # DeepSeek mHC：HC + Birkhoff 流形（双随机矩阵）约束解决梯度爆炸/消失
  career-wealth-freedom-philosophy.md # 财富自由哲学 7 条（精神自由 / 战略>战术 / 投资自己 / 多巴胺递减 / 中彩票难善终 / 黑客帝国脚本）
  hust-alumni-professor-network.md    # 华科校友教授网络（35+ 位美国/香港 CS 教授，套磁线索+面套目标，须核验）
  summer-research-practical-guide.md  # 暑研实操指南（三种找实验室路径/面套行程规划/暑研六优先事项/时间线）
examples/                    # fictional sample outputs (evidence map, school match, CV bullets)
```

## Commands

| Command | What it does |
| --- | --- |
| `/profile-intake` · `/build-evidence-map` | Collect background & build the reusable achievement library |
| `/school-match` | Reach/Target/Safety list from the CSV seed + official-page verification |
| `/gap-improve-plan` | 6–12 month background-building roadmap |
| `/cv-generate [fineng/cs/ece/mech/techtransfer/founder]` | Track-tailored CV (md or LaTeX) |
| `/sop-draft` · `/sop-review` | SOP drafting + admissions-officer scoring |
| `/lor-template` · `/prof-email-draft` | Recommendation outlines & professor cold emails |
| `/phd-advisor` | Advisor sourcing: 3-dimension match, current-student vetting, CS/AI red-list leads + applyphd.app (34K US records) + alumni network sourcing |
| `/phd-cold-email` | PhD cold-email & interview tactics: match>interest (paper+future work method), ability>passion (specific gap), proactive interview questions, follow-up cadence |
| `/hust-alumni` | 35+ HUST alumni professors at US/HK universities — warm-outreach leads for 套磁, 暑研面套, and referral networking; every entry must be re-verified |
| `/summer-research` | 暑研 full lifecycle: 3 paths to find a lab (official programme / self-套磁 / professor referral), 面套 logistics, 6 priorities during 暑研, ideal timeline |
| `/startup-coldstart` | Founder zero-budget cold-start: X/Reddit/LinkedIn cold outreach + subreddit→Discord funnel + UGC multi-channel |
| `/founder-antihedge` | Stanford GSB three anti-hedging principles: reject one-two-punch fallacy, no middle ground, tech ≠ win |
| `/founder-onchain` | On-chain payment infrastructure case (X/Meta/Visa/Standard Chartered) + three founder principles: user-assumption reset, settlement-as-scenario, compliance-as-product |
| `/founder-profile` | Founder personal profile building: identity-layer moat, authentic brand ≠ packaging, from single label to fully-rounded profile |
| `/fundraising-methodology` | Fundraising 5 cognitive corrections + 7-question pre-pitch self-audit; investor matching table, decision cost, rhythm, narrative explanation |
| `/returnee-market` | 2025 returnee employment snapshot: supply surge (1.51× since 2018), salary by sector (18k+ in new productive forces), city decentralisation; evaluate study-abroad ROI |
| `/ecm-interview` | MS HK ECM interview mentoring: Placement technicals (Primary/Secondary/Top-up/Block Trade), "Why Move" lateral hire narrative, Deal Experience storytelling framework |
| `/phd-cold-email` | PhD cold-email & interview tactics: match>interest (paper+future work method), ability>passion (specific gap), proactive interview questions, follow-up cadence |
| `/yale-m2m` | Yale M2M application review: candidate profile (social responsibility, critical thinking, AI optimism), ESG storyline, 1+1 alternative pathway |
| `/ai-flywheel` | AI investment flywheel: LLM stocks as token hedge, 8-stage positive feedback loop, wealth divergence, personal positioning |
| `/cognitive-revolution` | Sequoia's Cognitive Revolution: AI = industrial revolution rhyme, cognitive labor outsourcing, Jevons paradox, Engels' pause, speed risk |
| `/life-guide` | High cost-performance life guide: 552 evidence-based tips across 32 chapters (health, legal, career, finance, study abroad), online search link |
| `/jev-decision-model` | TypeSafe Jev decision model: parallel judgments, RLCD calibration, agent cost reduction, browser-use integration |
| `/incubator-guide` | Silicon Valley incubator guide + Startup Compass: non-YC incubators, residency matching for Chinese founders |
| `/capability-system` | Young people's "version answer": language + skill + AI + internet + globalization = capability system |
| `/sv-ai-observations` | Silicon Valley AI industry observations: China-US AI landscape, AI pharma directions, bubble risk, Google FDE, personal heroism vs efficiency |
| `/cold-email` | Cold email networking template: 4-part structure for 95% reply rate (source → purpose → strengths → next step) |
| `/deadline-timeline` · `/offer-compare` | Deadline tracker & offer decision matrix |
| `/visa-compare` | 2026 founder/post-study visa routes **with official source links** |
| `/founder-deck` | One-page venture brief + visa-evidence checklist + fundraising map |
| `/mindset` | Reframe credential/career anxiety — the "why" behind the skill （中文原文） |
| `/human-native` | Trust / taste / aesthetics / imagination / emotion as career moat against AI; Hassabis micro-structure argument |
| `/codex-hack` | Reverse-engineer semi-public US-stock blogger indicators with Codex: full ingestion → known/unknown split → bounded hypothesis search against published images |
| `/oak-state-transition` | Prof. Sutton's Oak framing: world as high-level state transitions; agents as temporally extended options rather than step-wise actions |
| `/yao-sutton` | Yao Qiqi vs Sutton: AI is structurally trapped inside the human symbolic system (mathematics/logic paradigm); only humans can potentially stand outside it. Three-layer career moat: L1 contents, L2 granularity, L3 symbolic trap |
| `/cv-review` | CV revision pass: skills-evidence backing, experience-hire weight, leadership/client balance |
| `/interview-prep` | Jargon-vs-plain-English calibration, presence for S&T/BD/founder pitches, story mechanics |
| `/leadership-stories` | Mine evidence map for leadership stories; place on the 5-tier influence ladder; upgrade to legacy/leverage narratives |
| `/grey-market` | 灰产认知对冲：灰产哥的非共识判断、钻空子思维、空子生命周期管理、索罗斯反身性、庙堂与江湖 |
| `/quant-weekly` | Quant行业周报：Jane Street算力军备、Systematic Flow影响、HFT基础设施扩张、大宗交易电子化、指数与市场分化 |
| `/sv-china-gap` | 硅谷与国内两周信息差：VC FOMO、泡沫共识、应用层vs模型层ROI、positioning startup、RSI、OAI机器人数据 |
| `/essmote` | Essmote AI 留学文书平台：PS/SOP/CV/推荐信生成 + 人工润色（essmote.com） |
| `/collaboration-postmortem` | 创业合作复盘：尽调缺失/先钱后干活/管理边界失守/止损信号/单向惩罚条款 |
| `/immigration-resources` | 移民/签证/海外工作开源资源合集：awesome-immigration/H1B数据/高技能求职/Five Flags/DiasporaAI |
| `/perm-suspension` | PERM暂停与科技行业留美影响：8家公司暂停、量化投行转型、加拿大香港替代 |
| `/return-vs-stay` | 回国or留美10条决策框架：储蓄速度/家庭/身份/性格/躺平/子女教育/人生目标 |
| `/ai-job-map` | 中国AI岗位地图：279家公司/12895+岗位、按城市区域分类（jobs.dinq.me） |
| `/industry-phd` | 海外企业联培博士指南：CIFRE/MSCA/Industrial PhD、6国路径、申请平台 |
| `/student-profiles` | 官网学生分享研究法（MIT MBAn Meet the Class）：问题框架反推录取偏好、why program逻辑链、diversity贡献、简历文书自检 |
| `/letsmigrate` | LetsMigrate.org欧洲居留路线：蓝卡/数字游民/创业/投资5类路线93+项目、18国对比、中国签证材料准备清单 |
| `/fee-ms` | 美国工科硕士免申请费 11 校：六机制可靠性排序（全免>代码>早鸟>会员>宣讲会>审批）+ 协会资格陷阱 + 先定清单后找豁免 + 申请季组合思维 |
| `/fee-waiver` | 美国PhD申请费减免：四档学校机制、waiver邮件模板、15申12中命中率、申请季费用预算 |
| `/study-roi` | 留学预算与回报率大表 + 海外实习全攻略：ROI四逻辑、10目的地/9专业组回本表、五类预算画像、工签与PR路径、秋招时间线 |
| `/ai-masters` | 全美AI硕士30项目清单：四类分型、独立AI学位vs CS-AI方向、首届项目风险、同校不同学院门槛 |
| `/ai-business` | AI生意三类分型：硬塞AI vs chatbot补位 vs AI native、识别信号、第二类天花板、第三类机会与陷阱 |
| `/sop-prompt` | 半小时出可提交SOP：提示词模板、四步执行顺序、去GPT味改写表、迁移文书避坑 |
| `/niche-routes` | 10条冷门出国路径 + 官方核查：RCIP、芬兰PR新规、冰岛18个月、瑞典科研签3年 |
| `/eures` | EURES 欧盟官方招聘：31 国岗位池 + 顾问用法 + B1 真实门槛 + 中国护照打法 |
| `/run-manual` | RUN 润手册导读：数据血缘/可靠边界 + 政策变化 17 条 + 中国护照排除清单 + 英国 Earned Settlement 档位表 |
| `/scholarships` | 冷门奖学金十二类：四类获取逻辑（劳动/身份/专业/稀缺性）+ 提名制与叠加限制 + 官方核查表 + 奖学金日历 |
| `/denmark-siri` | 丹麦 2026–2027：学签出口砍短（3年→1年、家属随行关闭、PhD豁免）+ 集体协议工签开门（DKK 322,000、16国含中国、需认证雇主）+ 三条策略含义 |
| `/product-sense` | 产品sense三轴与第四轴：基线（偏差方向）+ 舍弃判断（幸存者只有加法）+ 竞品三失效→前提清单 + 判断保鲜期分离 + AI 重心移到「值不值得做」 |
| `/job-bet` | AI时代求职不对称下注：竞争强度是价格的镜像不是价值的镜像 + 缩HC三分类（结构/效率/周期）+ 岗位定价五问 + 回报分布五拆 + 顺风18个月 + 签证过滤器 |
| `/ai-research` | 大模型研究方法与职业选择：scaling ladder 区分机制/规模 + 指标分工 + Taste=独立基线预期 + 生产方式 vs 判断力 + 会弹琴≠想当琴手 + 简历三证据 |
| `/ai-era` | AI 时代稀缺转移与个人定位：benchmark 判据（能否写成有标准答案的题）+ 衡量标准三档筛子 + 中间层五问自查 + 卖劳动力不卖软件（10 步挑 2 步）+ Harness 四层（判断/调度/验证/设计）|
| `/arb` | 人生路径套利透镜：七维候选发现 → 资格六门过滤（INFEASIBLE 不参与排序）→ 反事实表（主方案 + ≥3 替代 + 什么都不做 + 证据 A/B/C）→ 选择权三问 → 一个一周内可完成的下一步 |
| `/tiers` | 美研六专业难度分档：CS / EE / 商业分析 / 数据科学 / 金融 / 金工金数五档表，含「先读注意栏」读法、资格 vs 难度区分、学校×专业跨表矩阵、名校洼地三查、四个结构性缺陷与缺失七维度 |
| `/school-dd` | 选校尽调七源：Common Data Set C7 + College Scorecard + Clery ASR + 官网四角 + Niche + Reddit + Rate My Professors + RateMyDorm，含口径修正、信息五级模型、必补五源、时间盒流程与五红旗 |
| `/program-intel` | 项目情报搜集：Rustle（X/TikTok/Reddit/小红书/抖音）扒风评与面经 + 搜索词构造表 + 社区情报偏差处理 + 官方/社区/一手三层分工 |
| `/eu-platforms` | 欧洲申请平台路由：Studielink / uni-assist VPD / 瑞典统招 / EEF / Mon Master 分别什么时候用 + 四个国家对「截止日」的四种定义 + 联盟校两列法 |
| `/storytelling` | Lulu Cheng Meservey 叙事方法论全套：Go Direct + Narrative Arc + Underdog 五段式 + 宁可被低估 + prebuttal/压强/同心圆/文化敏感区 + Message-Market Fit（技术当背景·人当主角）+ 风险厌恶与独木舟（卖不改变的代价）+ 迁移到申请与求职 + 失效边界 |
| `/feiyue-oei` | HUST 光电/工程科学飞跃手册 2023：结构索引 + 七块方法论（转码路径/暑研三路径/推荐信黑推风险/三类面试/GPA 套利）+ 8 届去向表读法 + 五处已过期修正 |
| `/tool-stack` | 求职五环节工具栈 + 移民检索五层工具（广度/筛选/横比/时效/解读）+ 英国 Earned Settlement 核查 |
| `/top30-short-programs` | Top30 一年/一年半硕士 292 项目 × 2027 Fall 截止日期：按 12/01、12/15、1月、2月+ 聚类排组合，含 GRE 与时长结构判断 |

## Founder track at a glance
Hard-tech fundraising paths built in: **YC / Silicon Valley / California / Middle East sovereign capital
(Hub71, Mubadala, PIF/Sanabil, KAUST/MBZUAI)** overseas; **红杉中国 HongShan / 中科创星 / 深创投 / 高瓴 / CPE**
in China. Visa snapshot (Aug 2026): US no startup visa (IER parole rarely used → O-1A/EB-1A/NIW in practice;
E-2 unavailable to Chinese nationals); UK Innovator Founder (endorsement, 3yr→ILR); Singapore EntrePass;
France French Tech Visa; Canada SUV paused. Full thresholds & sources: `references/visa-policy-links.md`.

## Ethics
No fabrication of any kind; user owns final edits; personal materials stay private (`.gitignore`);
no copy-paste from sample essays; lawyer for all legal/visa filings.

## License
MIT (derivative/composite work). Referenced repos: taught-master-applications-skill, SOP_Consultant,
resume-assistant-skill, Horizon-Stopify, grad-agent, phd-master-application-docs,
chatgpt-prompts-for-academic-writing.
