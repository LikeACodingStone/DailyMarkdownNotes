---
tags: [ubuntu, linux, disk, mount, fstab, lvm, parted]
updated: 2026-11-04
---
# Ubuntu Disk, Mount & LVM

> [!summary] Contents
> 1. New disk: partition, format, mount at boot
> 2. Format a USB stick as FAT32
> 3. Ubuntu 26.04: 100 GiB system + two-disk LVM data volume

> [!danger] Partitioning and formatting erase data
> Always confirm the device with `lsblk` first.

---

## 1. New Disk: Partition, Format, Mount

### 1.1 Initialise

```bash
# First time only: partition table type
sudo parted /dev/sda mklabel gpt
# Create one partition using the whole disk
sudo parted /dev/sda mkpart primary ext4 0% 100%
# Format
sudo mkfs.ext4 /dev/sda1
```

### 1.2 Mount at boot

```bash
sudo mkdir /mnt/samsung4t
sudo blkid /dev/sda1
```

```text
/dev/sda1: UUID="92c64b14-0c78-409e-8d30-d9879638cd1b" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="primary" PARTUUID="5da5a230-6510-42d5-872a-ef66198fb157"
```

> [!bug] `UUID` and `PARTUUID` are two different IDs
> In `fstab`, `UUID=` must be followed by the **UUID** (`92c64b14-...`). The old note wrote `UUID=` with the **PARTUUID** (`5da5a230-...`), which doesn't match, so the disk wouldn't mount. To use the PARTUUID, write `PARTUUID=5da5a230-...`.

```bash
sudo cp /etc/fstab /etc/fstab.bak        # back up first
sudo vi /etc/fstab
```

Add this line, with **your** UUID:

```text
UUID=92c64b14-0c78-409e-8d30-d9879638cd1b  /mnt/samsung4t  ext4  defaults  0  2
```

```bash
sudo mount -a          # no error = fstab is correct
```

> [!tip] Secondary disk? Add `nofail`
> `defaults,nofail` lets the system keep booting if this disk is missing, instead of dropping into emergency mode.

---

## 2. Format a USB Stick as FAT32

```bash
lsblk                                  # find the stick, e.g. sdb

sudo umount /dev/sdb1                  # unmount first
sudo mkfs.vfat -F 32 /dev/sdb1         # format as FAT32
sudo mkdir -p /media/usb
sudo mount -t vfat /dev/sdb1 /media/usb
```

> [!bug] Use the same device for every step
> The old note formatted `/dev/sdb` (the **whole disk**) but then mounted `/dev/sdb1` (a partition), which don't match. Use the **partition** `/dev/sdb1` everywhere.

---

## 3. Ubuntu 26.04: 100 GiB System + Two-Disk LVM Data Volume

Two ~1.8 TB disks, UEFI, no encryption. The system goes on a **normal ext4 partition**; after installing, the leftover space of both disks is merged into one LVM volume mounted at `/data`.

> [!warning] LVM linear merge is NOT RAID
> If either disk fails, the whole `/data` can become unusable. Keep a separate backup.

> [!important] Why `/` is not on LVM
> The Ubuntu Desktop installer's manual partitioner **doesn't show existing LVM volumes** (Launchpad bugs #2065236 and #2058511), so a pre-made root LV can't be chosen as `/`. That is why LVM is created **after** the install.

### 3.1 Final layout

| Device | Size | Format / use | Mount |
|---|---:|---|---|
| `/dev/sda1` | 1 GiB | FAT32 EFI System Partition | `/boot/efi` |
| `/dev/sda2` | ~100 GiB | ext4, Ubuntu system | `/` |
| `/dev/sda3` | rest of disk 1 | LVM PV → `data-vg` | |
| `/dev/sdb1` | ~all of disk 2 | LVM PV → `data-vg` | |
| `/dev/data-vg/data` | all of both PVs | ext4 | `/data` |

> [!tip] More system space?
> For lots of Docker images, VMs, Steam games or SDKs use 150 to 200 GiB: change `101GiB` to `151GiB` / `201GiB` in the `parted` commands below.

### 3.2 Before installing (in the Live USB)

```bash
# Boot must be UEFI
test -d /sys/firmware/efi && echo "UEFI OK" || echo "ERROR: Legacy mode"

# Confirm the target disks: size, model, serial. The USB stick must not be sda/sdb
#
lsblk -e7 -d -o NAME,PATH,SIZE,MODEL,SERIAL,TRAN
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS,MODEL

# Stop the Live system auto-mounting the disks
gsettings set org.gnome.desktop.media-handling automount false
gsettings set org.gnome.desktop.media-handling automount-open false
sudo swapoff -a

# Unmount target partitions; "not mounted" can be ignored
udisksctl unmount -b /dev/sda1
udisksctl unmount -b /dev/sda2
udisksctl unmount -b /dev/sda3
udisksctl unmount -b /dev/sdb1
```

> [!danger] Stop if a target partition is mounted at `/`, `/cdrom` or `/rofs`
> You may have picked the Live USB or the running system disk.

**If an old `ubuntu-vg/root` exists (and holds no data you need):**

```bash
sudo pvs; sudo vgs; sudo lvs
sudo lvremove -y /dev/ubuntu-vg/root
sudo vgremove -y ubuntu-vg
sudo pvremove -ff -y /dev/sda3 /dev/sdb1
```

**Repartition `/dev/sda`** (keep `sda1` = EFI; delete the old `/boot` and LVM partitions):

```bash
sudo parted /dev/sda unit MiB print
sudo parted -s /dev/sda rm 3
sudo parted -s /dev/sda rm 2
sudo parted -s /dev/sda mkpart root ext4 1025MiB 101GiB      # ~100 GiB system
sudo parted -s /dev/sda mkpart lvm 101GiB 100%               # rest, for LVM
sudo parted -s /dev/sda set 3 lvm on
```

**Check `/dev/sdb1`** (keep it if it already covers nearly the whole disk):

```bash
sudo parted /dev/sdb unit MiB print
# If missing:
sudo parted -s /dev/sdb mklabel gpt
sudo parted -s /dev/sdb mkpart lvm 1MiB 100%
sudo parted -s /dev/sdb set 1 lvm on

sudo partprobe /dev/sda; sudo partprobe /dev/sdb; sudo udevadm settle
```

**Format the system partition:**

```bash
findmnt -S /dev/sda2                       # no output = not mounted
sudo wipefs --all --force /dev/sda2
sudo mkfs.ext4 -F -L ubuntu-root /dev/sda2

lsblk -f /dev/sda1                         # must be vfat, with the boot, esp flags
# Only if sda1 is NOT FAT32 and this is a fresh single-OS install:
# udisksctl unmount -b /dev/sda1
# sudo wipefs --all --force /dev/sda1
# sudo mkfs.fat -F 32 -n EFI /dev/sda1
```

> [!caution] Don't create `data-vg` yet
> Create it after the install, so the Desktop installer isn't confused by existing LVM.

**Expected state before installing:**

```text
sda1   vfat   EFI
sda2   ext4   ubuntu-root
sda3   (unformatted)
sdb1   (unformatted)
```

### 3.3 In the Ubuntu Desktop installer

1. **Interactive installation** → at *Disk setup* choose **Manual installation** (**not** *Erase disk*)
2. Set **only** these two:

| Partition | Use as | Mount | Format |
|---|---|---|---|
| `/dev/sda1` | EFI System Partition | `/boot/efi` | Yes (fresh single-OS install; **No** if the ESP is shared with another OS) |
| `/dev/sda2` | Ext4 | `/` | Yes |

3. `/dev/sda3` and `/dev/sdb1`: **Do not use**, no mount point, no format
4. Boot loader device (if shown): `/dev/sda`, **not** `sda1` / `sda2`
5. Summary must show only `sda1 → /boot/efi` and `sda2 → /`, and neither `sda3` nor `sdb1` formatted. Then **Install**.

### 3.4 After installing: create the LVM data volume

```bash
sudo apt update
sudo apt install lvm2
lsblk -e7 -o NAME,PATH,SIZE,TYPE,FSTYPE,LABEL,MOUNTPOINTS,MODEL     # sda2 is /, sda3 and sdb1 are NOT mounted

sudo pvcreate -ff -y /dev/sda3 /dev/sdb1
sudo vgcreate data-vg /dev/sda3 /dev/sdb1
sudo lvcreate --name data --extents 100%FREE data-vg
sudo mkfs.ext4 -F -L data /dev/data-vg/data
```

Verify: `data-vg` has **2** PVs, and `/dev/data-vg/data` uses both disks:

```bash
sudo pvs -o pv_name,vg_name,pv_size,pv_free
sudo vgs -o vg_name,vg_size,vg_free,pv_count,lv_count
sudo lvs --segments -o lv_name,vg_name,lv_size,segtype,seg_size,devices
```

### 3.5 Mount at `/data`

```bash
sudo mkdir -p /data
sudo blkid /dev/data-vg/data          # copy the UUID
sudo nano /etc/fstab
```

```text
UUID=<data-volume-UUID> /data ext4 defaults,nofail,x-systemd.device-timeout=10s 0 2
```

`nofail`: if the volume can't be activated, the system still boots instead of dropping into emergency mode.

```bash
sudo mount -a
findmnt /data
df -hT /data

sudo chown "$USER:$USER" /data        # only for you
touch /data/write-test && rm /data/write-test
mkdir -p /data/{Documents,Downloads,Projects,VMs,Backup}
```

> [!tip] Don't move all of `/home` onto the data volume
> Use `/data` for big files, VMs, Docker data and projects. Moving `/home` needs correct copying of permissions and hidden config files.
> Several users sharing `/data`: create a dedicated group instead of `777`.

**Final check:**

```text
/              from /dev/sda2, ~100 GiB
/boot/efi      from /dev/sda1
/data          from /dev/mapper/data--vg-data
data-vg/data   uses /dev/sda3 and /dev/sdb1
```

### 3.6 Troubleshooting

| Problem | Fix |
|---|---|
| `Device or resource busy` | `sudo fuser -vm /dev/sdXN`; close the installer, Files, Disks, GParted; unmount again. Also check `ls -l /sys/class/block/sda1/holders/`, `cat /proc/mdstat`, `sudo pvs/vgs/lvs`. **Don't** blindly `fuser -k`, and **don't** `umount -l` then format. |
| `/dev/sda1` still shows ext4 | `mkfs.fat` didn't succeed: unmount, then `sudo wipefs --all --force /dev/sda1 && sudo mkfs.fat -F 32 -n EFI /dev/sda1` |
| Installer **Next** button is grey | Check UEFI (`test -d /sys/firmware/efi`), `sudo parted /dev/sda print`, `lsblk -f /dev/sda1`. The installer needs `sda1 → /boot/efi` and `sda2 → /` |
| `pvcreate: command not found` | `sudo apt install lvm2` |
| `/data` not mounted after reboot | `sudo vgchange -ay data-vg`, `sudo lvs`, `sudo mount -a`, `systemctl status data.mount`; check the UUID in `/etc/fstab` against `sudo blkid /dev/data-vg/data` |
| `/data` not writable | `sudo chown "$USER:$USER" /data` |

### 3.7 Swap

```bash
swapon --show
free -h
```

No swap? Create an 8 GiB swap file (details: [[Ubuntu System Tweaks]]).

```bash
sudo fallocate -l 8G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile
grep -n '/swapfile' /etc/fstab || echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 3.8 Checklist

- [ ] **Before:** backup verified; backup disks unplugged; disk size / model / serial confirmed; USB is not a target; booted in UEFI; target disks not mounted
- [ ] **After repartitioning:** `sda1` ~1 GiB FAT32 EFI; `sda2` ~100 GiB ext4; `sda3` rest of disk 1; `sdb1` ~all of disk 2; **no** `data-vg` yet
- [ ] **Before pressing Install:** `sda1 → /boot/efi`; `sda2 → /`; `sda3` and `sdb1` not formatted; boot loader on `/dev/sda`
- [ ] **After installing:** `data-vg` has `sda3` + `sdb1`; `data` is ext4; `/data` is in `/etc/fstab`; `mount -a` clean; you can write to `/data`; a separate backup is set up and tested

### References

- [Ubuntu Desktop 26.04 install tutorial](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/install-ubuntu-desktop/)
- [Ubuntu 26.04 releases](https://releases.ubuntu.com/26.04/)
- [Manage logical volumes](https://documentation.ubuntu.com/server/how-to/storage/manage-logical-volumes/)
- [About LVM](https://documentation.ubuntu.com/server/explanation/storage/about-lvm/)
