### 安装系统一定次数以后出现MOKListRT错误
```
could not create MOKListRT: volume full
could not create MOKListXRT: volume full
could not create SBatLevel1RT: volume full
Something has gone serously wrong: import_mok_state() failed
```
### 意义
UEFI/BIOS 固件中的 NVRAM 存储空间已满，无法存储新的 Secure Boot (安全启动) 相关的密钥或启动条目，尤其是用于 Linux 发行版的 MOK (Machine Owner Key) 列表。
*************

### 解决方案
1. Press F2 during boot to enter the BIOS
2. Press F7 to enabled Advanced Mode
3. Security > Secure Boot > Secure Boot Control: Enabled. You need to enable Secure Boot to access the key management.
4. Security > Secure Boot > Key Management: Reset to Setup Mode to clear all the variables and keys. It should show "No Key" multiple times.
5. Security > Secure Boot > Secure Boot Control: Disabled. Secure boot must be disabled because there are no valid keys.
6. Save and exit
