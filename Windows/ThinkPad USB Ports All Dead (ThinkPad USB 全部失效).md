---
tags: [windows, thinkpad, hardware, usb]
updated: 2026-11-04
---
# ThinkPad USB Ports All Dead [ThinkPad USB 接口全部失效]

> [!summary] Summary [概要]
> All USB ports stop working at once: **USB Type-A, Type-C, Thunderbolt**. Usually not broken hardware; a power / EC reset fixes it.
> [所有 USB 接口同时失效：**USB Type-A、Type-C、Thunderbolt**。通常不是硬件坏了，断电 / EC 复位即可恢复。]

## Possible causes [可能原因]

- Motherboard power protection [主板供电保护]
- EC (Embedded Controller) stuck [EC 嵌入式控制器状态异常 / 挂起]
- BIOS hang [BIOS 挂起]
- Abnormal system state [系统状态异常]

## Quick flow [快速流程]

```text
Disconnect all devices        [拔掉所有外设]
        ↓
Unplug power                  [拔掉电源]
        ↓
Hold Power > 20 sec           [长按电源键 20 秒以上]
        ↓
Emergency Reset Hole 5–10 sec [紧急复位孔 5–10 秒]（if available [如果有]）
        ↓
Connect power, restart, test  [接回电源，开机测试]
```

## Steps [详细步骤]

### 1. Disconnect everything [拔掉所有设备]

USB devices, Type-C devices, Thunderbolt devices, USB hubs / adapters, **power adapter**.
[USB 设备、Type-C 设备、雷电设备、USB Hub / 转接器、**电源适配器**。]

### 2. Power reset [断电复位]

1. Make sure the laptop is **fully shut down** [确认电脑**完全关机**]
2. Unplug the power adapter [拔掉电源适配器]
3. Hold the **Power button for 20+ seconds** [长按**电源键 20 秒以上**]
4. Release [松开]

### 3. Emergency Reset Hole [紧急复位孔]

If the bottom of the ThinkPad has an **Emergency Reset Hole**: [如果 ThinkPad 底部有**紧急复位孔**：]

1. Keep the laptop off [保持关机]
2. Press and hold inside the hole with a SIM pin / paperclip [用卡针或细小工具按住复位孔]
3. Hold **5–10 seconds** [按住 **5–10 秒**]
4. Release [松开]

> [!warning] Check the hole position first [先确认复位孔位置]
> Location differs by model. Don't push a pin into a hole you're not sure about (could be a mic or speaker).
> [不同型号位置不同。不确定的孔不要插针（可能是麦克风或扬声器孔）。]

### 4. Restart and test [开机测试]

1. Reconnect the power adapter [接回电源适配器]
2. Power on [开机]
3. Plug in a known-good USB mouse or USB stick [插入一个正常的 USB 鼠标或 U 盘]
4. Check whether USB works again [检查 USB 是否恢复]
