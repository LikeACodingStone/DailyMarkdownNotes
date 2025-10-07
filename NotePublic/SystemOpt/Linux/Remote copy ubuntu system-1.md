# 1. Reciever Ubuntu
```
sudo apt update
sudo apt install nfs-kernel-server
```
```
sudo mkdir -p /mnt/nfs_share
```
```
sudo chown nobody:nogroup /mnt/nfs_share
sudo chmod 777 /mnt/nfs_share
```
```
sudo nano /etc/exports
```
```
/mnt/nfs_share *(rw,sync,no_subtree_check)
```
```
sudo exportfs -a
sudo systemctl restart nfs-kernel-server
sudo ufw allow from client_ip to any port nfs
```

# 2. Copy Ubuntu
```
sudo apt install nfs-common
sudo mkdir -p /mnt/nfs_client
sudo mount server_ip:/mnt/nfs_share /mnt/nfs_client
```
```
server_ip:/mnt/nfs_share /mnt/nfs_client nfs defaults 0 0
```
```
sudo mount 172.30.2.97:/mnt/nfs_share  /mnt/nfs_client
```

# Start Copy
```
sudo dd if=/dev/sda5 of=/mnt/nfs_client/sda5_backup.img bs=4M status=progress
```