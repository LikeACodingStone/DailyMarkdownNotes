## Radeon RX 7700 XT / 7800 XT
`
lspci | grep -E "VGA|3D"
`

### Install Kernel linux-headers-6.8.0-83-generic
- install
```
sudo apt update
apt-cache search linux-image-6.8.0-83-generic

sudo apt install linux-image-6.8.0-83-generic \
                 linux-modules-6.8.0-83-generic \
                 linux-headers-6.8.0-83-generic

sudo update-grub
```
- error
```
'make' KERNELVER=6.17.0-29-generic........(bad exit status: 2)
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 6.17.0-29-generic (x86_64)
...
Errors were encountered while processing: linux-image-6.17.0-29-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
- error fix
```
sudo apt purge linux-image-6.17.0-29-generic \
               linux-headers-6.17.0-29-generic \
               linux-modules-6.17.0-29-generic \
               linux-generic-hwe-24.04 \
               linux-headers-generic-hwe-24.04 -y

sudo apt install -f -y
sudo update-grub
sudo reboot
```
### Network Driver Install
```
sudo apt update
sudo apt install --only-upgrade linux-firmware

sudo update-initramfs -u -k 6.8.0-83-generic
sudo update-grub

sudo apt update
sudo apt install r8168-dkms

sudo dkms status
//// like this
// amdgpu/6.12.12-2187269.24.04, 6.8.0-124-generic, x86_64: installed 
// amdgpu/6.12.12-2187269.24.04, 6.8.0-83-generic, x86_64: installed 
// r8168/8.052.01, 6.8.0-83-generic, x86_64: installed
```
### Change Kernel
```
sudo grub-set-default "Advanced options for Ubuntu>Ubuntu, with Linux 6.8.0-83-generic"
sudo update-grub
```
### Remove Old Kernel
```
sudo dkms remove r8168/8.052.01 -k 6.17.0-35-generic
sudo apt-get purge linux-headers-6.17.0-35-generic linux-image-6.17.0-35-generic

sudo rm -f /var/crash/amdgpu-dkms.0.crash
sudo dpkg --configure -a
sudo apt-get autoremove --purge

sudo apt-get purge linux-headers-6.8.0-124-generic linux-image-6.8.0-124-generic linux-modules-6.8.0-124-generic

sudo dkms remove amdgpu/6.12.12-2187269.24.04 -k 6.8.0-124-generic
sudo dkms remove amdgpu/6.12.12-2187269.24.04 -k 6.8.0-83-generic

sudo apt-get autoremove --purge
sudo apt-get clean
sudo apt-get update

sudo apt-get install --reinstall linux-headers-6.8.0-83-generic linux-headers-6.8.0-83

sudo dkms add amdgpu/6.12.12-2187269.24.04
sudo dkms build amdgpu/6.12.12-2187269.24.04 -k 6.8.0-83-generic
sudo dkms install amdgpu/6.12.12-2187269.24.04 -k 6.8.0-83-generic


sudo amdgpu-install --uninstall -y
sudo apt-get purge "amdgpu*"
sudo dkms remove amdgpu/6.12.12-2187269.24.04 --all
sudo apt-get autoremove --purge

sudo reboot
```
***
***
## Install AMD GPU Driver
```
wget https://repo.radeon.com/amdgpu-install/6.4.2.1/ubuntu/noble/amdgpu-install_6.4.60402-1_all.deb

sudo dpkg -i amdgpu-install_*.deb

sudo apt update

sudo amdgpu-install -y --usecase=graphics,rocm --no-dkms

sudo usermod -aG video $USER
sudo usermod -aG render $USER
```