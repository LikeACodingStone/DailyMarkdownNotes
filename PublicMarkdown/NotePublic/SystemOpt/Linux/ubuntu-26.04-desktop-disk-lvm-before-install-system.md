# Ubuntu Desktop 26.04 双硬盘 LVM 重装与故障处理完整手册

版本日期：2026-08-04

## 1. 适用范围和重要结论

本手册适用于：

- Ubuntu Desktop 26.04 LTS
- `/dev/sda`：约 1.8 TB
- `/dev/sdb`：约 1.8 TB
- UEFI 启动
- 两块硬盘的主要空间组成一个 LVM 卷组
- 根逻辑卷为 `/dev/ubuntu-vg/root`
- 根文件系统挂载到 `/`
- 不启用磁盘加密

> **清盘警告**：本文中的 `wipefs`、`parted`、`pvcreate` 和 `mkfs` 会清空目标设备。操作前必须把数据备份到不参与安装的第三块磁盘或其他计算机。

> **可靠性警告**：这是 LVM 线性容量合并，不是 RAID。任意一块盘损坏，都可能导致整个根文件系统不可用。

### Ubuntu Desktop 安装器的重要限制

Ubuntu Desktop 26.04 的图形手动分区页面可能只显示：

```text
/dev/sda1
/dev/sda2
/dev/sda3   LVM2_member
/dev/sdb1   LVM2_member
```

但不显示：

```text
/dev/mapper/ubuntu--vg-root
```

如果根逻辑卷不显示，就无法在该页面把它设置为 `/`。这不是 LVM 创建错误，而是 Desktop 手动分区器不识别已有 LVM 的已知问题。

Canonical 缺陷记录：

- [Bug #2065236：手动分区器不识别已有 LVM/LUKS/MD](https://bugs.launchpad.net/ubuntu-desktop-provision/+bug/2065236)
- [Bug #2058511：手动安装缺少 LVM LV 目标](https://bugs.launchpad.net/ubuntu-desktop-provision/+bug/2058511)

如果你已经创建完分区和 LVM，可以直接跳到[第 13 节：启动 Desktop 安装器](#13-启动-ubuntu-desktop-安装器)。

## 2. 目标磁盘布局

| 设备 | 大小 | 格式或用途 | 挂载点 |
|---|---:|---|---|
| `/dev/sda1` | 1 GiB | FAT32 EFI System Partition | `/boot/efi` |
| `/dev/sda2` | 2 GiB | ext4 | `/boot` |
| `/dev/sda3` | 第一块盘剩余空间 | LVM PV | 加入 `ubuntu-vg` |
| `/dev/sdb1` | 第二块盘全部空间 | LVM PV | 加入 `ubuntu-vg` |
| `/dev/ubuntu-vg/root` | VG 全部空间 | ext4 | `/` |

结构：

```text
/dev/sda1 ── FAT32 ── /boot/efi
/dev/sda2 ── ext4  ── /boot

/dev/sda3 ─┐
           ├─ ubuntu-vg ── root ── ext4 ── /
/dev/sdb1 ─┘
```

两块标称 1.8 TB 硬盘合并后原始容量约 3.6 TB，即约 3.27 TiB。扣除 EFI、`/boot` 和文件系统开销后会略小。

## 3. 制作 Ubuntu Desktop 26.04 安装 U 盘

下载：

```text
ubuntu-26.04-desktop-amd64.iso
```

官方下载：

- [Ubuntu 26.04 发布目录](https://releases.ubuntu.com/26.04/)
- [Ubuntu Desktop 26.04 安装教程](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/install-ubuntu-desktop/)

使用 Rufus、balenaEtcher 或 Ubuntu Disks 把 ISO 写入 U 盘。

可选：检查下载文件：

```bash
sha256sum ubuntu-26.04-desktop-amd64.iso
```

将输出与发布目录中的 `SHA256SUMS` 对比。

## 4. 启动 Ubuntu Live 桌面

1. 插入 U 盘并重启。
2. 打开启动菜单，常见按键为 `F12`、`Esc`、`F2` 或 `F10`。
3. 选择带 `UEFI` 字样的 U 盘启动项。
4. 进入安装界面后选择 **Try Ubuntu / 试用 Ubuntu**。
5. 进入桌面后按 `Ctrl` + `Alt` + `T` 打开终端。

检查 UEFI：

```bash
test -d /sys/firmware/efi && echo "UEFI 模式正常" || echo "错误：当前为 Legacy 模式"
```

必须输出：

```text
UEFI 模式正常
```

如果显示 Legacy，重新启动并选择带 `UEFI` 字样的启动项。

## 5. 确认目标磁盘

查看磁盘容量、型号和序列号：

```bash
lsblk -e7 -d -o NAME,PATH,SIZE,MODEL,SERIAL,TRAN
```

查看分区和挂载点：

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS,MODEL
```

查看目标盘详细信息：

```bash
sudo fdisk -l /dev/sda
sudo fdisk -l /dev/sdb
```

必须确认：

- `/dev/sda`、`/dev/sdb` 是两块约 1.8 TB 的目标盘。
- 型号或序列号正确。
- 安装 U 盘不是 `/dev/sda` 或 `/dev/sdb`。
- 备份盘已经断开。

如果实际设备名不同，停止操作，把后面的设备名全部替换成实际名称。

## 6. 关闭自动挂载并解除设备占用

关闭以下程序：

- Ubuntu 安装器
- Files 文件管理器
- Disks
- GParted

禁止 Live 桌面自动挂载：

```bash
gsettings set org.gnome.desktop.media-handling automount false
gsettings set org.gnome.desktop.media-handling automount-open false
```

停用交换空间和旧 LVM：

```bash
sudo swapoff -a
sudo vgchange -an
```

检查挂载状态：

```bash
lsblk -e7 -o NAME,PATH,SIZE,FSTYPE,LABEL,MOUNTPOINTS
findmnt -S /dev/sda1
findmnt -S /dev/sda2
findmnt -S /dev/sdb1
```

### 必须停止的情况

如果目标盘上的分区挂载在以下位置，不要继续：

```text
/
/cdrom
/rofs
```

这说明可能选错了 Live U 盘或正在使用的系统盘。重新核对：

```bash
lsblk -e7 -d -o NAME,PATH,SIZE,MODEL,SERIAL,TRAN
```

### 卸载普通自动挂载分区

如果挂载点类似 `/media/ubuntu/xxxx`，执行：

```bash
udisksctl unmount -b /dev/sda1
udisksctl unmount -b /dev/sda2
udisksctl unmount -b /dev/sdb1
```

提示 `not mounted` 可以忽略。

旧分区数量不同的时候，根据 `lsblk` 输出逐个卸载，例如：

```bash
sudo umount /dev/sda3
```

再次检查：

```bash
lsblk -e7 -o NAME,PATH,SIZE,FSTYPE,MOUNTPOINTS
```

目标盘所有分区的 `MOUNTPOINTS` 必须为空。

## 7. 修复 Device or resource busy

如果 `wipefs`、`parted` 或 `mkfs` 出现：

```text
Device or resource busy
apparently in use by the system
target is busy
```

查看占用进程：

```bash
sudo fuser -vm /dev/sda1
sudo fuser -vm /dev/sda2
sudo fuser -vm /dev/sdb1
```

关闭输出中涉及的 Files、安装器、Disks、GParted 或终端窗口，再重新卸载。

不要直接运行 `fuser -k`，也不要使用 `umount -l` 后立即格式化。

如果没有挂载点但仍然 busy，检查设备依赖：

```bash
ls -l /sys/class/block/sda1/holders/
ls -l /sys/class/block/sda2/holders/
ls -l /sys/class/block/sdb1/holders/
cat /proc/mdstat
sudo pvs
sudo vgs
sudo lvs
```

如果 `holders` 目录有内容，说明设备仍被 LVM、设备映射或 RAID 使用。先停用对应设备，不要强行格式化。

旧 LVM 可以再次停用：

```bash
sudo vgchange -an
sudo udevadm settle
```

## 8. 清除旧分区表

> 从本节开始，两块目标盘上的旧数据将被覆盖。

```bash
sudo wipefs --all --force /dev/sda
sudo wipefs --all --force /dev/sdb
```

创建 GPT：

```bash
sudo parted -s /dev/sda mklabel gpt
sudo parted -s /dev/sdb mklabel gpt
```

检查：

```bash
sudo parted /dev/sda print
sudo parted /dev/sdb print
```

两块盘的 `Partition Table` 应为 `gpt`。

## 9. 创建分区

### `/dev/sda`

创建 1 GiB EFI 分区：

```bash
sudo parted -s /dev/sda mkpart ESP fat32 1MiB 1025MiB
sudo parted -s /dev/sda set 1 esp on
```

创建 2 GiB `/boot`：

```bash
sudo parted -s /dev/sda mkpart boot ext4 1025MiB 3073MiB
```

创建 LVM 分区：

```bash
sudo parted -s /dev/sda mkpart lvm 3073MiB 100%
sudo parted -s /dev/sda set 3 lvm on
```

### `/dev/sdb`

```bash
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
├─sda1   约 1 GiB
├─sda2   约 2 GiB
└─sda3   剩余空间
sdb
└─sdb1   几乎全盘
```

## 10. 格式化 EFI 和 `/boot`

新分区建立后，旧文件系统签名可能导致 Live 桌面再次挂载分区。格式化前再次检查：

```bash
findmnt -S /dev/sda1
findmnt -S /dev/sda2
lsblk -e7 -o NAME,PATH,SIZE,FSTYPE,MOUNTPOINTS /dev/sda
```

如果被挂载：

```bash
udisksctl unmount -b /dev/sda1
udisksctl unmount -b /dev/sda2
```

清除残留签名：

```bash
sudo wipefs --all --force /dev/sda1
sudo wipefs --all --force /dev/sda2
```

确认以下命令没有输出：

```bash
findmnt -S /dev/sda1
findmnt -S /dev/sda2
```

格式化：

```bash
sudo mkfs.fat -F 32 -n EFI /dev/sda1
sudo mkfs.ext4 -F -L boot /dev/sda2
```

检查：

```bash
sudo udevadm settle
lsblk -f /dev/sda
```

预期：

```text
sda1   vfat   EFI
sda2   ext4   boot
sda3   尚未格式化
```

如果 `/dev/sda1` 仍为 ext4，说明 `mkfs.fat` 没有成功。只要它报 busy，旧格式就不会改变，应返回第 7 节解除占用。

## 11. 创建双盘 LVM

检查 LVM 命令：

```bash
command -v pvcreate
command -v vgcreate
command -v lvcreate
```

如果命令不存在，联网后安装：

```bash
sudo apt update
sudo apt install lvm2
```

创建 PV：

```bash
sudo pvcreate -ff -y /dev/sda3 /dev/sdb1
```

创建 VG：

```bash
sudo vgcreate ubuntu-vg /dev/sda3 /dev/sdb1
```

创建使用全部空间的根 LV：

```bash
sudo lvcreate --name root --extents 100%FREE ubuntu-vg
```

激活 VG：

```bash
sudo vgchange -ay ubuntu-vg
```

格式化根 LV：

```bash
sudo mkfs.ext4 -F -L rootfs /dev/ubuntu-vg/root
```

## 12. 验证 LVM

```bash
sudo pvs -o pv_name,vg_name,pv_size,pv_free
sudo vgs -o vg_name,vg_size,vg_free,pv_count,lv_count
sudo lvs --segments -o lv_name,vg_name,lv_size,segtype,seg_size,devices
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS
```

必须满足：

- `/dev/sda3`、`/dev/sdb1` 都属于 `ubuntu-vg`。
- `ubuntu-vg` 的 PV 数量为 2。
- 存在 `ubuntu-vg/root`。
- 根 LV 是 ext4。
- `lvs --segments` 显示根 LV 使用两块硬盘。

检查设备节点：

```bash
ls -l /dev/ubuntu-vg/root
ls -l /dev/mapper/ubuntu--vg-root
```

如果根 LV 被自动挂载：

```bash
findmnt -S /dev/ubuntu-vg/root
```

使用实际挂载点卸载，例如：

```bash
sudo umount /media/ubuntu/rootfs
```

## 13. 启动 Ubuntu Desktop 安装器

1. 保持 `ubuntu-vg` 为激活状态。
2. 如果安装器已经打开，先关闭。
3. 双击 **Install Ubuntu 26.04 LTS**。
4. 选择语言、键盘、网络和应用。
5. 到达 `Disk setup`。
6. 不选择 `Erase disk and install Ubuntu`。
7. 选择 `Manual installation`。

![选择 Manual installation](./ubuntu-lvm-guide-assets/01-choose-manual-installation.svg)

## 14. 在手动分区页先检查根 LV 是否显示

查找：

```text
/dev/mapper/ubuntu--vg-root
/dev/ubuntu-vg/root
ubuntu-vg-root
```

不要把下面两个 PV 当成根 LV：

```text
/dev/sda3   LVM2_member
/dev/sdb1   LVM2_member
```

![检查根 LVM 是否可见](./ubuntu-lvm-guide-assets/02-check-lvm-visible.svg)

判断：

- 根 LV 能看到：继续第 15 节。
- 根 LV 看不到：跳到第 18 节。

## 15. 根 LV 能看到时设置挂载点

![根 LV 可见时的挂载点](./ubuntu-lvm-guide-assets/03-mount-selection-if-visible.svg)

### `/dev/sda1`

```text
Use as:       EFI System Partition 或 FAT32
Mount point:  /boot/efi
Format:       Yes
```

### `/dev/sda2`

```text
Use as:       Ext4 journaling file system
Mount point:  /boot
Format:       Yes
```

### `/dev/mapper/ubuntu--vg-root`

```text
Use as:       Ext4 journaling file system
Mount point:  /
Format:       Yes
```

### `/dev/sda3` 和 `/dev/sdb1`

```text
Mount point:  空
Format:       No
```

如果显示 `Device for boot loader installation`，选择整块磁盘：

```text
/dev/sda
```

不要选择 `/dev/sda1`、`/dev/sda3` 或根 LV 作为 boot loader 目标。

## 16. Next 按钮为灰色的处理

必须存在：

```text
/dev/sda1                      → /boot/efi
/dev/sda2                      → /boot
/dev/mapper/ubuntu--vg-root    → /
```

检查：

```bash
test -d /sys/firmware/efi && echo UEFI || echo Legacy
sudo parted /dev/sda print
lsblk -f /dev/sda1
```

正确状态：

- 启动模式是 UEFI。
- `/dev/sda1` 是 FAT32/vfat。
- `/dev/sda1` 带有 `boot, esp` 标志。
- 只有一个 `/`。
- 只有一个 `/boot/efi`。

## 17. Ready to install 最终核对

确认：

- `/dev/sda1` 用作 EFI 并挂载 `/boot/efi`。
- `/dev/sda2` 格式化为 ext4 并挂载 `/boot`。
- `ubuntu-vg/root` 格式化为 ext4 并挂载 `/`。
- `/dev/sda3`、`/dev/sdb1` 不会被单独格式化。
- 安装 U 盘不在修改列表中。

确认无误后点击 `Install`，设置用户名、密码和时区。安装完成后重启并拔出 U 盘。

## 18. 根 LV 不显示时的最终排查

关闭安装器后执行：

```bash
sudo vgchange -ay ubuntu-vg
sudo udevadm settle
sudo lvs --segments -o lv_path,lv_attr,lv_size,segtype,devices
ls -l /dev/ubuntu-vg/root
ls -l /dev/mapper/ubuntu--vg-root
```

确认根 LV 没有挂载：

```bash
findmnt -S /dev/ubuntu-vg/root
```

如果有输出，使用实际挂载点卸载。

联网时可以尝试更新安装器：

```bash
snap list ubuntu-desktop-bootstrap
sudo snap refresh ubuntu-desktop-bootstrap
```

重新激活 VG：

```bash
sudo vgchange -ay ubuntu-vg
sudo udevadm settle
```

重新打开安装器并进入 `Manual installation`。

如果仍不显示根 LV，就没有可用的 GUI 修复。不要继续反复格式化或重建 LVM。

![根 LV 不显示时的选择](./ubuntu-lvm-guide-assets/04-choose-supported-path.svg)

绝对不要：

- 把 `/dev/sda3` 设置为 `/`。
- 把 `/dev/sdb1` 设置为 `/`。
- 格式化任何 `LVM2_member`。
- 认为返回 `Erase disk` 可以保留当前双盘布局。

## 19. 根 LV 不显示时的可行方案

### 方案 A：使用支持 LVM 的安装流程，再安装桌面

这是实现“根目录跨两块盘 LVM”最可靠的方法。使用支持 LVM VG/LV 的安装器完成系统安装，之后安装桌面环境：

```bash
sudo apt update
sudo apt install ubuntu-desktop
sudo reboot
```

最终登录并使用的是 Ubuntu Desktop 图形环境。

### 方案 B：Ubuntu Desktop Autoinstall

Ubuntu Desktop 支持导入 `autoinstall.yaml`，后端可以描述 LVM VG、LV 和挂载点，但文件必须按实际磁盘序列号和精确分区大小生成。

收集：

```bash
lsblk -b -o NAME,PATH,SIZE,TYPE,FSTYPE,PARTUUID,UUID,MODEL,SERIAL
sudo pvs --units b --nosuffix -o pv_name,pv_uuid,vg_name,pv_size
sudo vgs --units b --nosuffix -o vg_name,vg_uuid,vg_size
sudo lvs --units b --nosuffix -o lv_path,lv_uuid,vg_name,lv_size
sudo blkid
```

使用这些数据生成绑定磁盘序列号的配置。不要使用只按 `/dev/sda`、`/dev/sdb` 匹配的通用 YAML，因为盘符可能变化。

官方资料：

- [Autoinstall 简介](https://canonical-subiquity.readthedocs-hosted.com/en/latest/intro-to-autoinstall.html)
- [Autoinstall storage 配置](https://canonical-subiquity.readthedocs-hosted.com/en/latest/reference/autoinstall-reference.html#storage)

### 方案 C：普通根分区 + 双盘 LVM 数据卷

如果必须使用 Desktop 图形手动安装，可以把普通物理分区作为 `/`，LVM 作为 `/data`：

```text
/dev/sda1 → /boot/efi
/dev/sda2 → /
/dev/sda3 + /dev/sdb1 → data-vg/data → /data
```

这不再是“根目录跨两块盘”，但 Desktop 图形安装器能够完成。

> 以下重建命令只适用于当前根 LV 没有需要保留的数据。

删除空 LV/VG：

```bash
sudo lvs
sudo lvremove -y /dev/ubuntu-vg/root
sudo vgremove -y ubuntu-vg
sudo pvremove -ff -y /dev/sda3 /dev/sdb1
```

保留 `/dev/sda1`，重新创建普通根分区：

```bash
sudo parted -s /dev/sda rm 3
sudo parted -s /dev/sda rm 2
sudo parted -s /dev/sda mkpart root ext4 1025MiB 121GiB
sudo parted -s /dev/sda mkpart lvm 121GiB 100%
sudo parted -s /dev/sda set 3 lvm on
sudo partprobe /dev/sda
sudo udevadm settle
sudo mkfs.ext4 -F -L ubuntu-root /dev/sda2
```

创建 LVM 数据卷：

```bash
sudo pvcreate -ff -y /dev/sda3 /dev/sdb1
sudo vgcreate data-vg /dev/sda3 /dev/sdb1
sudo lvcreate --name data --extents 100%FREE data-vg
sudo mkfs.ext4 -F -L data /dev/data-vg/data
```

Desktop 安装器中只设置：

```text
/dev/sda1 → EFI System Partition → /boot/efi
/dev/sda2 → Ext4 → /
```

不要修改 `/dev/sda3`、`/dev/sdb1`。

安装后挂载数据卷：

```bash
sudo apt update
sudo apt install lvm2
sudo vgchange -ay data-vg
sudo mkdir -p /data
sudo blkid /dev/data-vg/data
sudo nano /etc/fstab
```

添加：

```text
UUID=<数据卷实际UUID> /data ext4 defaults 0 2
```

测试：

```bash
sudo mount -a
findmnt /data
df -hT /data
```

## 20. 安装完成后的验证

检查系统版本：

```bash
lsb_release -ds
```

检查 LVM：

```bash
sudo pvs -o pv_name,vg_name,pv_size,pv_free
sudo vgs -o vg_name,vg_size,vg_free,pv_count,lv_count
sudo lvs --segments -o lv_name,vg_name,lv_size,segtype,seg_size,devices
```

检查完整结构：

```bash
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS
```

检查挂载点：

```bash
findmnt /
findmnt /boot
findmnt /boot/efi
df -hT /
```

正确结果：

- 两个 PV 均属于 `ubuntu-vg`。
- VG 的 PV 数量为 2。
- 根 LV 的设备包含 `/dev/sda3`、`/dev/sdb1`。
- `/` 来自 `/dev/mapper/ubuntu--vg-root`。
- `/boot` 来自 `/dev/sda2`。
- `/boot/efi` 来自 `/dev/sda1`。

## 21. 检查交换空间

```bash
swapon --show
free -h
```

如果没有交换空间，并需要 8 GiB 交换文件：

```bash
sudo fallocate -l 8G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

检查配置：

```bash
grep -n '/swapfile' /etc/fstab
```

只有在没有输出时才追加：

```bash
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

验证：

```bash
swapon --show
```

## 22. 常见错误速查

### `mkfs.fat: Device or resource busy`

```bash
findmnt -S /dev/sda1
sudo fuser -vm /dev/sda1
udisksctl unmount -b /dev/sda1
```

确认没有挂载后：

```bash
sudo wipefs --all --force /dev/sda1
sudo mkfs.fat -F 32 -n EFI /dev/sda1
```

### `/dev/sda2 is apparently in use by the system`

```bash
findmnt -S /dev/sda2
sudo fuser -vm /dev/sda2
udisksctl unmount -b /dev/sda2
```

确认没有挂载后：

```bash
sudo wipefs --all --force /dev/sda2
sudo mkfs.ext4 -F -L boot /dev/sda2
```

### `pvcreate: command not found`

```bash
sudo apt update
sudo apt install lvm2
```

### 安装器看不到 `ubuntu-vg/root`

```bash
sudo vgchange -ay ubuntu-vg
sudo udevadm settle
sudo lvs
ls -l /dev/mapper/ubuntu--vg-root
```

关闭并重新打开安装器。仍不显示时属于 Desktop GUI 限制，转到第 19 节。

### 安装器提示没有 EFI 分区

```bash
test -d /sys/firmware/efi && echo UEFI || echo Legacy
sudo parted /dev/sda print
lsblk -f /dev/sda1
```

确认 `/dev/sda1` 是 FAT32，带有 `esp` 标志，安装器中挂载为 `/boot/efi`。

## 23. 最终检查清单

执行清盘命令前：

- [ ] 已完成并验证备份
- [ ] 已断开备份盘和其他数据盘
- [ ] 已通过容量、型号和序列号确认目标盘
- [ ] 已确认 U 盘不是目标盘
- [ ] Live 环境以 UEFI 模式启动
- [ ] 已关闭安装器和文件管理器
- [ ] 已禁用自动挂载
- [ ] 目标盘没有挂载点

启动安装器前：

- [ ] `/dev/sda1` 为 FAT32 EFI
- [ ] `/dev/sda2` 为 ext4
- [ ] `/dev/sda3`、`/dev/sdb1` 都属于 `ubuntu-vg`
- [ ] `/dev/ubuntu-vg/root` 为 ext4
- [ ] 根 LV 使用两块硬盘

点击 Install 前：

- [ ] `/dev/sda1` 挂载 `/boot/efi`
- [ ] `/dev/sda2` 挂载 `/boot`
- [ ] 根 LV 挂载 `/`
- [ ] 两个 LVM2_member 不会被单独格式化
- [ ] 安装 U 盘不在修改列表中

安装完成后：

- [ ] `pvs` 显示两个 PV
- [ ] `vgs` 显示 PV 数量为 2
- [ ] `/`、`/boot`、`/boot/efi` 挂载正确
- [ ] 已重新配置并测试数据备份

## 参考资料

- [Ubuntu Desktop 26.04 官方安装教程](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/install-ubuntu-desktop/)
- [Ubuntu 26.04 发布目录](https://releases.ubuntu.com/26.04/)
- [Canonical Bug #2065236](https://bugs.launchpad.net/ubuntu-desktop-provision/+bug/2065236)
- [Canonical Bug #2058511](https://bugs.launchpad.net/ubuntu-desktop-provision/+bug/2058511)
- [Ubuntu Autoinstall 简介](https://canonical-subiquity.readthedocs-hosted.com/en/latest/intro-to-autoinstall.html)
- [Ubuntu Autoinstall 配置参考](https://canonical-subiquity.readthedocs-hosted.com/en/latest/reference/autoinstall-reference.html)
- [Ubuntu LVM 管理命令](https://documentation.ubuntu.com/server/how-to/storage/manage-logical-volumes/)
