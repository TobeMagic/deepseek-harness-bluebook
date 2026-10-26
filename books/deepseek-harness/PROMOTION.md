# 蓝宝书 01 推广投放包

> 渠道均经核实（2026-10-24 star 数）。文案可直接复制粘贴。
> 两个固定链接：**在线阅读** https://tobemagic.github.io/deepseek-harness-bluebook/ ｜ **仓库** https://github.com/TobeMagic/deepseek-harness-bluebook

## 执行记录（2026-10-26）

| 动作 | 状态 | 链接 |
|---|---|---|
| GitHubDaily 自荐 issue | ✅ 已发 #1287 | https://github.com/GitHubDaily/GitHubDaily/issues/1287 |
| 阮一峰周刊自荐 issue | ✅ 已发 #12791 | https://github.com/ruanyf/weekly/issues/12791 |
| skill PR（agentic-awesome-skills ★48.5k） | ✅ 已提 PR #2142，mergeable，安全扫描通过 | https://github.com/sickn33/agentic-awesome-skills/pull/2142 |
| ComposioHQ/awesome-claude-skills | ❌ PR 入口已关闭（REST 返 404），fork 已备好但放弃 | — |
| Show HN | ⬜ 待择时（周二至周四 7–10am PT） | — |
| X 线程 | ⬜ 待发（见下方文案） | — |
| 知乎/V2EX 长文 | ⬜ 待写 | — |

---

## 一、渠道清单（按优先级）

| 优先级 | 渠道 | 体量 | 投什么 | 怎么投 |
|---|---|---|---|---|
| ★★★★★ | **GitHubDaily**（github.com/GitHubDaily/GitHubDaily） | ★48.3k | 全书自荐 | 仓库 issues 新建自荐，X 账号 @GitHubDaily 同步转发 |
| ★★★★★ | **ComposioHQ/awesome-claude-skills** | ★77.8k | 「蓝宝书写作规范」**skill**（见下文切入点） | fork → 按 CONTRIBUTING 建 skill 目录 + README → PR |
| ★★★★ | **阮一峰周刊**（github.com/ruanyf/weekly） | ★106.9k | 资源推荐 | issues 提交，每周五发，被选中的曝光极大 |
| ★★★★ | **Hacker News Show HN** | — | 英文发布 | 周二至周四 7–10am PT 发，48 小时内回完每条评论 |
| ★★★ | **X 线程**（作者号 + @GitHubDaily 互动） | — | 中文/英文双版 thread | 周二三 15:00–18:00 UTC 发 |
| ★★★ | 知乎 / V2EX / LinuxDo / 掘金 | — | 长文首发 | 「为什么 DeepSeek Harness 最中间那层能整块抽走」选题切入 |
| ★★ | 0voice/awesome-ai-tools、best-of-ai/best-of-ai | ★0.4–0.7k | 目录收录 | issue 提交，顺手做 |

**最重要的切入点—— ComposioHQ/awesome-claude-skills 不收录「书」，只收录「skill」。**
但蓝宝书仓库里的 STYLE.md + WRITING-GUIDE.md 本身就是一套完整的写作规范，把它打包成一个真 skill 提交：

```
bluebook-writing-skill/
└── SKILL.md   （双层解释法 + 自包含 + 节标题三律 + 文风红线，frontmatter 两个字段）
```

三个好处：① 符合收录标准（解决真实问题、有 SKILL.md、可复用、有社交证明——Pages 线上版就是使用案例）② skill 描述里自然带出书的链接，是活的广告 ③ 书的规范第一次以「可执行的 skill」形态进入 Claude 生态，比干推一本书更容易被 merge。

---

## 二、投稿文案（直接复制）

### 1. GitHubDaily 自荐 issue

```markdown
## 项目名称
蓝宝书 01 · DeepSeek Harness——《一切皆插件：一个 AI 外壳是怎么长起来的》

## 项目链接
在线阅读（免下载）：https://tobemagic.github.io/deepseek-harness-bluebook/
GitHub：https://github.com/TobeMagic/deepseek-harness-bluebook

## 项目简介
一本免费的设计解读书，讲清楚 DeepSeek Harness 为什么被设计成这样。
全书 3.4 万字、42 张手绘流程图，用「师傅队伍修灯」一个故事贯穿，
零代码、零包名、不写代码的人也能读完。每节先讲人话再上术语，
结尾给「这条能搬去哪」。

## 与现有内容的区别
市面上的内容是「装上之后会发生什么」（教程）或「源码导读」。
这本书回答另一半：六层结构为什么这么切、最中间的内核为什么能整块抽走、
它与 Claude Code / Codex CLI 三家外壳的根本分歧在哪。

## 适合收录的类目
免费书籍 / AI 技术
```

### 2. Show HN（英文）

```markdown
Title: Show HN: A 42-diagram design reading of DeepSeek Harness (no code, plain language)

Body:
I wrote a book that explains why DeepSeek Harness is architected the way it
is — not how to install it. Three things it tries to do differently:

1. One running story (a repair crew fixing a lamp) carries every chapter,
   so non-programmers can finish it. No package names, no code.
2. 42 hand-drawn flow diagrams are the skeleton, not decoration.
3. Every section ends with "where can I take this" — the point is
   transferable design judgments, not this one repo.

It also compares the harness against Claude Code and Codex CLI:
three products, three different things being sold.

~34k Chinese characters, free, MIT. Read online (no download):
https://tobemagic.github.io/deepseek-harness-bluebook/

Honest limitation: sources are public docs and secondary material,
no hands-on benchmarking — it's a design reading, not a field test.
```

### 3. X 中文线程

```
1/ 花叔的橙皮书讲「装上之后会发生什么」，这本书讲被漏掉的另一半：
   DeepSeek Harness 为什么被设计成这样。
   3.4 万字，42 张流程图，一个修灯师傅的故事讲完全书🧵

2/ 它最反常识的一件事：最中间的那一层——连 agent 循环本身——
   可以整块抽走，别处一行都不用改。
   全书就从这里开始追问：为什么敢这么切，代价是什么。

3/ 写法：每节先讲人话（零术语，师傅队伍的故事），再上专业版
   （正式名、机制、边界、代价），最后一张对照表 + 最容易理解错的地方。

4/ 和 Claude Code、Codex CLI 摆在一起看：
   三家外壳，三种卖法——卖插座的、卖成品的、卖接口的。
   分歧比相似更有信息量。

5/ 不写代码的人能读，写代码的人能照着造。
   在线读，免下载：https://tobemagic.github.io/deepseek-harness-bluebook/
   GitHub：github.com/TobeMagic/deepseek-harness-bluebook
```

### 4. X 英文线程

```
1/ Orange Book explains what happens after you install a tool.
   This book explains the half everyone skips: why it's built this way.
   DeepSeek Harness, read through design decisions 🧵

2/ The most counter-intuitive fact: the layer in the middle —
   the agent loop itself — can be pulled out entirely.
   Everything else keeps working. The book starts there.

3/ One story (a repair crew fixing a lamp) runs through all 21 chapters.
   Zero package names. 42 hand-drawn flow diagrams.

4/ It also lines up DeepSeek Harness against Claude Code and Codex CLI:
   three harnesses, three different products.

5/ Free, MIT, read online:
   https://tobemagic.github.io/deepseek-harness-bluebook/
```

---

## 三、执行顺序建议

1. **本周**：GitHubDaily issue 自荐 + 阮一峰周刊提交（两个都是 issue，成本最低）
2. **下周**：蓝宝书写作规范打包成 SKILL.md → PR 到 ComposioHQ/awesome-claude-skills（需要一天打磨 skill）
3. **Show HN 择时**：周二至周四早上（PT 时间），发完 48 小时守在评论区
4. **X**：作者号发中文线程，@GitHubDaily 等账号在相关 thread 下真诚互动（不是转发了事）
5. **中文社区长文**：把 §07「内核为什么是空的」改写成知乎/V2EX 长文，文末带书链

> 红线：所有渠道都先以「内容价值」出现，不贴牛皮癣式广告。
> awesome 列表明确拒绝纯引流提交——skill 本身必须立得住。
