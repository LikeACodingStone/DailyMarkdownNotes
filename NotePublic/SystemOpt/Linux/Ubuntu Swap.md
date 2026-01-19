# Ubuntu 20.04 以后默认使用 swap 文件
### 当系统内存不足时，Linux 会把一部分暂时不用的内存页（page）写入 swap 空间，从而释放物理内存给更活跃的进程使用。

系统内存中的数据以 页（page） 为单位管理（通常每页 4KB）。
当内存吃紧时，Linux 内核会：

1. 检测内存压力（Memory Pressure）

2. 选择不活跃的内存页（Inactive Pages），例如：
	- 长时间未使用的应用数据
	- 后台程序占用但暂时不用的内容

3. 将这些页写入 swap 区

4. 释放这些页占用的 RAM

5. 当这些页再次被访问时，再从 swap 读回来

#### 这种机制称为 “页面置换（paging）”。
************
#### 修改swap大小, 临时
```
sudo swapoff -a
sudo rm /swapfile
sudo fallocate -l 32G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
free -h
```
#### 重启生效
```
sudo vi /etc/fstab

//添加
/swapfile none swap sw 0 0
```

*****
#### Swappiness 参数（内核策略）
vm.swappiness 是内核控制 swap 使用积极程度的参数，范围 0–100。
- 值越 高：系统更早开始使用 swap
- 值越 低：尽可能使用物理内存，最后才用 swap
常见配置：
```
cat /proc/sys/vm/swappiness
# 默认通常是 60

sudo sysctl vm.swappiness=10
# 临时调整
```
- 若你是高内存机器（>32GB），可设得低一点，比如 10 或 5；
- 如果是编译 AOSP 这类内存吃紧任务，可以临时提高到 40–60。
#### 重启生效
```
sudo vi /etc/sysctl.conf
vm.swappiness=20
```