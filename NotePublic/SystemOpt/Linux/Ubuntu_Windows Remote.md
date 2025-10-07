### Ubuntu Desktop

| 层级  | 默认 Ubuntu | 你切换后的方案 |
| --- | --- | --- |
| **桌面环境** | GNOME | MATE |
| **显示协议** | Wayland （或 Xorg 可选） | Xorg |

### 修改文件

```
sudo apt update
sudo apt install mate-core mate-desktop-environment mate-desktop-environment-extras -y

sudo apt install xrdp -y
/etc/xrdp/startwm.sh 
/etc/gdm3/custom.conf
echo "mate-session" > ~/.xsession
chmod +x ~/.xsession
sudo systemctl restart xrdp

// firefox access
echo "export XAUTHORITY=$HOME/.Xauthority" >> ~/.Xauthority  
```