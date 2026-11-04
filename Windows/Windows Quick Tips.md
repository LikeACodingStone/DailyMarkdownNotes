---
tags: [windows, tips]
updated: 2026-11-04
---
# Windows Quick Tips

> [!summary] Contents
> 1. Keyboard shortcut to launch a program
> 2. Microsoft Pinyin candidates not showing
> 3. Roll back after a bad update

---

## 1. Keyboard Shortcut to Launch a Program

**Right-click the shortcut → Properties → Shortcut tab → Shortcut key** → press your key combo (e.g. `Ctrl + Alt + T`).

> [!tip] Must be a shortcut on the Desktop or Start Menu
> Doesn't work on the `.exe` itself.

---

## 2. Microsoft Pinyin Candidates Not Showing

1. Right-click the IME icon in the taskbar → **Settings**
2. **General** → scroll to the bottom → **Compatibility**
3. Turn on **Use previous version of Microsoft Pinyin**
4. Restart `explorer.exe` (Task Manager → Windows Explorer → Restart)

> [!success] Confirmed working

---

## 3. Roll Back After a Bad Update

| System | Path |
|---|---|
| Win11 | Settings → System → Recovery → **Go back** |
| Win10 | Settings → Update & Security → Recovery → **Go back to the previous version** |

> [!warning] Only within 10 days
> After that, Windows deletes the old version (`Windows.old`) and the button disappears.
