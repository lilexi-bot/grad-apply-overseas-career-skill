# AGENTS.md — Grad Apply & Overseas Career Skill (v2.0)

This repository is a structured Claude-Code/Codex-compatible **Skill** for graduate applications,
overseas careers and founder planning.

@SKILL.md

The `SKILL.md` frontmatter auto-triggers on 留学申请/选校/文书/CV/SOP/海外工作/创业签证 etc. (EN & 中文).

## Operating protocol
1. **Progressive loading:** keep only `SKILL.md` in context. Load files under `templates/`, `references/`,
   `examples/` ONLY when the routing table (SKILL.md §0) calls for them — never bulk-load everything.
2. **Facts must be verified:** school figures from `references/school-programs.csv` are a seed — re-check
   on official URLs; visa claims must be output with the official links from `references/visa-policy-links.md`.
3. **Deliverables are files,** versioned Markdown under gitignored private folders
   (`profile/ evidence-map/ cv/ sop/ drafts/ offers/`) — never commit personal data to this public repo.
4. **Never fabricate** experience, results, funding or traction; the user owns final editing rights.
5. AI text is a draft: human rewrite + native proofread before any submission; visa matters → licensed lawyer.
