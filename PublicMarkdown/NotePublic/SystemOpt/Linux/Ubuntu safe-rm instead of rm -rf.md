# Safe-rm Quick Reference

## Overview

`safe-rm` is a wrapper around the standard `rm` command. It prevents accidental deletion of important files or directories by checking a list of protected paths before executing the removal.

Unlike a trash/recycle-bin utility, **safe-rm does not recover deleted files**. It simply refuses to delete files or directories that match its configuration.

---

# 1. Install safe-rm

Ubuntu / Debian

```bash
sudo apt update
sudo apt install safe-rm
```

Verify installation:

```bash
which safe-rm
```

Expected output:

```text
/usr/bin/safe-rm
```

Check version:

```bash
safe-rm --version
```

or

```bash
safe-rm --help
```

---

# 2. Check Whether rm Uses safe-rm

Check the current rm executable:

```bash
which rm
```

or

```bash
type rm
```

If the output is:

```text
/usr/bin/rm
```

then the original GNU `rm` is still being used.

---

# 3. Replace rm with safe-rm (Recommended)

Create a symbolic link:

```bash
sudo ln -sf /usr/bin/safe-rm /usr/local/bin/rm
```

Refresh the shell command cache:

```bash
hash -r
```

Or simply open a new terminal.

Verify:

```bash
which rm
```

Expected:

```text
/usr/local/bin/rm
```

Check the symbolic link:

```bash
ls -l /usr/local/bin/rm
```

Expected:

```text
/usr/local/bin/rm -> /usr/bin/safe-rm
```

---

# 4. Check PATH Priority

Ensure `/usr/local/bin` appears before `/usr/bin`.

```bash
echo $PATH
```

Example:

```text
/usr/local/bin:/usr/bin:/bin
```

If `/usr/local/bin` comes after `/usr/bin`, the symbolic link will not take effect.

---

# 5. Configuration Files

## System-wide configuration

Configuration file:

```text
/etc/safe-rm.conf
```

Edit:

```bash
sudo vi /etc/safe-rm.conf
```

---

## User configuration (if supported)

Some distributions also support:

```text
~/.config/safe-rm
```

Create it if it does not exist:

```bash
mkdir -p ~/.config
vi ~/.config/safe-rm
```

---

# 6. Protect Directories

Each line contains one protected path.

Example:

```text
/
/boot
/etc
/usr
/home
/home/dpc
/home/dpc/Documents
/home/dpc/Documents/*
```

It is recommended to protect both:

```text
/path
/path/*
```

This protects the directory itself and everything inside it.

---

# 7. Test Configuration

Suppose the following directory is protected:

```text
/home/dpc/Documents
```

Run:

```bash
rm -rf ~/Documents
```

Expected:

```text
safe-rm: Skipping /home/dpc/Documents
```

The directory will not be deleted.

---

# 8. Useful Commands

## Check safe-rm location

```bash
which safe-rm
```

---

## Check rm location

```bash
which rm
```

---

## Check rm type

```bash
type rm
```

---

## Check symbolic link

```bash
ls -l /usr/local/bin/rm
```

---

## Display PATH

```bash
echo $PATH
```

---

## View system configuration

```bash
cat /etc/safe-rm.conf
```

---

## Edit system configuration

```bash
sudo vi /etc/safe-rm.conf
```

---

## View user configuration

```bash
cat ~/.config/safe-rm
```

---

## Edit user configuration

```bash
vi ~/.config/safe-rm
```

---

## Check manual

```bash
man safe-rm
```

---

# 9. Remove the Replacement

Restore the original `rm` command:

```bash
sudo rm /usr/local/bin/rm
hash -r
```

Verify:

```bash
which rm
```

Expected:

```text
/usr/bin/rm
```

---

# 10. Recommended Protected Paths

### For Linux Development

```text
/
/boot
/etc
/usr
/usr/*
/opt
/var
/home
/home/dpc
/home/dpc/Desktop
/home/dpc/Documents
```

### For Android (AOSP) Development

```text
/ssd/aosp
/ssd/aosp/*
```

or

```text
/home/dpc/aosp
/home/dpc/aosp/*
```

---

# 11. Troubleshooting

### Check whether the symbolic link exists

```bash
ls -l /usr/local/bin/rm
```

### Verify that the shell is using the new rm

```bash
which rm
type rm
```

### Refresh the shell cache

```bash
hash -r
```

or simply open a new terminal.

### Verify PATH order

```bash
echo $PATH
```

`/usr/local/bin` should appear before `/usr/bin`.

---

# 12. Limitations

`safe-rm` only checks the command-line arguments passed to `rm`.

For example, this command will be blocked if `/home/dpc/Documents` is protected:

```bash
rm -rf ~/Documents
```

However, the following command **will not** be blocked:

```bash
cd ~/Documents
rm -rf *
```

This happens because `safe-rm` checks the arguments passed to `rm` (the expanded filenames), not the current working directory.

Therefore, `safe-rm` is a safeguard against accidental `rm` commands, **not** a complete file protection solution.

---

# 13. Summary

| Task | Command |
|------|---------|
| Install | `sudo apt install safe-rm` |
| Locate safe-rm | `which safe-rm` |
| Locate rm | `which rm` |
| Check rm type | `type rm` |
| Replace rm | `sudo ln -sf /usr/bin/safe-rm /usr/local/bin/rm` |
| Refresh shell | `hash -r` |
| Check symbolic link | `ls -l /usr/local/bin/rm` |
| Show PATH | `echo $PATH` |
| Edit system config | `sudo vi /etc/safe-rm.conf` |
| View system config | `cat /etc/safe-rm.conf` |
| Edit user config | `vi ~/.config/safe-rm` |
| View user config | `cat ~/.config/safe-rm` |
| Show manual | `man safe-rm` |
| Restore original rm | `sudo rm /usr/local/bin/rm` |