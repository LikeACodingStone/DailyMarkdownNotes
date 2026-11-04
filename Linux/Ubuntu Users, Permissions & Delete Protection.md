---
tags: [ubuntu, linux, permissions, acl, chattr, safe-rm]
updated: 2026-11-04
---
# Ubuntu Users, Permissions & Delete Protection

> [!summary] Contents
> 1. Users & groups
> 2. Run a program with its owner's rights (setuid)
> 3. ACL: per-user permissions
> 4. Delete protection: sticky bit / `chattr` / `safe-rm`

---

## 1. Users & Groups

```bash
# Create a group and users
sudo groupadd ccs2grp
sudo adduser ccs1
sudo adduser ccs2
sudo adduser ccs3

# Add a user to a group
sudo usermod -aG ccs2grp ccs1

# Give a user admin rights
sudo usermod -aG sudo ccs1

# Give a user + group ownership of a path
sudo chown -R ccs1:ccs2grp /path/to/dir

# Change the group only
sudo chgrp -R ccs2grp /path/to/dir
```

---

## 2. Run a Program With Its Owner's Rights (setuid)

```bash
which openconnect                      # e.g. /usr/sbin/openconnect
sudo chmod u+s /usr/sbin/openconnect   # normal users now run it as root
```

> [!warning] setuid = every local user runs it as root
> Only do this for tools you trust, and never for scripts or editors.

---

## 3. ACL: Per-User Permissions

Normal permissions only cover **owner / group / others**. An **ACL** adds extra entries for any single user or group, and the system checks the ACL first.

```bash
getfacl <path>                      # view
setfacl -m u:fred:rwx <path>        # give user fred rwx
setfacl -m g:devs:rx <path>         # give a group
setfacl -R -m u:fred:rwx <dir>      # recursive
setfacl -x u:fred <path>            # remove one entry
setfacl -b <path>                   # remove all ACL entries
```

**Example:** let `fred` use `/home/neu/baosp` without changing the normal permissions (both users in the same group):

```bash
sudo setfacl -m u:fred:rwx /home/neu/baosp
```

> [!tip] Parent folders need `x` too
> `fred` must also be able to pass through `/home/neu`. Linux walks a path level by level; a parent folder without `x` blocks access, even to a `777` target. See [[File Sharing Samba FTP FileBrowser]].

---

## 4. Delete Protection

| Goal | Use |
|---|---|
| Stop a typo like `rm -rf` in the terminal | **safe-rm** (4.3) |
| Nobody (even root) can modify or delete a path | **`chattr +i`** (4.2) |
| In a shared folder, others can't delete your files | **sticky bit** (4.1) |

### 4.1 Sticky bit: protect from deletion in the GUI file manager

```bash
sudo chown -R root:root ~/ccs2

# Sticky bit (1) + read/write/execute for all (777)
sudo chmod -R 1777 ~/ccs2
```

With the sticky bit, users can only delete **their own** files in the folder (like `/tmp`).

### 4.2 `chattr`: file attributes

`chattr` sets extended attributes, a level above `chmod` (ext2/3/4 only).

| Attribute | Effect |
|---|---|
| `+i` immutable | No modify, delete, rename; in a folder, no adding or removing files |
| `+a` append-only | Only append with `>>`, no overwrite with `>`, no delete. Good for log files |

```bash
sudo chattr +i <file>        # set
sudo chattr -i <file>        # unset
sudo chattr -R +i <dir>      # recursive
sudo chattr +a <logfile>     # append-only

lsattr <file>                # view
lsattr -d <dir>              # the folder itself
lsattr -aR <dir>             # recursive, including . and ..
```

For a root-protected folder: `sudo chattr +i ~/ccs2`.

> [!important] Why a parent's `i` blocks deleting the child
> Deleting `parent/child` actually **modifies `parent`**, not the child. So if the **parent** has `i`, you can't delete anything inside it. If `child` has `i`, only `child` itself can't be deleted.

> [!bug] `rm` says `Operation not permitted`?
> Run `lsattr -aR <dir>`. An `i` on `dir/.` means the folder is immutable; on `dir/..` it means the **parent** is.

### 4.3 `safe-rm`: block dangerous `rm`

`safe-rm` wraps `rm` and **refuses** to delete protected paths. It is **not** a recycle bin and can't restore anything.

**Install and replace `rm`**

```bash
sudo apt install safe-rm
sudo ln -sf /usr/bin/safe-rm /usr/local/bin/rm
hash -r                        # refresh the shell cache, or open a new terminal

which rm                       # expect /usr/local/bin/rm
echo $PATH                     # /usr/local/bin must come BEFORE /usr/bin
```

**Protect paths**

- System-wide: `/etc/safe-rm.conf` (`sudo vi /etc/safe-rm.conf`); per-user: `~/.config/safe-rm`
- One path per line. Protect both `/path` and `/path/*` (the folder itself and its contents)

```text
/
/boot
/etc
/usr
/usr/*
/opt
/var
/home
/home/dpc/Desktop
/home/dpc/Documents
/home/dpc/Documents/*
# AOSP
/ssd/aosp
/ssd/aosp/*
```

**Test**

```bash
rm -rf ~/Documents
# safe-rm: Skipping /home/dpc/Documents
```

**Remove the replacement**

```bash
sudo rm /usr/local/bin/rm && hash -r
which rm                       # expect /usr/bin/rm
```

> [!warning] Limitation: it only checks the arguments
> `rm -rf ~/Documents` is blocked, but this is **not**:
> ```bash
> cd ~/Documents
> rm -rf *
> ```
> `safe-rm` sees the expanded file names, not the current folder. It guards against typos, not against everything.
