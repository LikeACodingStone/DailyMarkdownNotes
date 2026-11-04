---
tags: [ubuntu, linux, grub, kernel, swap, sysctl, benchmark]
updated: 2026-11-04
---
# Ubuntu System Tweaks

> [!summary] Contents
> 1. Kernel: choose the default, remove old ones
> 2. Swap
> 3. Kernel parameters: `vm.max_map_count`
> 4. Benchmarks: CPU / AMD GPU

---

## 1. Kernel

### 1.1 Make GRUB remember the default

Do this **first**; `grub-set-default` only works when `GRUB_DEFAULT=saved`.

```bash
sudo nano /etc/default/grub
# change / add:
GRUB_DEFAULT=saved
GRUB_SAVEDEFAULT=true

sudo update-grub
```

### 1.2 List the boot entries

```bash
sudo grep "menuentry " /boot/grub/grub.cfg | cut -d"'" -f2
```

```text
Ubuntu, with Linux 6.14.0-29-generic
Ubuntu, with Linux 6.14.0-29-generic (recovery mode)
Ubuntu, with Linux 6.8.0-83-generic
Ubuntu, with Linux 6.8.0-83-generic (recovery mode)
```

### 1.3 Choose which kernel boots

```bash
# Permanent
sudo grub-set-default "Advanced options for Ubuntu>Ubuntu, with Linux 6.8.0-83-generic"

# Next reboot only
sudo grub-reboot "Advanced options for Ubuntu>Ubuntu, with Linux 6.8.0-83-generic"
```

### 1.4 Remove old kernels

> [!tip] Keep two kernels
> Keep the current one and one fallback. Never remove the one you are running (`uname -r`).

```bash
dpkg --list | grep linux-image         # list installed kernels

sudo apt remove --purge linux-image-6.14.0-29-generic linux-headers-6.14.0-29-generic
sudo apt autoremove --purge
sudo update-grub
```

---

## 2. Swap

Swap is a **buffer** for memory, not a replacement for RAM. When memory is tight, the kernel moves **inactive pages** (4 KB units) to Swap and frees the RAM. This is called **paging**.

### 2.1 Resize the swap file

```bash
sudo swapoff -a
sudo rm /swapfile
sudo fallocate -l 32G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
free -h
```

### 2.2 Enable at boot

Add this line to `/etc/fstab` (`sudo vi /etc/fstab`):

```text
/swapfile none swap sw 0 0
```

### 2.3 Swappiness (0 to 100)

`vm.swappiness` controls how early Swap is used: **higher** = earlier, **lower** = prefer RAM and use Swap last. Default is usually `60`.

| Scenario | Recommended |
|---|---|
| High-memory machine (> 32 GB) | 5 to 10 |
| AOSP build / heavy workload | 40 to 60 |
| General use | 10 to 20 |

```bash
cat /proc/sys/vm/swappiness            # current value
sudo sysctl vm.swappiness=10           # temporary, until reboot

sudo vi /etc/sysctl.conf               # persistent: add the line below
vm.swappiness=20
```

---

## 3. Kernel Parameter: `vm.max_map_count`

```bash
sysctl vm.max_map_count                # both commands do the same
cat /proc/sys/vm/max_map_count
```

> [!info] What it is
> The maximum number of memory-mapped areas (VMAs) one process can create. **SonarQube** needs a high value because its Elasticsearch / Lucene uses memory-mapped files (`mmap()`) for the index. If it is too low, indexing or search fails, or the search engine won't start. A higher value doesn't make it faster or use more RAM; it only allows enough mappings.

> [!tip] Set it for Elasticsearch / SonarQube
> Elasticsearch asks for at least `262144`:
> ```bash
> sudo sysctl -w vm.max_map_count=262144                                  # temporary
> echo "vm.max_map_count=262144" | sudo tee /etc/sysctl.d/99-sonarqube.conf   # persistent
> ```

---

## 4. Benchmarks

### CPU (7-Zip)

```bash
sudo apt update
sudo apt install p7zip-full -y
7z b
```

Look at the bottom line `Tot: XXXXX MIPS`: higher is better.

> [!tip] For stable results
> Close browsers, Docker, IDEs and downloads; wait 1 to 2 minutes if the CPU is hot; run 3 times and average.

### AMD GPU (works over SSH / Xshell, no monitor needed)

```bash
sudo apt update
sudo apt install xvfb glmark2 -y
xvfb-run -a glmark2 --off-screen
```

The last line shows `glmark2 Score: XXXX`: higher is better. Works for AMD discrete GPUs and iGPUs, and avoids the SSH / Xshell display errors.

### GPU monitoring

```bash
sudo apt install radeontop -y
sudo radeontop                          # live GPU utilisation

watch -n 1 rocm-smi                     # ROCm: AMD GPU status, every second
```
