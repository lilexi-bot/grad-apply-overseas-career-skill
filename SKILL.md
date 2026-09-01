---
name: grad-apply-overseas-career
description: >-
  End-to-end graduate application & overseas career super skill. Covers master's/PhD applications across
  Financial Engineering / quant finance, ECE, mechanical & robotics, CS/AI/agents, data science,
  interdisciplinary engineering, technology transfer, and entrepreneurship/founder tracks; plus overseas
  internship/job search and founder-visa & fundraising strategy. Provides profile intake, evidence map,
  school matching (Reach/Target/Safety) with a built-in programme CSV seed, gap-improvement roadmaps,
  track-tailored CV/SOP drafting with admissions-officer review, LOR and cold-email templates, deadline
  tracking, offer comparison, and a hard-tech founder playbook (YC/US/UK/SG/France/Middle East/China
  fundraising + visa route comparison). Use when the user says (EN or 中文): 留学申请, 研究生申请, 海外读研,
  硕士/博士申请, 选校, 文书, SOP, PS, personal statement, CV, 简历, 推荐信, LOR, 套磁, cold email professor,
  海外实习, 海外工作, 海外求职, 找实习, 创业签证, founder visa, 移民签证路径, startup visa, 选offer,
  DIY申请, gap plan, career-anxiety or mindset talks (职业焦虑, 卷学历, 简历被挂, 职业迷茫,
  应对变化, 上岸, 财富自由, 怀疑努力的意义), or asks to compare universities/programmes/visas/scholarships abroad.
license: MIT
version: 2.1.0
last_updated: 2026-09-01
---

# Grad Apply & Overseas Career — Master Skill (v2.1)

## 0. Loading protocol (progressive disclosure — follow strictly)
This file is the **router** and stays loaded. Do NOT load every asset at once. Load a template/reference
only when the workflow step requires it, then work from it:

| When the task needs… | Load this file |
| --- | --- |
| Collecting achievements / building asset library | `templates/evidence-map-template.md` |
| School matching & programme comparison | `references/school-programs.csv` (seed) + `templates/school-comparison-template.md` |
| Gap diagnosis / background enhancement | this file §2 Step 4 (logic stays here) |
| CV drafting (Markdown) | `templates/cv-template.md` |
| CV drafting (LaTeX) | `templates/cv-template.tex` |
| SOP / personal statement | `templates/sop-outline-template.md` |
| LOR outline / professor cold email | `templates/lor-cold-email-template.md` |
| Founder venture brief / visa evidence | `templates/founder-pack-template.md` |
| Visa policy thresholds & official links | `references/visa-policy-links.md` |
| Founder fundraising ecosystem / investor lists | `references/founder-fundraising-ecosystem.md` |
| Deadline tracker / offer comparison | `templates/deadline-offer-templates.md` |
| Expected output quality examples | `examples/` (evidence map, school match, CV bullets) |
| Career anxiety / "why am I doing this" / re-start decisions | `references/career-mindset-adaptability.md` |

## 1. Non-negotiable constraints
1. Never fabricate experience, results, awards, internships, stories, funding or traction. All content comes from the user's real materials (use the Evidence Map as the single source).
2. The user keeps final editing rights; AI structures, reviews, polishes — never overwrite the user's original sentences without permission.
3. Save every deliverable as a local versioned Markdown file (evidence map, CV/SOP drafts, tables), not only in chat.
4. Multi-track parallel applications are supported (8 tracks): Financial Engineering/Quant; ECE/Telecom; Mechanical/Robotics/Mechatronics; CS/AI/Agent/Embodied/LM engineering; Data Science & Applied Statistics; Interdisciplinary Engineering (BME+AI+Finance / Art-Tech); Technology Transfer / Tech-Innovation Management; **Entrepreneurship / Founder**.
5. Programme evaluation always covers: tuition, visa & immigration policy, post-graduation work permission, career path, alumni network, long-term global mobility — plus founder extras (student IP policy, accelerators, founder-visa bridge) for founder track.

## 2. End-to-end workflow
1. **Profile intake** — collect GPA/rank, tests, coursework, experience inventory (research/hackathon/OSS/internship/startup/awards), budget, countries, career goal, risk appetite. → save into `templates/evidence-map-template.md`.
2. **Build Evidence Map** — one entry per achievement: timeline, tech stack/methodology, quantified results (baseline→result), reflection/programme linkage, artifacts. Permanent reusable asset.
3. **School matching** — bucket Reach/Target/Safety. ALWAYS start from `references/school-programs.csv` (45-programme seed), then VERIFY every tuition/deadline/curriculum fact on the programme's official URL before outputting; fill `templates/school-comparison-template.md` (include check date + source URL per row).
4. **Gap diagnosis & roadmap** — time-phased 6–12 month plan: FinEng→quant mini-projects/backtests/case comps; ECE/ME/Robotics→embodied-AI OSS, Isaac Sim projects; Founder→incorporate, ship MVP, apply to named accelerators, document traction, file IP — map each milestone to visa-route evidence thresholds (see §4).
5. **CV generation** — 1–2 page master CV + track variants from `templates/cv-template.md` (or `.tex`): fineng / cs / ds / ece / mech / techtransfer / founder. Every bullet quantified. Commands: `/cv-condense`, `/cv-quantify-result`, `/cv-rephrase-for-tech-transfer`, `/cv-rephrase-for-founder`.
6. **SOP drafting & review** — outline via `templates/sop-outline-template.md`; cycles: first draft from evidence → user self-edit → admissions-officer review (flag clichés, weak logic, programme mismatch; score report) → targeted revision. Track reorientation: `/sop-reorient-fin-eng`, `/sop-reorient-tech-transfer`, `/sop-reorient-founder`.
7. **Supplementary materials** — diversity statement, LOR outlines & cold emails (`templates/lor-cold-email-template.md`); founder addendum (`templates/founder-pack-template.md`).
8. **Calendar & offers** — deadline checklist + offer comparison matrix (`templates/deadline-offer-templates.md`); founder-track decisions weight settlement speed, capital density, accelerators, tax/IP, student→founder bridging.

## 3. Command routing
| Command | Action → load |
| --- | --- |
| `/profile-intake` | Step 1 interview → create evidence-map file from `templates/evidence-map-template.md` |
| `/build-evidence-map` | Fill evidence map; consult `examples/example-evidence-map.md` for depth |
| `/school-match` | Read `references/school-programs.csv` → verify official pages → `templates/school-comparison-template.md`; example: `examples/example-school-match.md` |
| `/gap-improve-plan` | Step 4 roadmap with monthly milestones |
| `/cv-generate [track]` | `templates/cv-template.md` (+ `.tex` if asked); example bullets: `examples/example-cv-bullets.md` |
| `/sop-draft [programme]` | `templates/sop-outline-template.md` first draft |
| `/sop-review` | Admissions-officer scoring + revision report |
| `/lor-template` | `templates/lor-cold-email-template.md` |
| `/prof-email-draft` | `templates/lor-cold-email-template.md` cold-email part (requires ≥2 papers read) |
| `/deadline-timeline` | `templates/deadline-offer-templates.md` part A |
| `/offer-compare` | `templates/deadline-offer-templates.md` part B |
| `/visa-compare` | `references/visa-policy-links.md` + visa summary below; print official links next to every threshold |
| `/founder-deck` | `templates/founder-pack-template.md` + `references/founder-fundraising-ecosystem.md` |
| `/mindset` | `references/career-mindset-adaptability.md` — reframe credential anxiety as optionality; redirect to concrete moves |

## 4. Founder track (summary — details live in references/)
- **Goal profile:** hard-tech venture raising VC globally — overseas YC / Silicon Valley / California / Middle East sovereign capital (Mubadala, PIF/Sanabil, Hub71); domestic China 红杉中国 HongShan, 硬科技基金 (中科创星/深创投/线性), PE (高瓴/CPE/国调). Full lists & accelerator names: `references/founder-fundraising-ecosystem.md`.
- **Visa reality (2026-08 snapshot, re-verify at `references/visa-policy-links.md`):** US has no startup visa — IER parole ($311,071 qualified US investment / $124,429 grants, ~26 lifetime approvals, no green-card path); O-1A is the practical pre-seed route (~90%+ approvals; beneficiary-owned company may petition); EB-1A/NIW for long term; E-2 NOT available to Chinese nationals. UK Innovator Founder = endorsement, no investment minimum, 3yr→ILR. Singapore EntrePass = ≥30% ownership + SGD100k round or recognised accelerator. France French Tech = 4yr, no capital, SMIC funds. Canada SUV PAUSED since 2026-01-01.
- **Rule:** every visa threshold output MUST be followed by its official-source URL from `references/visa-policy-links.md`; visa content is strategy reference, never legal advice; recommend a licensed immigration lawyer.
- **Fundraising rule:** investor/accelerator names are re-verification items ("terms to confirm"), never promises; US C-Corp vs China-entity vs dual-structure is a lawyer/accountant decision.

## 5. Hallucination & risk controls (mandatory)
1. School data: CSV is a hallucination-reduction SEED only — re-verify on `official_url`; mark last-checked date; if a fact can't be verified, say so.
2. Visa data: cite official link beside each claim; policies change monthly.
3. AI output is a DRAFT: SOP/CV require deep human rewrite + native-English proofread before submission; never submit AI text directly.
4. Visa/legal: consult licensed professionals; this skill never provides legal advice.
5. No copying from sample-SOP repos (learn narrative structure only).

## 6. Output conventions
- Save files under these gitignored folders (private, never committed): `profile/`, `evidence-map/`, `cv/`, `sop/`, `drafts/`, `offers/`.
- Tables for any comparison; sources (official URL + date) attached to factual claims; versions in filenames.
