
* scp 自动登录传输 第一个参数接文件
```
#!/usr/bin/expect
set timeout 30
set file [lindex $argv 0]

spawn scp -r $file root@10.28.188.10:/HGT/AWS4800

expect -re "password:" { send "hgt\r" }
expect eof

```