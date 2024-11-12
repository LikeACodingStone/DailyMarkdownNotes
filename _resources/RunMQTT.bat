@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("%~nx0 h",0)(window.close)&&exit
:begin
d:
cd D:\hgt-platform_vs2015\foundation\x86-win32\mosquitto-1.6.2\bin
mosquitto.exe -c mosquitto.conf