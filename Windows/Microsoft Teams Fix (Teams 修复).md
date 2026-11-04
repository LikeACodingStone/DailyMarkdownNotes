---
tags: [windows, teams, powershell]
updated: 2026-11-04
---
# Microsoft Teams Fix [Teams 修复]

> [!summary] Summary [概要]
> Teams won't install, won't open, or keeps failing to sign in. [Teams 无法安装、打不开或反复登录失败。]
> Part A = clean reinstall [彻底重装]. Part B = sign-in failures, from light to heavy fixes [登录失败，由轻到重逐级尝试].

> [!warning] Most important: select "No" [最重要：选择 No]
> When the sign-in popup asks **"Stay signed in to all your apps"**:
> - **Uncheck** "Allow my organization to manage my device" [**取消勾选** "允许我的组织管理我的设备"]
> - Click **"No, sign in to this app only"** [点击 **"否，仅登录此应用"**]
>
> Choosing Yes binds the whole PC to the company account and causes repeated login loops. [选 Yes 会把整台电脑绑定到公司账户，导致反复登录失败。]

All commands: run **PowerShell as Administrator** [以管理员身份运行 PowerShell].

---

## Part A — Clean Uninstall & Reinstall [彻底卸载重装]

### A1. Delete leftover folders [手动删除残留文件夹]

Delete every folder / file containing `teams` in: [删除以下目录中所有包含 `teams` 的文件夹和文件：]

- `%appdata%\Microsoft`
- `%localappdata%\Packages\`
- `%localappdata%\Microsoft\WindowsApps`
- `%localappdata%\Microsoft\Packages`

> [!tip] "Access denied" on WindowsApps? [WindowsApps 提示拒绝访问？]
> Take ownership and reset permissions first: [先获取所有权并重置权限：]
> ```powershell
> # 1. Take ownership for Administrators [将所有者改为管理员组]
> takeown /f "$env:LOCALAPPDATA\Microsoft\WindowsApps" /r /d y
> # 2. Grant full control [赋予管理员完全控制权限]
> icacls "$env:LOCALAPPDATA\Microsoft\WindowsApps" /grant administrators:F /t
> # 3. Reset inheritance, clear explicit "deny" [重置继承权限，清除"拒绝"属性]
> icacls "$env:LOCALAPPDATA\Microsoft\WindowsApps" /reset /t
> ```

### A2. Remove the Teams app package [卸载 Teams 应用包]

```powershell
# Check installed version [查看已安装版本]
Get-AppxPackage -AllUsers *MSTeams*

# Remove new + old Teams for all users [为所有用户卸载新版和旧版 Teams]
Get-AppxPackage -AllUsers -Name "MSTeams"        | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
Get-AppxPackage -AllUsers -Name "Microsoft.Teams" | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue

# Remove provisioned package (stops auto-reinstall for new users) [清除系统预置安装包]
Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like "*Teams*"} |
    Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue
```

### A3. Delete registry entry [删除注册表项]

Open `regedit`, go to the key below, and delete the `msteams.exe` subkey: [打开 `regedit`，删除下面的 `msteams.exe` 子项：]

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\App Paths\msteams.exe
```

### A4. Reinstall [重新安装]

```powershell
# Install latest Teams from official source via winget [用 winget 从官方源安装最新版]
winget install --id Microsoft.Teams -e --accept-source-agreements --accept-package-agreements
```

> [!caution]- Store apps broken too? Re-register all apps [商店应用也异常？重新注册所有应用]
> Slow (several minutes), lots of red errors are normal. Use only if other Store apps are broken. [很慢，出现大量红色报错是正常的。仅在其他商店应用也坏掉时使用。]
> ```powershell
> Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml" -Verbose}
> ```

---

## Part B — Sign-in Failed [登录失败]

Try levels in order; reopen Teams after each one. [按顺序尝试，每一级完成后重新打开 Teams 测试。]

### Level 1 — Clear Teams cache [清理 Teams 缓存]

```powershell
# 1. Kill Teams processes [强制关闭 Teams 进程]
Stop-Process -Name "Teams", "ms-teams" -Force -ErrorAction SilentlyContinue

# 2. Clear new Teams cache [清理新版 Teams 缓存]
Get-ChildItem -Path "$env:LOCALAPPDATA\Packages" -Filter "*Teams*" -ErrorAction SilentlyContinue | ForEach-Object {
    $cache = "$($_.FullName)\LocalCache\Microsoft\ms-teams"
    if (Test-Path $cache) {
        Remove-Item -Path $cache -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "Cleared [已清理]: $cache" -ForegroundColor Green
    }
}

# 3. Clear classic Teams cache, just in case [清理经典版 Teams 缓存，以防万一]
$classic = "$env:APPDATA\Microsoft\Teams"
if (Test-Path $classic) {
    Remove-Item -Path $classic -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Cleared classic cache [已清理经典版缓存]" -ForegroundColor Green
}
```

Or simply reset the app (same as Settings → Apps → Teams → Reset): [或直接重置应用（等同于 设置 → 应用 → Teams → 重置）：]

```powershell
Get-AppxPackage *MSTeams* | Reset-AppxPackage
```

### Level 2 — Clear sign-in tokens & saved credentials [清理登录令牌和凭据]

> [!tip] This is the core fix for "ghost" accounts [这是解决"幽灵账户"的核心步骤]
> Teams keeps signing into an old / wrong company account. [Teams 总是自动登录旧的或错误的公司账户。]

```powershell
Stop-Process -Name "Teams", "ms-teams" -Force -ErrorAction SilentlyContinue

# 1. Clear AAD (Azure AD) token cache [清理 AAD 令牌缓存]
$aad = "$env:LOCALAPPDATA\Packages\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy"
if (Test-Path $aad) {
    Remove-Item -Path "$aad\AC\TokenBroker\Accounts" -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path "$aad\LocalState"              -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "Cleared AAD tokens [已清理 AAD 令牌]" -ForegroundColor Green
}

# 2. Delete Microsoft / Teams entries in Credential Manager [删除凭据管理器中的微软/Teams 凭据]
cmdkey /list | Select-String "Target:" | ForEach-Object {
    $target = ($_.Line -replace "^\s*Target:\s*", "").Trim()
    if ($target -match "MicrosoftAccount|MicrosoftOffice|msteams") {
        cmdkey /delete:$target | Out-Null
        Write-Host "Deleted [已删除]: $target" -ForegroundColor Green
    }
}

# 3. Stop Windows auto-linking the old work account [禁止系统自动关联旧企业账号，强制重新弹窗]
$reg = "HKCU:\Software\Microsoft\Office\16.0\Common\Identity"
if (Test-Path $reg) {
    Remove-ItemProperty -Path $reg -Name "EnableADAL" -ErrorAction SilentlyContinue
    New-ItemProperty -Path $reg -Name "DisableAADAutoConnect" -Value 1 -PropertyType DWORD -Force | Out-Null
    Write-Host "AAD auto-connect disabled [已禁用自动关联]" -ForegroundColor Green
}
```

Reopen Teams → when the popup appears, follow the **select "No"** warning at the top. [重新打开 Teams → 弹窗时按顶部的 **选择 No** 操作。]

### Level 3 — Reinstall Teams [重装 Teams]

Do **Part A** (A2 + A4 is usually enough). [执行 **Part A**（通常 A2 + A4 就够了）。]

### Level 4 — Repair system sign-in components [修复系统登录组件]

> [!danger] Last resort [最后手段]
> `netsh` resets **all** network settings (VPN / proxy / static IP may need re-setup). **Reboot required.**
> [`netsh` 会重置**所有**网络设置（VPN、代理、固定 IP 可能需要重新配置）。**必须重启。**]

```powershell
# 1. Microsoft Account Sign-in Assistant service → Automatic + start [微软账户登录助手服务设为自动并启动]
Set-Service   -Name "wlidsvc" -StartupType Automatic -ErrorAction SilentlyContinue
Start-Service -Name "wlidsvc" -ErrorAction SilentlyContinue

# 2. Re-register Windows sign-in components [重新注册系统登录组件]
$components = @(
    "C:\Windows\SystemApps\Microsoft.Windows.CloudExperienceHost_cw5n1h2txyewy",  # local account provider [本地账户认证]
    "C:\Windows\SystemApps\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy"              # Azure AD broker [AAD 认证插件]
)
foreach ($c in $components) {
    if (Test-Path $c) {
        Add-AppxPackage -Register "$c\AppxManifest.xml" -DisableDevelopmentMode -ForceApplicationShutdown
    }
}

# 3. Reset network stack (fixes proxy hijack / server not found) [重置网络协议栈，防止代理劫持]
netsh winsock reset
netsh int ip reset

Write-Host "Done. Please REBOOT. [完成，请务必重启电脑。]" -ForegroundColor Cyan
```
