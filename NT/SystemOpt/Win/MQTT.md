
- mqtt服务器无法启动时候，手动用命令 mosquitto.exe -c mosquitto.conf 进行启动

- 为了方便将mqtt加入开机启动
- 将RunMQTT.bat（附件）更改成实际mosquitto.exe的路径，然后复制到
`
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup		
`
- 注意"Administrator" 有时候可能要换成其他实际用户名


[RunMQTT.bat](../../../_resources/RunMQTT.bat)

*** 
**Mqtt Server 启动后无法连接**
-  修改 mosquitto.conf 
```
设置匿名访问
allow_anonymous true
3.配置端口号
listener 1883 0.0.0.0
```
- 重启服务