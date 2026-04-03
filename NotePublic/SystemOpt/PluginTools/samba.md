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
sudo chmod o+x /mnt
sudo chmod o+x /mnt/samsung4t
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