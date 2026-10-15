### check default grub
```
sudo grep "menuentry " /boot/grub/grub.cfg | cut -d"'" -f2

//result
Ubuntu Ubuntu, with Linux 6.14.0-29-generic
Ubuntu, with Linux 6.14.0-29-generic (recovery mode)
Ubuntu, with Linux 6.8.0-83-generic
Ubuntu, with Linux 6.8.0-83-generic (recovery mode)
```

### Set default grub for reboot
```
//permanent setting
sudo grub-set-default "Advanced options for Ubuntu>Ubuntu, with Linux 6.8.0-83-generic"

//once setting only 
sudo grub-reboot "Advanced options for Ubuntu>Ubuntu, with Linux 6.8.0-83-generic"

sudo nano /etc/default/grub
	//Change
	GRUB_DEFAULT=saved
	GRUB_SAVEDEFAULT=true

sudo update-grub
```

### Remove kernel(Recommand keep two kernel)
```
dpkg --list | grep linux-image

// result 
ii  linux-image-6.14.0-29-generic                 6.14.0-29.29~24.04.1                     amd64        Signed kernel image generic
ii  linux-image-6.8.0-83-generic                  6.8.0-83.83                              amd64        Signed kernel image generic
ii  linux-image-generic                           6.8.0-83.83                              amd64        Generic Linux kernel image
ii  linux-image-generic-hwe-24.04                 6.14.0-29.29~24.04.1                     amd64        Generic Linux kernel image

sudo apt remove --purge linux-image-6.14.0-29-generic linux-headers-6.14.0-29-generic
sudo apt autoremove --purge
sudo update-grub
```