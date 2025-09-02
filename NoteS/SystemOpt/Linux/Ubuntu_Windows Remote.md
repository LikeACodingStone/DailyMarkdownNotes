# Ubuntu 图形系统组件分类说明

将常见的 Ubuntu 图形系统相关组件按功能划分如下：

---

## 🧠 1. 显示服务（Display Server）

| 组件名 | 说明 |
|--------|------|
| **Xorg** | 传统的图形显示服务器（X Window System），兼容性好，xrdp 支持 |
| **Wayland** | 新一代显示协议，性能和安全性更强，但与 xrdp 不兼容 |

---

## 🔑 2. 显示管理器（Display Manager）

| 组件名 | 说明 |
|--------|------|
| **gdm3** | GNOME 的登录界面管理器，负责用户登录及图形会话启动。支持 Xorg 和 Wayland |

---

## 🧩 3. 会话管理器（Session Manager）

| 组件名 | 说明 |
|--------|------|
| **gnome-session** | GNOME 桌面环境的会话启动器，启动 GNOME Shell、窗口管理器等 |
| **startxfce4** | XFCE 桌面环境的会话启动命令，适合轻量远程桌面使用 |

---

## 🌐 4. 远程桌面服务（Remote Desktop Server）

| 组件名 | 说明 |
|--------|------|
| **xrdp** | 实现 RDP 协议服务端，允许 Windows 的 mstsc 连接 Ubuntu，需 Xorg 支持 |

---

## 🖥️ 5. 桌面环境（Desktop Environment）

| 组件名 | 说明 |
|--------|------|
| **GNOME** | Ubuntu 默认桌面环境，现代、完整，资源较重，不适合远程桌面 |
| **XFCE (xfce4)** | 轻量级桌面环境，资源占用少，适合远程连接，默认搭配 startxfce4 使用 |

---

## ✅ 推荐远程桌面配置（xrdp）

- 使用显示服务器：**Xorg**
- 禁用 Wayland（编辑 `/etc/gdm3/custom.conf`）
- 使用桌面环境：**XFCE**
- 启动命令：在 `~/.xsession` 中添加：
  ```bash
  exec startxfce4
  ```
- 重启服务：
  ```bash
  sudo systemctl restart xrdp
  ```

---
