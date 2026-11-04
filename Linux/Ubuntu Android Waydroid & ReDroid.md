---
tags: [ubuntu, linux, android, waydroid, redroid, docker, scrcpy]
updated: 2026-11-04
---
# Run Android on Ubuntu: Waydroid & ReDroid

> [!summary] Summary
> Two ways to run Android apps on a **headless / remote** Ubuntu.

| | **Waydroid** | **ReDroid** |
|---|---|---|
| How | Android in a container, shown with a Wayland compositor (`weston` / `cage`) | Android in **Docker**, shown with `scrcpy` over ADB |
| Fits | Needs a **Wayland** session (nested with weston / cage) | **xrdp + MATE (X11)** works fine |
| Section | 1 | 2 |

> [!tip] Why ReDroid for xrdp
> Waydroid needs Wayland but xrdp defaults to X11; traditional emulators (Genymotion, VirtualBox) lag or show a black screen in xrdp because there is no 3D acceleration. ReDroid has neither problem.

---

## 1. Waydroid (no monitor)

### 1.1 Install

**Add the official repository** (`noble` = Ubuntu 24.04):

```bash
sudo apt update
sudo apt install -y curl ca-certificates

curl -s https://repo.waydro.id/waydroid.gpg | sudo tee /usr/share/keyrings/waydroid.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/waydroid.gpg] https://repo.waydro.id/ noble main" | sudo tee /etc/apt/sources.list.d/waydroid.list
sudo apt update
```

**Install Waydroid + Weston** (Weston = nested Wayland compositor):

```bash
sudo apt install -y waydroid weston
```

**Initialise the container**

```bash
sudo waydroid init
# With Google Play services (GApps):
# sudo waydroid init -s GAPPS
```

**Enable the service**

```bash
sudo systemctl enable waydroid-container.service
sudo systemctl start waydroid-container.service
```

### 1.2 Start & stop

```bash
# Start Weston, then inside the Weston terminal:
weston
waydroid show-full-ui
```

```bash
# Stop
sudo systemctl stop waydroid-container.service
waydroid session stop
```

**Switch to `cage`**

```bash
sudo apt install cage
cage waydroid show-full-ui
```

> [!tip] If Weston crashes, use `cage`
> With `cage`, the network doesn't drop when the window size changes.

### 1.3 Resolution

```bash
# With Weston
sudo waydroid prop set persist.waydroid.width 1920
sudo waydroid prop set persist.waydroid.height 1080
```

> [!warning] In `cage`: set it after Android is fully started, and **never use `sudo`**
> ```bash
> waydroid prop set persist.waydroid.width 720
> waydroid prop set persist.waydroid.height 720
> waydroid prop set persist.waydroid.dpi 320
> ```

### 1.4 Register the device (GApps)

```bash
sudo waydroid shell
```

Inside the shell, print the device ID and copy it:

```bash
ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"
```

Register it at https://www.google.com/android/uncertified, then **restart Waydroid**.

### 1.5 Start / stop scripts

```bash
# Start
sudo systemctl start waydroid-container.service
cage waydroid show-full-ui

# Stop
waydroid session stop
sudo systemctl stop waydroid-container.service
```

---

## 2. ReDroid in Docker + scrcpy (xrdp + MATE) [ReDroid + scrcpy]

Example: install the **YTDLnis** APK on Ubuntu 24.04 + xrdp + MATE.

> [!bug] Two errors you will meet
> **1. `Emulate Docker CLI using podman` + `short-name "redroid/redroid:11.0.0-latest" did not resolve to an alias`**
> The `docker` command is really Podman (package `podman-docker`). → Remove Podman and install real Docker (steps 1 and 2).
>
> **2. `adb connect localhost:5555` → `Connection refused`**
> The container didn't boot: Ubuntu 24.04 doesn't load the Android **binder** modules by default. → Load `binder_linux` (step 3).

**1. Remove Podman**

```bash
sudo apt remove podman buildah skopeo -y
sudo apt autoremove -y
```

**2. Install native Docker**

```bash
curl -fsSL https://get.docker.com | sh
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
newgrp docker                      # or reconnect the xrdp session
```

**3. Load the binder kernel module**

```bash
sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"

# If the module isn't found:
sudo apt install linux-modules-extra-$(uname -r)
sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"
```

**4. Run the ReDroid container (Android 11)**

```bash
docker run -d -p 5555:5555 \
    --name redroid \
    --privileged \
    -v ~/redroid-data:/data \
    docker.io/redroid/redroid:11.0.0-latest
```

**5. Install the tools**

```bash
sudo apt update
sudo apt install scrcpy adb -y
```

**6. Connect and install the APK**, after waiting 10 to 15 seconds for Android to start:

```bash
adb connect localhost:5555
adb devices                        # expect: localhost:5555   device
adb install ~/tools/ytdlnis.apk
```

**7. Open the Android screen**

```bash
scrcpy -s localhost:5555
```

A lightweight Android window appears inside your xrdp desktop.
