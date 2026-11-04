---
tags: [ubuntu, linux, vpn, openconnect, desktop-entry]
updated: 2026-11-04
---
# Ubuntu VPN & Custom Launchers

> [!summary] Summary
> Make a clickable desktop icon that connects your VPN. Two examples: **OpenConnect (AnyConnect)** and an **auto-login script**.

> [!warning] Company details
> Real user IDs were replaced with placeholders. Keep the VPN host and any internal paths out of public Gists.

---

## 1. How a Launcher Works

A launcher is a `.desktop` file. Put it in `~/.local/share/applications/`, then refresh:

```bash
cp my_app.desktop ~/.local/share/applications/
update-desktop-database ~/.local/share/applications
```

Template:

```ini
[Desktop Entry]
Version=1.0
Name=<name shown in the menu>
Comment=<description>
Exec=sh /path/to/script.sh
Icon=/path/to/icon.png
Terminal=true
Type=Application
Categories=Utility;
```

`Terminal=true` opens a terminal window, so `sudo` can ask for a password and you can see the output.

Reference: https://blog.csdn.net/u010329292/article/details/128755379

---

## 2. Example 1: OpenConnect VPN

`boschVPN.desktop`

```ini
[Desktop Entry]
Version=1.0
Name=boschVPN
Comment=connect to bosch with <vpn-user>
Exec=sh /home/<user>/user/bin/VPNFiles/connectVpn.sh
Icon=/home/<user>/user/bin/VPNFiles/boschIcon.png
Terminal=true
Type=Application
Categories=Utility;
```

`connectVpn.sh`

```bash
# Switch to the company git identity
cp gitconfig/.gitconfig-bosch ~/.gitconfig

# Connect
sudo openconnect --protocol=anyconnect --useragent=AnyConnect -u <vpn-user> rasvpn-ext-emea.bosch.com/rbextssl
```

> [!caution] Two small things
> - `cp` already overwrites, so the old `rm ~/.gitconfig` line is not needed (and deletes your config if the next `cp` fails).
> - `gitconfig/.gitconfig-bosch` is a **relative** path: it only works if the script runs from the folder that contains `gitconfig/`. Use an absolute path to be safe.

---

## 3. Example 2: Auto-Login Script

**Prepare:**

```bash
sudo apt update
sudo apt install python3-evdev
```

**Files:**

| File | Purpose |
|---|---|
| `vpn_login.py` | The login script: [vpn_auto_login (Gist)](https://gist.github.com/LikeACodingStone/9d6d57b31ed273c12de439340a9ca91a) |
| `run_vpn.sh` | Starts it with `sudo` |
| `vpn_icon.desktop` | The desktop icon |

> [!warning] The Gist file name and the name in `run_vpn.sh` differ
> The Gist is called `vpn_auto_login.py`, but the script runs `vpn_login.py`. Pick one name and use it everywhere.

### `run_vpn.sh`: don't store your sudo password in the script

The old version put the password in a variable (`SYS_PASS`) and piped it into `sudo -S`. Anyone who can read the file gets your sudo password, and it ends up in backups and Git.

**Option A, simple and safe**: let `sudo` ask in the terminal window (`Terminal=true`):

```bash
#!/bin/bash
# Folder of this script, so vpn_login.py is found next to it
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo python3 "$SCRIPT_DIR/vpn_login.py"
```

**Option B, no password prompt**: allow only this one command in `sudoers`.

```bash
sudo visudo -f /etc/sudoers.d/vpn-login
```

```text
<user> ALL=(root) NOPASSWD: /usr/bin/python3 /home/<user>/scripts/vpn_login.py
```

> [!danger] The script must not be writable by you
> With option B, whoever can edit `vpn_login.py` gets root. Make it root-owned: `sudo chown root:root vpn_login.py && sudo chmod 755 vpn_login.py`.

### `vpn_icon.desktop`

```ini
[Desktop Entry]
Version=1.0
Name=vpn
Comment=connect to vpn
Exec=bash /home/<user>/scripts/run_vpn.sh
Icon=/home/<user>/scripts/Icon.png
Terminal=true
Type=Application
Categories=Utility;
```

Then install it as in section 1.
