## 安装

#### 1.添加 Waydroid 官方仓库

```
# 1. 安装必要的工具
sudo apt update
sudo apt install -y curl ca-certificates

# 2. 导入 Waydroid 仓库 GPG 密钥
curl -s https://repo.waydro.id/waydroid.gpg | sudo tee /usr/share/keyrings/waydroid.gpg > /dev/null

# 3. 添加 Waydroid 仓库到 sources.list.d (使用 noble 代号)
echo "deb [signed-by=/usr/share/keyrings/waydroid.gpg] https://repo.waydro.id/ noble main" | sudo tee /etc/apt/sources.list.d/waydroid.list

# 4. 更新 APT 缓存
sudo apt update
```

#### 2.安装 Waydroid 和 Weston

```
# 1. 安装 Waydroid 主程序
sudo apt install -y waydroid

# 2. 安装 Weston（作为嵌套的 Wayland 合成器）
# 如果您的 MATE 桌面还没有安装，现在安装
sudo apt install -y weston
```

#### 3\. 初始化 Waydroid 容器

```
# 运行初始化命令
sudo waydroid init

# 提示：如果您需要 Google Play 服务 (GApps)，请改用以下命令：
# sudo waydroid init -s GAPPS
```

#### 4\. 启用 Waydroid 服务

```
sudo systemctl enable waydroid-container.service
sudo systemctl start waydroid-container.service
```

* * *

### 启动

```
# 启动 Weston
weston

//在启动weston得命令行窗口内部
waydroid show-full-ui
```

### 关闭

```
sudo systemctl stop waydroid-container.service
waydroid session stop
```

* * *

### 从weston切换到cage

```
sudo apt install cage
cage waydroid show-full-ui
```

* * *

### Weston属性设置

```
sudo waydroid prop set persist.waydroid.width 1920
sudo waydroid prop set persist.waydroid.height 1080
```
****
### 注册
```
sudo waydroid shell
```
- 生成设备ID并且复制出来
```
ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"
```
[Android设备注册网址](https://www.google.com/android/uncertified)
- 最后重启Waydroid

### 分辨率更改
#### 在cage把系统完全启动以后设置，一定不要加 sudo
```
waydroid prop set persist.waydroid.width 720
waydroid prop set persist.waydroid.height 720
waydroid prop set persist.waydroid.dpi 320
```
***
### 如果weston挂了，可以切换到cage, cage网络不会随着窗口大小断开
***
### 启动脚本
```
sudo systemctl start waydroid-container.service
cage waydroid show-full-ui
```
### 停止脚本
```
sudo systemctl stop waydroid-container 
waydroid session stop
sudo systemctl stop waydroid-container.service
```