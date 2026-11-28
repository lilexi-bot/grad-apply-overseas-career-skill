# Auto-update workflow — grad-apply-overseas-career-skill

每周自动巡检一次，不自动改学费、不自动合并。

## 这套东西包含什么

```
.github/workflows/update-check.yml   # 每周一 02:00 UTC 跑一次，也可手动跑
scripts/check_sources.py             # 核心脚本：读 CSV + 签证 MD → 抓官网 → 比 hash
scripts/requirements.txt             # 只有 requests
.lychee.toml                         # 链接检查配置
data/source-state.json               # 上次抓到的每个 URL 的 hash + 状态，自动生成
reports/source-check.md              # 每次跑完生成的报告（在 PR 里看）
SKILL-patch.md                       # 贴到 SKILL.md §0.5 的运行时现查规则
```

## ⚠️ 安装前必读：workflow 文件需要单独的 token 权限（2026-11-28 实测）

推送 `.github/workflows/*.yml` 时 GitHub 会拒绝：

```
refusing to allow a Personal Access Token to create or update
workflow `.github/workflows/update-check.yml` without `workflow` scope
```

**这是 GitHub 的强制限制，不是仓库配置问题。** PAT 默认只有 `repo`，改 workflow 需要额外 `workflow` scope。两条路，任选一条：

**路 A — 给 PAT 加 `workflow` scope（推荐，一次性）**
1. GitHub → Settings → Developer settings → Personal access tokens → 找到当前 token
2. 勾上 `workflow`，保存
3. 然后把 `ci/update-check.yml` 移到 `.github/workflows/update-check.yml` 再 push

**路 B — 用网页 UI 建文件（不用改 token）**
1. 在 GitHub 网页打开仓库 → Add file → Create new file
2. 文件名填 `.github/workflows/update-check.yml`
3. 把 `ci/update-check.yml` 的全部内容粘进去，提交

在 workflow 到位之前，`ci/update-check.yml` 就是这份文件的正本——内容完全一样，只是放错目录不会被 GitHub 当成 workflow 执行。**其余部分（脚本、state、配置、SKILL 规则）都已经装好，不依赖它。**

## 安装（5 分钟）

1. 把这个文件夹里的全部内容复制到你的仓库根目录，保持相对路径不变：
   - `.github/workflows/update-check.yml`（仓库里现放在 `ci/update-check.yml`，见上方权限说明）
   - `scripts/check_sources.py`、`scripts/requirements.txt`
   - `.lychee.toml`
   - `data/source-state.json`
   - 报告目录 `reports/` 第一次跑的时候会自动生成，不用提前建
2. 推到 `main`，去 GitHub → Actions → Weekly source check → Run workflow，手动跑一次。
   第一次跑，`data/source-state.json` 里所有 URL 都会标为 `new`，这是正常的——它在建基线。
   第二次跑开始，才会真正出现 `changed / broken`。
3. 等每周一的自动 PR。标题是 `chore: weekly source check — review changed official pages`。

不需要任何 secret。默认只用 `GITHUB_TOKEN`，GitHub Actions 自带。
如果大学官网开始挡 GitHub 的 IP（403 变多），再考虑加 `FIRECRAWL_API_KEY`，现在先不用。

## 它到底查什么

来源就是你仓库里已经有的两个文件，不用再维护一份 URL 清单：

- `references/school-programs.csv`：45 个项目的 `official_url` 列
- `references/visa-policy-links.md`：各国官方链接，跳过“2026 snapshot secondary sources”那一节的二手链接

每个 URL 抓一次，记 HTTP 状态 + 清理后正文的 sha256 前 16 位，下次对比。
lychee 另外再查一遍 README.md、SKILL.md、`references/*.md` 里的所有链接有没有死链。

## 收到 PR 以后怎么审（必做，别直接合并）

PR 里只有三样东西变了：`data/source-state.json` + 两份报告。
CSV 里的学费 / 截止日一个字都没动，这是故意设计的。

审的时候按这个清单走：

1. 打开 `reports/source-check.md`，先看 **Broken**：是不是 URL 搬家了？是就更新 CSV / MD 里的链接。
2. 再看 **Changed**：逐个打开官网，核对学费 / 截止日 / 签证门槛是不是真的变了。
   变了 → 手动改 `references/school-programs.csv` 里那一行，把 `last_verified` 改成今天。
   没变（只是官网改版、加了横幅）→ 不用改 CSV，只让 state 里的新 hash 留下来。
3. 看 `reports/link-check.md`，死链修掉或删掉。
4. 确认无误再合并。合并后 `data/source-state.json` 就成了新的基线。

**不要做的事：** 不要把脚本改成自动提取学费写回 CSV。
你现在的 CSV 学费格式不统一（`95000 (total~$190k)`、`~105000 total`、`~80000 total`），大学页面结构也常变，自动提取一定会写错数字。先把 CSV 的学费列规范成“数字 + 币种 + total/yr”再考虑这一步。

## 本地怎么跑

```bash
pip install -r scripts/requirements.txt
python scripts/check_sources.py \
  --csv references/school-programs.csv \
  --visa references/visa-policy-links.md \
  --state data/source-state.json \
  --report reports/source-check.md
cat reports/source-check.md
```

脚本退出码永远是 0，broken / changed 都写在报告里，不靠退出码判断。
请求之间停 1 秒，45 + 20 多个 URL 一次跑完大约 1-2 分钟。

## 它做不到的事（先说清楚）

- 做不到“实时”：最快也是一周一次 + 用的时候现查。SKILL.md 里那条运行时现查规则（见 `SKILL-patch.md`）才是真正的实时层。
- 查不到去哪儿 / 携程 / 飞猪：登录墙 + 验证码，脚本会直接报 broken，别往里加。
- 抓不到 JS 重度渲染的页面：如果某大学官网全是 JS，requests 抓到的是空壳，hash 会一直变或一直空。这类 URL 在 `data/source-state.json` 里看到反复 `changed` 也别慌，人工打开看一眼就行。真要解决再上 Firecrawl / Playwright。
- 第一次跑没有对比基线，全是 `new`，不是 bug。

## 常见问题

**Q: 每周一几点跑？**
A: `cron: '0 2 * * 1'`，UTC 周一 02:00 = 北京时间 10:00。改 cron 那一行就能改时间。

**Q: 我想加一个新项目 / 新签证链接，要改脚本吗？**
A: 不用。加到 CSV 的 `official_url` 或签证 MD 里就行，下次跑自动会被收进来。

**Q: 某个学校官网老是 403，怎么办？**
A: 先确认浏览器里能打开。如果能打开、Actions 里 403，就是对方挡了 GitHub 的出口 IP。可以在 `.lychee.toml` 里把 403 当可接受（已经是这样了），`check_sources.py` 里那一行还是会标 broken，人工看一眼、确认数字没变就不用管，或者把它从 CSV 里暂时移到“手动核查”清单。

---

## 当前基线状态（2026-11-28 首次真跑）

69 个 URL（CSV 45 + 签证 24）：**34 个拿到真实基线 / 4 个空壳 / 31 个 broken**。

**这个数字是这套系统最重要的产出，不是 bug。** 31 个打不开意味着：

- 那些行的学费 / 截止日**没有可验证来源**；
- SKILL.md §0.5 规则 7（输出数字前必须抓同一行的官方 URL）对它们**无法执行**——不是不想查，是查不到。

### 31 个 broken 分四类，处理优先级不同

| 类别 | 数量 | 含义 | 怎么办 |
|---|---|---|---|
| 域名已死（DNS 解析不到） | 4 | 项目官网真的没了 | 换官方域名；换不到就把该行标 C 级并注明来源缺失 |
| 路径搬家（404） | 19 | 站还在，URL 变了 | 打开学校首页找新路径，改 CSV / MD |
| 挡 bot（403） | 4 | 浏览器能开，Actions 打不开 | 不算死链；人工核一次后接受它长期 broken |
| 连接层失败 | 4 | 证书 / 超时 / 老 TLS | 浏览器打开确认，能开就忽略 |

**域名已死的 4 个（优先修）：**
`mfe.ieor.columbia.edu`（Columbia MFE）· `msqf.nus.edu.sg`（NUS MSQF）· `fmath.hkust.edu.hk`（HKUST 金融数学）· `msdsml.nus.edu.sg`（NUS DSML）

**路径搬家的 19 个高度集中：** Stanford 四个系页（CS / EE / ME / MS&E）全 404、NTU 三个（EEE / MAE / NTC）全 404。这类通常是学校统一改了 URL 结构，去系首页找一次能批量修。

**挡 bot 的 4 个：** MBZUAI、Columbia Data Science、UCL taught-degrees、travel.state.gov treaty fees。

### 空壳（empty）4 个

`www.imperial.ac.uk` 的四个学院页返回 202 但正文为空（JS 渲染或软挡），hash 会算成 `e3b0c44298fc1c14`——这是 **sha256 空串**。脚本已把它们单独归为 `empty`，不当成基线，否则下周一定报假 `changed`。

---

## 相对上传版本的改动（2026-11-28）

上传的 `check_sources.py` 有三个会**静默失效**的问题，已修：

1. **CSV 一条 URL 都读不到。**`school-programs.csv` 在注释块和表头之间有一个空行，而脚本只过滤 `#` 开头的行、保留了空行。`csv.DictReader` 会把第一个看到的行当表头 → `fieldnames=[]` → 每行变成 `{None: [...]}` → `row.get("official_url")` 恒为 None。结果：45 个项目全被跳过，只查签证链接，报告显示「一切正常」。现在空行也过滤，且表头缺失时直接 `SystemExit` 而不是输出一个假的零。
2. **空壳页被写成基线。**`e3b0c44298fc1c14`（sha256 空串）原先被当成正常 hash 存进 state，导致页面后来能读时必报假 `changed`，而永远读不到的页面永远不会报真变化。现在单独 `empty` 分类，且**空 hash 不会覆盖已有的真实 hash**。
3. **读 CSV 未去 BOM。**改用 `utf-8-sig`，防止 Excel 另存后表头变成 `\ufefftrack`。

另外：`_.lychee.toml` 已按工作流引用的名字落为 `.lychee.toml`；`requirements.txt` 落到 `scripts/`；`reports/.gitkeep` 保证目录存在（lychee 的 `--output` 需要目录先存在）。
