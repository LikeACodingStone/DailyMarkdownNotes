- CTRL + SHIFT + T 终端垂直多开
- CTRL + PgUp 或者 CTRL + PgDn 切换
***

- 安装Buildozer python for android
```
sudo apt install python3-pip
pip3 install --user --upgrade buildozer
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
sudo apt update
sudo apt install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
pip3 install --user --upgrade Cython==0.29.19 virtualenv		//也可以自行安装cython
buildozer -v android debug					// 下载android NDK

```

- Ubuntu 设置只启动终端命令
` 
ubuntu static ip set must check dhcp dns and set the same dns for static
`