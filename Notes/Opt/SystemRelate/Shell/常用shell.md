
```
sudo alien jdk-18_linux-x64_bin.rpm 		//解压已经安装过的rpm文件，生成deb文件
rpm -ivh jdk-18_linux-x64_bin.rpm  		//解压并安装未安装的rpm文件
```

```
 apt-get --purge remove adb //卸载程序adb
 Apt-cache search setuptools		// ubuntu 搜索安装包
```

```
sudo usermod -aG vboxsf $(whoami)  // virtualBox 共享目录权限问题
```

```
qmake -project -t lib 		//指定生成lib库
```

```
arecord -l  			//查看linux麦克风设备{card 0或者card 1或者类似}
alsamixer -c 0 		//查看声卡0的混音器
```