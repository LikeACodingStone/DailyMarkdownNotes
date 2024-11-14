
* **adb push libxxx.so /system/libs**  
	- 出现错误 failed to copy 'libxxx.so' to '/system/lib/libxxx.so': Read-only file system
	- 首先adb remount
	- adb shell 然后
	- 将system 和lib文件夹的读写模式改掉， chmod 777 system
