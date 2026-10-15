## 初始化
  - 设置分区类型(第一次初始化盘)
  `
  sudo parted /dev/sda mklabel gpt
  `
  - 创建分区
  `
  sudo parted /dev/sda mkpart primary ext4 0% 100%
  `
  - 格式化分区
  `
  sudo mkfs.ext4 /dev/sda1
  `

***
## 挂载

```
sudo mkdir /mnt/samsung4t
sudo blkid /dev/sda1
```

- 注意UUID 和 PARTUUID的区别
```
/dev/sda1: UUID="92c64b14-0c78-409e-8d30-d9879638cd1b" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="primary" PARTUUID="5da5a230-6510-42d5-872a-ef66198fb157"
```

- 添加到系统启动
```
sudo cp /etc/fstab /etc/fstab.bak
sudo vi /etc/fstab

//添加，替换UUID
UUID=5da5a230-6510-42d5-872a-ef66198fb157  /mnt/samsung4t  ext4  defaults  0  2

sudo mount -a
```
