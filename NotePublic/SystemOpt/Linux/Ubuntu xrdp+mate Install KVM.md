<div style="border: 3px solid #333; padding: 10px; border-radius: 8px;">

# <span style="color: red;">Install KVM on Ubuntu</span>
#### 1. check CPU supportting（Intel VT-x 或 AMD-V), 
- Select one command. if result is 0. need the BIOS open virtualization
```
egrep -c '(vmx|svm)' /proc/cpuinfo
lscpu | grep Virtualization
```
#### 2. update system
```
sudo apt update 
sudo apt upgrade -y
```
#### 3. Install KVM Enviroment
```
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```
#### 4. check service status
```
sudo systemctl enable --now libvirtd
sudo systemctl status libvirtd
```
#### 5. add user to the libvirt group
```
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
newgrp libvirt
```
#### 6. verify KVM running status, the fellowing is normal
```
virsh list --all
kvm-ok
```
- ![alt text](_resources/vscodeImages-1)
#### 7. Start graphic tools
```
virt-manager
```
</div>

***

<div style="border: 3px solid #333; padding: 10px; border-radius: 8px;">

# <span style="color: red;"> Bridge network config </span>
### 1. Reference to this file.
- cat /etc/netplan/01-network-manager-all.yaml 
```
network:
  version: 2
  renderer: networkd

  ethernets:
    enp1s0:
      dhcp4: no

  bridges:
    br0:
      interfaces:
        - enp1s0
      dhcp4: no
      addresses:
        - 172.30.2.201/24
      routes:
        - to: default
          via: 172.30.2.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
``` 
### Reboot machine

</div>

***

<div style="border: 3px solid #333; padding: 10px; border-radius: 8px;">

# <span style="color: red;"> Create Virtual Ubuntu </span>
#### 1. move iso into libvirt folder
```
$ sudo mv ~/ubuntu-24.04.3-desktop-amd64.iso /var/lib/libvirt/images/
cd /var/lib/libvirt; sudo chmod -R 755 images
```

#### 2. create new machine 
- ![alt text](_resources/vscodeImages-3)
#### 3. select ubuntu iso
- ![alt text](_resources/vscodeImages-4)
#### 4. arrange resource and start install ubuntu.
#### 5. after install finished and restart, might met this issues
- ![alt text](_resources/vscodeImages-6)
- ensure 3D acceleration is not selected
- ![alt text](_resources/vscodeImages-7)
</div>