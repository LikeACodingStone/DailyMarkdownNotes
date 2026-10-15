# 🧠 Ubuntu 20.04 Swap Mechanism & Configuration Guide

---

## 📌 1. What is Swap?

When system memory is insufficient, Linux moves some inactive memory pages into **Swap space**, freeing up physical memory for more active processes.

### 🧩 Memory Management Basics

* Memory is managed in units called **pages** (typically **4KB** each)
* When memory becomes tight, the Linux kernel performs the following:

### ⚙️ Paging Process

1. 🔍 Detect memory pressure (Memory Pressure)
2. 📉 Select inactive pages (Inactive Pages), such as:

   * 💤 Application data not used for a long time
   * 🧊 Background program data temporarily unused
3. 💾 Write these pages into Swap space
4. 🧹 Free up RAM occupied by these pages
5. 🔄 When needed again, read them back from Swap

> 📘 This mechanism is called: **Paging**

---

## 🛠️ 2. Modify Swap Size (Temporary)

```bash
sudo swapoff -a
sudo rm /swapfile
sudo fallocate -l 32G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
free -h
```

---

## 🔁 3. Enable Swap on Boot

Edit `/etc/fstab`:

```bash
sudo vi /etc/fstab
```

Add the following line:

```bash
/swapfile none swap sw 0 0
```

---

## 🎛️ 4. Swappiness Parameter (Kernel Policy)

`vm.swappiness` controls how aggressively the system uses Swap. Range:

```
0 – 100
```

### 📊 Meaning

* 🔺 Higher value → system uses Swap earlier
* 🔻 Lower value → prefer RAM as much as possible, use Swap last

---

### 🔍 Check Current Value

```bash
cat /proc/sys/vm/swappiness
```

👉 Default is usually: `60`

---

### ⚡ Temporary Adjustment

```bash
sudo sysctl vm.swappiness=10
```

---

### 💡 Recommended Settings

| Scenario                        | Recommended Value |
| ------------------------------- | ----------------- |
| 🖥️ High-memory machine (>32GB) | 5 – 10            |
| 🏗️ AOSP build / heavy workload | 40 – 60           |
| ⚖️ General usage                | 10 – 20           |

---

### 🔒 Make It Persistent

Edit the configuration file:

```bash
sudo vi /etc/sysctl.conf
```

Add:

```bash
vm.swappiness=20
```

---

## ✅ Summary

* 🧠 Swap is a “buffer” for memory, not a replacement
* ⚡ Adjusting swappiness helps optimize performance
* 🛠️ Proper Swap sizing is important for heavy workloads

---
