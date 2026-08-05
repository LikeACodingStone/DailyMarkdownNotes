# Ubuntu Desktop 26.04：100 GiB 系统分区 + 双硬盘 LVM 数据卷安装手册

版本日期：2026-08-05

## 1. 新方案说明

本方案不再把 Ubuntu 根文件系统 `/` 放进 LVM。

系统直接安装到第一块硬盘的普通 ext4 分区 `/dev/sda2`；系统安装完成后，再把第一块盘的剩余空间 `/dev/sda3` 和第二块盘 `/dev/sdb1` 合并为一个 LVM 数据卷，并挂载到 `/data`。

适用环境：

- Ubuntu Desktop 26.04 LTS
- `/dev/sda`：约 1.8 TB
- `/dev/sdb`：约 1.8 TB
- UEFI 启动
- 系统分区：100 GiB
- 数据卷：两块盘剩余空间之和
- 不启用磁盘加密

> **数据清除警告**：本文包含删除旧 LV/VG、重新分区和格式化命令。执行前必须备份数据，并通过磁盘型号、容量和序列号确认目标设备。

> **数据卷故障警告**：`/data` 跨越两块硬盘，不是 RAID。任意一块盘损坏，都可能导致整个 `/data` 无法使用。

如果需要运行大量 Docker 镜像、虚拟机、Steam 游戏或大型 SDK，建议把系统分区从 100 GiB 调整为 150–200 GiB。普通办公和一般开发场景可以使用 100 GiB。

## 2. 最终布局

| 设备 | 大小 | 格式或用途 | 挂载点 |
|---|---:|---|---|
| `/dev/sda1` | 1 GiB | FAT32 EFI System Partition | `/boot/efi` |
| `/dev/sda2` | 约 100 GiB | ext4 Ubuntu 系统分区 | `/` |
| `/dev/sda3` | 第一块盘剩余空间 | LVM PV | 加入 `data-vg` |
| `/dev/sdb1` | 第二块盘几乎全部空间 | LVM PV | 加入 `data-vg` |
| `/dev/data-vg/data` | 两个 PV 的全部空间 | ext4 | `/data` |

![新方案磁盘布局](./ubuntu-data-lvm-guide-assets/01-final-layout.svg)

这个方案不需要单独的 `/boot` 分区。GRUB 和内核文件位于普通根分区 `/dev/sda2` 中，EFI 文件位于 `/dev/sda1`。

## 3. 操作顺序

整个过程分为两个阶段：

### 安装 Ubuntu 之前

1. 进入 Ubuntu Desktop Live 环境。
2. 删除之前创建的空根 LV/VG。
3. 把 `/dev/sda2` 重新创建为约 100 GiB 的普通 ext4 分区。
4. 保留 `/dev/sda3`、`/dev/sdb1`，暂时不创建 LVM。
5. 在 Desktop 安装器中把 `/dev/sda2` 设置为 `/`。

### Ubuntu 安装完成之后

1. 安装 `lvm2`。
2. 把 `/dev/sda3` 和 `/dev/sdb1` 创建为 PV。
3. 创建 `data-vg/data`。
4. 格式化并挂载到 `/data`。

## 4. 制作并启动 Ubuntu Desktop U 盘

下载：

```text
ubuntu-26.04-desktop-amd64.iso
```

官方下载：

- [Ubuntu 26.04 发布目录](https://releases.ubuntu.com/26.04/)
- [Ubuntu Desktop 26.04 安装教程](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/install-ubuntu-desktop/)

使用 Rufus、balenaEtcher 或 Ubuntu Disks 写入 U 盘。

启动时选择带 `UEFI` 字样的 U 盘启动项，然后选择 **Try Ubuntu / 试用 Ubuntu**。

进入桌面后按 `Ctrl` + `Alt` + `T` 打开终端。

检查 UEFI：

```bash
test -d /sys/firmware/efi && echo "UEFI 模式正常" || echo "错误：当前为 Legacy 模式"
```

必须输出：

```text
UEFI 模式正常
```

## 5. 确认两块目标硬盘

```bash
lsblk -e7 -d -o NAME,PATH,SIZE,MODEL,SERIAL,TRAN
```

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS,MODEL
```

```bash
sudo fdisk -l /dev/sda
sudo fdisk -l /dev/sdb
```

继续之前必须确认：

- `/dev/sda`、`/dev/sdb` 是目标硬盘。
- 两块盘容量约 1.8 TB。
- 型号或序列号正确。
- 安装 U 盘不是 `/dev/sda` 或 `/dev/sdb`。
- 备份盘已经断开。

如果设备名称不同，应把后续命令中的设备名全部替换为实际名称。

## 6. 禁止 Live 系统自动挂载

关闭 Ubuntu 安装器、Files、Disks 和 GParted。

禁止自动挂载：

```bash
gsettings set org.gnome.desktop.media-handling automount false
gsettings set org.gnome.desktop.media-handling automount-open false
```

停用交换空间：

```bash
sudo swapoff -a
```

检查挂载情况：

```bash
lsblk -e7 -o NAME,PATH,SIZE,FSTYPE,LABEL,MOUNTPOINTS
```

如果目标盘分区挂载在 `/media/ubuntu/...`，逐个卸载：

```bash
udisksctl unmount -b /dev/sda1
udisksctl unmount -b /dev/sda2
udisksctl unmount -b /dev/sda3
udisksctl unmount -b /dev/sdb1
```

提示 `not mounted` 可以忽略。

如果目标盘上的任何分区挂载在以下位置，立即停止：

```text
/
/cdrom
/rofs
```

这说明可能选错了 Live U 盘或正在使用的系统盘。

## 7. 如果当前已经创建了 `ubuntu-vg/root`

本节只适用于之前创建的 `ubuntu-vg/root` 还没有需要保留的数据。

查看当前 LVM：

```bash
sudo pvs
sudo vgs
sudo lvs
```

检查根 LV 是否挂载：

```bash
findmnt -S /dev/ubuntu-vg/root
```

如果有输出，使用实际挂载点卸载。例如：

```bash
sudo umount /media/ubuntu/rootfs
```

删除空根逻辑卷：

```bash
sudo lvremove -y /dev/ubuntu-vg/root
```

删除卷组：

```bash
sudo vgremove -y ubuntu-vg
```

清除 PV 标签：

```bash
sudo pvremove -ff -y /dev/sda3 /dev/sdb1
```

确认旧 VG 已消失：

```bash
sudo pvs
sudo vgs
sudo lvs
```

如果当前不存在 `ubuntu-vg`，可以跳过本节删除命令。

## 8. 修复 Device or resource busy

如果删除、分区或格式化时出现：

```text
Device or resource busy
apparently in use by the system
target is busy
```

检查占用：

```bash
sudo fuser -vm /dev/sda1
sudo fuser -vm /dev/sda2
sudo fuser -vm /dev/sda3
sudo fuser -vm /dev/sdb1
```

关闭输出中涉及的安装器、Files、Disks 或 GParted，再重新卸载。

如果没有挂载点但仍然 busy，检查：

```bash
ls -l /sys/class/block/sda1/holders/
ls -l /sys/class/block/sda2/holders/
ls -l /sys/class/block/sda3/holders/
ls -l /sys/class/block/sdb1/holders/
cat /proc/mdstat
sudo pvs
sudo vgs
sudo lvs
```

不要使用 `fuser -k` 盲目杀进程，也不要使用 `umount -l` 后立即格式化。

## 9. 重新划分 `/dev/sda`

本方案保留 `/dev/sda1` EFI 分区，删除原来的 2 GiB `/boot` 分区和旧 LVM 分区。

再次检查分区：

```bash
sudo parted /dev/sda unit MiB print
```

删除旧 `/dev/sda3`：

```bash
sudo parted -s /dev/sda rm 3
```

删除旧 `/dev/sda2`：

```bash
sudo parted -s /dev/sda rm 2
```

创建约 100 GiB 的普通根分区：

```bash
sudo parted -s /dev/sda mkpart root ext4 1025MiB 101GiB
```

创建使用剩余空间的 LVM 预留分区：

```bash
sudo parted -s /dev/sda mkpart lvm 101GiB 100%
sudo parted -s /dev/sda set 3 lvm on
```

如果希望使用约 200 GiB 系统分区，把上面两个命令中的 `101GiB` 改为 `201GiB`。

## 10. 确认 `/dev/sdb1`

查看第二块盘：

```bash
sudo parted /dev/sdb unit MiB print
```

如果 `/dev/sdb1` 已经覆盖几乎整个磁盘，可以保留。

如果不存在，创建：

```bash
sudo parted -s /dev/sdb mklabel gpt
sudo parted -s /dev/sdb mkpart lvm 1MiB 100%
sudo parted -s /dev/sdb set 1 lvm on
```

重新读取分区表：

```bash
sudo partprobe /dev/sda
sudo partprobe /dev/sdb
sudo udevadm settle
```

检查：

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS
sudo parted /dev/sda unit MiB print
sudo parted /dev/sdb unit MiB print
```

预期：

```text
sda
├─sda1     约 1 GiB
├─sda2     约 100 GiB
└─sda3     第一块盘剩余空间
sdb
└─sdb1     第二块盘几乎全部空间
```

## 11. 格式化系统分区

确认 `/dev/sda2` 没有挂载：

```bash
findmnt -S /dev/sda2
```

如果有输出，先卸载：

```bash
udisksctl unmount -b /dev/sda2
```

清除旧签名并格式化：

```bash
sudo wipefs --all --force /dev/sda2
sudo mkfs.ext4 -F -L ubuntu-root /dev/sda2
```

检查 EFI 分区：

```bash
lsblk -f /dev/sda1
sudo parted /dev/sda print
```

正确状态：

- `/dev/sda1` 是 `vfat`/FAT32。
- `/dev/sda1` 带有 `boot, esp` 标志。

如果 `/dev/sda1` 不是 FAT32，并且确认是全新单系统安装：

```bash
udisksctl unmount -b /dev/sda1
sudo wipefs --all --force /dev/sda1
sudo mkfs.fat -F 32 -n EFI /dev/sda1
```

如果仍出现 busy，返回第 8 节处理。

## 12. 安装前最终磁盘检查

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS
```

预期：

```text
sda1   vfat   EFI
sda2   ext4   ubuntu-root
sda3   未格式化或仅显示分区类型
sdb1   未格式化或仅显示分区类型
```

安装前不要创建 `data-vg`。在 Ubuntu 安装完成后再创建，避免 Desktop 安装器受到已有 LVM 的影响。

## 13. 启动 Ubuntu Desktop 安装器

1. 双击桌面的 **Install Ubuntu 26.04 LTS**。
2. 选择语言、辅助功能、键盘和网络。
3. 选择 `Interactive installation`。
4. 根据需要选择默认或扩展应用。
5. 到达 `Disk setup` 后选择：

   ```text
   Manual installation
   ```

6. 不要选择 `Erase disk and install Ubuntu`。

## 14. 手动安装页面的正确选择

只配置 `/dev/sda1` 和 `/dev/sda2`。

![Desktop 安装器中的分区选择](./ubuntu-data-lvm-guide-assets/02-installer-selection.svg)

### `/dev/sda1`

选择 `/dev/sda1`，点击 `Edit`、`Change` 或铅笔按钮：

```text
Use as:       EFI System Partition
Mount point:  /boot/efi
Format:       Yes
```

如果机器还保留其他操作系统并共用这个 ESP，`Format` 应选择 `No`。本手册的全新单系统安装可以选择 `Yes`。

### `/dev/sda2`

选择 `/dev/sda2`：

```text
Use as:       Ext4 journaling file system
Mount point:  /
Format:       Yes
```

### `/dev/sda3`

保持：

```text
Use as:       Do not use 或不修改
Mount point:  空
Format:       No
```

### `/dev/sdb1`

保持：

```text
Use as:       Do not use 或不修改
Mount point:  空
Format:       No
```

### Boot loader

如果安装器显示 `Device for boot loader installation`，选择：

```text
/dev/sda
```

不要选择 `/dev/sda1` 或 `/dev/sda2`。

## 15. 安装前摘要核对

安装摘要应该只有：

```text
/dev/sda1 → EFI System Partition → /boot/efi
/dev/sda2 → ext4 → /
```

必须确认：

- `/dev/sda3` 不会被格式化。
- `/dev/sdb1` 不会被格式化。
- 安装 U 盘不在修改列表中。
- `/` 只有一个。
- `/boot/efi` 只有一个。

确认后点击 `Install`，设置用户名、计算机名、密码和时区。

安装完成后重启并拔出 U 盘。

## 16. 第一次进入系统后安装 LVM 工具

打开终端：

```bash
sudo apt update
sudo apt install lvm2
```

再次确认目标分区：

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS,MODEL
```

必须确认：

- `/dev/sda2` 正挂载到 `/`。
- `/dev/sda3` 没有挂载。
- `/dev/sdb1` 没有挂载。
- `/dev/sda3`、`/dev/sdb1` 是计划用于数据 LVM 的分区。

## 17. 创建 LVM 数据卷

![安装后创建 LVM 数据卷](./ubuntu-data-lvm-guide-assets/03-postinstall-lvm.svg)

创建两个 PV：

```bash
sudo pvcreate -ff -y /dev/sda3 /dev/sdb1
```

检查：

```bash
sudo pvs
```

创建卷组：

```bash
sudo vgcreate data-vg /dev/sda3 /dev/sdb1
```

检查：

```bash
sudo vgs
```

创建一个使用全部空间的数据 LV：

```bash
sudo lvcreate --name data --extents 100%FREE data-vg
```

格式化数据 LV：

```bash
sudo mkfs.ext4 -F -L data /dev/data-vg/data
```

检查：

```bash
sudo pvs -o pv_name,vg_name,pv_size,pv_free
sudo vgs -o vg_name,vg_size,vg_free,pv_count,lv_count
sudo lvs --segments -o lv_name,vg_name,lv_size,segtype,seg_size,devices
```

正确结果：

- `/dev/sda3`、`/dev/sdb1` 均属于 `data-vg`。
- `data-vg` 的 PV 数量为 2。
- 存在 `/dev/data-vg/data`。
- `lvs --segments` 显示数据 LV 使用两块硬盘。

## 18. 把数据卷挂载到 `/data`

创建目录：

```bash
sudo mkdir -p /data
```

取得数据卷 UUID：

```bash
sudo blkid /dev/data-vg/data
```

输出类似：

```text
/dev/mapper/data--vg-data: UUID="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" TYPE="ext4"
```

编辑 `/etc/fstab`：

```bash
sudo nano /etc/fstab
```

添加一行，将 `<数据卷UUID>` 替换为实际 UUID：

```text
UUID=<数据卷UUID> /data ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2
```

`nofail` 的作用是：如果数据卷无法激活，系统仍可以继续启动，而不是直接进入紧急模式。

保存后测试：

```bash
sudo mount -a
findmnt /data
df -hT /data
```

如果 `mount -a` 没有错误，说明 `fstab` 配置正确。

## 19. 设置 `/data` 权限

如果 `/data` 只给当前用户使用：

```bash
sudo chown "$USER:$USER" /data
```

检查：

```bash
ls -ld /data
touch /data/write-test
rm /data/write-test
```

如果有多个用户共享 `/data`，建议创建专用用户组，而不是把整个目录设置成 `777`。

## 20. 建议的数据目录结构

```bash
mkdir -p /data/Documents
mkdir -p /data/Downloads
mkdir -p /data/Projects
mkdir -p /data/VMs
mkdir -p /data/Backup
```

大型文件、虚拟机、Docker 数据和项目可以放在 `/data`，减少 100 GiB 根分区的压力。

不要直接把整个 `/home` 改为新数据卷，除非已经正确复制用户目录、权限和隐藏配置文件。优先使用 `/data` 最安全。

## 21. 最终验证

检查系统分区：

```bash
findmnt /
df -hT /
```

检查 EFI：

```bash
findmnt /boot/efi
```

检查数据卷：

```bash
findmnt /data
df -hT /data
```

检查 LVM：

```bash
sudo pvs
sudo vgs
sudo lvs --segments -o lv_name,vg_name,lv_size,segtype,devices
```

检查完整磁盘结构：

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS
```

预期结果：

```text
/                  来自 /dev/sda2，约 100 GiB
/boot/efi          来自 /dev/sda1
/data              来自 /dev/mapper/data--vg-data
data-vg/data       使用 /dev/sda3 和 /dev/sdb1
```

## 22. 检查交换空间

```bash
swapon --show
free -h
```

如果没有交换空间，并需要创建 8 GiB 交换文件：

```bash
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

检查 `/etc/fstab`：

```bash
grep -n '/swapfile' /etc/fstab
```

只有没有输出时才追加：

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

验证：

```bash
swapon --show
```

## 23. 常见问题

### `/dev/sda2` 格式化时提示 busy

```bash
findmnt -S /dev/sda2
sudo fuser -vm /dev/sda2
udisksctl unmount -b /dev/sda2
```

确认没有挂载后：

```bash
sudo wipefs --all --force /dev/sda2
sudo mkfs.ext4 -F -L ubuntu-root /dev/sda2
```

### `/dev/sda1` 仍显示 ext4

说明 `mkfs.fat` 没有成功。检查并卸载：

```bash
findmnt -S /dev/sda1
sudo fuser -vm /dev/sda1
udisksctl unmount -b /dev/sda1
```

重新格式化：

```bash
sudo wipefs --all --force /dev/sda1
sudo mkfs.fat -F 32 -n EFI /dev/sda1
```

### Desktop 安装器的 Next 按钮为灰色

检查：

```bash
test -d /sys/firmware/efi && echo UEFI || echo Legacy
sudo parted /dev/sda print
lsblk -f /dev/sda1
```

安装器必须存在：

```text
/dev/sda1 → /boot/efi
/dev/sda2 → /
```

本方案的根分区是普通 `/dev/sda2`，不需要等待安装器显示 `/dev/mapper` 设备。

### `pvcreate: command not found`

```bash
sudo apt update
sudo apt install lvm2
```

### 重启后 `/data` 没有挂载

```bash
sudo vgchange -ay data-vg
sudo lvs
sudo mount -a
systemctl status data.mount
```

检查 `/etc/fstab` 中的 UUID：

```bash
sudo blkid /dev/data-vg/data
grep -n '/data' /etc/fstab
```

### `/data` 无法写入

```bash
ls -ld /data
sudo chown "$USER:$USER" /data
```

## 24. 操作检查清单

安装前：

- [ ] 已完成并验证备份
- [ ] 已断开备份盘和其他数据盘
- [ ] 已确认 `/dev/sda`、`/dev/sdb` 的容量、型号和序列号
- [ ] 已确认安装 U 盘不是目标盘
- [ ] Live 环境以 UEFI 模式启动
- [ ] 已关闭安装器和文件管理器
- [ ] 目标盘没有挂载点

重建分区后：

- [ ] `/dev/sda1` 为约 1 GiB FAT32 EFI
- [ ] `/dev/sda2` 为约 100 GiB ext4
- [ ] `/dev/sda3` 为第一块盘剩余空间
- [ ] `/dev/sdb1` 为第二块盘几乎全部空间
- [ ] 尚未创建 `data-vg`

点击 Install 前：

- [ ] `/dev/sda1` 挂载 `/boot/efi`
- [ ] `/dev/sda2` 挂载 `/`
- [ ] `/dev/sda3` 不格式化
- [ ] `/dev/sdb1` 不格式化
- [ ] Boot loader 目标为 `/dev/sda`（如果显示）

系统安装后：

- [ ] `data-vg` 包含 `/dev/sda3`、`/dev/sdb1`
- [ ] `data-vg/data` 格式为 ext4
- [ ] `/data` 已写入 `/etc/fstab`
- [ ] `mount -a` 没有错误
- [ ] 当前用户可以写入 `/data`
- [ ] 已配置并测试独立备份

## 参考资料

- [Ubuntu Desktop 26.04 官方安装教程](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/install-ubuntu-desktop/)
- [Ubuntu 26.04 发布目录](https://releases.ubuntu.com/26.04/)
- [Ubuntu LVM 管理命令](https://documentation.ubuntu.com/server/how-to/storage/manage-logical-volumes/)
- [Ubuntu LVM 概念说明](https://documentation.ubuntu.com/server/explanation/storage/about-lvm/)
