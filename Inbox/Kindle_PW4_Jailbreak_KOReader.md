# Kindle PW4 越狱 + OTA 防护 + KOReader 笔记

> 适用背景：Kindle Paperwhite 4（10th Gen）。  
> **越狱方法必须以 KindleModding Jailbreaking Wizard 当前结果为准。** 本笔记以 Wizard 为准，并记录 SpiderCat 路线作为示例。
>
> 官方文档会随着固件变化而更新，操作前建议重新打开官方页面确认。

---

## 1. 设备信息

本次设备：

- Kindle Paperwhite 4 / 10th Generation
- Serial：G8S0
- Firmware：5.16.8
- 已注册 Amazon 账号
- 已确认有广告
- 已成功越狱
- 已确认 OTA 被禁止

---

## 2. 越狱前：先防止自动升级

### 为什么要先做

Kindle 连接 Wi-Fi 后可能自动下载/安装新固件。新固件可能修补当前可用的越狱方法。

官方 KindleModding 建议在越狱前填满存储空间，使可用空间只剩 **50–90 MB**。

本次可以直接以：

> **约 70 MB 可用空间**

作为目标值。

官方说明：
- [KindleModding：Prevent Automatic Updates](https://kindlemodding.org/jailbreaking/prevent-auto-update/)
- [KindleModding：Jailbreaking Wizard](https://kindlemodding.org/kindle-models)

### 操作

1. Kindle 连接电脑。
2. 使用 Kindle-Filler-Disk 工具填充 Kindle。
3. 最终检查可用空间：
   - **约 70 MB**
   - 官方允许范围：50–90 MB
4. 在越狱完成前，不要随意恢复空间。
5. 如果根目录出现 `update*.bin`，不要运行。

### Filler

官方说明页：

https://kindlemodding.org/jailbreaking/prevent-auto-update/

该页面提供 Kindle-Filler-Disk GitHub 仓库以及：

- Windows：`Filler.ps1`
- macOS/Linux：`Filler.sh`

---

## 3. 用官方 Wizard 确定越狱方法

不要根据网上旧教程自己猜方法。

打开：

https://kindlemodding.org/kindle-models

输入：

1. Serial 前 8 位
2. Firmware
3. 是否可以注册
4. 锁屏是否有广告

Wizard 会给出适合当前设备/固件的越狱方法。

---

# 4. SpiderCat 越狱

> **只有当 Wizard 当前把你的设备引导到 SpiderCat 时才使用这一部分。**

官方 SpiderCat 页面：

https://kindlemodding.org/jailbreaking/SpiderCat/

### SpiderCat 下载

官方直接下载：

https://kindlemodding.org/spidercat/spidercat.azw3

文件名：

```text
spidercat.azw3
```

### 通过 USB 安装

把：

```text
spidercat.azw3
```

复制到：

```text
Kindle/documents/
```

然后安全弹出 Kindle。

SpiderCat 会出现在 Kindle Library 中。

### 运行

1. 确保 Wi-Fi 开启。
2. 打开 SpiderCat。
3. 等待脚本执行。
4. 中途出现 Application Error / 错误弹窗，官方说明可以忽略。
5. 最终出现 `Restarting GUI`，等待 Kindle 返回主界面。

官方说明：
- SpiderCat 执行过程中不要关闭 Wi-Fi。
- 如果 `Restarting GUI` 持续 ≥10 分钟，可以按住电源键重启。

---

# 5. 如何确认越狱成功

在 Kindle 主界面搜索框输入：

```text
;log
```

然后回车。

如果出现类似：

```text
no arg passed
select from mrpi or runme
```

说明 `;log` 已经能够工作。

官方判断标准：

> 输入 `;log` 后出现提示文字 = 已越狱。

官方 FAQ：

https://kindlemodding.org/jailbreaking/jailbreak-faq.html

---

# 6. 越狱完成后：清理填充文件

现代 KindleModding 越狱完成后会自动阻止 OTA。

官方说明可以删除之前用于填满磁盘的 filler 文件。

检查 Kindle 根目录：

```text
Kindle/
├── documents/
├── fill_disk/       ← 越狱成功 + OTA 阻止后可以删除
└── ...
```

删除：

```text
fill_disk/
```

或者删除之前使用的 filler 文件。

这样可以恢复 Kindle 的可用空间。

### 同时检查

Kindle 根目录有没有：

```text
update*.bin
```

例如：

```text
update.bin
update-xxxxx.bin
update.partial.bin
```

如果有残留的固件更新文件，官方建议删除。

参考：

https://kindlemodding.org/jailbreaking/whats-next/

---

# 7. 删除 SpiderCat

越狱已经成功以后，SpiderCat 本身不再需要。

可以从：

```text
Kindle/documents/
```

删除：

```text
spidercat.azw3
```

不要删除其他越狱组件。

---

# 8. 检查 OTA 是否真的被禁止

推荐使用官方 FAQ 提供的 **Check OTA Status** scriptlet。

官方 FAQ：

https://kindlemodding.org/jailbreaking/jailbreak-faq.html

### 下载

GitHub：

https://github.com/neura-neura/Check-OTA-status/blob/main/Check%20OTA%20status_current.sh

Raw 直接下载：

https://raw.githubusercontent.com/neura-neura/Check-OTA-status/refs/heads/main/Check%20OTA%20status_current.sh

建议保存为：

```text
Check OTA status_current.sh
```

### 安装

把 `.sh` 文件复制到：

```text
Kindle/documents/
```

然后在 Kindle Library 中点击运行。

### 5.16.8 应该看到

类似：

```text
OTA blocking is enabled (>=5.11.x method).
Your Kindle will NOT update.
Your jailbreak is safe.
```

看到这一类结果，就说明 OTA 已经被禁止。

---

# 9. 安装 KOReader

现代 KindleModding 越狱已经预装 KPM。

安装前：

1. 越狱完成后已经重启过 Kindle。
2. 打开 Wi-Fi。
3. 保持 Kindle 可以访问网络。

### 第一步：更新 KPM 软件源

在 Kindle 主界面搜索：

```text
;kpm update
```

按回车。

等待执行结束。

### 第二步：安装 KOReader

搜索：

```text
;kpm install koreader
```

等待安装完成。

之后 Kindle Library 中会出现 KOReader 的启动项。

点击即可启动。

也可以搜索：

```text
;kpm launch koreader
```

### 卸载

如果以后需要卸载：

```text
;kpm uninstall koreader
```

官方说明：

https://kindlemodding.org/jailbreaking/whats-next/getting-koreader/

---

# 10. KOReader 以后怎么管理电子书

推荐把 Kindle 当成：

```text
Kindle
└── documents/
    ├── C++/
    ├── Linux/
    ├── Android/
    ├── Automotive/
    ├── Japanese/
    ├── English/
    ├── Novels/
    └── PDF/
        ├── Technical/
        └── Other/
```

KOReader 可以直接浏览这些真实目录。

### 推荐组合

```text
电脑
  ↓
Calibre
  ↓
整理电子书 / 作者 / 标签 / 格式
  ↓
Kindle
  ↓
KOReader
  ↓
阅读 EPUB / PDF
```

KOReader 支持 EPUB、PDF、DjVu、CBZ、CBT、FB2、TXT、MOBI 等多种格式。

官方：

https://koreader.rocks/user_guide/

---

# 11. 关于 Kindle 原生阅读器

越狱不会删除 Kindle 原生系统。

可以同时使用：

```text
Kindle 原生系统
    ├── Amazon 书籍
    └── Kindle 原生功能

KOReader
    ├── EPUB
    ├── PDF
    ├── 漫画
    └── 自己管理的文件夹
```

如果主要阅读自己的 EPUB/PDF，可以把 KOReader 作为主要阅读器。

注意：KOReader 对 Amazon 专有的 KFX、AZW3 等格式支持有限/不完整，官方建议给 KOReader 使用 EPUB。

---

# 12. 最终状态检查

完成后建议确认：

- [x] Wizard 确认正确越狱方法
- [x] 越狱成功
- [x] `;log` 有响应
- [x] OTA Status 显示 OTA blocking enabled
- [x] `update*.bin` 已清理
- [x] filler 文件已删除
- [x] SpiderCat 已删除
- [x] KPM 可用
- [x] KOReader 已安装
- [x] EPUB/PDF 已按文件夹整理

---

## 官方链接汇总

### KindleModding
https://kindlemodding.org/

### Jailbreaking Wizard
https://kindlemodding.org/kindle-models

### SpiderCat
https://kindlemodding.org/jailbreaking/SpiderCat/

### SpiderCat AZW3
https://kindlemodding.org/spidercat/spidercat.azw3

### 防止 OTA / 填满磁盘
https://kindlemodding.org/jailbreaking/prevent-auto-update/

### 越狱 FAQ
https://kindlemodding.org/jailbreaking/jailbreak-faq.html

### KOReader 安装
https://kindlemodding.org/jailbreaking/whats-next/getting-koreader/

### KOReader 官方
https://koreader.rocks/

### Check OTA Status
https://github.com/neura-neura/Check-OTA-status/blob/main/Check%20OTA%20status_current.sh

### Check OTA Status Raw
https://raw.githubusercontent.com/neura-neura/Check-OTA-status/refs/heads/main/Check%20OTA%20status_current.sh
