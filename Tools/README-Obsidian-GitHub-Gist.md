---
gists:
  - id: ea85fdbb22279def0882de0e8ac3fd76
    url: 'https://gist.github.com/LikeACodingStone/ea85fdbb22279def0882de0e8ac3fd76'
    createdAt: '2026-09-10T08:28:01Z'
    updatedAt: '2026-09-10T08:28:18Z'
    filename: README-Obsidian-GitHub-Gist.md
    isPublic: true
    baseUrl: 'https://api.github.com'
---
# Obsidian + GitHub Gist 使用手册

## 1. 目的

本文记录如何在 Obsidian 中配置 GitHub Gist 插件，并实现：

-   将 Obsidian Markdown 笔记上传到 GitHub Gist
-   将一个 Obsidian Note 与一个 Gist 建立关联
-   修改 Obsidian Note 后自动更新 Gist
-   手动重新同步 Gist
-   理解 `gists` Property 的作用
-   排查 Token、同步和 Gist 更新问题

> 适合把 Obsidian 作为个人技术笔记，并使用 GitHub Gist 保存和分享
> Markdown / C++ / Linux / AOSP 等技术资料。

------------------------------------------------------------------------

# 2. 工作原理

整体关系：

``` text
Obsidian Markdown Note
        |
        | Share as Gist
        v
GitHub Gist
        |
        | Gist ID / URL
        v
Obsidian Properties
```

第一次上传之后，插件会在 Note 中保存 Gist 的关联信息。

例如：

``` yaml
---
gists:
  - id: xxxxxxxxxxxxxxxxxxxxxxxxx
    url: https://gist.github.com/xxxxxxxxxxxxxxxxxxxxxxxxx
---
```

这个信息非常重要。

它告诉插件：

> 当前 Obsidian Note 对应 GitHub 上的哪个 Gist。

因此：

**不要随意删除 `gists` Property。**

------------------------------------------------------------------------

# 3. GitHub Token 配置

## 3.1 为什么需要 Token

Obsidian 插件需要通过 GitHub API 创建和更新 Gist。

GitHub API 对 Gist 的创建和修改需要身份验证。

因此必须配置 Personal Access Token。

------------------------------------------------------------------------

# 4. 创建 GitHub Token

进入 GitHub：

https://github.com/settings/tokens

推荐使用：

## Fine-grained Personal Access Token

需要允许：

``` text
Gists
    Read and write
```

如果使用 Classic Personal Access Token，则只需要：

``` text
gist
```

权限。

### 安全注意

不要：

-   把 Token 写进 README
-   把 Token 放进 Markdown Note
-   把 Token 上传到 Gist
-   把 Token 提交到 Git Repository
-   把 Token 发给其他人

Token 相当于访问 GitHub API 的密码。

------------------------------------------------------------------------

# 5. Obsidian 插件配置

进入：

``` text
Obsidian
    → Settings
    → Community plugins
    → Share as Gist
```

然后找到：

``` text
Personal access token
```

把 GitHub Token 填进去。

------------------------------------------------------------------------

# 6. 推荐配置

推荐使用以下设置：

``` text
Enable updating Gists after creation
    ON

Include front matter in gists
    OFF

Enable auto-saving Gists after edit
    ON

Enable auto-save notice
    ON / OFF 均可

Include table of contents
    OFF
```

## 6.1 Enable updating Gists after creation

``` text
ON
```

作用：

允许插件更新已经创建的 Gist。

建议打开。

------------------------------------------------------------------------

## 6.2 Include front matter in gists

``` text
OFF
```

作用：

控制 Obsidian 的 front matter / properties 是否上传到 Gist。

推荐关闭。

注意：

``` text
OFF
```

并不代表删除 Obsidian 本地的 Properties。

例如本地仍然可能存在：

``` yaml
---
gists:
  - id: xxxxx
    url: https://gist.github.com/xxxxx
---
```

这些信息仍然用于建立 Obsidian Note 与 Gist 的关联。

------------------------------------------------------------------------

## 6.3 Enable auto-saving Gists after edit

``` text
ON
```

作用：

修改已经关联 Gist 的 Obsidian Note 后，自动更新 GitHub Gist。

推荐打开。

例如：

``` text
Obsidian Note
      ↓
修改内容
      ↓
保存
      ↓
插件自动更新
      ↓
GitHub Gist
```

------------------------------------------------------------------------

## 6.4 Enable auto-save notice

``` text
ON
```

建议打开。

这样自动保存 Gist 时可以看到通知。

如果觉得通知太多，可以关闭。

------------------------------------------------------------------------

## 6.5 Include table of contents

``` text
OFF
```

如果不需要插件自动生成目录，保持关闭。

------------------------------------------------------------------------

# 7. 第一次上传 Note

打开需要上传的 Markdown Note。

例如：

``` text
ubuntu install tools.md
```

然后：

``` text
Ctrl + P
```

输入：

``` text
gist
```

选择插件提供的：

``` text
Share as public gist on GitHub.com
```

或者：

``` text
Share as secret gist on GitHub.com
```

根据需要选择。

------------------------------------------------------------------------

# 8. Public Gist 和 Secret Gist

GitHub Gist 有两种主要可见性：

``` text
Public
Secret
```

## Public

公开 Gist：

-   可以被其他人发现
-   可以被搜索
-   适合公开技术笔记
-   适合分享代码

## Secret

Secret Gist：

-   不会出现在公开 Gist 列表中
-   但是知道 URL 的人仍然可以访问
-   因此它不是严格意义上的私有存储

如果内容真的敏感，不应该依赖 Secret Gist。

应该使用：

``` text
Private GitHub Repository
```

------------------------------------------------------------------------

# 9. 第一次上传成功后的状态

上传成功后，GitHub 页面会出现类似：

``` text
Gist_Public / ubuntu install tools
```

Obsidian Note 中会出现类似：

``` yaml
gists:
  - id: d642d78d5f946adab5bfaa86534bde
    url: https://gist.github.com/...
```

这表示：

``` text
上传成功
+
Gist 已创建
+
Obsidian Note 已与 Gist 建立关联
```

------------------------------------------------------------------------

# 10. 修改 Note 后自动同步

例如原来的 Note：

``` markdown
# ubuntu install tools

```bash
sudo apt install batcat
```


    修改成：

    ```markdown
    # ubuntu install tools

    ```bash
    sudo apt install batcat
    sudo apt install tree


    如果：

    ```text
    Enable auto-saving Gists after edit = ON

插件会自动更新对应的 GitHub Gist。

------------------------------------------------------------------------

# 11. 如何确认同步成功

打开对应 GitHub Gist 页面。

刷新：

``` text
Ctrl + R
```

检查内容是否已经变化。

如果 GitHub Gist 内容已经更新：

``` text
Obsidian → GitHub Gist
```

同步正常。

------------------------------------------------------------------------

# 12. 手动同步

如果自动同步没有立即发生，可以：

``` text
Ctrl + P
```

搜索：

``` text
gist
```

查看插件提供的更新 / 保存相关命令。

可以使用对应的 Update / Save Gist 命令手动同步。

------------------------------------------------------------------------

# 13. 最重要的 Property：gists

上传成功后不要随便删除：

``` yaml
gists:
```

例如：

``` yaml
---
gists:
  - id: xxxxxxxxx
    url: https://gist.github.com/xxxxxxxxx
---
```

它相当于：

``` text
Obsidian Note
      |
      +---- Gist ID
      |
      +---- Gist URL
```

如果删除这个关联信息，插件可能无法知道当前 Note 对应哪个 Gist。

------------------------------------------------------------------------

# 14. 推荐的使用方式

建议把 Obsidian 当作：

``` text
本地知识库
```

把 GitHub Gist 当作：

``` text
在线技术笔记 / 分享页面
```

例如：

``` text
Obsidian
├── C++
│   ├── move-semantics.md
│   ├── perfect-forwarding.md
│   └── coroutine.md
│
├── Linux
│   ├── ubuntu-install-tools.md
│   ├── adb.md
│   └── ssh.md
│
├── AOSP
│   ├── sepolicy.md
│   ├── android-build.md
│   └── git.md
│
└── Git
    ├── github-cli.md
    └── gist.md
```

需要公开分享的 Note，再通过 Gist 上传。

不建议把所有 Obsidian Note 都自动公开。

------------------------------------------------------------------------

# 15. 推荐的命名方式

建议文件名直接使用英文技术名称：

``` text
ubuntu-install-tools.md
adb-wifi.md
git-cherry-pick.md
cpp-move-semantics.md
cpp-perfect-forwarding.md
aosp-sepolicy.md
aosp-build.md
linux-smb.md
```

这样 GitHub Gist 页面和 Raw URL 更容易使用。

------------------------------------------------------------------------

# 16. Gist 的版本历史

GitHub Gist 本质上是 Git Repository。

因此 Gist 可以查看修改历史和 Diff。

例如：

``` text
Version 1
    ↓
Version 2
    ↓
Version 3
```

可以用来查看 Note 的历史修改。

因此 Gist 很适合保存：

-   C++ 示例
-   Linux 命令
-   AOSP 笔记
-   Shell 脚本
-   配置文件
-   技术 Cheat Sheet

------------------------------------------------------------------------

# 17. 不要把 Gist 当作完整备份

Gist 很方便，但不建议把它当成整个 Obsidian Vault 的唯一备份。

推荐：

``` text
Obsidian Vault
       |
       +---- 本地备份
       |
       +---- Git Repository / GitHub
       |
       +---- Gist（用于分享特定 Note）
```

Gist 更适合：

``` text
分享单个技术 Note
```

而 Git Repository 更适合：

``` text
完整 Obsidian Vault
```

------------------------------------------------------------------------

# 18. 常见问题

## 18.1 Token 无法使用

检查：

``` text
Token 是否过期
```

以及权限：

``` text
Fine-grained Token
    Gists → Read and write
```

Classic Token：

``` text
gist
```

------------------------------------------------------------------------

## 18.2 上传成功，但是修改后没有更新

检查：

``` text
Enable updating Gists after creation
    ON

Enable auto-saving Gists after edit
    ON
```

然后确认 Note 中仍然存在：

``` text
gists
```

Property。

------------------------------------------------------------------------

## 18.3 Gist 页面没有变化

先：

``` text
Ctrl + R
```

刷新 GitHub 页面。

如果仍然没有变化：

``` text
Obsidian
→ Ctrl + P
→ 搜索 gist
→ 执行 Update / Save Gist
```

------------------------------------------------------------------------

## 18.4 删除了 gists Property

如果已经删除：

``` yaml
gists:
```

插件可能无法继续识别当前 Note 对应的 Gist。

可以重新执行 Share as Gist。

------------------------------------------------------------------------

## 18.5 Secret Gist 是否真正私密？

不是。

Secret Gist：

``` text
不公开展示
≠
真正私有
```

只要别人拿到了 URL，就可以访问。

真正敏感的信息应该放在：

``` text
Private GitHub Repository
```

------------------------------------------------------------------------

# 19. 推荐工作流

我的推荐工作流：

``` text
                ┌─────────────────┐
                │     Obsidian    │
                │  本地 Markdown   │
                └────────┬────────┘
                         │
                         │ 写作 / 修改
                         ▼
                ┌─────────────────┐
                │  Enable Auto    │
                │     Saving      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   GitHub Gist   │
                └─────────────────┘
                         │
                         ▼
                    分享 / 查看
```

第一次：

``` text
创建 Note
   ↓
Ctrl + P
   ↓
Share as Gist
```

以后：

``` text
修改 Note
   ↓
保存
   ↓
自动更新 Gist
```

------------------------------------------------------------------------

# 20. 最终配置 Checklist

``` text
[✓] GitHub Account
[✓] GitHub Token
[✓] Gists Read/Write permission
[✓] Obsidian Share as Gist plugin
[✓] Personal access token 已填写

[✓] Enable updating Gists after creation
[✓] Enable auto-saving Gists after edit

[ ] Include front matter in gists
    推荐 OFF

[ ] Include table of contents
    推荐 OFF
```

------------------------------------------------------------------------

# 21. GitHub 官方资料

GitHub Gist 官方文档：

https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists

GitHub Gist 创建说明：

https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists

GitHub Gist REST API：

https://docs.github.com/en/rest/gists/gists

------------------------------------------------------------------------

# 22. 一句话总结

``` text
Obsidian = 本地编辑和管理 Markdown

GitHub Gist = 在线保存、版本历史和分享

gists Property = Obsidian Note 与 Gist 之间的关联

Auto-saving = 修改 Obsidian 后自动更新 Gist
```

最重要的配置：

``` text
Token
  ↓
Gists Read/Write
  ↓
Enable updating Gists = ON
  ↓
Enable auto-saving = ON
  ↓
第一次 Share as Gist
  ↓
以后自动同步
```
