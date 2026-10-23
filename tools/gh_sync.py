#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
不依赖 `git push` 的同步：用 GitHub Git Data API 把本地文件提交到远程。

为什么需要它：某些环境里 git 的网络操作会被杀掉（无输出、SIGTERM），
但 `gh auth token` 与 HTTPS API 正常。这个脚本走 HTTP 提交，
可以做单个 commit，也支持二进制文件（PDF / EPUB / 图片）。

用法（路径相对仓库根，前面加 ! 表示删除；local:remote 可指定远程路径）：
    python tools/gh_sync.py README.md tools/foo.py !old.md -m "提交说明"
    python tools/gh_sync.py books/x/book.html:index.html --branch gh-pages -m "发布"

选项：
    --repo  owner/name   默认读 git remote
    --branch main
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def token() -> str:
    r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    t = r.stdout.strip()
    if not t:
        sys.exit("拿不到 gh token，先 gh auth login")
    return t


def api(method: str, path: str, payload=None, tok: str = ""):
    url = path if path.startswith("http") else f"https://api.github.com/repos/{path}"
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {tok}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "bluebook-gh-sync")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"API {method} {path} 失败 {e.code}: {e.read().decode('utf-8', 'ignore')[:400]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("-m", "--message", required=True)
    ap.add_argument("--repo", default="")
    ap.add_argument("--branch", default="main")
    args = ap.parse_args()

    repo = args.repo
    if not repo:
        r = subprocess.run(["git", "-C", ROOT, "remote", "get-url", "origin"],
                           capture_output=True, text=True)
        m = re.search(r"github\.com[:/]([^/\s]+/[^/\s]+?)(?:\.git)?$", r.stdout.strip())
        if not m:
            sys.exit("拿不到仓库名，用 --repo owner/name 指定")
        repo = m.group(1)

    tok = token()
    base = f"{repo}/git"

    # 1. 当前分支指针
    ref = api("GET", f"{base}/ref/heads/{args.branch}", tok=tok)
    parent = ref["object"]["sha"]
    tree_sha = api("GET", f"{base}/commits/{parent}", tok=tok)["tree"]["sha"]

    entries = []
    for p in args.paths:
        # local:remote 冒号映射，远程路径可与本地不同（用于 Pages 入口 index.html）
        remote = p
        if not p.startswith("!") and p.count(":") == 1 and p[1] != ":":
            p, remote = p.split(":", 1)
        if p.startswith("!"):
            entries.append({"path": p[1:], "mode": "100644", "type": "blob", "sha": None})
            print("  D", p[1:])
            continue
        full = os.path.join(ROOT, p)
        if not os.path.exists(full):
            sys.exit(f"找不到本地文件：{p}")
        raw = open(full, "rb").read()
        blob = api("POST", f"{base}/blobs",
                   {"content": base64.b64encode(raw).decode("ascii"),
                    "encoding": "base64"}, tok=tok)
        entries.append({"path": remote.replace("\\", "/"), "mode": "100644",
                        "type": "blob", "sha": blob["sha"]})
        print(f"  A {p} -> {remote}  ({len(raw)//1024} KB)")

    tree = api("POST", f"{base}/trees", {"base_tree": tree_sha, "tree": entries}, tok=tok)
    commit = api("POST", f"{base}/commits",
                 {"message": args.message, "tree": tree["sha"], "parents": [parent]}, tok=tok)
    api("PATCH", f"{base}/refs/heads/{args.branch}", {"sha": commit["sha"]}, tok=tok)
    print(f"pushed {commit['sha'][:8]} -> {repo}@{args.branch}")


if __name__ == "__main__":
    main()
