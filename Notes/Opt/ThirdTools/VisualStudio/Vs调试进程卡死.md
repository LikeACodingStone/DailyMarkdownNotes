- VS调试过程中出现进程卡死，停止运行后依旧卡死
- 在后台任务管理器也找不到工程的进程名字。
# 使用一下方法强制关闭
- 打开CMD窗口输入
- tasklist | findstr  "HGT*"	（HGT是进程关键字）
- ![3859a1df9a2c2c90980b147b15cfbbf2.png](../../../../_resources/3859a1df9a2c2c90980b147b15cfbbf2.png)
- taskkill /PID 1208 -f -t
- ![5ef8b1b4bb662500dce9b036b50f9b2f.png](../../../../_resources/5ef8b1b4bb662500dce9b036b50f9b2f.png)
- 这个时候把PID改成 6520
- taskkill /PID 6520 -f -t
- 同样 taskkill /PID 11032 -f -t
***

# 以上方法不成功，也有可能USB口被锁定，考虑重新插拔USB口外设