### Ubuntu Desktop
#### 不接显示器得情况推荐Xorg+MATE

| 层级  | 默认 Ubuntu | 你切换后的方案 |
| --- | --- | --- |
| **桌面环境** | GNOME | MATE |
| **显示协议** | Wayland （或 Xorg 可选） | Xorg |

### 修改文件

```
sudo apt update
sudo apt install mate-core mate-desktop-environment mate-desktop-environment-extras -y
sudo apt install xrdp -y
```
- vi /etc/xrdp/startwm.sh
```
#!/bin/sh
if [ -r /etc/default/locale ]; then
  . /etc/default/locale
  export LANG LANGUAGE
fi
export XDG_SESSION_TYPE=x11
exec mate-session
````
- vi /etc/gdm3/custom.conf
`
WaylandEnable=false
`
```
echo "mate-session" > ~/.xsession
chmod +x ~/.xsession
sudo systemctl restart xrdp

// firefox access
echo "export XAUTHORITY=$HOME/.Xauthority" >> ~/.Xauthority  
```

### 远程remote出现异常得时候可以重启service
```
sudo systemctl restart xrdp
sudo systemctl restart gdm3
```