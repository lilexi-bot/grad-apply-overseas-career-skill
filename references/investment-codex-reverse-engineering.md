# Codex Reverse-Engineering of Semi-Public Investment Indicators / Strategies

> Methodology note (Chinese original verbatim at the bottom). Load when: the user wants to use an
> LLM coding agent (Codex / Claude / GPT-Codex) to reverse-engineer the proprietary indicators or
> strategies shared by US-stock finance YouTubers/bloggers — i.e. cases where the creator reveals
> *part* of the logic but keeps the full picture hidden.
> Pairs with the human-native career moat note (`career-what-ai-cannot-encode.md`): the "public
> secret" in discretionary trading circles is exactly the kind of non-tokenised domain knowledge that
> is hard to extract without this methodology （Codex 破解指标， 美股博主， 半公开策略， 假设空间限定，
> 图像吻合验证， 公开的秘密）。

## The three-step methodology
**Goal:** extract a blogger's hidden indicator logic using a coding agent (Codex), given that the
blogger has revealed partial signals (screenshots of indicator images, vague descriptions, domain
hints) but not the full formula.

### Step 1 — Full ingestion of the source material
- Have the coding agent consume the video / content end-to-end (transcript + screenshots + every
  caption/overlay).
- Do NOT skip "intro" segments — bloggers often leak the most honest signals in offhand remarks.

### Step 2 — Separate *known-and-certain* from *unknown*
- Have the agent compile two lists:
  - **Known & certain:** explicitly stated logic, visible formulas, confirmed parameter ranges.
  - **Unknown but hinted:** things the blogger disclosed but did not fully reveal.
- **Hard rule:** the agent is *not allowed* to fill gaps with its own speculation. No "I assume the
  rest looks like X because it usually does."
- **Hard rule:** the agent is *not allowed* to copy indicator images from the video as the basis for
  constructing indicator visuals. No pixel-level reconstruction.

### Step 3 — Constrained hypothesis search in the "public secret" space
- Define a **bounded hypothesis space** from hints the blogger dropped. The hint typically points to
  a "public secret" — discretionary trading circles openly know the trick, but retail traders do not.
- Let the agent generate candidate indicator formulas within that bounded space, then **test each
  against the blogger's published images**.
- **Success criterion:** a candidate that produces an output image *visually identical* to the
  blogger's screenshot is a strong signal that the underlying logic has been recovered.
- Caveats: (a) visual match ≠ ground truth — backtest the recovered indicator on out-of-sample data
  before using it; (b) "public secret" is a finite set but the search space of parameter combinations
  is not — prune aggressively using the blogger's hints.

## Why this methodology matters
- It is a concrete example of *how to extract non-tokenised domain knowledge* using LLM agents:
  force the agent to stay within a hypothesis space bounded by human knowledge, and verify against a
  human-observable output (the image).
- It inverts the usual LLM failure mode (hallucination into the unknown) by making the agent *stop
  guessing* and instead *search a bounded space* + *verify against external signal*.
- Transferable beyond trading: any "semi-public craft knowledge" (hedge-fund playbook, VC pattern
  matching, macro regime identification) can be reverse-engineered with this three-step loop.

## Cross-reference
- `founder-coldstart-playbook.md` — "deep research before posting" is the *creator* counterpart to
  this methodology (the *consumer* counterpart).
- `career-what-ai-cannot-encode.md` — the "public secret" in trading is the kind of
  non-tokenisable, human-native judgment that AI cannot discover on its own; it must be *seeded* by
  human disclosure and then *bounded* by human constraint.

---

## 中文原稿（verbatim）

用codex破解美股博主半公开的指标和策略 1. 让codex把视频扒下来，完整看完全部内容 2. 让codex整理好已知的、确信的逻辑，不允许它靠自己的猜想补全指标逻辑的全貌，也不允许copy视频中的图像表征来制作指标图像 3. 根据博主透露了但没完全透露的信息，给codex限定一个提出假设的范围，然后让codex基于公开的秘密（一般是主观交易圈内公开的秘密，但散户一般unaware的方法）提出假设，然后验证这些假设，看看有没有结果跟博主视频中的图像完全吻合的，如果有那应该就是成功hack出来了
