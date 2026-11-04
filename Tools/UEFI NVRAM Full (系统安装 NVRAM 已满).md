---
tags: [tools, uefi, bios, secure-boot, linux]
updated: 2026-11-04
---
# UEFI NVRAM Full [系统安装 NVRAM 已满]

> [!summary] Summary [概要]
> After installing operating systems many times, boot fails with `volume full` errors. The firmware's NVRAM is full; resetting the Secure Boot keys clears it.
> [多次安装系统后，开机出现 `volume full` 错误：固件 NVRAM 已满，重置 Secure Boot 密钥即可清空。]

## Symptom [现象]

```text
could not create MOKListRT: volume full
could not create MOKListXRT: volume full
could not create SBatLevel1RT: volume full
Something has gone seriously wrong: import_mok_state() failed
```

## What it means [含义]

The UEFI / BIOS **NVRAM** storage is full. It can't store new Secure Boot keys or boot entries, especially the **MOK** (Machine Owner Key) list used by Linux distributions.
[UEFI / BIOS 固件的 **NVRAM** 存储空间已满，无法存放新的 Secure Boot 密钥或启动项，尤其是 Linux 发行版使用的 **MOK**（Machine Owner Key）列表。]

## Fix [解决方案]

> [!warning] This erases ALL Secure Boot keys [会清除所有 Secure Boot 密钥]
> Step 4 wipes every key, and Secure Boot must then stay disabled. If you need Secure Boot again later, restore the default keys in the same menu.
> [第 4 步会清除所有密钥，之后 Secure Boot 必须保持关闭。以后需要时，在同一菜单中恢复默认密钥。]

1. Press **F2** during boot to enter the BIOS [开机按 **F2** 进入 BIOS]
2. Press **F7** to enable **Advanced Mode** [按 **F7** 进入高级模式]
3. **Security → Secure Boot → Secure Boot Control: Enabled**. You must enable Secure Boot to reach key management. [必须先启用 Secure Boot 才能进入密钥管理]
4. **Security → Secure Boot → Key Management: Reset to Setup Mode**. This clears all variables and keys; it should show "No Key" several times. [重置为 Setup Mode，清除所有变量和密钥]
5. **Secure Boot Control: Disabled**. It must be disabled now, because there are no valid keys. [现在没有有效密钥，必须关闭]
6. **Save and exit** [保存并退出]

> [!note] Keys vary by board [按键因主板而异]
> F2 / F7 and the menu names are from the motherboard this was done on; other boards differ.
> [F2 / F7 和菜单名称来自当时的主板，其他主板可能不同。]
