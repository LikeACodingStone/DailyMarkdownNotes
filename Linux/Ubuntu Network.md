---
tags: [ubuntu, linux, network, netplan, wifi, vpn]
updated: 2026-11-04
---
# Ubuntu Network

> [!summary] Contents
> 1. Static IP with Netplan, and back to DHCP
> 2. No network after an OpenConnect VPN
> 3. Wi-Fi: password box hangs

---

## 1. Static IP with Netplan (22.04)

Edit the Netplan file. The name may differ, e.g. `01-network-manager-all.yaml` or `00-installer-config.yaml`:

```bash
ls /etc/netplan/
sudo vi /etc/netplan/01-network-manager-all.yaml
```

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:                      # your real interface name
      dhcp4: no
      addresses:
        - 172.30.2.200/24
      routes:
        - to: default
          via: 172.30.2.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

```bash
sudo netplan apply
```

> [!note] `gateway4` is deprecated
> The old note used `gateway4: 172.30.2.1`. Use `routes: - to: default via: ...` as above.

> [!warning] Also remember
> - **Network → Wired → IPv4 → Disable** in the desktop settings, then **reboot**, so NetworkManager doesn't fight Netplan.
> - Check the **DHCP's DNS** first and set the **same DNS** for the static config.
> - On a remote machine, a wrong config disconnects you. Keep console access, or run `sudo netplan try` first.

### Back to DHCP

```bash
sudo vi /etc/netplan/01-network-manager-all.yaml
```

```yaml
network:
  version: 2
  renderer: NetworkManager
```

```bash
sudo vi /etc/NetworkManager/NetworkManager.conf
```

```ini
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true            # set to true

[device]
wifi.scan-rand-mac-address=no
```

---

## 2. No Network After an OpenConnect VPN

> [!bug] Symptom
> After disconnecting the VPN, there is no network: the default route is gone.

```bash
# 1. Check the default route
ip route

# 2. Restore it by hand
sudo ip route add default via <gateway> dev <interface>     # e.g. via 192.168.1.1 dev eth0

# 3. Test
ping -c 3 8.8.8.8

# 4. If still broken
sudo netplan apply
```

> [!tip] Adjust the values
> `<gateway>` and `<interface>` are the ones from your own network (see `ip route` before connecting the VPN).

---

## 3. Wi-Fi: Password Box Hangs

> [!bug] Symptom
> "System policy prevents Wi-Fi scans". You can't enter the password; the dialog hangs.

![[Pasted image 20261027182104.png]]

**Fix: kill the stuck `nm-applet` from another machine**

```bash
# 1. Find the process
ps aux | grep -E "nm-applet|plasmashell|gnome-shell|network-manager"
# neu   273370  ...  nm-applet --indicator      ← the one to kill

# 2. Kill it
kill -9 273370
# or
pkill nm-applet
```
