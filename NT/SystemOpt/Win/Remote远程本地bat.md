```
ECHO OFF

start psexec -d \\AOIJ0-S0-IPC0 -u aoi -p kgk -i 2 C:\IPC-V22\Debug\Kensabu.exe

REM start utility
taskkill /F /IM Tool.exe /T
start C:\Theme\OCAM\V22-Tools\Debug\Tool.exe

cmd
query user //查看user ID

```