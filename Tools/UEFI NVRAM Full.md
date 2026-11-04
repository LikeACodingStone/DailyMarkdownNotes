---
tags: [tools, uefi, bios, secure-boot, linux]
updated: 2026-11-04
---
# UEFI NVRAM Full

> [!summary] Summary
> After installing operating systems many times, boot fails with `volume full` errors. The firmware's NVRAM is full; resetting the Secure Boot keys clears it.

## Symptom

```text
could not create MOKListRT: volume full
could not create MOKListXRT: volume full
could not create SBatLevel1RT: volume full
Something has gone seriously wrong: import_mok_state() failed
```

## What it means

The UEFI / BIOS **NVRAM** storage is full. It can't store new Secure Boot keys or boot entries, especially the **MOK** (Machine Owner Key) list used by Linux distributions.

## Fix

> [!warning] This erases ALL Secure Boot keys
> Step 4 wipes every key, and Secure Boot must then stay disabled. If you need Secure Boot again later, restore the default keys in the same menu.

1. Press **F2** during boot to enter the BIOS
2. Press **F7** to enable **Advanced Mode**
3. **Security → Secure Boot → Secure Boot Control: Enabled**. You must enable Secure Boot to reach key management.
4. **Security → Secure Boot → Key Management: Reset to Setup Mode**. This clears all variables and keys; it should show "No Key" several times.
5. **Secure Boot Control: Disabled**. It must be disabled now, because there are no valid keys.
6. **Save and exit**

> [!note] Keys vary by board
> F2 / F7 and the menu names are from the motherboard this was done on; other boards differ.
