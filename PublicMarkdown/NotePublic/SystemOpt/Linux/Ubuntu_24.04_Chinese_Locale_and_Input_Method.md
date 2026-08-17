# Ubuntu 24.04 中文语言环境与中文输入法配置

> 来源：CSDN 文章  
> https://blog.csdn.net/unravel_tom/article/details/139360244
>
> 本笔记整理文章中的全部主要操作步骤，并按实际执行顺序重新编排。

---

## 1. 安装中文语言包

更新软件源：

```bash
sudo apt-get update
```

安装简体中文语言包：

```bash
sudo apt-get install language-pack-zh-hans
```

---

## 2. 配置 Locale

执行：

```bash
sudo dpkg-reconfigure locales
```

进入交互界面后：

1. 找到：

   ```text
   zh_CN.UTF-8
   ```

2. 选择 `zh_CN.UTF-8` 生成该 Locale。
3. 后续再次要求选择默认 Locale 时，选择：

   ```text
   zh_CN.UTF-8
   ```

最终默认 Locale 应为：

```text
zh_CN.UTF-8
```

---

## 3. 安装 Vim

如果系统没有 Vim：

```bash
sudo apt install vim
```

---

## 4. 修改 ~/.profile

编辑：

```bash
vim ~/.profile
```

在文件末尾加入：

```bash
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN:zh
export LC_ALL=zh_CN.UTF-8
```

保存退出 Vim：

```text
Esc
:wq
Enter
```

---

## 5. 立即应用配置

执行：

```bash
source ~/.profile
```

检查环境变量：

```bash
echo $LANG
echo $LANGUAGE
echo $LC_ALL
```

正常情况下：

```text
zh_CN.UTF-8
zh_CN:zh
zh_CN.UTF-8
```

---

## 6. 重启系统

为了让桌面环境和所有应用程序完整加载新的语言环境：

```bash
sudo reboot
```

---

# 中文输入法

## 7. 添加 Ubuntu 自带中文输入法

重启后打开：

```text
Settings
    ↓
Keyboard
    ↓
Input Sources
    ↓
Add Input Source
```

选择：

```text
Chinese
```

然后选择：

```text
Intelligent Pinyin
```

添加完成后，可以通过 Ubuntu 顶部栏的输入法指示器查看和切换输入法。

---

## 8. 找不到 Intelligent Pinyin 时

如果：

```text
Chinese → Intelligent Pinyin
```

中没有找到智能拼音，需要进一步配置输入法框架。

文章中提到可以通过 Ubuntu 的语言支持相关设置继续配置。

---

# 全部命令汇总

以下是文章中主要命令的集中版本：

```bash
sudo apt-get update

sudo apt-get install language-pack-zh-hans

sudo dpkg-reconfigure locales

sudo apt install vim

vim ~/.profile
```

向 `~/.profile` 添加：

```bash
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN:zh
export LC_ALL=zh_CN.UTF-8
```

然后：

```bash
source ~/.profile

echo $LANG
echo $LANGUAGE
echo $LC_ALL

sudo reboot
```

---

# 注意事项

## 1. 这套配置会改变系统语言环境

下面三个变量：

```bash
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN:zh
export LC_ALL=zh_CN.UTF-8
```

会让当前用户环境倾向于使用中文。

如果你的目的只是：

> 保持 Ubuntu 系统界面为英文，但能够输入中文

那么**不建议直接加入这三行**。

---

## 2. Ubuntu 24.04 + GNOME + Wayland

如果使用的是：

```text
Ubuntu 24.04
GNOME
Wayland
```

并且主要需求只是中文输入，通常更适合单独配置输入法框架，例如：

```text
Fcitx5
+
fcitx5-chinese-addons
+
Pinyin
```

这样可以保持系统 UI 为英文，同时提供中文拼音输入。

---

# 推荐使用场景

### 需要完整中文系统

可以按照本文完整执行：

```text
中文 Locale
+
中文系统界面
+
Intelligent Pinyin
```

### 只需要中文输入

建议：

```text
英文系统界面
+
Fcitx5
+
中文拼音
```

不要修改：

```bash
LANG
LANGUAGE
LC_ALL
```

---

## 参考

原始文章：

https://blog.csdn.net/unravel_tom/article/details/139360244
