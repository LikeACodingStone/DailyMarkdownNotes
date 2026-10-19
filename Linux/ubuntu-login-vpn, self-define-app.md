
- vpn_auto_login.py
	-  [vpn_auto_login](https://gist.github.com/LikeACodingStone/9d6d57b31ed273c12de439340a9ca91a)
- run_vpn.sh
```bash
#!/bin/bash
# 定义你的 Ubuntu 系统 sudo 密码
SYS_PASS="xxxx"
# 获取当前脚本所在的绝对路径，确保能找到同目录下的 vpn_login.py
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# 使用 sudo -S 自动输入密码并执行 Python 脚本
echo "$SYS_PASS" | sudo -S python3 "$SCRIPT_DIR/vpn_login.py"
```
- vpn_icon.desktop
```
[Desktop Entry]
Version=1.0
Name=vpn
Comment=connect to vpn
Exec=bash /home/dpc/scripts/run_vpn.sh
Icon=/home/dpc/scripts/Icon.png
Terminal=true
Type=Application
Categories=Utility;
```

### ### 拷贝vpn_icon.desktop 到 ~/.local/share/applications/路径下面刷新
```bash
update-desktop-database ~/.local/share/applications
```
`
