#!/usr/bin/env python3
"""Weekly source check for grad-apply-overseas-career-skill.

Reads the single sources of truth the repo already has:
  - references/school-programs.csv  (column: official_url)
  - references/visa-policy-links.md (markdown links under each ## heading)

For each URL it records HTTP status + a hash of the cleaned page text,
compares it with data/source-state.json, and writes reports/source-check.md.

It deliberately does NOT extract tuition / deadlines / visa thresholds.
Those formats change often and the CSV tuition column is already
inconsistent (e.g. "95000 (total~$190k)" vs "~105000 total").
Auto-extracting them would silently write wrong numbers.
Changed pages are flagged for human review instead.

Usage:
  python scripts/check_sources.py \
    --csv references/school-programs.csv \
    --visa references/visa-policy-links.md \
    --state data/source-state.json \
    --report reports/source-check.md

Exit code is always 0. Broken / changed links are reported in the
markdown file, not by failing the job, so lychee + this report can
both be reviewed in the same PR.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

import requests

USER_AGENT = (
    "Mozilla/5.0 (compatible; grad-apply-skill-check/1.0; "
    "+https://github.com/lilexi-bot/grad-apply-overseas-career-skill)"
)
TIMEOUT = 20
SLEEP_BETWEEN_REQUESTS = 1.0

URL_RE = re.compile(r"https?://[^\s\)\]>\"']+")


def clean_text(html: str) -> str:
    """Strip tags / scripts / styles and normalise whitespace for hashing."""
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", html)
    text = re.sub(r"(?is)<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:16]

# sha256("")[:16]. A page that returns 202/200 with an empty body (JS-only
# shell, soft bot-block) hashes to exactly this. Treating it as a real
# baseline is worse than useless: it records "the page was empty" as if it
# were content, so the next successful fetch always reports a false
# `changed`, and a permanently-empty page never reports a real change.
EMPTY_HASH = content_hash("")


def read_program_urls(csv_path: Path) -> list[dict]:
    """Parse school-programs.csv, skipping leading # comment lines.

    Blank lines MUST be dropped as well as comment lines: the CSV has a
    blank line between the comment header and the real header row, and
    csv.DictReader treats the first line it sees as the fieldnames. With
    that blank line present, fieldnames becomes [] and every data row
    collapses to {None: [...]} — silently collecting zero URLs. Reading
    with utf-8-sig also strips a BOM if one is ever added by Excel.
    """
    urls: list[dict] = []
    lines = [
        line
        for line in csv_path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    reader = csv.DictReader(lines)
    if not reader.fieldnames or "official_url" not in reader.fieldnames:
        raise SystemExit(
            f"FATAL: {csv_path} header row not found or missing 'official_url'. "
            f"Got fieldnames={reader.fieldnames!r}. Refusing to report a false zero."
        )
    for row in reader:
        url = (row.get("official_url") or "").strip()
        if not url.startswith("http"):
            continue
        label = f"{row.get('university','').strip()} — {row.get('program','').strip()}"
        urls.append(
            {"id": f"program:{row.get('track','').strip()}:{label}", "url": url, "label": label, "group": "school-programs.csv"}
        )
    return urls


def read_visa_urls(md_path: Path) -> list[dict]:
    """Parse visa-policy-links.md. Group by ## heading, skip secondary sources."""
    urls: list[dict] = []
    group = "visa"
    in_secondary = False
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            group = line[3:].strip()
            in_secondary = "secondary" in group.lower()
        if in_secondary:
            continue
        for url in URL_RE.findall(line):
            url = url.rstrip(".,)")
            urls.append({"id": f"visa:{group}:{url}", "url": url, "label": url, "group": f"visa:{group}"})
    # Deduplicate by URL, keep first group.
    seen: set[str] = set()
    deduped: list[dict] = []
    for item in urls:
        if item["url"] in seen:
            continue
        seen.add(item["url"])
        deduped.append(item)
    return deduped


def fetch(session: requests.Session, url: str) -> dict:
    try:
        resp = session.get(url, timeout=TIMEOUT, allow_redirects=True)
        status = resp.status_code
        final_url = resp.url
        if status < 400:
            h = content_hash(clean_text(resp.text))
            return {"status": status, "final_url": final_url, "hash": h, "error": ""}
        return {"status": status, "final_url": final_url, "hash": "", "error": f"HTTP {status}"}
    except requests.RequestException as exc:
        return {"status": 0, "final_url": url, "hash": "", "error": str(exc)[:200]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--visa", required=True)
    parser.add_argument("--state", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    csv_path = Path(args.csv)
    visa_path = Path(args.visa)
    state_path = Path(args.state)
    report_path = Path(args.report)

    sources = read_program_urls(csv_path) + read_visa_urls(visa_path)
    print(f"Found {len(sources)} source URLs", flush=True)

    state: dict = {}
    if state_path.exists():
        try:
            state = json.loads(state_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            state = {}

    today = date.today().isoformat()
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    rows: list[dict] = []
    new_state: dict = dict(state)
    for item in sources:
        result = fetch(session, item["url"])
        prev = state.get(item["url"], {})
        prev_hash = prev.get("hash", "")
        if result["status"] >= 400 or result["status"] == 0:
            verdict = "broken"
        elif result["hash"] == EMPTY_HASH:
            verdict = "empty"
        elif not prev_hash:
            verdict = "new"
        elif prev_hash != result["hash"]:
            verdict = "changed"
        else:
            verdict = "unchanged"
        rows.append({**item, **result, "verdict": verdict})
        # Keep the previous real hash if this fetch came back empty: an empty
        # body is not evidence that the page changed, it is evidence that we
        # could not read it.
        stored_hash = result["hash"]
        stored_error = result["error"]
        if stored_hash == EMPTY_HASH:
            stored_error = "empty body (JS shell or soft block)"
            if prev_hash and prev_hash != EMPTY_HASH:
                stored_hash = prev_hash
        new_state[item["url"]] = {
            "label": item["label"],
            "group": item["group"],
            "status": result["status"],
            "final_url": result["final_url"],
            "hash": stored_hash,
            "last_checked": today,
            "last_error": stored_error,
        }
        time.sleep(SLEEP_BETWEEN_REQUESTS)

    changed = [r for r in rows if r["verdict"] == "changed"]
    broken = [r for r in rows if r["verdict"] == "broken"]
    new = [r for r in rows if r["verdict"] == "new"]
    unchanged = [r for r in rows if r["verdict"] == "unchanged"]
    empty = [r for r in rows if r["verdict"] == "empty"]

    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(new_state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# Source check — {today}",
        "",
        f"Checked {len(rows)} URLs: {len(unchanged)} unchanged, "
        f"{len(changed)} changed, {len(broken)} broken, "
        f"{len(empty)} empty, {len(new)} new.",
        "",
        "> This report only flags change. It does NOT update tuition /",
        "> deadlines / visa thresholds. For every `changed` row, open the",
        "> official URL, verify the figure on the page, then update the CSV",
        "> / MD file by hand and bump its `last_verified` to today.",
        "",
    ]
    for title, group_rows in [
        ("## Broken — check first", broken),
        ("## Changed — verify on official page, then update CSV/MD", changed),
        ("## Empty — page returned no text (JS shell or soft block); hash is not a baseline", empty),
        ("## New (first seen)", new),
        ("## Unchanged", unchanged),
    ]:
        lines.append(title)
        lines.append("")
        if not group_rows:
            lines.append("_(none)_")
            lines.append("")
            continue
        lines.append("| Verdict | URL | Status | Note |")
        lines.append("| --- | --- | --- | --- |")
        for r in group_rows:
            note = r["error"] or (f"hash {r['hash']}" if r["hash"] else "")
            if r["final_url"] != r["url"]:
                note += f" → redirected to {r['final_url']}"
            lines.append(f"| {r['verdict']} | {r['url']} | {r['status']} | {note} |")
        lines.append("")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"Changed: {len(changed)}, broken: {len(broken)}, empty: {len(empty)}, "
        f"new: {len(new)}, unchanged: {len(unchanged)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
