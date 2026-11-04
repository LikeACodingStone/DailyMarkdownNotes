---
tags: [tools, docker, linux, proxy]
updated: 2026-11-04
---
# Docker Work Setup

> [!summary] Summary
> Docker on Ubuntu inside the company network: **install → DNS & registry → proxy → certificates → permission fix → save/load → debug**.

> [!warning] Contains internal addresses
> DNS servers, proxy, and registry names below are company-internal. Don't share this note publicly (no Gist).

---

## 1. Install

```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io

# Install and start
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

> [!note]- Old method: official repo with `apt-key`
> `apt-key` is deprecated; for current steps see docs.docker.com/engine/install/ubuntu.
> ```bash
> sudo apt-get update
> sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
>
> curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
> sudo apt-key fingerprint 0EBFCD88     # expect: 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88
>
> sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
> # then install from this repo: sudo apt-get install docker-ce docker-ce-cli containerd.io
> ```

---

## 2. Company Config

### 2.1 DNS & insecure registries

`/etc/docker/daemon.json` can be replaced directly with:

```json
{
  "dns": ["172.31.0.10", "172.31.0.11"],
  "insecure-registries": [
    "buildbot.nts.neusoft.local:5000",
    "ntssy-lxbbma01.nts.neusoft.local:5000"
  ]
}
```

### 2.2 Let your user run Docker

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### 2.3 Restart & verify

```bash
sudo systemctl daemon-reload && sudo service docker restart
docker images        # should list images without errors
```

---

## 3. Proxy

Every `*.conf` file in this folder is loaded as proxy config:

```text
/etc/systemd/system/docker.service.d/
```

Example `proxy.conf`:

```ini
[Service]
Environment="HTTP_PROXY=http://10.4.103.143:8080/"
Environment="HTTPS_PROXY=http://10.4.103.143:8080/"
Environment="NO_PROXY=localhost,127.0.0.1"
```

> [!warning] About `NO_PROXY`
> `NO_PROXY` lists the addresses that **skip** the proxy. Never put anything proxy-related there.

Then reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 4. Certificates

**1. System certificate:** copy it to this folder, then update

```bash
/usr/local/share/ca-certificates/
sudo update-ca-certificates
```

**2. Docker registry certificate:** create a folder named after the registry host and put `ca.crt` in it, then restart.

```bash
# Example registry: ccs2-docker.rb-cmbinex-lud-p1.emea.bosch.com
/etc/docker/certs.d/ccs2-docker.rb-cmbinex-lud-p1.emea.bosch.com/ca.crt

sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 5. Common Errors

### Permission denied on the Docker socket

```text
permission denied while trying to connect to the Docker daemon socket at
unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/load?quiet=0":
dial unix /var/run/docker.sock: connect: permission denied
```

```bash
sudo usermod -aG docker $USER

# reboot the machine, then check Docker is running
sudo systemctl status docker
sudo systemctl start docker
```

---

## 6. Save / Load Images

```bash
# Export one image
docker save -o <output_file>.tar <image_name>:<tag>

# Export several images into one file
docker save -o multiple_images.tar <image1>:<tag> <image2>:<tag>

# Import
docker load -i <input_file>.tar
```

---

## 7. Debug

```bash
sudo dockerd -D                                     # run the daemon in debug mode
cat /var/log/docker.log                             # daemon log
journalctl -u docker.service --no-pager -n 50       # last 50 service log lines
```
