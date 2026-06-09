# Ubuntu 24.04 XRDP + MATE: Installing and Running Android APK (YTDLnis)

This guide provides a comprehensive step-by-step walkthrough for installing and running Android APK files (such as **YTDLnis**) on an **Ubuntu 24.04** system running a **MATE Desktop environment via XRDP remote desktop connection**.

It also documents the installation issues encountered during setup (such as Podman emulation issues and ADB connection failures) and explains how to resolve them.

---

## Technical Overview & Challenges

Running Android applications on a remote Linux server via XRDP presents two primary challenges:

1. **Wayland Compatibility**  
   Popular tools like **Waydroid** require a Wayland session. However, XRDP defaults to **X11**, which causes compatibility issues.

2. **GPU Acceleration**  
   Traditional emulators (such as **Genymotion** or **VirtualBox**) may experience severe lag or black screens in XRDP sessions due to missing 3D hardware acceleration.

### Recommended Solution

Use **ReDroid (Remote Android in Docker)**.

ReDroid runs a lightweight, headless Android container inside Docker and streams only the Android UI through `scrcpy` over ADB, resulting in smoother performance in XRDP environments.

---

# Troubleshooting

## Error 1: Podman Emulation Issue

### Symptom

```bash
xdrp@ccs0:~/tools$ sudo docker run -d -p 5555:5555 ...
Emulate Docker CLI using podman.
Create /etc/containers/nodocker to quiet msg.

Error: short-name "redroid/redroid:11.0.0-latest"
did not resolve to an alias...
```

### Cause

The system was using `podman-docker`, which aliases the `docker` command to Podman.

Podman uses stricter sandboxing and often fails with:
- image short-name resolution issues
- container runtime errors
- missing registry configuration

### Fix

Completely remove Podman and install the native Docker Engine.

---

## Error 2: ADB Connection Refused

### Symptom

```bash
xdrp@ccs0:~/tools$ adb connect localhost:5555
Connection refused
```

### Cause

The Android container failed to boot correctly, or required Android kernel modules were not loaded.

Ubuntu 24.04 may not load required Android Binder modules by default.

### Fix

Manually load the required kernel module (`binder_linux`).

---

# Step-by-Step Installation Guide

## Step 1 — Remove Podman and Clean the Environment

To avoid Docker/Podman conflicts:

```bash
sudo apt remove podman buildah skopeo -y
sudo apt autoremove -y
```

---

## Step 2 — Install Native Docker Engine

Install official Docker components:

```bash
# Download and run the official Docker installation script
curl -fsSL https://get.docker.com | sh

# Start and enable Docker daemon
sudo systemctl start docker
sudo systemctl enable docker

# Add current user to docker group
sudo usermod -aG docker $USER
```

### Apply Group Changes

Either reconnect your XRDP session or run:

```bash
newgrp docker
```

---

## Step 3 — Load Required Android Kernel Modules

Ubuntu 24.04 requires Binder drivers for Android container communication.

Run:

```bash
sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"
```

If the module cannot be found:

```bash
sudo apt install linux-modules-extra-$(uname -r)
```

Then rerun:

```bash
sudo modprobe binder_linux devices="binder,hwbinder,vndbinder"
```

---

## Step 4 — Run the ReDroid Android Container

Deploy Android 11 container:

```bash
docker run -d -p 5555:5555 \
    --name redroid \
    --privileged \
    -v ~/redroid-data:/data \
    docker.io/redroid/redroid:11.0.0-latest
```

---

## Step 5 — Install Required Desktop Tools

Install `adb` and `scrcpy`:

```bash
sudo apt update
sudo apt install scrcpy adb -y
```

---

## Step 6 — Connect to Android and Install YTDLnis APK

Wait approximately **10–15 seconds** for Android initialization.

### Connect ADB

```bash
adb connect localhost:5555
```

### Verify Device Status

```bash
adb devices
```

Expected output:

```text
localhost:5555 device
```

### Install APK

```bash
adb install ~/tools/ytdlnis.apk
```

---

## Step 7 — Launch Android UI

Open the Android interface inside your XRDP MATE desktop:

```bash
scrcpy -s localhost:5555
```

A lightweight Android desktop window should appear.

You can now use **YTDLnis** with mouse and keyboard directly in your Ubuntu XRDP environment.

---

# Summary

This setup avoids:

- Wayland compatibility issues
- Heavy emulator lag
- GPU passthrough problems in XRDP

By combining:

- **Docker**
- **ReDroid**
- **ADB**
- **scrcpy**

You get a lightweight Android environment suitable for remote Ubuntu desktops.
