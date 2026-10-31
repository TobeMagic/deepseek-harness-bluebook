# Show HN 执行卡

> HN 发帖必须用本人账号登录 news.ycombinator.com 操作，无 API 可代发。这张卡把「择时、操作、守评论区」压到照着做即可。

## 一、什么时候发

今天是 **2026-10-31（周六）**。Show HN 的黄金窗口是**周二至周四早 7–10 点（美东时间，PT）**，周末发等于白扔。

下一个最佳档期：

| 日期 | PT 时间 | 北京时间 | 备注 |
|---|---|---|---|
| 周二 2026-11-03 | 07:00–09:00 | 22:00–24:00 | **首选**，周二 HN 流量最厚 |
| 周三 2026-11-04 | 07:00–09:00 | 22:00–24:00 | 备选 |

换算口径：11 月起美国进入冬令时，PT = UTC-8；北京时间 = UTC+8，即**北京比 PT 快 16 小时**。晚上 10 点后发，正对着美国东海岸早晨到岗、西海岸 7 点喝咖啡刷 HN 的时段。

避开：周五下午、周末全天、美国法定假日（11 月 11 日退伍军人节前后各避开一天）。

## 二、怎么发（5 分钟）

1. 登录 https://news.ycombinator.com/login（账号需注册满 **1 小时**且有少量 karma 才能发帖；新号第一次发建议先养一天）
2. 打开 https://news.ycombinator.com/submit
3. **Title**（照抄，不要改）：

   ```
   Show HN: A 42-diagram design reading of DeepSeek Harness (no code, plain language)
   ```

4. **URL**（填 Pages 地址，不要填 GitHub——HN 用户被跳转到 GitHub 仓库页会认为是普通开源推荐，不是 Show）：

   ```
   https://tobemagic.github.io/deepseek-harness-bluebook/
   ```

5. **Text**（正文直接粘贴下面这段，HN 的 text 字段自带排版）：

   ```
   I wrote a book that explains why DeepSeek Harness is architected the
   way it is — not how to install it. Three things it tries to do
   differently:

   1. One running story (a repair crew fixing a lamp) carries every
      chapter, so non-programmers can finish it. No package names,
      no code.
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

6. 勾选 **Show HN**，提交。

## 三、发完前 2 小时（决定生死）

HN 首页竞争是前 60–90 分钟定胜负。发完盯着：

**必做：**
- 发完 **15 分钟内**自己在评论区发第一条补充：点明书的立场是「设计解读，不是使用教程」，并预告会回答所有问题。HN 作者亲自下场是加分项。
- 每条评论都回。前 2 小时做到 100% 回复，哪怕只说「good point, thanks」。
- 有技术质疑（「这是二手资料拼的吧」）不辩解，直接承认原文口径：素材来自公开资料与官方文档，不含实测——把诚实声明顶在前面，HN 吃这套。

**预期会来的问题（先想好答案）：**
- 「MIT 的书和 GitHub 上的 harness 什么关系？」——两回事：书是第三方设计解读，仓库不是 DSH 官方仓库，书里已声明。
- 「为什么用中文写？」——目标读者是不写代码的人；已备 PDF/EPUB，英译在考虑。
- 「和橙皮书系列的差别？」——橙皮书讲「装上之后会发生什么」，这本讲「为什么被设计成这样」，互补不竞争。

**别做：**
- 不要找任何人投票。HN 的投票操纵检测会直接毙掉帖子，且封号。
- 不要把同一个链接换标题重发（HN 会合并并降权）。
- 前 2 小时别干别的，评论区冷清就等于死。

## 四、如果冲上首页会怎样

正常曲线：发后 30 分钟上 Newest，1–2 小时内冲 front page 或第二页，停留 4–8 小时。中文书在 HN 属于稀有内容，「42 张图 + 零代码 + 中文原创」的组合有辨识度，冲上去的概率不低。

带好两样东西再发：
1. Pages 页面本身能承受流量（GitHub Pages 无此虞）
2. 手机能刷 HN 评论区——晚上 10 点后大概率不在电脑前

## 五、复盘要记的数

发布后 24 小时记下：points、评论数、是否上过 front page、Pages 访问量（GitHub 仓库 Insights → Traffic 可看 referrer）。这几个数决定下一本书（第二本蓝宝书）要不要再走 HN。
