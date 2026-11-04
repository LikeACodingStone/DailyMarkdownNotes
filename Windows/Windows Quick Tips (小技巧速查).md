---
tags: [windows, tips]
updated: 2026-11-04
---
# Windows Quick Tips [小技巧速查]

> [!summary] Contents [目录]
> 1. Keyboard shortcut to launch a program [设置快捷键启动程序]
> 2. Microsoft Pinyin candidates not showing [微软拼音不显示候选词]
> 3. Roll back after a bad update [更新后出问题，回退版本]

---

## 1. Keyboard Shortcut to Launch a Program [设置快捷键启动程序]

**Right-click the shortcut → Properties → Shortcut tab → Shortcut key** → press your key combo (e.g. `Ctrl + Alt + T`).
[**右键快捷方式 → 属性 → 快捷方式 → 快捷键** → 按下组合键。]

> [!tip] Must be a shortcut on the Desktop or Start Menu [必须是桌面或开始菜单中的快捷方式]
> Doesn't work on the `.exe` itself. [直接对 `.exe` 设置无效。]

---

## 2. Microsoft Pinyin Candidates Not Showing [微软拼音不显示候选词]

1. Right-click the IME icon in the taskbar → **Settings** [右键任务栏输入法图标 → **设置**]
2. **General** → scroll to the bottom → **Compatibility** [**常规** → 拉到最下方 → **兼容性**]
3. Turn on **Use previous version of Microsoft Pinyin** [开启 **使用以前版本的微软拼音输入法**]
4. Restart `explorer.exe` (Task Manager → Windows Explorer → Restart) [重启资源管理器（任务管理器 → Windows 资源管理器 → 重新启动）]

> [!success] Confirmed working [实测有效]

---

## 3. Roll Back After a Bad Update [更新后出问题，回退版本]

| System [系统] | Path [路径] |
|---|---|
| Win11 | Settings → System → Recovery → **Go back** [设置 → 系统 → 恢复 → **返回**] |
| Win10 | Settings → Update & Security → Recovery → **Go back to the previous version** [设置 → 更新和安全 → 恢复 → **回退到以前的版本**] |

> [!warning] Only within 10 days [只能在 10 天内回退]
> After that, Windows deletes the old version (`Windows.old`) and the button disappears.
> [超过 10 天系统会删除旧版本（`Windows.old`），回退按钮消失。]
