## Microsoft Teams Reset and Install solution
### 1. Delete folder by manual, delete every folder and file contains "teams" 
- %appdata%\Microsoft
- %localappdata%\Packages\
- %localappdata%\Microsoft\WindowsApps
- %localappdata%\Microsoft\Packages
### 2. PowerShell administrator running
```
Get-AppxPackage -AllUsers *MSTeams*
```
```
Remove-AppxPackage -Package "MSTeams_26106.1906.4665.7308_x64__8wekyb3d8bbwe" -AllUsers
```
```
Get-AppXPackage -AllUsers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml" -Verbose}
```
```
Remove-AppxPackage -Package "MSTeams_26106.1906.4665.7308_x64__8wekyb3d8bbwe" -AllUsers
```
```
# 1. 强行将该残留文件夹的所有者更改为当前管理员组
takeown /f "$env:LOCALAPPDATA\Microsoft\WindowsApps" /r /d y

# 2. 赋予管理员组对该目录及其子文件的完全控制权限
icacls "$env:LOCALAPPDATA\Microsoft\WindowsApps" /grant administrators:F /t

# 3. 强制重置继承权限并清除任何显式的“拒绝”属性
icacls "$env:LOCALAPPDATA\Microsoft\WindowsApps" /reset /t
```
### 3. Delete regedit 
```
// msteams.exe
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\App Paths
```

### 4. Login Failed
```
# 1. 强行关闭所有 Teams 进程
Write-Host "正在关闭 Teams 进程..." -ForegroundColor Yellow
Stop-Process -Name "Teams" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "ms-teams" -Force -ErrorAction SilentlyContinue

# 2. 清理新版 Teams (TypeApp) 的本地数据与缓存
Write-Host "正在清理新版 Teams 缓存..." -ForegroundColor Yellow
$LocalPackages = "$env:LOCALAPPDATA\Packages"
Get-ChildItem -Path $LocalPackages -Filter "*Teams*" -ErrorAction SilentlyContinue | ForEach-Object {
    $SettingsPath = "$($_.FullName)\LocalCache\Microsoft\ms-teams"
    if (Test-Path $SettingsPath) {
        Remove-Item -Path $SettingsPath -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "已清理: $SettingsPath" -ForegroundColor Green
    }
}

# 3. 清理经典版 Teams 的缓存（以防万一）
Write-Host "正在清理经典版 Teams 缓存..." -ForegroundColor Yellow
$ClassicTeamsCache = "$env:APPDATA\Microsoft\Teams"
if (Test-Path $ClassicTeamsCache) {
    Remove-Item -Path $ClassicTeamsCache -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "已清理经典版 Teams 缓存" -ForegroundColor Green
}

# 4. 清理 Windows 凭据管理器中的 Teams 登录凭据
Write-Host "正在清理 Windows 凭据管理器中的 Teams 相关凭据..." -ForegroundColor Yellow
cmdkey /list | Select-String "target=" | ForEach-Object {
    if ($_ -match "MicrosoftAccount:user=|Microsoft_me_=|msteams_") {
        $target = ($_ -split "target=")[1].Trim()
        cmdkey /delete:$target | Out-Null
        Write-Host "已删除凭据: $target" -ForegroundColor Green
    }
}

Write-Host "【修复完成】请重新启动 Teams 并尝试登录！" -ForegroundColor Cyan
```
```
# 重新注册 Windows.Identity.LocalAccountProvider 组件
Write-Host "正在重置本地账户认证组件..." -ForegroundColor Yellow
if (Test-Path "C:\Windows\SystemApps\Microsoft.Windows.CloudExperienceHost_cw5n1h2txyewy") {
    Add-AppxPackage -Register "C:\Windows\SystemApps\Microsoft.Windows.CloudExperienceHost_cw5n1h2txyewy\AppxManifest.xml" -DisableDevelopmentMode -ForceApplicationShutdown
}

# 重新注册 Microsoft.AAD.BrokerPlugin (Azure 活动目录认证插件)
Write-Host "正在重置 AAD 认证插件..." -ForegroundColor Yellow
if (Test-Path "C:\Windows\SystemApps\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy") {
    Add-AppxPackage -Register "C:\Windows\SystemApps\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy\AppxManifest.xml" -DisableDevelopmentMode -ForceApplicationShutdown
}

Write-Host "【组件重置完成】建议重启电脑后再次尝试登录 Teams。" -ForegroundColor Cyan
```
```
# 1. 将微软账户登录助手服务（wlidsvc）设置为自动启动
Write-Host "正在恢复微软账户登录服务..." -ForegroundColor Yellow
Set-Service -Name "wlidsvc" -StartupType Automatic -ErrorAction SilentlyContinue

# 2. 启动该服务
Start-Service -Name "wlidsvc" -ErrorAction SilentlyContinue

# 3. 修复网络底层协议栈（防止代理劫持导致找不到服务器文件）
Write-Host "正在重置网络协议栈..." -ForegroundColor Yellow
netsh winsock reset
netsh int ip reset

Write-Host "【修复完成】请务必重启电脑，然后再次尝试登录 Teams。" -ForegroundColor Cyan
```
```
Write-Host "正在强制卸载所有 Teams 关联组件..." -ForegroundColor Yellow

# 强制卸载新版 Teams
Get-AppxPackage -AllUsers -Name "Microsoft.Teams" | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue
Get-AppxPackage -AllUsers -Name "MSTeams" | Remove-AppxPackage -AllUsers -ErrorAction SilentlyContinue

# 清理残留的系统应用商店安装包
Get-AppxProvisionedPackage -Online | Where-Object {$_.PackageName -like "*Teams*"} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue

Write-Host "卸载完成！" -ForegroundColor Green
Write-Host "正在通过微软官方源重新下载安装最新版 Teams..." -ForegroundColor Yellow

# 使用 Windows 自带的 winget 工具静默安装最新版 Teams
winget install --id Microsoft.Teams -e --accept-source-agreements --accept-package-agreements

Write-Host "【安装完成】请尝试重新打开 Teams 登录。" -ForegroundColor Cyan
```
```
Write-Host "正在强制清理公司账户死锁的注册表键值..." -ForegroundColor Yellow

# 1. 强杀进程
Stop-Process -Name "Teams" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "ms-teams" -Force -ErrorAction SilentlyContinue

# 2. 清理 AAD (Azure Active Directory) 缓存在当前用户下的身份插件数据
$IdentityPath = "$env:LOCALAPPDATA\Packages\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy"
if (Test-Path $IdentityPath) {
    Remove-Item -Path "$IdentityPath\AC\TokenBroker\Accounts" -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item -Path "$IdentityPath\LocalState" -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "已清理 AAD 核心令牌缓存。" -ForegroundColor Green
}

# 3. 强制清理注册表中残留的身份验证错误状态
$RegPath = "HKCU:\Software\Microsoft\Office\16.0\Common\Identity"
if (Test-Path $RegPath) {
    Remove-ItemProperty -Path $RegPath -Name "EnableADAL" -ErrorAction SilentlyContinue
    New-ItemProperty -Path $RegPath -Name "DisableAADAutoConnect" -Value 1 -PropertyType DWORD -Force -ErrorAction SilentlyContinue
    Write-Host "已禁用系统自动关联旧企业账号，强制 Teams 重新弹窗。" -ForegroundColor Green
}

Write-Host "【修复完成】请重新打开 Teams。如果弹窗，千万不要勾选 '允许我的组织管理我的设备'！" -ForegroundColor Cyan
```
```
Get-AppxPackage -Name "*Teams*" | ForEach-Object {Reset-AppxPackage $_.PackageUserInformation.UserSecurityId.Value}
```
```
# 1. 强制结束 Teams
Stop-Process -Name "Teams" -Force -ErrorAction SilentlyContinue
Stop-Process -Name "ms-teams" -Force -ErrorAction SilentlyContinue

# 2. 清理当前用户路径下的微软登录令牌（核心步骤）
$WamPath = "$env:LOCALAPPDATA\Packages\Microsoft.AAD.BrokerPlugin_cw5n1h2txyewy\AC\TokenBroker\Accounts"
if (Test-Path $WamPath) {
    Get-ChildItem -Path $WamPath -Recurse | Remove-Item -Force -Recurse -ErrorAction SilentlyContinue
    Write-Host "已成功粉碎幽灵登录凭据！" -ForegroundColor Green
}

# 3. 清理新版 Teams 的本地配置文件
$TeamsIdentity = "$env:LOCALAPPDATA\Packages\Microsoft.Teams_8wekyb3d8bbwe\LocalCache\Microsoft\ms-teams"
if (Test-Path $TeamsIdentity) {
    Remove-Item -Path $TeamsIdentity -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "已清理 Teams 独立缓存。" -ForegroundColor Green
}

Write-Host "【清理完成】请重新打开 Teams 尝试登录。" -ForegroundColor Cyan
```
### 5. Important,  Select No,
![alt text](_resources/vscodeImages)