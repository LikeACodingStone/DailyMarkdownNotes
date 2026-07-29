```
#!/bin/bash

set -e

echo "========================================="
echo "Install keyd (Ubuntu 24.04)"
echo "========================================="

if [ "$EUID" -ne 0 ]; then
    echo "请使用 sudo 运行"
    exit 1
fi

apt update

apt install -y \
    git \
    build-essential \
    pkg-config \
    libevdev-dev

cd /tmp

rm -rf keyd

git clone https://github.com/rvaiya/keyd.git

cd keyd

make

make install

mkdir -p /etc/keyd

cat >/etc/keyd/default.conf <<EOF
[ids]
*

[main]
S-delete = delete
leftshift+delete = delete
rightshift+delete = delete
EOF

systemctl enable keyd
systemctl restart keyd

echo
echo "========================================="
echo "安装完成"
echo "========================================="
echo

echo "测试："
echo "sudo keyd monitor"

sudo keyd reload
sudo systemctl restart keyd

sudo reboot
```