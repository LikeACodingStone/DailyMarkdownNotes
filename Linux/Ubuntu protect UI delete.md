## Using chmod 1777
```
sudo chown -R root:root ~/ccs2

# 设置粘滞位(1) 和 读写执行权限(777)
sudo chmod -R 1777 ~/ccs2
```

### For root folder protect
```
sudo chattr +i ~/ccs2
```

### For rm -rf or sudo rm -rf please refer to safe-rm