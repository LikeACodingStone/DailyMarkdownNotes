---
tags: [tools, docker, linux, proxy]
updated: 2026-11-04
---
# Docker Work Setup [Docker 公司环境配置]

> [!summary] Summary [概要]
> Docker on Ubuntu inside the company network: **install → DNS & registry → proxy → certificates → permission fix → save/load → debug**.
> [在公司网络内的 Ubuntu 上使用 Docker：**安装 → DNS 与镜像仓库 → 代理 → 证书 → 权限修复 → 导入导出 → 调试**。]

> [!warning] Contains internal addresses [包含内部地址]
> DNS servers, proxy, and registry names below are company-internal. Don't share this note publicly (no Gist).
> [下面的 DNS、代理、仓库地址是公司内部信息，不要公开分享（不要上传 Gist）。]

---

## 1. Install [安装]

```bash
# Remove old versions [卸载旧版本]
sudo apt-get remove docker docker-engine docker.io

# Install and start [安装并启动]
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

> [!note]- Old method: official repo with `apt-key` [旧方法：官方仓库 + apt-key]
> `apt-key` is deprecated; for current steps see docs.docker.com/engine/install/ubuntu. [`apt-key` 已弃用，最新步骤见官方文档。]
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

## 2. Company Config [公司环境配置]

### 2.1 DNS & insecure registries [DNS 与非安全仓库]

`/etc/docker/daemon.json` can be replaced directly with: [可直接整体替换为：]

```json
{
  "dns": ["172.31.0.10", "172.31.0.11"],
  "insecure-registries": [
    "buildbot.nts.neusoft.local:5000",
    "ntssy-lxbbma01.nts.neusoft.local:5000"
  ]
}
```

### 2.2 Let your user run Docker [让当前用户使用 Docker]

```bash
sudo usermod -aG docker $USER
newgrp docker
```

### 2.3 Restart & verify [重启并验证]

```bash
sudo systemctl daemon-reload && sudo service docker restart
docker images        # should list images without errors [能正常列出镜像]
```

---

## 3. Proxy [代理]

Every `*.conf` file in this folder is loaded as proxy config: [此目录下所有 `.conf` 文件都会被加载为代理配置：]

```text
/etc/systemd/system/docker.service.d/
```

Example `proxy.conf` [示例]:

```ini
[Service]
Environment="HTTP_PROXY=http://10.4.103.143:8080/"
Environment="HTTPS_PROXY=http://10.4.103.143:8080/"
Environment="NO_PROXY=localhost,127.0.0.1"
```

> [!warning] About `NO_PROXY` [关于 NO_PROXY]
> `NO_PROXY` lists the addresses that **skip** the proxy. Never put anything proxy-related there.
> [`NO_PROXY` 是**不走代理**的地址列表，一定不要把代理相关内容放在这里。]

Then reload and restart [然后重载并重启]:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 4. Certificates [证书]

**1. System certificate [系统证书]:** copy it to this folder, then update [拷贝到此目录再更新]

```bash
/usr/local/share/ca-certificates/
sudo update-ca-certificates
```

**2. Docker registry certificate [Docker 仓库证书]:** create a folder named after the registry host and put `ca.crt` in it, then restart.
[以仓库域名建文件夹，放入 `ca.crt`，然后重启。]

```bash
# Example registry [例如]: ccs2-docker.rb-cmbinex-lud-p1.emea.bosch.com
/etc/docker/certs.d/ccs2-docker.rb-cmbinex-lud-p1.emea.bosch.com/ca.crt

sudo systemctl daemon-reload
sudo systemctl restart docker
```

---

## 5. Common Errors [常见错误]

### Permission denied on the Docker socket [无法连接 Docker 守护进程，权限不足]

```text
permission denied while trying to connect to the Docker daemon socket at
unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/load?quiet=0":
dial unix /var/run/docker.sock: connect: permission denied
```

```bash
sudo usermod -aG docker $USER

# reboot the machine, then check Docker is running [重启电脑后，检查 Docker 状态]
sudo systemctl status docker
sudo systemctl start docker
```

---

## 6. Save / Load Images [导入导出镜像]

```bash
# Export one image [导出单个镜像]
docker save -o <output_file>.tar <image_name>:<tag>

# Export several images into one file [导出多个镜像]
docker save -o multiple_images.tar <image1>:<tag> <image2>:<tag>

# Import [导入]
docker load -i <input_file>.tar
```

---

## 7. Debug [调试]

```bash
sudo dockerd -D                                     # run the daemon in debug mode [调试模式运行]
cat /var/log/docker.log                             # daemon log [日志]
journalctl -u docker.service --no-pager -n 50       # last 50 service log lines [最近 50 行服务日志]
```
