
- sudo umount /dev/sdb #先卸载u盘
- sudo mkfs.vfat /dev/sdb #格式化为fat32模式
- mount -t vfat /dev/sdb1 /media/usb