---
tags: [windows, psexec, remote, bat]
updated: 2026-11-04
---
# IPC Remote Launch with PsExec

> [!summary] Summary
> One `.bat` that starts **Kensabu.exe** on the remote IPC `AOIJ0-S0-IPC0` (visible on its desktop), then restarts the local **Tool.exe**.

## Script

```bat
@echo off

REM 1. Start Kensabu on remote IPC, in user session 2
start psexec -d \\AOIJ0-S0-IPC0 -u aoi -p kgk -i 2 C:\IPC-V22\Debug\Kensabu.exe

REM 2. Restart local utility
taskkill /F /IM Tool.exe /T
start C:\Theme\OCAM\V22-Tools\Debug\Tool.exe
```

## PsExec options

| Option | Meaning |
|---|---|
| `-d` | Don't wait for the program to exit |
| `\\AOIJ0-S0-IPC0` | Remote computer |
| `-u aoi -p kgk` | Remote user / password |
| `-i 2` | Show the window in **session ID 2** (the logged-in desktop) |

> [!tip] Find the correct session ID
> If the window doesn't appear on the remote screen, the session ID is wrong. Check it:
> ```bat
> query user                         REM on the remote PC
> query user /server:AOIJ0-S0-IPC0   REM from this PC
> ```
> Use the number in the `ID` column for `-i`.
