---
tags: [windows, thinkpad, hardware, usb]
updated: 2026-11-04
---
# ThinkPad USB Ports All Dead

> [!summary] Summary
> All USB ports stop working at once: **USB Type-A, Type-C, Thunderbolt**. Usually not broken hardware; a power / EC reset fixes it.

## Possible causes

- Motherboard power protection
- EC (Embedded Controller) stuck
- BIOS hang
- Abnormal system state

## Quick flow

```text
Disconnect all devices
        ↓
Unplug power
        ↓
Hold Power > 20 sec
        ↓
Emergency Reset Hole 5–10 sec (if available)
        ↓
Connect power, restart, test
```

## Steps

### 1. Disconnect everything

USB devices, Type-C devices, Thunderbolt devices, USB hubs / adapters, **power adapter**.

### 2. Power reset

1. Make sure the laptop is **fully shut down**
2. Unplug the power adapter
3. Hold the **Power button for 20+ seconds**
4. Release

### 3. Emergency Reset Hole

If the bottom of the ThinkPad has an **Emergency Reset Hole**:

1. Keep the laptop off
2. Press and hold inside the hole with a SIM pin / paperclip
3. Hold **5–10 seconds**
4. Release

> [!warning] Check the hole position first
> Location differs by model. Don't push a pin into a hole you're not sure about (could be a mic or speaker).

### 4. Restart and test

1. Reconnect the power adapter
2. Power on
3. Plug in a known-good USB mouse or USB stick
4. Check whether USB works again
