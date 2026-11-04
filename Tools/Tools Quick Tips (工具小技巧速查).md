---
tags: [tools, tips, jdk, chrome, audacity, word]
updated: 2026-11-04
---
# Tools Quick Tips [工具小技巧速查]

> [!summary] Contents [目录]
> 1. JDK install pitfall + download links [JDK 安装注意与下载]
> 2. Chrome can't get online [Chrome 无法上网]
> 3. Audacity "another copy is running" [Audacity 提示已有另一个实例在运行]
> 4. Word: can't add a next page [Word 无法添加下一页]

---

## 1. JDK [JDK 安装注意]

> [!warning] Install the JDK and the JRE in **different** folders [JDK 和 JRE 必须装在**不同**目录]
> The (older) installer asks for two paths: first the JDK, then the JRE. If both are the same, the JRE **overwrites** the JDK's files, and afterwards `tools.jar` and `dt.jar` are missing.
> [（旧版）安装程序会让你选两次路径：先 JDK，再 JRE。如果两个路径相同，JRE 会**覆盖** JDK 的内容，装完就找不到 `tools.jar` 和 `dt.jar`。]
>
> Mostly an old-installer problem (JDK 8 and earlier). [主要是旧版安装程序的问题（JDK 8 及更早）。]

**Archive downloads [历史版本下载]** (an Oracle account is needed [需要 Oracle 账号登录]):

| Version | Link |
|---|---|
| JDK 1.8 | https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html |
| JDK 1.7 | https://www.oracle.com/java/technologies/javase/javase7-archive-downloads.html |
| JDK 1.6 | https://www.oracle.com/java/technologies/javase-java-archive-javase6-downloads.html |

---

## 2. Chrome Can't Get Online [Chrome 无法上网]

1. Search for **proxy** in Windows and turn the proxy **off** [搜索"代理"，关闭代理]
2. Control Panel → **Internet Options → Content → Clear SSL state** [控制面板 → Internet 属性 → 内容 → 清除 SSL 状态]

---

## 3. Audacity: "Another copy of Audacity is running" [Audacity 已有另一个实例]

> [!bug] Message [提示]
> `The system has detected that another copy of Audacity is running`

**Fix [解决]:** delete the Audacity lock file in `/var/tmp`. [删除 `/var/tmp` 里的 lock 文件。]

```bash
ls -la /var/tmp        # find the lock file [找到 lock 文件]
```

---

## 4. Word: Can't Add a Next Page [Word 无法添加下一页]

> [!bug] Problem [问题]
> In a template-based document you can't add a next page. [基于模板的文档无法添加下一页。]

1. `Ctrl + A` to select the whole page [选中整页]
2. `Ctrl + End` to move the cursor to the end [光标移动到末尾]
3. **Insert → Blank Page** [插入 → 空白页]
