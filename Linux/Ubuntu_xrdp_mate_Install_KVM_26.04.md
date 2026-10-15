# Install KVM on Ubuntu 26.04 LTS

> **Ubuntu version:** Ubuntu 26.04 LTS (Resolute Raccoon)
>
> This guide is adapted from the original Ubuntu 24.04 KVM notes. The original workflow is preserved, while Ubuntu 24.04-specific references are updated for Ubuntu 26.04.

---

## 1. Check CPU virtualization support

Check whether the CPU supports hardware virtualization (Intel VT-x or AMD-V).

Use either command:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

or:

```bash
lscpu | grep Virtualization
```

If the first command returns `0`, hardware virtualization may be disabled in the BIOS/UEFI. Enable **Intel VT-x / Intel Virtualization Technology** or **AMD-V / SVM Mode** in the firmware settings.

You can also verify KVM support later with:

```bash
kvm-ok
```

---

## 2. Update the system

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 3. Install the KVM environment

Ubuntu 26.04 provides the QEMU/libvirt virtualization stack in the official repositories. The following packages are suitable for the same workflow as the original document:

```bash
sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils virt-manager
```

Ubuntu 26.04 ships a newer libvirt/QEMU stack than Ubuntu 24.04, so there is no need to install the old 24.04-specific versions manually.

---

## 4. Check and enable the libvirt service

Enable libvirt and start it immediately:

```bash
sudo systemctl enable --now libvirtd
```

Check its status:

```bash
sudo systemctl status libvirtd
```

If the service is running, it should show:

```text
Active: active (running)
```

---

## 5. Add your user to the required groups

```bash
sudo usermod -aG libvirt $USER
sudo usermod -aG kvm $USER
```

Apply the `libvirt` group to the current shell:

```bash
newgrp libvirt
```

For the most reliable result, log out and log back in after changing group membership.

Check:

```bash
groups
```

---

## 6. Verify KVM is working

List all libvirt virtual machines:

```bash
virsh list --all
```

Check hardware virtualization/KVM support:

```bash
kvm-ok
```

A normal result should indicate that KVM acceleration can be used.

---

## 7. Start the graphical management tool

Launch Virtual Machine Manager:

```bash
virt-manager
```

Use **Virtual Machine Manager** to create, configure, start, stop, and manage the Ubuntu virtual machines.

---

# Bridge Network Configuration

A bridge allows the virtual machine to appear directly on the physical network, rather than using libvirt's default NAT network.

Ubuntu uses **Netplan** for network configuration. Netplan supports both `networkd` and `NetworkManager`; the original configuration uses `networkd`, so that approach is retained here.

## 1. Check the current network interface name

Do not assume the interface is `enp1s0`.

Run:

```bash
ip link
```

or:

```bash
ip -br link
```

Find the physical Ethernet interface, for example:

```text
enp1s0
```

Replace `enp1s0` below with the actual interface name on your machine.

---

## 2. Edit the Netplan configuration

Check the files:

```bash
ls -l /etc/netplan/
```

For example:

```bash
sudo vi /etc/netplan/01-network-manager-all.yaml
```

A static-IP bridge configuration based on the original document is:

```yaml
network:
  version: 2
  renderer: networkd

  ethernets:
    enp1s0:
      dhcp4: false

  bridges:
    br0:
      interfaces:
        - enp1s0
      dhcp4: false
      addresses:
        - 172.30.2.201/24
      routes:
        - to: default
          via: 172.30.2.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

### Important

Replace these values with the actual network configuration:

```text
enp1s0       -> your physical Ethernet interface
172.30.2.201 -> host's static IP
172.30.2.1   -> your gateway
8.8.8.8      -> DNS server
8.8.4.4      -> DNS server
```

The physical Ethernet interface itself should not normally keep the host IP. The IP address belongs on `br0`.

---

## 3. Validate the Netplan configuration

Before applying a network change, validate it:

```bash
sudo netplan generate
```

If there are no errors, apply it:

```bash
sudo netplan apply
```

Then check:

```bash
ip addr show br0
ip route
```

You should see the host IP assigned to `br0`.

> **Remote SSH/RDP warning:** Changing the network configuration can immediately disconnect a remote session. If this is a remote machine, preferably keep local/console access available before applying the bridge configuration.

---

## 4. Reboot if necessary

If the network configuration is correct but the bridge is not behaving as expected:

```bash
sudo reboot
```

For static IPs on both the host and VM, configure the host bridge and the VM network adapter appropriately in Virtual Machine Manager.

---

# Create a Virtual Ubuntu 26.04 Machine

## 1. Move the Ubuntu 26.04 ISO into the libvirt image directory

The original document uses Ubuntu 24.04.3. For Ubuntu 26.04, use the 26.04 ISO instead.

Example:

```bash
sudo mv ~/ubuntu-26.04-desktop-amd64.iso /var/lib/libvirt/images/
```

Then:

```bash
cd /var/lib/libvirt
sudo chmod -R 755 images
```

The official Ubuntu 26.04 AMD64 desktop ISO is named:

```text
ubuntu-26.04-desktop-amd64.iso
```

---

## 2. Create a new virtual machine

Start:

```bash
virt-manager
```

Then:

1. Click **Create a new virtual machine**.
2. Select **Local install media (ISO image or CDROM)**.
3. Select the Ubuntu 26.04 ISO.
4. Configure the VM memory and CPU.
5. Configure the virtual disk.
6. Configure the network.
7. Start the installation.

---

## 3. Select the Ubuntu 26.04 ISO

Use:

```text
/var/lib/libvirt/images/ubuntu-26.04-desktop-amd64.iso
```

Ubuntu 26.04 is an AMD64/x86-64 desktop image for standard Intel/AMD PCs.

---

## 4. Configure resources

Choose the resources according to the workload.

For example:

- CPU: allocate the number of cores you need.
- RAM: allocate enough memory for the guest OS and applications.
- Disk: allocate enough storage for the VM.
- Network: select `br0` if the VM needs direct access to the physical LAN.

---

## 5. If Ubuntu does not boot correctly after installation

If you encounter a black screen or display-related boot problem, check the VM's display configuration.

In particular, make sure **3D acceleration is disabled** if it causes the guest to fail to start.

In Virtual Machine Manager:

```text
VM → View Details → Video / Display
```

Then disable 3D acceleration if necessary.

---

# Create a Shared Folder with VirtioFS

VirtioFS provides a high-performance way to share a host directory with a virtual machine.

## 1. Create the host shared folder

```bash
mkdir -p ~/vmshare
```

For example:

```text
Host:
~/vmshare

Guest:
/mnt/vmshare
```

---

## 2. Enable shared memory in the VM

In Virtual Machine Manager:

```text
VM → View Details → Add Hardware
```

Configure the shared-memory/MemoryBacking option required by the VirtioFS setup.

Follow the same VM configuration shown in the original screenshots.

---

## 3. Add the Filesystem device

In Virtual Machine Manager:

```text
VM → View Details → Add Hardware → Filesystem
```

Configure:

```text
Driver / Type: virtiofs
Source Path: /home/<your-user>/vmshare
Target: vmshare
```

Replace `<your-user>` with your actual Linux username.

---

## 4. If the VM reports a VirtioFS start error

Install the required packages on the Ubuntu 26.04 host:

```bash
sudo apt update
sudo apt install -y virtiofsd qemu-system-common
```

Restart libvirt:

```bash
sudo systemctl restart libvirtd
```

Check that `virtiofsd` exists:

```bash
ls -l /usr/lib/qemu/virtiofsd
```

If that path exists, the VirtioFS daemon is installed.

---

## 5. Mount the shared folder inside the virtual machine

Create the mount point:

```bash
sudo mkdir -p /mnt/vmshare
```

Mount the VirtioFS filesystem:

```bash
sudo mount -t virtiofs vmshare /mnt/vmshare
```

Check:

```bash
mount | grep vmshare
```

Then test:

```bash
ls -la /mnt/vmshare
```

Files placed in the host directory should now be accessible from the VM.

---

# Additional Knowledge

## 1. Use a separate disk for VM images

If VM images are stored on another disk, create a dedicated directory.

Example:

```bash
sudo mkdir -p /media/neu/kvm_images
```

Put VM images or ISO files in:

```text
/media/neu/kvm_images
```

Grant libvirt/QEMU access to the directory:

```bash
sudo setfacl -m u:libvirt-qemu:rx /media/neu
sudo setfacl -R -m u:libvirt-qemu:rwx /media/neu/kvm_images
```

Check the permissions:

```bash
getfacl /media/neu/kvm_images
```

---

## 2. ISO is not detected / VM does not boot from ISO

If the ISO is attached but the VM does not boot from it, check the VM boot order.

In Virtual Machine Manager:

```text
VM → View Details → Boot Options
```

Make sure the CDROM/ISO device is enabled and placed before the virtual disk in the boot order.

---

# Ubuntu 26.04 Quick Verification

After installation, these commands are useful for checking the complete KVM environment:

```bash
lsb_release -a
```

```bash
uname -r
```

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

```bash
kvm-ok
```

```bash
systemctl status libvirtd
```

```bash
virsh list --all
```

```bash
ip -br addr
```

```bash
ip route
```

```bash
virsh net-list --all
```

If using a bridge:

```bash
ip addr show br0
```

If using VirtioFS:

```bash
ls -l /usr/lib/qemu/virtiofsd
```

---

# Ubuntu 26.04 Notes

- Ubuntu 26.04 LTS is **Resolute Raccoon**.
- The Ubuntu 26.04 desktop AMD64 ISO is `ubuntu-26.04-desktop-amd64.iso`.
- Ubuntu 26.04 includes the current QEMU/libvirt stack in the official repositories.
- `virtiofsd` is available from the Ubuntu 26.04 repositories.
- Netplan continues to support bridge configuration with either `networkd` or `NetworkManager`.
- The original static bridge example uses `networkd`, so this document keeps that configuration.
- Always verify your actual Ethernet interface name with `ip -br link` before applying the bridge configuration.
- If the machine is accessed remotely, be careful when changing Netplan because an incorrect bridge configuration can disconnect SSH/RDP.

