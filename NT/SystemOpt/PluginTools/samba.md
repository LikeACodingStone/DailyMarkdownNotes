- samba server config 
```
[PRV]
   browseable = yes
   path = /home/neusoft/share
   guest ok = yes
   read only = no
   writable = yes
   create mask = 0644
   directory mask = 0755
   force directory mode = 0755
   valid user = neusoft
   force user = neusoft
   force group = neusoft
   available = yes
```
- 我們只能對一臺計算機設置一個登錄賬戶， 一般權限問題都是user 和group 或者 chmod 引起的

```
sudo mkdir -p /srv/samba/public
sudo chown -R nobody:nogroup /srv/samba/public
sudo chmod -R 0775 /srv/samba/public

sudo useradd nobody
sudo smbpasswd -a nobody
```

- restart
```
sudo systemctl restart smbd
sudo systemctl restart nmbd
sudo systemctl restart samba

sudo systemctl status smbd
sudo systemctl status nmbd
```