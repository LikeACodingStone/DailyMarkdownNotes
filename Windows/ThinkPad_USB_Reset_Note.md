# ThinkPad USB 接口全部失效

## Problem

ThinkPad 的 USB 接口突然全部失效，包括：

- USB Type-A
- USB Type-C
- Thunderbolt

可能原因：

- 主板供电保护
- EC 状态异常
- BIOS / EC 控制器挂起
- 系统状态异常

## Step 1 — Disconnect Everything

拔掉所有外接设备：

- USB 设备
- Type-C 设备
- Thunderbolt 设备
- USB Hub / 转接器
- 电源适配器

## Step 2 — Power Reset

1. 确认电脑完全关机
2. 拔掉电源适配器
3. 长按 **Power 键 20 秒以上**
4. 松开 Power 键

## Step 3 — Emergency Reset Hole

如果 ThinkPad 底部有 **Emergency Reset Hole（紧急复位孔）**：

1. 保持电脑关机
2. 使用卡针或细小工具按住复位孔
3. 按住 **5～10 秒**
4. 松开

> 不同 ThinkPad 型号的位置不同，不要把针插入不确定的孔。

## Step 4 — Restart and Test

1. 接回电源适配器
2. 开机
3. 插入一个正常的 USB 鼠标或 U 盘
4. 检查 USB 是否恢复

### Quick Flow

```text
Disconnect all devices
        ↓
Unplug power
        ↓
Hold Power > 20 sec
        ↓
Emergency Reset Hole
(if available, 5–10 sec)
        ↓
Connect power
        ↓
Restart and test USB
```
