# Linux `chattr` 简明笔记

## 什么是 chattr

`chattr`（Change Attribute）用于修改 Linux 文件/目录的扩展属性，比 `chmod` 权限更高一级（主要支持 ext2/ext3/ext4）。

查看属性：

```bash
lsattr file
lsattr -d dir      # 查看目录本身
lsattr -R dir      # 递归查看
lsattr -aR dir     # 包含 . 和 ..
```

---

## 常用属性

### `+i`（immutable，不可变）

设置：

```bash
sudo chattr +i file
```

取消：

```bash
sudo chattr -i file
```

作用：

- 不能修改
    
- 不能删除
    
- 不能重命名
    
- 目录不能新增/删除文件
    

---

### `+a`（append only，只追加）

设置：

```bash
sudo chattr +a log.txt
```

作用：

- 只能追加内容（`>>`）
    
- 不能覆盖（`>`）
    
- 不能删除
    

适用于日志文件。

---

## 工作原理

Linux 删除文件时，**修改的是父目录，而不是文件本身。**

例如：

```text
parent/
└── child
```

执行：

```bash
rm parent/child
```

实际上修改的是：

```text
parent/
```

因此：

- **父目录有 `i` → 不能删除子文件/子目录**
    
- **子目录有 `i` → 子目录自身不能删除**
    

---

## 常用命令

```bash
# 设置 immutable
sudo chattr +i file

# 取消 immutable
sudo chattr -i file

# 递归设置
sudo chattr -R +i dir

# 递归取消
sudo chattr -R -i dir

# 设置 append-only
sudo chattr +a file

# 查看属性
lsattr file
lsattr -d dir
lsattr -aR dir
```

---

## 常见问题

### 为什么 `rm` 提示 `Operation not permitted`？

检查：

```bash
lsattr -aR dir
```

如果看到：

```text
----i--------- dir/.
```

说明当前目录不可变。

如果看到：

```text
----i--------- dir/..
```

说明**父目录**不可变，因此无法删除当前目录。

---

## 总结

- `chmod`：控制 **读/写/执行权限（rwx）**
    
- `chattr`：控制 **文件系统扩展属性**
    
- `+i`：不可修改、不可删除
    
- `+a`：只能追加
    
- **删除文件/目录需要修改父目录，因此父目录有 `i` 时，无法删除子项。**