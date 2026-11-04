---
tags: [tools, samba, ftp, filebrowser, linux]
updated: 2026-11-04
---
# File Sharing: Samba, FTP, FileBrowser

> [!summary] Summary
> 1. **Samba**: share a folder from Ubuntu to Windows
> 2. **FileBrowser**: web page for the same folder
> 3. **FTP**: client commands and the upload-corruption fix, plus a Win10 FTP server

---

## 1. Samba (Ubuntu)

### 1.1 Install

```bash
sudo apt update
sudo apt install samba -y
```

### 1.2 Share with everyone (no login)

Add to `/etc/samba/smb.conf`:

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

Folder permissions (**required**):

```bash
sudo chown -R nobody:nogroup /mnt/samsung4t/sharefolder
sudo chmod -R 777 /mnt/samsung4t/sharefolder

# Often not needed under /mnt; REQUIRED when the share is under /home/<user>
#
sudo chmod o+x /mnt
sudo chmod o+x /mnt/samsung4t
```

Then restart:

```bash
sudo systemctl restart smbd
```

> [!important] Why `o+x`: path traversal
> Linux resolves a path left to right, level by level. If any parent folder lacks the `x` permission, you can't "pass through" it. Even a `777` target below it fails with **Permission denied**.
>
> ```text
> Share under /home
> /               → does nobody have x? yes by default
>  └── home       → yes by default
>       └── neu   → ❌ NO by default → blocked here
>            └── ccs2 → never reached
> Fix: sudo chmod o+x /home/neu
>
> Share under /mnt
> /               → yes by default
>  └── mnt        → yes by default, no change needed
>       └── ccs2  → reached directly; just make sure ccs2's own permissions are enough
> ```

### 1.3 Two shares: PRV (hidden) and COMMON

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

> [!warning] `guest ok = yes` means no login
> If you want these shares to require an account, set `guest ok = no` and add a Samba user (`sudo smbpasswd -a <user>`). `browseable = no` only hides PRV from the list; it is **not** access control.

---

## 2. FileBrowser (web UI)

```bash
# Install; success shows "FileBrowser installed successfully"
curl -fsSL https://raw.githubusercontent.com/filebrowser/get/master/get.sh | bash

# Start the server
filebrowser -d /mnt/samsung4t/sharefolder/filebrowser.db -r /mnt/samsung4t/sharefolder -a 0.0.0.0 -p 8080

# Change the admin password
filebrowser users update admin --password "<new-password>" -d /mnt/samsung4t/sharefolder/filebrowser.db
```

| Option | Meaning |
|---|---|
| `-d` | Database file |
| `-r` | Root folder to serve |
| `-a 0.0.0.0` | Listen on all network interfaces |
| `-p 8080` | Port |

> [!warning] Two things to avoid
> - Don't write real passwords in notes. Use a placeholder like `<new-password>`.
> - The database sits **inside** the shared folder, so anyone with write access to the share can read or replace it. Consider keeping `filebrowser.db` outside the share (e.g. `/var/lib/filebrowser/`).

---

## 3. FTP

> [!tip] Files corrupted after upload? Use binary mode
> After connecting, type `bin` **first**, then upload.

| Command | Meaning |
|---|---|
| `bin` | Binary mode |
| `get <file>` | Download |
| `put <file>` | Upload |
| `lcd <dir>` | Change the **local** directory, like `cd` |

### Win10 as an FTP server (IIS)

> [!note]- Steps
> 1. Control Panel → Programs → **Turn Windows features on or off** → tick **FTP Service**, **FTP Extensibility** and **IIS Management Console** under *Internet Information Services*
> 2. Search for **IIS** and open IIS Manager
> 3. Right-click **Sites → Add FTP Site**
> 4. Enter a site name and the folder to serve
> 5. IP address = this PC's IP, SSL = **No SSL**
> 6. Choose authentication, authorization and permissions as needed
> 7. Control Panel → System and Security → Windows Firewall → **Allow an app or feature** → Change settings → tick **FTP Server** for Private and Public
> 8. **Allow another app** → `C:\Windows\System32\svchost.exe` → Add → OK
> 9. Test by opening `ftp://<IP>`
