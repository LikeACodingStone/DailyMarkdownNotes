
* windows adb设别遵循以下步骤测试
	- 安装android_winusb.inf ，位于usb_driver内，右键安装即可
	- 安装adb，并且添加至环境变量
	- 重启电脑，禁用驱动程序强制签名  F7
	- 开启两个服务 service.msc里面的（名字忘记了)
	- 如果adb设备无法登入，就删除.android文件夹下面的adbkey 和 adbkey.pub