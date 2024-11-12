# ftp 上传丢失解决
- 进入ftp以后首先输入 bin 进入二进制模式，然后再上传 

***
- get file  下载 
- put file  上传
- lcd  相当于cd
***

# Win10开启FTP
- 1.控制面板>程序>启用或关闭Windows功能>…
(控制面板可在 桌面右键>个性化>主题>桌面图标设置>勾选控制面板>确定)
![5d09c1a4e284638b7fff8ed36178f9b1.png](../../../../_resources/5d09c1a4e284638b7fff8ed36178f9b1.png)
- 2.小娜搜索IIS打开IIS
- ![de664e1479ab5b00b0a6c3f647de7717.png](../../../../_resources/de664e1479ab5b00b0a6c3f647de7717.png)
- 3.右击网站添加FTP站点
- ![25d0fa40dd3805ba2ba96093caa55ac4.png](../../../../_resources/25d0fa40dd3805ba2ba96093caa55ac4.png)
- 4.输入站点名称和作为FTP的目录
- ![962fd885e8553f3f529108aa050dbe7b.png](../../../../_resources/962fd885e8553f3f529108aa050dbe7b.png)
- 5.IP地址填FTP本机IP，选择无SSL
- ![e836c58af2649128f6b85dbd96de82d2.png](../../../../_resources/e836c58af2649128f6b85dbd96de82d2.png)
- 6.根据需要选择身份验证，授权与权限
- ![646a2a8c91fc583b8f224fd766e80884.png](../../../../_resources/646a2a8c91fc583b8f224fd766e80884.png)
- 7.控制面板>系统和安全>防火墙>允许应用或功能通过Window防火墙>...
- ![e36312b2c4c467b8f14aea9e9b0e16e9.png](../../../../_resources/e36312b2c4c467b8f14aea9e9b0e16e9.png)
- 8.点击更改设置，勾选FTP服务器&专用&公用
- ![9b67bd172608cffa6b96011f78767e20.png](../../../../_resources/9b67bd172608cffa6b96011f78767e20.png)
- 9.点击允许其它应用,选择C:\Windows\System32\svchost.exe然后添加，最后确定。
- ![50308838a15b6866a759a81aff55ad1d.png](../../../../_resources/50308838a15b6866a759a81aff55ad1d.png)
- 10.文件访问ftp:// IP 试试吧！
- ![a9c477f7d06c8af3bb31541116443d75.png](../../../../_resources/a9c477f7d06c8af3bb31541116443d75.png)