# Grad Apply & Overseas Career — Master Skill

**留学申请 + 海外工作 + 创业路径 一体化 AI Skill** · v2.0 · MIT

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
  sop-outline-template.md
  founder-pack-template.md   #   venture brief + visa-evidence checklist
  lor-cold-email-template.md
  deadline-offer-templates.md
references/                  # external data loaded on demand
  school-programs.csv        #   45-programme seed DB (verify on official URLs!)
  visa-policy-links.md       #   official immigration source links (UK/US/CA/SG/FR/…)
  founder-fundraising-ecosystem.md  # YC/US/Middle East/China hard-tech investors + accelerators
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
| `/deadline-timeline` · `/offer-compare` | Deadline tracker & offer decision matrix |
| `/visa-compare` | 2026 founder/post-study visa routes **with official source links** |
| `/founder-deck` | One-page venture brief + visa-evidence checklist + fundraising map |

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
