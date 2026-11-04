---
tags: [windows, psexec, remote, bat]
updated: 2026-11-04
---
# IPC Remote Launch with PsExec [IPC 远程启动程序]

> [!summary] Summary [概要]
> One `.bat` that starts **Kensabu.exe** on the remote IPC `AOIJ0-S0-IPC0` (visible on its desktop), then restarts the local **Tool.exe**.
> [一个 `.bat`：在远程 IPC `AOIJ0-S0-IPC0` 上启动 **Kensabu.exe**（显示在对方桌面上），然后重启本机的 **Tool.exe**。]

## Script [脚本]

```bat
@echo off

REM 1. Start Kensabu on remote IPC, in user session 2 [在远程 IPC 的第 2 个会话中启动 Kensabu]
start psexec -d \\AOIJ0-S0-IPC0 -u aoi -p kgk -i 2 C:\IPC-V22\Debug\Kensabu.exe

REM 2. Restart local utility [重启本机工具]
taskkill /F /IM Tool.exe /T
start C:\Theme\OCAM\V22-Tools\Debug\Tool.exe
```

## PsExec options [参数说明]

| Option [参数] | Meaning [含义] |
|---|---|
| `-d` | Don't wait for the program to exit [不等待程序结束] |
| `\\AOIJ0-S0-IPC0` | Remote computer [远程电脑] |
| `-u aoi -p kgk` | Remote user / password [远程用户名 / 密码] |
| `-i 2` | Show the window in **session ID 2** (the logged-in desktop) [在**会话 ID 2**（已登录的桌面）中显示窗口] |

> [!tip] Find the correct session ID [查找正确的会话 ID]
> If the window doesn't appear on the remote screen, the session ID is wrong. Check it: [如果远程屏幕上看不到窗口，说明会话 ID 不对。查看方法：]
> ```bat
> query user                         REM on the remote PC [在远程电脑上执行]
> query user /server:AOIJ0-S0-IPC0   REM from this PC [在本机查询远程]
> ```
> Use the number in the `ID` column for `-i`. [把 `ID` 列的数字填到 `-i` 后面。]
