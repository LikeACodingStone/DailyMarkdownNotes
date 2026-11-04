---
tags: [tools, mqtt, mosquitto, windows]
updated: 2026-11-04
---
# MQTT Mosquitto Server [MQTT 服务器]

> [!summary] Summary [概要]
> Start the Mosquitto server by hand, make it start at boot, and fix "can't connect after it starts".
> [手动启动 Mosquitto、设置开机自启，以及解决"启动后无法连接"。]

## 1. Server won't start [服务器无法启动]

Start it manually with the config file: [手动用配置文件启动：]

```bat
mosquitto.exe -c mosquitto.conf
```

## 2. Start at boot [开机自启]

1. Edit `RunMQTT.bat` and change the path to the real location of `mosquitto.exe` [把 `RunMQTT.bat` 里的路径改成 `mosquitto.exe` 的实际路径]
2. Copy it to the Startup folder [复制到开机启动目录]:

```text
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

Attachment [附件]: [RunMQTT.bat](../_assets/shared/RunMQTT.bat)

> [!tip] Wrong user name? [用户名不对？]
> `Administrator` may need to be your real user name. The quick way: press `Win + R`, type `shell:startup`.
> [`Administrator` 有时要换成实际用户名。快捷方式：`Win + R` 输入 `shell:startup`。]

## 3. Started but clients can't connect [启动后无法连接]

Edit `mosquitto.conf`: [修改 `mosquitto.conf`：]

```conf
# Allow anonymous access [允许匿名访问]
allow_anonymous true

# Listen on port 1883 on all interfaces [监听所有网卡的 1883 端口]
listener 1883 0.0.0.0
```

Then restart the service. [然后重启服务。]

> [!warning] Anyone on the network can connect [网络中任何人都能连接]
> Anonymous access on `0.0.0.0` has no login at all. Use it only on a trusted LAN; otherwise set up `password_file`.
> [`0.0.0.0` 加匿名访问等于完全没有登录验证，只在可信的局域网使用，否则请配置 `password_file`。]
