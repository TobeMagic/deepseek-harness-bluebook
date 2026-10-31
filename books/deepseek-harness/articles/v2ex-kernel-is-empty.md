# 一个把 agent 循环都做成插件的开源外壳：DSH，以及我拿它写的一本图解

最近读了一个开源项目 DeepSeek Harness，写书的思路被它带了一遍，把过程记下来。

**它的内核是空的。**

就是字面意思：中心那一层可以整块拿走，别处一行都不用改。大多数同类软件（Claude Code、Codex CLI）把那个「看情况→决定→动手→看结果→再决定」的循环焊在最里面，DSH 把这个循环也做成了插件，和拧螺丝的、记笔记的站同一层，由同一张装配清单决定今天谁上。

代价也真实：读一遍装配清单，看不出系统在干什么，行为得从配置里重建。复杂度从实现方转移给了使用者。换来的是换得动，且内核不长胖。

**两个从它身上拿走的判据**（这两条是我写这本书真正的收获）：

1. 量「改动半径」：挑出系统里那个一请假全瘫的组件，数有多少处直接写了它的名字。数字越大，替换越是空话。工牌上印「灵活编制」不算数，多少人直接点名找它才算数。
2. 判断组件该不该进内核，问的不是它重不重要，是它会不会被换。重要会骗人，重要却很少被动的东西才该待在内核里。

**关于书**：写《蓝宝书 01 · DeepSeek Harness》的过程中，我把 DSH 和 Claude Code、Codex CLI 摆在一起对比——三种外壳三种卖法：卖成品（Claude Code）、卖接口（Codex CLI）、卖插座（DSH）。3.4 万字、42 张流程图，用「修灯师傅队伍」一个故事贯穿，零代码零包名，不写代码能读完，每节结尾给「这条能搬去哪」。

在线阅读（单文件 HTML，免下载）：https://tobemagic.github.io/deepseek-harness-bluebook/

仓库（含 PDF/EPUB，MIT）：https://github.com/TobeMagic/deepseek-harness-bluebook

素材来自公开资料与官方文档整理，不含实测，书里没有引用清单、没有 commit hash，口径全部在正文内讲完。

顺便，这个写作方法（双层解释法）被 agentic-awesome-skills 收成了一个 skill，对写技术科普的人可能有用：https://github.com/sickn33/agentic-awesome-skills/blob/main/skills/bluebook-writing/SKILL.md
