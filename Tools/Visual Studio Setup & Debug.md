---
tags: [tools, visual-studio, license, debug]
updated: 2026-11-04
---
# Visual Studio Setup & Debug

> [!summary] Summary
> 1. Sign-in / license problems
> 2. Debug process hangs and can't be killed

---

## 1. Sign-in / License Problems

> [!bug] Symptoms
> - `the online service is not available`
> - `sign in, sorry, we ran into a problem`
> - Can't enter the license

Try the steps in order.

### Step 1 — Clear the old account info

1. Go to the VS 2013 install folder:
   `C:\Program Files\Microsoft Visual Studio\2013\Professional\Common7\IDE`
2. Open **cmd as Administrator** in that folder (or **Developer Command Prompt for VS2013** as Administrator)
3. Run:

```bat
devenv /resetuserdata
```

> [!tip]- Still not working? Clean the registry
> Back up the key first. Under the key below, delete everything and keep only `(Default)`:
> ```text
> HKEY_CURRENT_USER\Software\Microsoft\VSCommon\12.0\ClientServices\TokenStorage\VisualStudio\IdeUser
> ```

### Step 2 — Repair

1. Control Panel → right-click Visual Studio → **Change → Repair**
2. When it finishes, close it, wait a few minutes, then restart

> [!example]- Screenshot
> ![image](_resources/77076d87173a6700f5e924a813df7002.png)

### Step 3 — Enable strong crypto (TLS 1.2), then sign in again

Add two DWORD values (= `1`) so the old .NET Framework uses strong crypto, which the sign-in server needs.

```text
HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v4.0.30319
    SystemDefaultTlsVersions = 00000001
    SchUseStrongCrypto       = 00000001
```

Or in **PowerShell (Administrator)**:

```powershell
New-ItemProperty -Path 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NetFramework\v4.0.30319' -Name 'SystemDefaultTlsVersions' -Value '1' -PropertyType 'DWord' -Force | Out-Null
New-ItemProperty -Path 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\.NetFramework\v4.0.30319' -Name 'SchUseStrongCrypto'       -Value '1' -PropertyType 'DWord' -Force | Out-Null
```

> [!example]- Screenshots
> Registry
> ![image](_resources/8469b40d157562b5024368911cce2413.png)
> ![image](_resources/ae1a68c6403eb03ba72c4765837d2c02.png)
> ![image](_resources/9a1f6e51b589db837472a8c584f6fb84.png)
>
> PowerShell
> ![image](_resources/bdd83371146bf89315017ba0f73ee8cc.png)
> ![image](_resources/59d669cc511462c1e08b855929156ef3.png)

---

## 2. Debug Process Hangs

> [!bug] Symptoms
> - The process hangs while debugging, and is still hung after stopping
> - The project's process can't be found in Task Manager

**Fix: kill it from cmd**

```bat
:: 1. Find the process by keyword (HGT = the process name prefix)
tasklist | findstr "HGT*"

:: 2. Kill every PID that shows up (repeat for each one)
taskkill /PID <PID> /F /T
```

> [!example]- Screenshots
> ![image](_resources/3859a1df9a2c2c90980b147b15cfbbf2.png)
> ![image](_resources/5ef8b1b4bb662500dce9b036b50f9b2f.png)

> [!tip] Still stuck? Check the USB port
> The USB port / external device may be locked: **unplug and replug the USB device**.
