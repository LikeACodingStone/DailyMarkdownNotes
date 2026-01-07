### Proxy

- 这个路径下的所有.conf 结尾的文件都会被加载成proxy

```
/etc/systemd/system/docker.service.d/
```

- 例: 注意
- 这个NO_PROXY 表示不参与代理的IP，一定不要把代理相关内容放在这个位置

```
/etc/systemd/system/docker.service.d/proxy.conf 
[Service]
Environment="HTTP_PROXY=http://10.4.103.143:8080/"
Environment="HTTPS_PROXY=http://10.4.103.143:8080/"
Environment="NO_PROXY=localhost,127.0.0.1"
```

### 证书 Cert

- 更新证书到系统路径，拷贝到这个路径，并更新到系统

```
/usr/local/share/ca-certificates/

sudo update-ca-certificates
```

- 创建docker证书， 并且更新重启

```
// 例如登录ccs2-docker.rb-cmbinex-lud-p1.emea.bosch.com

/etc/docker/certs.d/ccs2-docker.rb-cmbinex-lud-p1.emea.bosch.com/ca.crt

sudo systemctl daemon-reload
sudo systemctl restart docker
```