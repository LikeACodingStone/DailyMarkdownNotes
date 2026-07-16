# Bosch CCS2 Android 14 (A14) Development Guide

> [!IMPORTANT]
> **Confidentiality Notice:** This document contains internal project configurations and VPN credentials. Use only within authorized environments.

---

## 📂 Table of Contents
1. [Network Connectivity (VPN)](#network-connectivity-vpn)
2. [Environment Initialization & Sync](#environment-initialization-sync)
3. [Version Rollback & Deep Cleanup](#version-rollback-cleanup)
4. [Internal Project Dashboards & Resources](#internal-project-dashboards)
---

<a id="network-connectivity-vpn"></a>
## 1. 🌐 Network Connectivity (VPN)

Ensure you are connected to the correct Bosch gateway before executing `repo sync`.

### 🔹 Method A: Cisco Secure Client (GUI) - Recommended for Windows/macOS

#### (1). Installation
1. **Download:** Obtain the `Cisco Secure Client` (formerly AnyConnect) installer from the internal Bosch IT portal.
2. **Execute:** Run the installer and follow the wizard. Ensure the **"VPN"** module is selected during installation.
3. **Profile Setup:** - Navigate to: `C:\ProgramData\Cisco\Cisco Secure Client\Profile` (Windows) or `/opt/cisco/anyconnect/profile/` (Linux).
   - Copy the provided `VPN_Cisco_ACP_RB_EXT.xml` file into this folder to pre-configure the server list.

#### (2). Launch & Connect
1. **Start:** Search for "Cisco Secure Client" in your application menu and launch it.
2. **Select Gateway:** From the drop-down menu, choose your closest location:
   * **EMEA Node:** `rasvpn-ext-emea.bosch.com`
   * **APAC Node:** `rasvpn-apac-sgp-ext.bosch.com`
   * **Americas Node:** `rasvpn-ext-americas.bosch.com`
3. **Authenticate:** - **User Group:** Select `TG_RBExt_AAD`.
   - **Credentials:** Enter your Bosch Username and your PIN + Tokencode (Microsoft MFA).
4. **Status:** Once the icon in the tray bar shows a locked padlock, your connection is active.

***
### 🔹 Method B: OpenConnect (CLI) - Preferred for Linux Developers
### 🇩🇪 EMEA Node (Germany)
```bash
sudo openconnect --protocol=anyconnect --useragent=AnyConnect -u zhs2yh [rasvpn-ext-emea.bosch.com/rbextssl](https://rasvpn-ext-emea.bosch.com/rbextssl)
```
### 🇯🇵 APAC Node (Japan)
```
sudo openconnect --protocol=anyconnect --useragent=AnyConnect -u zhs2yh [rasvpn-apac-sgp-ext.bosch.com/rbextssl](https://rasvpn-apac-sgp-ext.bosch.com/rbextssl)
```
***
<a id="environment-initialization-sync"></a>
## 2. 🚀 Environment Initialization & Sync

For **Android 14 (A14)**, follow the standard initialization and synchronization sequence:

### 🔹 Step 1: Initialize Manifest
```bash
repo init -u ssh://[rbcm-gerrit.de.bosch.com:29418/projects/ccs2/manifests](https://rbcm-gerrit.de.bosch.com:29418/projects/ccs2/manifests) -b ccs2_a14_vf_int
```
### 🔹 Step 2: Base Synchronization
Perform the initial sync using 4 threads:
````
repo sync -d -c --force-sync --no-tags --no-clone-bundle -j4
````
### 🔹 Step 3: LFS Resource Sync
<font color="#dd0000">CRITICAL:</font> A14 requires Large File Storage (LFS) binaries. You must execute the ./repo-lfs script to complete the sync.
```
repo sync -d -c --force-sync --no-clone-bundle --tags -j4 && ./repo-lfs
```
***
<a id="version-rollback-cleanup"></a>
## 3. 🛠️ Version Rollback & Deep Cleanup

Use these procedures to resolve "untracked files" errors or to strictly align your local workspace with the manifest state.

### 🧱 Force Reset All Sub-modules
Run this command to discard all local changes and remove untracked files across all repositories:
```bash
repo forall -c "git reset --hard && git clean -xdf"
```
### ⏪ Manifest Rollback Procedure
If you need to revert to a previous manifest version and force all sub-projects to synchronize with that specific point in history:

1. Enter Manifest Directory & Revert:
Move into the internal manifest repository and roll back the pointer (e.g., to the previous commit):
````
cd .repo/manifests
git reset --hard HEAD^
````
2. Force Sync:
Return to the root directory and synchronize. This ensures all sub-repositories follow the reverted manifest definition:
```
cd ../..
repo sync -d -c --force-sync -j4
````
3. Ultimate Cleanup:
To resolve persistent issues with files that are not being tracked or are interfering with the build:
````
# Remove all untracked files, including those ignored by .gitignore (-x)
repo forall -c "git clean -dfx"

# Physically delete the output directory to ensure a completely clean build environment
rm -rf out/
````

***

<a id="internal-project-dashboards"></a>
## 4. 📊 Internal Project Dashboards & Resources

Quick access to mail, build repositories, and project metrics.

### 📧 Communication & Reviews
* **Bosch Outlook:** [Web Mail](https://outlook.office.com/mail)
* **Gerrit Dashboard:** [My Reviews & Changes](https://rbcm-gerrit.de.bosch.com/dashboard/self)

### 📦 Build Artifacts & OTA Packages
* **Latest OTA Package:** [ISH.25.17.05 A12 Full OTA Zip](https://rb-cmbinex-yh-p1.apac.bosch.com/ui/repos/tree/General/rnm-ccs2.0-repos/bosch/deployment/android_qpr3_12/ccs2_qpr3_a12_int_2025.17.5/OTA/ISH.25.17.05.S0M_ccs2_qpr3_a12_int_2025.17.5_aivi2_b-userdebug_full_ota.zip)
* **Daily Build (Mainpage):** [Android QPR3 A12 Repos](https://rb-cmbinex-yh-p1.apac.bosch.com/ui/repos/tree/General/rnm-ccs2.0-repos/bosch/deployment/android_qpr3_12)
* **Daily Build (Japan):** [Artifactory Local Deployment](https://rb-cmbinex-artifactory.jp.bosch.com/artifactory/rnm-ccs2.0-fe-local/bosch/deployment/)
* **Aurix Firmware:** [AURIX PF Generic Autosar Download](https://rb-cmbinex-fe-p1.de.bosch.com/ui/repos/tree/General/basesoftware-repos/basesoftware/gen4/AURIX/pf_generic-autosar)

### 📊 Metrics & Documentation
* **Project Metrics (German):** [CCS2 Nissan SW Release Info (Grafana)](https://ccs2-metrics.apac.bosch.com/d/UcrU38F4z/ccs2-nissan-sw-release-info-table?orgId=1)
* **Development Wiki:** [CCS2 Developer Sync & Instructions](https://inside-docupedia.bosch.com/confluence/display/AIVI/CCS2+developer+sync+instructions)

---
**Internal Document** | **Generated for Bosch CCS2 Project**