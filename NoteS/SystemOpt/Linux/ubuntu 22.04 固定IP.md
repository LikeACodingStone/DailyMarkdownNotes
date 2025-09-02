### **1. 编辑 Netplan 配置文件**

使用以下命令打开 Netplan 配置文件（文件名可能不同，如 `00-installer-config.yaml` 或 `01-network-manager-all.yaml`）:

`
em: /etc/netplan/01-network-manager-all.yaml
`
```
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:  # real net id
      dhcp4: no
      addresses:
        - 172.30.2.200/24
      gateway4: 172.30.2.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```
 
### 应用 Netplan 配置
```
sudo netplan apply
```
### 同时 Network->Wired->IPv4 设置成Disable , 重启电脑
