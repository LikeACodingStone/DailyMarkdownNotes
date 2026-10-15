### install samba
```
sudo apt update
sudo apt install samba -y
```
***
### everyone access config
```
[public]
   path = /mnt/samsung4t/sharefolder
   browseable = yes
   writable = yes
   guest ok = yes
   read only = no
   force user = nobody
   create mask = 0777
   directory mask = 0777

```
- setting folder access, necessary
```
sudo chown -R nobody:nogroup /mnt/samsung4t/sharefolder
sudo chmod -R 777 /mnt/samsung4t/sharefolder

//看情况可以不添加，/home/user则必须添加
sudo chmod o+x /mnt
sudo chmod o+x /mnt/samsung4t
```

- access穿透核心原理：Linux 查找文件是从左到右、层层递进的，如果一个目录没有 x 权限，你就无法“穿过”它。即使你明确知道该目录下面有一个权限为 777 的文件，只要上级目录没有 x 权限，系统内核在沿着路径寻找时，就会在这一层被挡住，直接报 Permission denied。
```
/ (根目录)         --> 检查 nobody 是否有 x 权限 (默认都有)
   └── home        --> 检查 nobody 是否有 x 权限 (默认都有)
        └── neu    --> 检查 nobody 是否有 x 权限 (❌ 默认没有！卡在这里报错)
             └── ccs2 --> 根本还没走到这一步
// 如果是home目录下，意味着共享目录用户要加这个，就是 /home/neu，类似
sudo chmod o+x /home/neu

/ (根目录)       --> 检查 nobody 是否有 x 权限 (默认允许)
   └── mnt       --> 检查 nobody 是否有 x 权限 (默认允许！无需手动修改)
        └── ccs2 --> 直接到达目标，只需确保 ccs2 自身权限足够
```
- sudo systemctl restart smbd
****
### with account access config
```
[PRV]
   browseable = no
   path = /home/neusoft/share/Private
   guest ok = yes
   read only = no
   writable = yes
   create mask = 0644
   directory mask = 0755
   force directory mode = 0755
   force user = neusoft
   force group = neusoft
   available = yes

[COMMON]
   browseable = yes
   path = /home/neusoft/share/Common
   guest ok = yes
   writable = yes
   create mask = 0644
   directory mask = 0755
   force directory mode = 0755
   force user = neusoft
   force group = neusoft
   available = yes
```
***
### FileBrowser Settings
- 如果安裝成功，你會看到類似 FileBrowser installed successfully 的提示。
```
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash
```
- start browser server
```
filebrowser -d /mnt/samsung4t/sharefolder/filebrowser.db -r /mnt/samsung4t/sharefolder -a 0.0.0.0 -p 8080
```
- updating password
```
filebrowser users update admin --password "admin12345678" -d /mnt/samsung4t/sharefolder/filebrowser.db
```