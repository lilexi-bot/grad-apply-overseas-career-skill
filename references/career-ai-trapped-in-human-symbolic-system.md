# AI Is Trapped in the Human Symbolic System — Yao Qiqi vs. Sutton exchange

> Field philosophical note (Chinese original verbatim at the bottom). Load when: the user is thinking
> about the *deepest* boundary of AI vs. human intelligence — not "what can AI do that humans cannot"
> or the reverse, but *whether AI is structurally trapped inside the symbolic system humans invented*.
> Pairs with the human-native career moat note (trust/taste/aesthetics/imagination/emotion) and the
> Oak framing (high-level state transition vs. low-level physics); this note is the *deeper* layer —
> the symbolic system that defines the boundary itself.
> Core claim: AI is built on the human symbolic system (mathematics, logic, proof), and therefore
> cannot *subvert* that system — only humans themselves potentially can.
> （姚期智， Richard Sutton， 符号系统， 数学范式， AI局限， 人类智慧局限， 自洽封闭系统， 不失真建模）。

## The exchange
- **Setting:** Prof. Andrew Yao (Turing Award 2000) and Prof. Richard Sutton (RL founding figure) in
  conversation.
- **Meta-observation first:** Prof. Yao, at an advanced age, gave a talk *without just reading the
  slides*. (This is itself data — the gap between what is written and what is spoken-from-deep-
  understanding is exactly where the human-native moat lives.)
- **Sutton's question:** "Is AI limited in any way that human is not limited?"
- **Yao's answer (after a deep pause):**
  > Our mathematical world is built on a symbolic system *we* invented. But this physical universe
  > may have other ways of extracting information [than ours].
- The user's paraphrase of what was said (some specifics forgotten): the universe may admit
  modelling / information-extraction methods that are *less lossy* than the mathematical framework
  humans built.

## The reconstructed argument
1. Human research into the world is *entirely* built on mathematics: modelling the world
   mathematically, with mathematics itself being a logic (deduction + proof) system built on a
   *self-invented* symbolic system.
2. This is a **self-consistent closed system**. It works internally. But it is *very possibly not an
   unbiased modelling of the universe's actual laws*.
3. There may exist **less-lossy ways** to model or extract information from the universe — ways that
   do not pass through the human-invented symbolic bottleneck.
4. AI's intelligence is **built on the human symbolic system and logic paradigm**. Even the most
   capable AI today is trained on data expressed in our symbolic system, reasoning within our logic.
5. Therefore **AI cannot subvert the human mathematical paradigm**. Not in the sense of "AI cannot
   prove a conjecture humans haven't" — but in the deeper sense that AI cannot step *outside* the
   symbolic system to see whether there is a fundamentally different one.
6. **Only humans themselves potentially can** — precisely because humans are not bound by the same
   structural constraint (they invented the system; they can in principle stand outside it).

## The deeper frame — three layers of "what AI cannot do"
Reading the three career notes in sequence gives a clean three-layer stack:

| Layer | File | Boundary description |
|---|---|---|
| L1 — What AI cannot (yet) encode | `career-what-ai-cannot-encode.md` | Trust, taste, aesthetics, imagination, emotion — *contents* of human experience not yet tokenisable |
| L2 — Right granularity of description | `career-oak-high-level-state-transition.md` | The right description of the world is high-level state transition, not micro-physics — AI trained on tokens sees only low-level |
| L3 — Symbolic system trap | *this file* | AI is built on the *human symbolic system*; it cannot step outside to discover fundamentally different modelling frameworks |

- **L1** is empirical / contingent (what we can't encode *yet*).
- **L2** is architectural (what kind of policy the agent should learn).
- **L3** is structural / civilizational (whether AI can ever invent a *new* symbolic framework).

## Career implication
- The moat is not just "what AI cannot compute yet" — it is also "whether AI can ever escape the
  symbolic framework humans invented."
- For anyone building a career in a field AI touches: the most durable edge is in asking questions
  that *live outside the current symbolic system*. Not "how do I make this model faster?" but
  "is there a fundamentally different way to frame this problem that does not pass through our
  current math?"
- That kind of framing-question is the highest-order human-native trait. It is not a skill you learn;
  it is a stance toward the world.

## The meta-observation
Both speakers in this exchange embody the very thing being discussed:
- Sutton has spent 30 years on "learning from experience" and barely mentions LLMs — he operates at
  a level of abstraction where the dominant discourse is not the point.
- Yao gives a talk without reading slides — his knowledge lives at a level where the *written* form
  is not the point.
- The content of their conversation (the symbolic system argument) is about the boundary of the
  symbolic system. The *form* of the conversation is itself a demonstration of that boundary.

## Cross-reference
- `career-what-ai-cannot-encode.md` — L1: contents AI cannot yet encode.
- `career-oak-high-level-state-transition.md` — L2: right granularity of description.
- `founder-anti-hedging-principles.md` — the conviction to stand on a non-mainstream framing is the
  same kind of stance as standing outside the dominant symbolic system.

---

## 中文原稿（verbatim）

姚期智回答强化学习之父Richard Sutton 姚期智教授一把年纪了对外讲课竟然没有纯念ppt[抱拳R][抱拳R][抱拳R] Richard Sutton的提问： Is AI limited in any way that human is not limited? AI是否存在人类（智慧）没有的局限？ prof姚貌似先深度思考了一会儿[笑哭R]，然后说： 我和你之前有聊到过，我们人类的数学世界建立在我们自己发明的符号系统上，但这个物理宇宙可能有其他的信息提取方式 （大致是这么说的，前面忘了后面也忘了） 主包的解读：人类对世界的研究完全建立在数学上，即用数学建模世界，但这个数学是人类基于自己发明的符号系统建立起来的逻辑（推演与证明）体系，which is a自洽的封闭系统，但它很有可能不是对宇宙规律的无偏建模，这个宇宙可能有更不失真的建模方式/信息提取方式 AI的智慧建立在人类建立的符号系统和逻辑范式上，简单来说就是AI不能颠覆人类的数学体系（但不是指不能证明人类没能证明的猜想等），但或许人类自己可以(?)
