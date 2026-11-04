---
gists:
  - id: ea85fdbb22279def0882de0e8ac3fd76
    url: 'https://gist.github.com/LikeACodingStone/ea85fdbb22279def0882de0e8ac3fd76'
    createdAt: '2026-09-10T08:28:01Z'
    updatedAt: '2026-09-10T08:28:18Z'
    filename: README-Obsidian-GitHub-Gist.md
    isPublic: true
    baseUrl: 'https://api.github.com'
tags: [tools, obsidian, github, gist]
updated: 2026-11-04
---
# Obsidian + GitHub Gist Guide [使用手册]

> [!summary] Summary [概要]
> Share an Obsidian note as a GitHub Gist, and have the Gist update automatically whenever you edit the note.
> [把 Obsidian 笔记分享为 GitHub Gist，之后每次修改笔记都自动更新 Gist。]

```text
Obsidian note ── Share as Gist ──► GitHub Gist
      ▲                                │
      └── `gists` property (id + url) ◄┘
```

> [!danger] Never delete the `gists` property [不要删除 `gists` 属性]
> It is the link between the note and its Gist (id + url). Without it the plugin can't tell which Gist to update.
> [它是笔记与 Gist 之间的关联（id + url）。没有它，插件不知道该更新哪个 Gist。]

---

## 1. Create a GitHub Token [创建 GitHub Token]

GitHub → Settings → Developer settings → Personal access tokens (`github.com/settings/tokens`).

| Token type [类型] | Permission needed [所需权限] |
|---|---|
| **Fine-grained** (recommended [推荐]) | **Gists: Read and write** |
| Classic | `gist` scope |

> [!warning] Treat the token like a password [Token 等同于密码]
> Never put it in a note, a README, a Gist, a Git repository, or send it to anyone.
> [不要写进笔记、README、Gist、Git 仓库，也不要发给别人。]

## 2. Plugin Setup [插件配置]

**Obsidian → Settings → Community plugins → Share as Gist** → paste the token into **Personal access token**.

Recommended settings [推荐设置]:

| Setting [设置项] | Value | Why [作用] |
|---|---|---|
| Enable updating Gists after creation | **ON** | Lets the plugin update Gists it already created [允许更新已创建的 Gist] |
| Enable auto-saving Gists after edit | **ON** | Edit a linked note → the Gist updates automatically [修改已关联的笔记后自动更新 Gist] |
| Include front matter in gists | **OFF** | Don't upload the properties. The local `gists` property stays [不上传属性，本地 `gists` 属性不受影响] |
| Enable auto-save notice | ON / OFF | Shows a toast on each auto-save; turn off if noisy [自动保存时弹出通知，嫌烦可关闭] |
| Include table of contents | **OFF** | No auto-generated TOC [不自动生成目录] |

## 3. Share a Note [分享笔记]

1. Open the note [打开笔记]
2. `Ctrl + P` → type `gist` [输入 `gist`]
3. Choose **Share as public gist on GitHub.com** or **Share as secret gist on GitHub.com**

On success the note gets a `gists:` property with the Gist `id` and `url`; that means the Gist is created **and** linked.
[成功后笔记里会出现带 `id` 和 `url` 的 `gists:` 属性，表示 Gist 已创建**并且**已关联。]

> [!warning] Secret Gist is not private [Secret Gist 不是私密的]
> Secret = not listed publicly, but **anyone with the URL can read it**. Truly sensitive content belongs in a **private GitHub repository**.
> [Secret 只是不公开列出，**拿到 URL 的人都能访问**。真正敏感的内容请放**私有 GitHub 仓库**。]

## 4. Sync & Verify [同步与确认]

- Edit the note and save: the Gist updates automatically (with auto-saving ON) [修改并保存，Gist 自动更新]
- Verify: open the Gist page and refresh with `Ctrl + R` [打开 Gist 页面，`Ctrl + R` 刷新确认]
- Manual sync: `Ctrl + P` → `gist` → run the **Update / Save Gist** command [手动同步]

## 5. Troubleshooting [常见问题]

| Problem [问题] | Check [检查] |
|---|---|
| Token doesn't work [Token 无法使用] | Expired? Permission correct (fine-grained: **Gists → Read and write**; classic: `gist`)? [是否过期、权限是否正确] |
| Edits don't update the Gist [修改后没有更新] | Both **Enable updating Gists after creation** and **Enable auto-saving Gists after edit** are ON, and the note still has the `gists` property [两个开关都开启，且笔记里仍有 `gists` 属性] |
| Gist page looks unchanged [Gist 页面没变化] | Refresh with `Ctrl + R`; if still old, run **Update / Save Gist** manually [先刷新，仍无变化就手动执行更新] |
| Deleted the `gists` property [删除了 `gists` 属性] | The plugin can't find the Gist any more; run **Share as Gist** again (this may create a new Gist) [重新执行 Share as Gist，可能会创建新的 Gist] |

## 6. How I Use It [使用习惯]

- **Obsidian = local knowledge base [本地知识库].** **Gist = online sharing page with version history [在线分享页，带版本历史].** A Gist is a Git repo, so you can see every revision and diff. [Gist 本质是 Git 仓库，可查看每次修改和 Diff。]
- Share only the notes you want to publish. Don't auto-publish the whole vault. [只分享需要公开的笔记，不要把整个库自动公开。]
- **A Gist is not a backup [Gist 不是备份].** Back up the whole vault with a Git repository; use Gists to share single notes. [整库备份用 Git 仓库，Gist 只用来分享单篇笔记。]
- Use English file names, so Gist pages and Raw URLs are easier to use (e.g. `ubuntu-install-tools.md`, `adb-wifi.md`). [文件名用英文，Gist 页面和 Raw URL 更好用。]

## 7. References [参考资料]

- GitHub Gists docs: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists
- Creating Gists: https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists
- Gists REST API: https://docs.github.com/en/rest/gists/gists

---

> [!success] One-line summary [一句话总结]
> Token (**Gists: Read and write**) → both switches **ON** → **Share as Gist** once → every later edit syncs automatically.
> [Token（**Gists 读写**）→ 两个开关**打开** → 第一次 **Share as Gist** → 以后修改自动同步。]
