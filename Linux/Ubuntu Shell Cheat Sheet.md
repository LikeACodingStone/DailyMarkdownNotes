---
tags: [ubuntu, linux, shell, cheat-sheet]
updated: 2026-11-04
---
# Ubuntu Shell Cheat Sheet

> [!summary] Contents
> 1. Terminal shortcuts & boot mode
> 2. SSH & copying files
> 3. RPM packages
> 4. Shared libraries (`.so`)
> 5. Vim fixes
> 6. Small tools: VirtualBox / Qt / audio
>
> Searching and counting files: see [[Ubuntu-quick-search]]

---

## 1. Terminal Shortcuts & Boot Mode

| Key | Action |
|---|---|
| `Ctrl + Shift + T` | Open a new terminal tab |
| `Ctrl + PgUp` / `Ctrl + PgDn` | Switch tabs |

```bash
# Boot to the terminal only (no desktop)
sudo systemctl set-default multi-user.target
# Back to the desktop
sudo systemctl set-default graphical.target
```

---

## 2. SSH & Copying Files

### Remove a stale host key

```bash
ssh-keygen -R <hostname-or-ip>
```

> [!note] About the old "ssh timeout → delete `known_hosts`" tip
> It worked for you, so a stale host key was the cause. Prefer `ssh-keygen -R`, which removes **only that host** instead of the whole file.
> A real timeout (no reply at all) is usually a network or firewall problem; a changed key shows `REMOTE HOST IDENTIFICATION HAS CHANGED`.

### Copy files

```bash
# Local → remote
scp <file> <user>@<host>:<remote_dir>/

# rsync: -a archive, -v verbose, -h human-readable
rsync -avh <local_dir> <user>@<host>:<remote_dir>/

# Example
rsync -avh CEODiary_New ccs2@172.30.2.200:/home/ccs2/Desktop/ytbMedia/Resource/chineseTTS/
```

---

## 3. RPM Packages

```bash
# Convert .rpm → .deb, then install the .deb
sudo alien jdk-18_linux-x64_bin.rpm

# Or install the .rpm directly (needs the rpm tool)
rpm -ivh jdk-18_linux-x64_bin.rpm
```

---

## 4. Shared Libraries (`.so`)

```bash
# 1. Add the library folder to the config
echo "/path/to/lib" | sudo tee -a /etc/ld.so.conf
#    (or put a file in /etc/ld.so.conf.d/)

# 2. Rebuild the cache
sudo ldconfig

# 3. Check
ldconfig -p | grep <libname>
```

> [!note] Plain `sudo ldconfig`
> `ldconfig` reads `/etc/ld.so.conf` by itself. The old note ran `ldconfig /etc/ld.so.conf`, which passes the config file as if it were a folder to scan.

---

## 5. Vim Fixes

### `^M` characters (Windows line endings)

- Type one: `Ctrl + V`, then `Ctrl + M`
- Remove them from a file:

```bash
fromdos <filename>      # package: tofrodos
```

### Arrow keys print letters in Vim

Edit `/etc/vim/vimrc.tiny`:

1. Change `set compatible` (second to last line) to `set nocompatible`
2. Add a new line below it: `set backspace=2`

---

## 6. Small Tools

```bash
# VirtualBox shared-folder permission problem
sudo usermod -aG vboxsf $(whoami)        # then log out and back in

# Qt: generate a lib project
qmake -project -t lib

# Audio
arecord -l                               # list microphones: card 0 / card 1 ...
alsamixer -c 0                           # mixer of sound card 0
```
