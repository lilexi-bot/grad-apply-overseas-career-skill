# Oak Architecture / Prof. Sutton — high-level state transition over low-level physics

> Field philosophical note on RL framing (Chinese original verbatim at the bottom). Load when: the
> user is thinking about the right granularity of description for the world, agent design, or how
> to reason about learning systems — and pushing back against the "everything is LLM" orthodoxy.
> Core claim: in Prof. Sutton's Oak architecture framing, the optimal description of the world is
> **high-level state transitions**, not low-level physics. Very Markovian. For agents: **take
> temporally extended options, not solely step-wise actions**. (Oak, Sutton, 高层状态转移, 马尔可夫,
> 时间延展选项, LLM 之外, learning from experience, 学习颗粒度)。

## The argument
1. In the Oak-architecture framing, Prof. Richard Sutton holds that the optimal granularity for
   describing the world is **high-level state transition**, not low-level physics.
2. This is deeply Markovian — Sutton *is* the "father of RL," and the observation is consistent with
   the whole RL lineage: the agent doesn't need (and is worse off with) every micro-physical
   observation; it needs a compressed state representation that is sufficient to predict the next
   *relevant* state.
3. For agents, this translates into: **take temporally extended options** rather than solely
   step-wise actions. An "option" is a macro-action with its own termination condition; choosing at
   the option level is what makes learning tractable in high-dimensional worlds.
4. **The meta-observation:** in an era where LLMs have brainwashed everyone, listening to someone
   spend an hour on "learning from experience" and barely mention LLMs at all is itself a profound
   *learning experience*.

## Why this matters beyond RL
- The Oak framing is a stance on **abstraction level**: the right description of a complex system is
  not the lowest-level one, but the one that makes state transitions *predictable at the level you
  actually care about*.
- Transferable to:
  - **Career framing** — the right description of a career is not a list of every job / task /
    credential (low-level physics), but the high-level state transitions: which "modes" did I move
    between, and what triggered each transition.
  - **Founder narrative** (`founder-anti-hedging-principles.md`) — the right description of a
    company is not its day-to-day decisions but the high-level strategic transitions: when did we
    commit to a market, when did we pivot, when did we double down.
  - **LLM-era learning** — the LLM training loop operates on next-token prediction (step-wise);
    Sutton is pointing at a different axis — learning *policies over options*, not policies over
    tokens.

## The "learning experience" meta-pattern
When someone who has spent 30 years building RL talks about learning from experience and *does not*
frame the whole thing through LLMs, that silence is data. It is not that LLMs are wrong; it is
that the framing "learning = next-token prediction" is a *special case* of a much larger design
space. Anyone working in AI (or in a field being reshaped by AI) should sit with that silence.

## Cross-reference
- `career-what-ai-cannot-encode.md` — trust, taste, aesthetics, imagination are non-tokenisable
  *because* they live at the level of high-level state transition, not micro-physical
  pixel/token sequence. Sutton's framing explains *why* the human-native moat exists.
- `career-mindset-adaptability.md` — "the meta-skill is responding to world change" — that is an
  option-level policy, not a step-wise reaction.

---

## 中文原稿（verbatim）

至少在OaK架构的语境里，在prof sutton眼里，对世界的更优的描述颗粒度不是low level physics而是high level state transition，非常马尔可夫（看来他是真的rl之父[笑哭R][笑哭R]），放在agent身上即take temporally extended options rather than solely step-wise actions 在llm洗脑所有人的时代听一个人讲了整整1小时的learning from experience并对llm几乎只字未提，这本身也是个很神奇的learning experience
