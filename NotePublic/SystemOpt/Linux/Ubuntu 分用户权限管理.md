### 创建group 和 用户
```
sudo groupadd ccs2grp
sudo adduser ccs1
sudo adduser ccs2
sudo adduser ccs3
```

### 将user 加入到组
```
sudo usermod -aG ccs2grp ccs1
```
### 赋予user 管理员权限
```
sudo usermod -aG sudo ccs1
```
### 某个路径添加权限为组或者用户
```
sudo chown -R ccs1:ccs2grp /user/home/Fred/

//单纯改变组
sudo chgrp ccs2grp -R  /user/home/Fred/
```

### 给某个程序添加用户的执行权限
```
which openconnect
# 假设路径是 /usr/sbin/openconnect
sudo chmod u+s /usr/sbin/openconnect
```