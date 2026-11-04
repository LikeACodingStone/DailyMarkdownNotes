---
tags: [ubuntu, linux, apt, snap, flatpak, dpkg, npm]
updated: 2026-11-04
---
# Ubuntu Packages

> [!summary] Contents
> 1. Install with snap / flatpak / dpkg
> 2. Remove a package installed from a `.deb`
> 3. Handy apps
> 4. npm global install without `sudo`
> 5. A `.sh` launcher fails: SmartGit
> 6. Buildozer (Kivy → APK)

---

## 1. snap / flatpak / dpkg

```bash
# snap
sudo snap install android-studio --classic

# dpkg: list the files a package installed
dpkg -L smartgit
```

**flatpak: install Firefox**

```bash
sudo apt update
sudo apt install flatpak -y
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.mozilla.firefox
sudo reboot

# Run
flatpak run org.mozilla.firefox
```

---

## 2. Remove a Package Installed from a `.deb`

```bash
# 1. Read the package name from the .deb file
dpkg -f ./superProductivity-amd64.deb Package      # prints: superproductivity

# 2. Remove it
sudo apt-get remove superproductivity
```

---

## 3. Handy Apps

```bash
# bat: syntax-highlighted file viewer for terminals, e.g. over Xshell/SSH
sudo apt install bat          # the package is `bat`, the command is `batcat`
batcat <file>

# Markdown
sudo apt install pandoc
xdg-open README.md            # open with the default app
sudo apt install ghostwriter  # GUI Markdown editor
```

> [!warning] Typos fixed in the old note
> `apt install batcat` fails (the package is `bat`), and `ghoshwriter` is really `ghostwriter`.

**seahorse** is a GUI app ("Passwords and Keys") for managing **passwords, SSH keys, GPG keys and certificates**.

---

## 4. npm Global Install Without `sudo`

> [!bug] Symptom
> `npm install -g <package>` fails with `EACCES: permission denied`, because normal users can't write to `/usr/local/lib/node_modules`.

**Fix: move the global folder into your home**

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

npm install -g @openai/codex        # example; no sudo needed
```

Verify:

```bash
npm prefix -g              # should be ~/.npm-global
npm list -g --depth=0      # installed global packages
```

> [!warning] Don't keep using `sudo npm install -g`
> It creates root-owned files and more permission problems later.

---

## 5. A `.sh` Launcher Fails: SmartGit

> [!tip] General method
> When a program's `.sh` start script fails, add an `echo` to see what it actually runs.

1. Add to `/usr/share/smartgit/bin/smartgit.sh`:

```bash
echo "SmartGit is trying to execute: $_JAVA_EXEC"
```

2. Output:

```text
SmartGit is trying to execute: /usr/share/smartgit/jre/bin/java
```

3. **Cause:** SmartGit uses its own bundled JRE. **Fix:** remove that bundled `jre` folder so it falls back to the system Java.

> [!caution] Rename instead of delete first
> `sudo mv /usr/share/smartgit/jre /usr/share/smartgit/jre.bak`, and make sure a system Java is installed.

---

## 6. Buildozer: Python (Kivy) → Android APK

> [!note]- Old install steps (check the Buildozer docs for current versions)
> ```bash
> sudo apt install python3-pip
> pip3 install --user --upgrade buildozer
> git clone https://github.com/kivy/buildozer.git
> cd buildozer
> sudo python setup.py install
> sudo apt update
> sudo apt install -y git zip unzip openjdk-8-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
> pip3 install --user --upgrade Cython==0.29.19 virtualenv    # or install Cython yourself
> buildozer -v android debug                                   # downloads the Android NDK
> ```
