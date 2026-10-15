# ACL（Access Control List，访问控制列表）简介

## 1. 传统 Linux 权限模型回顾

- Linux 文件系统传统权限基于三类主体和三种权限：
  - **主体**：文件所有者（User）、所属组（Group）、其他用户（Others）
  - **权限**：读（r）、写（w）、执行（x）
- 权限是针对这三类主体整体设置的，无法细粒度区分具体用户

---

## 2. ACL 的作用

- ACL 是对传统权限的扩展，允许给**任意单个用户或组**单独设置权限
- 通过 ACL，可以实现更加灵活和细粒度的权限管理

---

## 3. ACL 的工作原理

- 每个文件或目录除了传统的权限位外，还有一份 ACL 表
- ACL 表记录多个条目（Access Control Entries，ACE），每个条目定义了某个用户或组的权限
- 系统在判断访问权限时，会先检查 ACL 表，优先使用 ACL 里的权限规则

---

## 4. ACL 相关命令

- **查看 ACL**：

  ```bash
  getfacl 文件或目录路径
### 6. ACL 使用示例

假设：

    你想让用户 fred 访问目录 /home/neu/baosp，但不改变传统权限

操作(前提所属同一个组)：
```
sudo setfacl -m u:fred:rwx /home/neu/baosp
```

