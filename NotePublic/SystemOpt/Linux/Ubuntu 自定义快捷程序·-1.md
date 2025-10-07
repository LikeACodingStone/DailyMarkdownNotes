`
https://blog.csdn.net/u010329292/article/details/128755379
`
- 定义 process.desktop文件
```
[Desktop Entry]
Version=1.0
Name=boschVPN
Comment=connect to bosch with zhs2yh
Exec=sh /home/taj4yh/user/bin/VPNFiles/connectVpn.sh
Icon=/home/taj4yh/user/bin/VPNFiles/boschIcon.png
Terminal=true
Type=Application
Categories=Utility;
```
- 定义 connectVpn.sh
```
rm ~/.gitconfig
cp gitconfig/.gitconfig-bosch ~/.gitconfig

sudo openconnect --protocol=anyconnect --useragent=AnyConnect -u zhs2yh  rasvpn-ext-emea.bosch.com/rbextssl
```

### 拷贝process.desktop 到 ~/.local/share/applications/路径下面刷新
`
update-desktop-database ~/.local/share/applications
`

