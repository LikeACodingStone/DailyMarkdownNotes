---
tags: [windows, teams, powershell]
updated: 2026-11-04
---
# Microsoft Teams Fix

> [!summary] Summary
> Teams won't install, won't open, or keeps failing to sign in.
> Part A = clean reinstall. Part B = sign-in failures, from light to heavy fixes.

> [!warning] Most important: select "No"
> When the sign-in popup asks **"Stay signed in to all your apps"**:
> - **Uncheck** "Allow my organization to manage my device"
> - Click **"No, sign in to this app only"**
>
> Choosing Yes binds the whole PC to the company account and causes repeated login loops.

All commands: run **PowerShell as Administrator**.

---

## Part A — Clean Uninstall & Reinstall

### A1. Delete leftover folders

Delete every folder / file containing `teams` in:

- `%appdata%\Microsoft`
- `%localappdata%\Packages\`
- `%localappdata%\Microsoft\WindowsApps`
- `%localappdata%\Microsoft\Packages`

> [!tip] "Access denied" on WindowsApps?
> Take ownership and reset permissions first:
> ```powershell
> # 1. Take ownership for Administrators
> takeown /f "$env:LOCALAPPDATA\Microsoft\WindowsApps" /r /d y
> # 2. Grant full control
> icacls "$env:LOCALAPPDATA\Microsoft\WindowsApps" /grant administrators:F /t
> # 3. Reset inheritance, clear explicit "deny"
> icacls "$env:LOCALAPPDATA\Microsoft\WindowsApps" /reset /t
> ```

### A2. Remove the Teams app package

```powershell
# Check installed version
Get-AppxPackage -AllUsers *MSTeams*

# Remove new + old Teams for all users
Get-AppxPackage -AllUsers -Name "MSTeams"        | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
Get-AppxPackage -AllUsers -Name "Microsoft.Teams" | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue

# Remove provisioned package (stops auto-reinstall for new users)
Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like "*Teams*"} |
    Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
```

### A3. Delete registry entry

Open `regedit`, go to the key below, and delete the `msteams.exe` subkey:

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\App Paths\msteams.exe
```

### A4. Reinstall

```powershell
# Install latest Teams from official source via winget
winget install --id Microsoft.Teams -e --accept-source-agreements --accept-package-agreements
```

> [!caution]- Store apps broken too? Re-register all apps
> Slow (several minutes), lots of red errors are normal. Use only if other Store apps are broken.
> ```powershell
> Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml" -Verbose}
> ```

---

## Part B — Sign-in Failed

Try levels in order; reopen Teams after each one.

### Level 1 — Clear Teams cache

```powershell
# 1. Kill Teams processes
Stop-Process -Name "Teams", "ms-teams" -Force -ErrorAction SilentlyContinue

# 2. Clear new Teams cache
Get-ChildItem -Path "$env:LOCALAPPDATA\Packages" -Filter "*Teams*" -ErrorAction SilentlyContinue | ForEach-Object {
    $cache = "$($_.FullName)\LocalCache\Microsoft\ms-teams"
    if (Test-Path $cache) {
        Remove-Item -Path $cache -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "Cleared: $cache" -ForegroundColor Green
    }
}

# 3. Clear classic Teams cache, just in case
$classic = "$env:APPDATA\Microsoft\Teams"
if (Test-Path $classic) {
    Remove-Item -Path $classic -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Cleared classic cache" -ForegroundColor Green
}
```

Or simply reset the app (same as Settings → Apps → Teams → Reset):

```powershell
Get-AppxPackage *MSTeams* | Reset-AppxPackage
```

### Level 2 — Clear sign-in tokens & saved credentials

> [!tip] This is the core fix for "ghost" accounts
> Teams keeps signing into an old / wrong company account.

```powershell
Stop-Process -Name "Teams", "ms-teams" -Force -ErrorAction SilentlyContinue

# 1. Clear AAD (Azure AD) token cache
$aad = "$env:LOCALAPPDATA\Packages\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy"
if (Test-Path $aad) {
    Remove-Item -Path "$aad\AC\TokenBroker\Accounts" -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path "$aad\LocalState"              -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Cleared AAD tokens" -ForegroundColor Green
}

# 2. Delete Microsoft / Teams entries in Credential Manager
cmdkey /list | Select-String "Target:" | ForEach-Object {
    $target = ($_.Line -replace "^\s*Target:\s*", "").Trim()
    if ($target -match "MicrosoftAccount|MicrosoftOffice|msteams") {
        cmdkey /delete:$target | Out-Null
        Write-Host "Deleted: $target" -ForegroundColor Green
    }
}

# 3. Stop Windows auto-linking the old work account
$reg = "HKCU:\Software\Microsoft\Office\16.0\Common\Identity"
if (Test-Path $reg) {
    Remove-ItemProperty -Path $reg -Name "EnableADAL" -ErrorAction SilentlyContinue
    New-ItemProperty -Path $reg -Name "DisableAADAutoConnect" -Value 1 -PropertyType DWORD -Force | Out-Null
    Write-Host "AAD auto-connect disabled" -ForegroundColor Green
}
```

Reopen Teams → when the popup appears, follow the **select "No"** warning at the top.

### Level 3 — Reinstall Teams

Do **Part A** (A2 + A4 is usually enough).

### Level 4 — Repair system sign-in components

> [!danger] Last resort
> `netsh` resets **all** network settings (VPN / proxy / static IP may need re-setup). **Reboot required.**

```powershell
# 1. Microsoft Account Sign-in Assistant service → Automatic + start
Set-Service   -Name "wlidsvc" -StartupType Automatic -ErrorAction SilentlyContinue
Start-Service -Name "wlidsvc" -ErrorAction SilentlyContinue

# 2. Re-register Windows sign-in components
$components = @(
    "C:\Windows\SystemApps\Microsoft.Windows.CloudExperienceHost_cw5n1h2txyewy",  # local account provider
    "C:\Windows\SystemApps\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy"              # Azure AD broker
)
foreach ($c in $components) {
    if (Test-Path $c) {
        Add-AppxPackage -Register "$c\AppxManifest.xml" -DisableDevelopmentMode -ForceApplicationShutdown
    }
}

# 3. Reset network stack (fixes proxy hijack / server not found)
netsh winsock reset
netsh int ip reset

Write-Host "Done. Please REBOOT." -ForegroundColor Cyan
```
