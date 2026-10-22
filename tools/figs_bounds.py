#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
蓝宝书 §15–§17 图（边界部分）。

配合 tools/build_figures.py 使用：
    python tools/build_figures.py --only 15-1 15-2 15-3 16-1 16-2 16-3 17-1 17-2 17-3
"""
from __future__ import annotations

from svgkit import (  # noqa: F401
    INK, GRAY, BLUE, CREAM, TEAL, LINE, HAIR, PAPER,
    B1, B2, B3, B4, ONB, T1,
    rect, txt, vtxt, path, line, circle, diamond, note, tag, banner, write,
    W,
)


# ---------------------------------------------------------------- 图 46
def fig_15_1(out_dir):
    rows = [
        ("主干", "核心主干服务", "空", BLUE, "#FFFFFF"),
        ("可换", "可替换的能力", "有平级实现包", TEAL, "#FFFFFF"),
        ("服务", "独立服务", "空", B3, INK),
        ("组合", "组合包／组合点", "空", B1, INK),
    ]
    b = []
    b.append(txt(40, 22, "角色", size=11, fill=GRAY))
    b.append(txt(180, 22, "官方名", size=11, fill=GRAY))
    b.append(txt(392, 22, "实现列", size=11, fill=GRAY))
    y0, step, rh = 40, 54, 42
    for i, (role, name, why, fill, fg) in enumerate(rows):
        y = y0 + i * step
        b.append(rect(40, y, 608, rh, fill=PAPER, stroke=HAIR))
        b.append(rect(52, y + 8, 92, 26, fill=fill, rx=13))
        b.append(txt(98, y + 21, role, size=11.5, fill=fg, anchor="middle"))
        b.append(txt(180, y + 21, name, size=12.5, fill=INK, weight=600))
        b.append(txt(392, y + 21, why, size=11, fill=GRAY if i != 1 else TEAL))
    b.extend(banner(40, 264, 608, "实现列有平级实现包的一定是能换的那类；空的三类靠角色列区分。", fill=CREAM))
    b.append(note(40, 306, "看实现列：有平级实现的一定是能换的那类；空的几类靠角色列区分"))
    return write(
        out_dir, "fig-15-1-four-roles.svg", 320,
        "图 37：四种角色看实现列",
        "四种角色并排：核心主干服务、可替换的能力、独立服务、组合包。后三列的实现列都是空的，只能靠角色列区分；可替换的那"
        "一类有平级实现包——有第二个实现可换的，一定在这一类里。",
        b,
    )


# ---------------------------------------------------------------- 图 47
def fig_15_2(out_dir):
    b = []
    b.append(rect(60, 20, 190, 46, fill=PAPER, stroke=LINE, rx=8))
    b.append(txt(155, 43, "agent-loop", size=12.5, fill=INK, weight=600, anchor="middle", mono=True))
    b.append(rect(430, 20, 190, 46, fill=PAPER, stroke=LINE, rx=8))
    b.append(txt(525, 43, "compaction-basic", size=12.5, fill=INK, weight=600, anchor="middle", mono=True))

    b.append(rect(240, 118, 200, 58, fill=BLUE, rx=8))
    b.append(txt(340, 139, "ctx.llm", size=14, fill="#FFFFFF", weight=600, anchor="middle", mono=True))
    b.append(txt(340, 159, "适配器注册表", size=11, fill=ONB, anchor="middle"))

    b.append(path("M155,66 C155,96 300,92 322,116", stroke=BLUE, sw=1.4, marker="arb"))
    b.append(path("M525,66 C525,96 380,92 358,116", stroke=BLUE, sw=1.4, marker="arb"))
    b.append(txt(160, 92, "查 key", size=10.5, fill=GRAY))
    b.append(txt(486, 92, "查 key", size=10.5, fill=GRAY))

    impls = [("llm-deepseek", 40), ("llm-pi-ai", 250), ("llm-replay", 460)]
    for name, x in impls:
        b.append(rect(x, 244, 180, 46, fill=B1, stroke=HAIR, rx=8))
        b.append(txt(x + 90, 267, name, size=12, fill=INK, weight=600, anchor="middle", mono=True))
        b.append(path(f"M{x + 90},242 C{x + 90},210 340,208 340,178", stroke=GRAY, sw=1.2, marker="ar"))
    b.append(txt(148, 226, "供 key", size=10.5, fill=GRAY))
    b.append(txt(340, 226, "供 key", size=10.5, fill=GRAY))
    b.append(txt(548, 226, "供 key", size=10.5, fill=GRAY))

    b.extend(banner(40, 308, 608, "消费方只认 key，实现平级挂着；换掉一个实现，消费方不动。"))
    b.append(note(40, 350, "ctx.llm 三个实现：llm-deepseek / llm-pi-ai / llm-replay（后者在 test-support 分组）"))
    return write(
        out_dir, "fig-15-2-seam-fanout.svg", 364,
        "图 38：一个 seam 的多个实现平级挂在同一个 key 下",
        "上方两个消费方 agent-loop 与 compaction-basic 只连到 ctx.llm 这个 key；下方 llm-deepseek、"
        "llm-pi-ai、llm-replay 三个实现包平级挂在同一个 key 下。消费方与实现之间没有直接的边。",
        b,
    )


# ---------------------------------------------------------------- 图 48
def fig_15_3(out_dir):
    b = []
    cols = 11
    cw, ch, gx, gy, y0 = 22, 22, 3, 8, 48
    lw = cols * (cw + gx) - gx
    x_l, x_r = 60, 368
    b.append(txt(x_l + lw / 2, 30, "有替换位", size=13, fill=INK, weight=600, anchor="middle"))
    b.append(txt(x_r + lw / 2, 30, "已备好第二个实现", size=13, fill=INK, weight=600, anchor="middle"))
    for n in range(33):
        i, j = n % cols, n // cols
        b.append(rect(x_l + i * (cw + gx), y0 + j * (ch + gy), cw, ch, fill=B1, stroke=HAIR, rx=3))
    for n in range(33):
        i, j = n % cols, n // cols
        x, y = x_r + i * (cw + gx), y0 + j * (ch + gy)
        if n < 15:
            b.append(rect(x, y, cw, ch, fill=TEAL, rx=3))
        else:
            b.append(rect(x, y, cw, ch, fill="#FFFFFF", stroke=LINE, rx=3, dash="3 3"))
    solid_bot = y0 + (ch + gy) + ch
    grid_bot = y0 + 2 * (ch + gy) + ch
    b.append(line(x_r + lw + 4, solid_bot, x_r + lw + 4, grid_bot, stroke=LINE, sw=1.2, dash="3 3"))
    b.append(vtxt(x_r + lw + 14, (solid_bot + grid_bot) / 2, "还空着", size=11, fill=GRAY))
    b.extend(banner(40, 170, 608, "有替换位，不等于备好了第二个实现。"))
    b.append(note(40, 218, "一格里一个位子 · 实心 = 第二个实现已到岗 · 虚线空格 = 契约立好了，实现还只有一份"))
    return write(
        out_dir, "fig-15-3-seam-second-impl.svg", 268,
        "图 39：有替换位的，不一定都备好了第二个实现",
        "一条横轴摆着一格格替换位。绿色那些已经有了两个以上平级实现；灰色的契约立好了，眼下只有一份实现。有替换位和有没有"
        "现成的第二个实现，是两笔账。",
        b,
    )


# ---------------------------------------------------------------- 图 49
def fig_16_1(out_dir):
    rows = [
        ("收紧", "权限收紧", "策略写到的模式", "策略没写到的模式", BLUE),
        ("审批", "人工审批", "没被授权的操作", "人批错；无人应答按拒绝", BLUE),
        ("隔离", "沙箱隔离", "越出文件边界的写", "获准访问的资源；后端不齐全时只部分强制", BLUE),
    ]
    b = []
    y0, step, rh = 16, 88, 74
    for i, (name, duty, can, cannot, fill) in enumerate(rows):
        y = y0 + i * step
        b.append(rect(40, y, 608, rh, fill=PAPER, stroke=HAIR))
        b.append(rect(52, y + 16, 118, 42, fill=fill, rx=6))
        b.append(txt(111, y + 30, name, size=12.5, fill="#FFFFFF", weight=600, anchor="middle"))
        b.append(txt(111, y + 47, duty, size=10.5, fill=ONB, anchor="middle"))
        b.append(rect(186, y + 12, 226, 50, fill=B1, stroke=HAIR, rx=6))
        b.append(txt(299, y + 27, "挡得住", size=11, fill=TEAL, anchor="middle"))
        b.append(txt(299, y + 46, can, size=11, fill=INK, anchor="middle"))
        b.append(rect(422, y + 12, 214, 50, fill="#FFFFFF", stroke=HAIR, rx=6, dash="4 3"))
        b.append(txt(529, y + 27, "挡不住", size=11, fill=GRAY, anchor="middle"))
        b.append(txt(529, y + 46, cannot, size=11, fill=INK, anchor="middle"))
    b.extend(banner(40, 288, 608, "三道闸降低风险，不保证隔离。", "默认姿态是只读：能力一项一项授。", fill=CREAM))
    b.append(note(40, 348, "三层依次收紧：先收权限，再问人，最后圈地盘"))
    return write(
        out_dir, "fig-16-1-three-layers.svg", 362,
        "图 40：三道闸各挡什么、挡不住什么",
        "收紧挡得住的只有策略写到的模式；审批挡不住人批错与没人应答；隔离挡不住获准访问的资源，后端不齐全时还只做到部分强"
        "制。三层都降低风险，都不保证隔离。",
        b,
    )


# ---------------------------------------------------------------- 图 50
def fig_16_2(out_dir):
    b = []
    b.append(rect(40, 108, 176, 68, fill=BLUE, rx=8))
    b.append(txt(128, 132, "审批请求", size=12, fill="#FFFFFF", weight=600, anchor="middle"))
    b.append(txt(128, 152, "瀑布式分派", size=11, fill=ONB, anchor="middle"))
    outs = [
        ("授权这一次", "唯一放行", TEAL, "#FFFFFF"),
        ("拒绝", "归入拒绝", PAPER, INK),
        ("取消", "归入拒绝", PAPER, INK),
        ("无人应答", "也归入拒绝", PAPER, INK),
    ]
    for i, (name, desc, fill, fg) in enumerate(outs):
        y = 20 + i * 56
        b.append(rect(300, y, 336, 42, fill=fill, stroke=HAIR if fill != TEAL else None, rx=6))
        b.append(txt(318, y + 21, name, size=12, fill=fg, weight=600))
        b.append(txt(620, y + 21, desc, size=11, fill=TEAL if fill == TEAL else GRAY, anchor="end"))
        b.append(path(f"M218,142 C258,142 262,{y + 21} 296,{y + 21}", stroke=GRAY, sw=1.2, marker="ar"))
    b.extend(banner(40, 258, 596, "四个结果里只有一格放行；没人应答，不等于放行。"))
    b.append(note(40, 300, "四个结果是封闭的：没人应答时倒向拒绝，不倒向放行"))
    return write(
        out_dir, "fig-16-2-approval-outcomes.svg", 314,
        "图 41：审批的四个结果，只有一个放行",
        "审批请求经分派后只有四种结果：授权这一次（只放行所问的那一个操作）、拒绝、取消、无人应答。只有授权这一次放行；缺"
        "失或抛错的应答方归为无人应答，同样拒绝。",
        b,
    )


# ---------------------------------------------------------------- 图 51
def fig_16_3(out_dir):
    rows = [
        ("只读", "只让看，不让动", B1),
        ("放开工作区", "再加工作区一角与临时区", B2),
        ("绕开隔离", "沙箱这一层被整个绕过", BLUE),
    ]
    b = []
    y0, step, rh = 34, 60, 44
    for i, (name, desc, fill) in enumerate(rows):
        y = y0 + i * step
        b.append(rect(40, y, 300, rh, fill=fill, rx=6))
        fg = "#FFFFFF" if fill == BLUE else INK
        b.append(txt(58, y + 22, name, size=12, fill=fg, weight=600))
        b.append(txt(356, y + 22, desc, size=11, fill=GRAY))
    b.append(vtxt(628, 130, "只管文件系统效果 · 网络与进程可见性不在范围内"))
    b.append(rect(40, 222, 150, 26, fill=TEAL, rx=13))
    b.append(txt(115, 235, "完整", size=11, fill="#FFFFFF", anchor="middle"))
    b.append(rect(200, 222, 150, 26, fill=B3, rx=13))
    b.append(txt(275, 235, "部分", size=11, fill=INK, anchor="middle"))
    b.append(txt(366, 235, "后端不齐全时，只做到部分强制", size=11, fill=GRAY))
    b.extend(banner(40, 264, 608, "沙箱管文件效果；网络与进程可见性不在它范围。"))
    b.append(note(40, 306, "三档里只有前两档受沙箱管；第三档整个绕过它"))
    return write(
        out_dir, "fig-16-3-sandbox-modes.svg", 318,
        "图 42：沙箱的三档模式与两种强制完整性",
        "三档模式：只读只让看不让动；放开工作区再加工作区一角与临时区；绕开隔离则沙箱这一层被整个绕过。强制完整性分完整与"
        "部分两档，报部分时，要求绝对保证的消费方必须拒绝。它只管文件效果。",
        b,
    )


# ---------------------------------------------------------------- 图 52
def fig_17_1(out_dir):
    rows = [
        ("100% 行覆盖率", "装配路径从未被测"),
        ("快照通过", "回放确定性 ≠ 行为正确"),
        ("HTTP 200", "页面白屏"),
        ("非零退出码", "子程序正常完成"),
    ]
    b = []
    b.append(txt(56, 24, "看起来对的信号", size=11, fill=GRAY))
    b.append(txt(368, 24, "真实状态", size=11, fill=GRAY))
    y0, step, rh = 42, 54, 42
    for i, (sig, real) in enumerate(rows):
        y = y0 + i * step
        b.append(rect(40, y, 290, rh, fill=B1, stroke=HAIR, rx=6))
        b.append(txt(58, y + 21, sig, size=12, fill=INK, weight=600, mono=(i != 1)))
        b.append(path(f"M334,{y + 21} H364", stroke=GRAY, sw=1.2, marker="ar"))
        b.append(rect(368, y, 280, rh, fill="#FFFFFF", stroke=HAIR, rx=6, dash="4 3"))
        b.append(txt(386, y + 21, real, size=12, fill=INK))
    b.extend(banner(40, 268, 608, "四个看起来对的信号，指向四个错的状态。"))
    b.append(note(40, 310, "四起事故：信号都绿，状态都错"))
    return write(
        out_dir, "fig-17-1-four-signals.svg", 322,
        "图 43：四起事故的信号都指向错的状态",
        "四起事故的信号分别是 100% 行覆盖率、快照通过、HTTP 200 和非零退出码。它们的真实状态分别是装配路径"
        "从未被测、回放确定性不等于行为正确、页面白屏、子程序正常完成。看起来对的信号，指向错的状态。",
        b,
    )


# ---------------------------------------------------------------- 图 53
def fig_17_2(out_dir):
    b = []
    b.append(rect(40, 30, 608, 64, fill=B1, stroke=HAIR, rx=8))
    b.append(txt(58, 50, "测试路径", size=12, fill=INK, weight=600))
    b.append(txt(58, 72, "直接摆一个插件上场 → 手动递家伙 → 绿信号", size=11, fill=GRAY))
    b.append(rect(560, 42, 74, 26, fill=TEAL, rx=13))
    b.append(txt(597, 55, "通过", size=11, fill="#FFFFFF", anchor="middle"))

    b.append(rect(40, 150, 608, 64, fill=PAPER, stroke=LINE, rx=8))
    b.append(txt(58, 170, "生产路径", size=12, fill=INK, weight=600))
    b.append(txt(58, 192, "正式装载走全流程 → 真实解析服务 → 崩溃", size=11, fill=GRAY))
    b.append(rect(560, 162, 74, 26, fill=GRAY, rx=13))
    b.append(txt(597, 175, "失败", size=11, fill="#FFFFFF", anchor="middle"))

    b.append(path("M420,96 V148", stroke=GRAY, sw=1.2, dash="4 3", marker="ar"))
    b.append(txt(432, 122, "信号测的是上面这条路", size=10.5, fill=GRAY))
    b.extend(banner(40, 236, 608, "检验：这个信号是在哪条路径上产生的？那条路径和生产路径是同一条吗？"))
    return write(
        out_dir, "fig-17-2-signal-path.svg", 298,
        "图 44：信号产生的路径与生产路径不是同一条",
        "上一条是彩排路径：直接摆一个插件上场、手动递家伙，信号为通过。下一条是正式路径：装载走全流程、真实解析服务，结果"
        "是崩溃。信号测的是上面这条路，所以它不能证明下面这条也对。",
        b,
    )


# ---------------------------------------------------------------- 图 54
def fig_17_3(out_dir):
    b = []
    b.append(rect(40, 60, 250, 74, fill="#FFFFFF", stroke=HAIR, rx=8, dash="4 3"))
    b.append(txt(165, 84, "agent 自述", size=12.5, fill=INK, weight=600, anchor="middle"))
    b.append(txt(165, 106, "事后报告，反推意图", size=11, fill=GRAY, anchor="middle"))

    b.append(rect(390, 60, 250, 74, fill=BLUE, rx=8))
    b.append(txt(515, 84, "持久化事件日志", size=12.5, fill="#FFFFFF", weight=600, anchor="middle"))
    b.append(txt(515, 106, "一次会话的全程", size=11, fill=ONB, anchor="middle"))

    b.append(rect(288, 74, 104, 46, fill=CREAM, stroke=HAIR, rx=6))
    b.append(txt(340, 97, "复盘", size=12.5, fill=INK, weight=600, anchor="middle"))

    b.append(path("M290,97 H288", stroke=LINE, sw=1.2))
    b.append(path("M340,60 C340,40 200,40 180,56", stroke=GRAY, sw=1.2, dash="4 3"))
    b.append(txt(206, 34, "不可作为事实", size=10.5, fill=GRAY))
    b.append(path("M428,97 H392", stroke=BLUE, sw=1.6, marker="arb"))
    b.append(txt(410, 82, "依据", size=10.5, fill=BLUE, anchor="middle"))

    b.extend(banner(40, 168, 608, "复盘以事件日志为依据，不以事后报告反推意图。"))
    return write(
        out_dir, "fig-17-3-log-is-evidence.svg", 224,
        "图 45：复盘依据事件日志，不依据事后报告",
        "左边是事后自述，属反推意图，不能作为事实。右边是记好的总账，带序号、可回放，是复盘的依据。复盘只走总账这一条路。",
        b,
    )


FIGURES = [
    ("15-1", fig_15_1),
    ("15-2", fig_15_2),
    ("15-3", fig_15_3),
    ("16-1", fig_16_1),
    ("16-2", fig_16_2),
    ("16-3", fig_16_3),
    ("17-1", fig_17_1),
    ("17-2", fig_17_2),
    ("17-3", fig_17_3),
]
