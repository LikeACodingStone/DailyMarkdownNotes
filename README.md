# 笔记导航

按主题找笔记；不知道放哪里时，先放 Inbox。Git 保存历史，Gist 分享选定笔记。

<!-- BEGIN AUTO NAVIGATION -->

## Linux

- [Ubuntu Android Waydroid & ReDroid](Linux/Ubuntu%20Android%20Waydroid%20&%20ReDroid.md)
- [Ubuntu Chinese Locale & Input](Linux/Ubuntu%20Chinese%20Locale%20&%20Input.md)
- [Ubuntu Disk, Mount & LVM](Linux/Ubuntu%20Disk,%20Mount%20&%20LVM.md)
- [Ubuntu KVM Virtual Machines](Linux/Ubuntu%20KVM%20Virtual%20Machines.md)
- [Ubuntu Network](Linux/Ubuntu%20Network.md)
- [Ubuntu Packages](Linux/Ubuntu%20Packages.md)
- [Ubuntu Shell Cheat Sheet](Linux/Ubuntu%20Shell%20Cheat%20Sheet.md)
- [Ubuntu System Tweaks](Linux/Ubuntu%20System%20Tweaks.md)
- [Ubuntu Users, Permissions & Delete Protection](Linux/Ubuntu%20Users,%20Permissions%20&%20Delete%20Protection.md)
- [Ubuntu VPN & Custom Launchers](Linux/Ubuntu%20VPN%20&%20Custom%20Launchers.md)
- [Ubuntu xrdp MATE Remote Desktop](Linux/Ubuntu%20xrdp%20MATE%20Remote%20Desktop.md)
- [Ubuntu-quick-search](Linux/Ubuntu-quick-search.md)

## Windows

- [IPC Remote Launch with PsExec](Windows/IPC%20Remote%20Launch%20with%20PsExec.md)
- [Microsoft Teams Fix](Windows/Microsoft%20Teams%20Fix.md)
- [ThinkPad USB Ports All Dead](Windows/ThinkPad%20USB%20Ports%20All%20Dead.md)
- [Windows Accounts & Permissions](Windows/Windows%20Accounts%20&%20Permissions.md)
- [Windows Quick Tips](Windows/Windows%20Quick%20Tips.md)

## Git_Repo

- [Git-change-previous-commit-message](Git_Repo/Git-change-previous-commit-message.md)
- [git-cmd-summary](Git_Repo/git-cmd-summary.md)
- [git-config-two-account](Git_Repo/git-config-two-account.md)
- [git-hooks-related](Git_Repo/git-hooks-related.md)
- [git-reset-user-name](Git_Repo/git-reset-user-name.md)
- [repo-cmd-summary](Git_Repo/repo-cmd-summary.md)
- [repo-usually-error-case](Git_Repo/repo-usually-error-case.md)

## Android

- [adb](Android/adb.md)
- [Android Studio](Android/Android%20Studio.md)
- [Android-Studio Gradle](Android/Android-Studio%20Gradle.md)
- [aosp task](Android/aosp%20task.md)
- [windows adb识别异常处理](Android/windows%20adb%E8%AF%86%E5%88%AB%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86.md)

## Programming

- [Building QJson on Windows](Programming/Building%20QJson%20on%20Windows.md)
- [C++, gcc & Java Notes](Programming/C++,%20gcc%20&%20Java%20Notes.md)
- [Python Setup & PyInstaller](Programming/Python%20Setup%20&%20PyInstaller.md)
- [Qt Basics](Programming/Qt%20Basics.md)
- [Qt Tips & Pitfalls](Programming/Qt%20Tips%20&%20Pitfalls.md)

## Tools

- [Beyond Compare](Tools/Beyond%20Compare.md)
- [Docker Work Setup](Tools/Docker%20Work%20Setup.md)
- [File Sharing Samba FTP FileBrowser](Tools/File%20Sharing%20Samba%20FTP%20FileBrowser.md)
- [MQTT Mosquitto](Tools/MQTT%20Mosquitto.md)
- [README-Obsidian-GitHub-Gist](Tools/README-Obsidian-GitHub-Gist.md)
- [Tools Quick Tips](Tools/Tools%20Quick%20Tips.md)
- [UEFI NVRAM Full](Tools/UEFI%20NVRAM%20Full.md)
- [Visual Studio Build Errors](Tools/Visual%20Studio%20Build%20Errors.md)
- [Visual Studio Setup & Debug](Tools/Visual%20Studio%20Setup%20&%20Debug.md)
- [VMware Fixes](Tools/VMware%20Fixes.md)
- [VS Code Setup](Tools/VS%20Code%20Setup.md)

## Japanese

- [202602](Japanese/202602.md)
- [202603](Japanese/202603.md)
- [N3_Grammer](Japanese/N3_Grammer.md)

## AI

- [AMD AI搭建](AI/AMD%20AI%E6%90%AD%E5%BB%BA.md)
- [Ubuntu24.04 搭建AMD GPU工具链](AI/Ubuntu24.04%20%E6%90%AD%E5%BB%BAAMD%20GPU%E5%B7%A5%E5%85%B7%E9%93%BE.md)

## Inbox

- [anki_fsrs_optimization_guide](Inbox/anki_fsrs_optimization_guide.md)
- [Ankidroid](Inbox/Ankidroid.md)
- [Kindle_PW4_Jailbreak_KOReader](Inbox/Kindle_PW4_Jailbreak_KOReader.md)
- [Obsidian settings](Inbox/Obsidian%20settings.md)
- [Obsidian+git+gist](Inbox/Obsidian+git+gist.md)
- [RepoNote_Android_GitHub_Setup](Inbox/RepoNote_Android_GitHub_Setup.md)
- [VSCODE_Plugins](Inbox/VSCODE_Plugins.md)
- [Windows_Develop_ToolList](Inbox/Windows_Develop_ToolList.md)
- [Windows_Plugins](Inbox/Windows_Plugins.md)

<!-- END AUTO NAVIGATION -->

## 工作记录

工作记录位于 `ZTokyoBigsiteLogs`，不纳入本页自动导航。

## 使用方法

1. 搜索关键词，找到已有笔记就补充。
2. 新问题放入对应主题目录，文件名写清楚问题。
3. 不确定分类时放入 Inbox。
4. 在本地编辑，Git 保存历史；需要分享时更新对应 Gist。

移动清单和原有缺失链接见 `classification-moves.json`。


## 更新导航

新增、移动或删除笔记后，在 `DailyMarkdownNotes` 目录运行：

```bash
python3 scripts/update_readme.py
```

脚本只更新自动导航标记之间的内容，其余文字保留。扫描主题目录及子目录，排除附件、隐藏目录和 Git 忽略的笔记。添加新的主题目录时，修改脚本中的 `TOPICS`。
