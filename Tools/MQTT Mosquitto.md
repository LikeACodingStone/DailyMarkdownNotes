---
tags: [tools, mqtt, mosquitto, windows]
updated: 2026-11-04
---
# MQTT Mosquitto Server

> [!summary] Summary
> Start the Mosquitto server by hand, make it start at boot, and fix "can't connect after it starts".

## 1. Server won't start

Start it manually with the config file:

```bat
mosquitto.exe -c mosquitto.conf
```

## 2. Start at boot

1. Edit `RunMQTT.bat` and change the path to the real location of `mosquitto.exe`
2. Copy it to the Startup folder:

```text
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```

Attachment: [RunMQTT.bat](../_assets/shared/RunMQTT.bat)

> [!tip] Wrong user name?
> `Administrator` may need to be your real user name. The quick way: press `Win + R`, type `shell:startup`.

## 3. Started but clients can't connect

Edit `mosquitto.conf`:

```conf
# Allow anonymous access
allow_anonymous true

# Listen on port 1883 on all interfaces
listener 1883 0.0.0.0
```

Then restart the service.

> [!warning] Anyone on the network can connect
> Anonymous access on `0.0.0.0` has no login at all. Use it only on a trusted LAN; otherwise set up `password_file`.
