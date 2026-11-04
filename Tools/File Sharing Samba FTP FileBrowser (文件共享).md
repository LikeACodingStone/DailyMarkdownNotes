---
tags: [tools, samba, ftp, filebrowser, linux]
updated: 2026-11-04
---
# File Sharing: Samba, FTP, FileBrowser [文件共享]

> [!summary] Summary [概要]
> 1. **Samba**: share a folder from Ubuntu to Windows [Ubuntu 共享目录给 Windows]
> 2. **FileBrowser**: web page for the same folder [同一目录的网页管理界面]
> 3. **FTP**: client commands and the upload-corruption fix, plus a Win10 FTP server [FTP 客户端命令与上传损坏的解决办法，以及 Win10 FTP 服务器]

---

## 1. Samba (Ubuntu)

### 1.1 Install [安装]

```bash
sudo apt update
sudo apt install samba -y
```

### 1.2 Share with everyone (no login) [所有人可访问（无需登录）]

Add to `/etc/samba/smb.conf`: [添加到 `/etc/samba/smb.conf`：]

```ini
[public]
   path = /mnt/samsung4t/sharefolder
   browseable = yes
   writable = yes
   guest ok = yes
   read only = no
   force user = nobody
   create mask = 0777
   directory mask = 0777
```

Folder permissions (**required** [必须设置]):

```bash
sudo chown -R nobody:nogroup /mnt/samsung4t/sharefolder
sudo chmod -R 777 /mnt/samsung4t/sharefolder

# Often not needed under /mnt; REQUIRED when the share is under /home/<user>
# [/mnt 下看情况可不加；共享目录在 /home/<user> 下则必须添加]
sudo chmod o+x /mnt
sudo chmod o+x /mnt/samsung4t
```

Then restart [然后重启]:

```bash
sudo systemctl restart smbd
```

> [!important] Why `o+x`: path traversal [为什么要 `o+x`：路径穿透原理]
> Linux resolves a path left to right, level by level. If any parent folder lacks the `x` permission, you can't "pass through" it. Even a `777` target below it fails with **Permission denied**.
> [Linux 查找文件是从左到右、层层递进的。只要某一级上级目录没有 `x` 权限，就无法"穿过"它；即使下面的目录是 777，也会报 **Permission denied**。]
>
> ```text
> Share under /home [共享目录在 /home 下]
> /               → does nobody have x? yes by default       [默认有]
>  └── home       → yes by default                           [默认有]
>       └── neu   → ❌ NO by default → blocked here          [默认没有！卡在这里报错]
>            └── ccs2 → never reached                        [根本走不到这一步]
> Fix [解决]: sudo chmod o+x /home/neu
>
> Share under /mnt [共享目录在 /mnt 下]
> /               → yes by default                           [默认允许]
>  └── mnt        → yes by default, no change needed         [默认允许，无需修改]
>       └── ccs2  → reached directly; just make sure ccs2's own permissions are enough
>                                                            [直接到达，只需确保 ccs2 自身权限足够]
> ```

### 1.3 Two shares: PRV (hidden) and COMMON [两个共享：隐藏的 PRV 与 COMMON]

```ini
[PRV]
   browseable = no
   path = /home/neusoft/share/Private
   guest ok = yes
   read only = no
   writable = yes
   create mask = 0644
   directory mask = 0755
   force directory mode = 0755
   force user = neusoft
   force group = neusoft
   available = yes

[COMMON]
   browseable = yes
   path = /home/neusoft/share/Common
   guest ok = yes
   writable = yes
   create mask = 0644
   directory mask = 0755
   force directory mode = 0755
   force user = neusoft
   force group = neusoft
   available = yes
```

> [!warning] `guest ok = yes` means no login [`guest ok = yes` 表示不需要登录]
> If you want these shares to require an account, set `guest ok = no` and add a Samba user (`sudo smbpasswd -a <user>`). `browseable = no` only hides PRV from the list; it is **not** access control.
> [如果希望共享需要账号，改成 `guest ok = no` 并添加 Samba 用户。`browseable = no` 只是在列表中隐藏，**不是**访问控制。]

---

## 2. FileBrowser (web UI) [网页管理界面]

```bash
# Install; success shows "FileBrowser installed successfully" [安装，成功会显示 FileBrowser installed successfully]
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

# Start the server [启动服务]
filebrowser -d /mnt/samsung4t/sharefolder/filebrowser.db -r /mnt/samsung4t/sharefolder -a 0.0.0.0 -p 8080

# Change the admin password [修改密码]
filebrowser users update admin --password "<new-password>" -d /mnt/samsung4t/sharefolder/filebrowser.db
```

| Option [参数] | Meaning [含义] |
|---|---|
| `-d` | Database file [数据库文件] |
| `-r` | Root folder to serve [共享根目录] |
| `-a 0.0.0.0` | Listen on all network interfaces [监听所有网卡] |
| `-p 8080` | Port [端口] |

> [!warning] Two things to avoid [两点注意]
> - Don't write real passwords in notes. Use a placeholder like `<new-password>`. [不要把真实密码写进笔记]
> - The database sits **inside** the shared folder, so anyone with write access to the share can read or replace it. Consider keeping `filebrowser.db` outside the share (e.g. `/var/lib/filebrowser/`). [数据库放在共享目录**里面**，有写权限的人都能读取或替换；建议放到共享目录之外]

---

## 3. FTP

> [!tip] Files corrupted after upload? Use binary mode [上传后文件损坏？用二进制模式]
> After connecting, type `bin` **first**, then upload. [连接后**先输入 `bin`**，再上传。]

| Command [命令] | Meaning [含义] |
|---|---|
| `bin` | Binary mode [二进制模式] |
| `get <file>` | Download [下载] |
| `put <file>` | Upload [上传] |
| `lcd <dir>` | Change the **local** directory, like `cd` [切换**本地**目录，相当于 `cd`] |

### Win10 as an FTP server (IIS) [Win10 开启 FTP 服务]

> [!note]- Steps [步骤]
> 1. Control Panel → Programs → **Turn Windows features on or off** → tick **FTP Service**, **FTP Extensibility** and **IIS Management Console** under *Internet Information Services*
>    [控制面板 → 程序 → 启用或关闭 Windows 功能 → 勾选 FTP 服务、FTP 扩展性、IIS 管理控制台]
> 2. Search for **IIS** and open IIS Manager [搜索 IIS 并打开]
> 3. Right-click **Sites → Add FTP Site** [右击网站 → 添加 FTP 站点]
> 4. Enter a site name and the folder to serve [输入站点名称和作为 FTP 的目录]
> 5. IP address = this PC's IP, SSL = **No SSL** [IP 填本机 IP，选择无 SSL]
> 6. Choose authentication, authorization and permissions as needed [按需选择身份验证、授权与权限]
> 7. Control Panel → System and Security → Windows Firewall → **Allow an app or feature** → Change settings → tick **FTP Server** for Private and Public
>    [防火墙 → 允许应用或功能 → 更改设置 → 勾选 FTP 服务器（专用 + 公用）]
> 8. **Allow another app** → `C:\Windows\System32\svchost.exe` → Add → OK [允许其他应用 → 选择 svchost.exe → 添加 → 确定]
> 9. Test by opening `ftp://<IP>` [浏览器 / 资源管理器打开 `ftp://<IP>` 测试]
