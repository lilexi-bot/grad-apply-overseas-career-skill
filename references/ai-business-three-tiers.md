# 做 AI 生意的 3 个思路：三类 AI 业务的分层判断

> **When to load:** 用户判断某个 AI 产品/赛道值不值得做、评估大厂 AI 业务真假、找 AI 创业切入点、被问"AI 能做什么生意"、或需要给 AI 项目做定位时。
> **Trigger:** AI生意, AI业务分类, AI创业方向, AI native, 硬塞AI, chatbot套壳, AI产品定位, 大厂all in ai, 负一屏, 行业AI, AI赛道判断, 技术革命周期, killer app
> **Source:** 用户分享《做AI生意的3个思路》（2026-11-03）
> **Keywords:** AI business taxonomy, AI-native, chatbot wrapper, industry AI, LLM applications, startup positioning, killer app, technology cycle

---

## 中文原文

太长不读，市面上的 AI 业务可被分为三类：

1. **互联网时代已经被解决得差不多的需求，硬塞 AI**
2. **互联网时代没被很好地解决的需求，接个 chatbot**
3. **AI 时代独有的需求，真正的 AI native 生意**

几个例子：

**1** 是现在互联网大厂所谓 all in ai 的重灾区，例如钉钉 one、支付宝 AI，大家早已用惯，user journey 已稳定收敛，这时加个负一屏搞一些没啥体验增量、甚至增加使用摩擦的 AI 功能，像是全组被裁前的最后挣扎。

**2** 是现在互联网大厂／当下 startup 做得还不错的业务，例如小红书点点 ai、视频内容审核模型、🦘ai 客服、openevidence 的 healthcare ai、harvey 的法律 ai 等等，互联网时代就已经很有需求，但当时没有大模型所以解决得并不好。

**3** 是创业机会最多的方向，也是互联网大厂最有可能掉队的方向，例如 claude code/codex（即时大规模 coding）、typeless（理解意图的语音输入）、非专业的内容创作平台（冕神教）、模型 api 分发等等。

从技术革命宏观周期的角度看，这个大方向也才刚刚开始，或许未来我们将看到 ai native 场景与需求的井喷、对应解决方案的大量出现而后消亡、killer app 的收敛（刻舟求剑移动互联网[扯脸H]）。

---

## 三类业务的判断标准（本仓库归纳）

原文给了分类和例子，落到实操还要一个可用的判断口径。三类业务的差别本质上是**"需求是否已存在 + 旧方案是否真的差 + AI 是否是唯一解法"**：

| | 第一类 | 第二类 | 第三类 |
|---|---|---|---|
| 需求是否存在 | 已存在且已被满足 | 已存在但解决得差 | 不存在，AI 创造了它 |
| 旧方案状态 | user journey 已收敛 | 有人工/规则方案，但成本高或质量差 | 无方案（做不了） |
| AI 的作用 | 附加功能 | 替代人工/提升质量 | 使新行为成为可能 |
| 体验增量 | ≈0，甚至为负（摩擦） | 明显（更快/更便宜/更准） | 全新（以前根本没这个行为） |
| 商业结果 | 组织动作，不是业务 | 现金流稳，天花板在行业规模 | 天花板未知，可能收敛成 killer app |
| 谁在做得好 | 几乎没人 | 大厂 + 垂类 startup | 新公司，大厂反而掉队 |

### 第一类的识别信号：出现这些特征基本就是"硬塞"

- 需求本来已经稳定，AI 功能被放在**入口层**（负一屏、侧边栏、悬浮球）而不是任务流内
- 加了 AI 之后**操作步数变多**，用户需要先跟 AI 对话才能回到原来的路径
- 功能指标好看但**留存不动**——因为原用户根本不需要它
- 项目由**组织动作**驱动（"全员 all in AI"、季度 OKR），而不是由用户问题驱动
- 典型话术："我们给 XX 也接上了大模型"

> 原文的判断很狠："像是全组被裁前的最后挣扎"。这句话的可用版本是：**如果一个 AI 功能的成功标准是"上线了"，而不是"用户改变了行为"，它就不是生意。**

### 第二类的价值与天花板

第二类是当下最扎实的一类——**需求在互联网时代就存在，只是当时没有大模型所以解决得差**。这也解释了为什么 Harvey（法律）、OpenEvidence（医疗）这类垂类能跑出来：不是发明了新需求，是把一个贵、慢、依赖专家的旧流程做便宜了。

- 优势：需求已验证，付费意愿存在，销售路径清晰（卖给企业/机构）
- 天花板：受行业规模和渗透率限制，很难出现平台级爆发
- 护城河关键：**数据与流程嵌入深度**，而不是模型能力——模型是公共的，流程不是
- 风险：大厂一旦把同一垂类做成免费插件，垂类公司会被压价

### 第三类的机会与陷阱

第三类是创业机会最多、也是大厂最容易掉队的方向。原因很简单：**大厂的组织结构是为"已有业务的效率优化"设计的，不是为"创造新行为"设计的。**

例子里的共同特征：它们都在**放大人的单位产能**，而不是替人做已有的事——

- claude code / codex：即时大规模 coding（把"写代码"这件事的规模上限改掉了）
- typeless：理解意图的语音输入（把"输入"从键盘操作变成意图表达）
- 非专业的内容创作平台：让原本不做内容的人开始生产内容
- 模型 API 分发：新的基础设施层

但第三类也最容易死。原文那句"解决方案的大量出现而后消亡、killer app 的收敛"是重点：**在技术周期早期，涌现的数量远大于最终存活的数量**。判断自己是不是那个能活下来的，看的不是"需求新不新"，而是"用户行为是否真的改变了并且留下来了"。

---

## 三条可迁移的推论（本仓库补充）

1. **用"移动互联网刻舟求剑"做反向检查。** 原文结尾提到这个比喻。具体用法：把你要做的 AI 产品，假设成"没有 AI 的版本"，如果它作为普通互联网产品也能成立，那它就是第二类（不错）；如果它作为普通产品根本不成立，那它才是第三类（真 AI native）；如果它作为普通产品早就有更好方案，那它就是第一类（硬塞）。
2. **第三类不要用第一类的成功标准去衡量。** 第一类看上线，第二类看收入，第三类只能看**行为改变率**——用户在 AI 消失后会不会明显不适应。
3. **大厂掉队不是能力问题，是结构问题。** 看到"大厂也在做 XX 方向"不必紧张；要紧张的是它把 XX 做成了入口功能而不是独立产品。

---

## English Key Takeaways

1. **Three tiers of AI business:** (1) needs the internet already solved well, with AI bolted on; (2) needs the internet couldn't solve well, now served by an LLM; (3) needs that only exist because of AI — genuine AI-native businesses.
2. **Tier 1 is the graveyard of "all-in-AI":** DingTalk One, Alipay AI — stable user journeys with a negative-one-screen AI layer that adds friction, not value. Organizational motion, not business.
3. **Tier 2 is where real cash flow is today:** Xiaohongshu's AI, content moderation models, AI customer service, OpenEvidence (healthcare), Harvey (legal) — the demand predates LLMs; the LLM just made an expensive, slow, expert-dependent workflow cheap. Moat = data and process embedding, not model capability.
4. **Tier 3 holds most startup opportunity and the biggest big-company blind spot:** Claude Code/Codex (instant large-scale coding), Typeless (intent-level voice input), non-professional content platforms, model API distribution. They expand per-person throughput rather than doing existing work for you.
5. **Test for tier 3:** strip the AI away — if the product still works as an ordinary internet product, it's tier 2; if it cannot exist at all without AI, it's genuinely tier 3; if an ordinary product already does it better, it's tier 1.
6. **Judge tier 3 by behaviour change, not revenue:** would users feel the loss if the AI disappeared tomorrow?
7. **Big companies fall behind structurally, not technically** — their org design optimises existing business, not the creation of new behaviour.
8. **Early-cycle math:** many solutions appear, most die, a killer app converges. Volume of emergence ≫ volume of survival — "mobile internet thinking applied to AI" is the classic failure mode.

---

## Connection to Repo Themes

- **`founder-collaboration-postmortem.md`** (`/collaboration-postmortem`) — tier-3 ventures are exactly where "先查后签、先钱后干、节奏可控" matters most, because there is no validated demand to fall back on.
- **`founder-antihedge.md`** — the tier taxonomy is a positioning hedge: knowing which tier you're in tells you what the honest pitch is and which investors will believe it.
- **`startup-coldstart-playbook.md`** — tier-2 businesses can cold-start by selling to an existing budget line; tier-3 must create the behaviour first, so the cold-start sequence differs.
- **`founder-deck-outline.md`** — tier matters for the deck: tier-2 decks lead with market size and unit economics; tier-3 decks lead with the behaviour change and evidence of retention.
- **`sv-china-info-gap-fomo-bubble.md`** (`/sv-china-gap`) — the "Neo Lab FOMO / application-layer vs model-layer ROI" observations are the same question asked from the capital side.
- **`ai-job-map.md`** (`/ai-job-map`) — job mapping by company type tracks the same tiers: tier-1 AI teams are cost centres, tier-2 are revenue teams, tier-3 are product teams.
- **`grey-market-cognition-hedge.md`** (`/grey-market`) — the "庙堂与江湖" lens: tier-1 failures happen where the org is insulated from real user pain.
- **`us-ai-masters-30-programs.md`** (`/ai-masters`) — students choosing AI programmes should know which tier their target employers sit in; tier-1 teams are where new grads get hired into work that later gets cut.
