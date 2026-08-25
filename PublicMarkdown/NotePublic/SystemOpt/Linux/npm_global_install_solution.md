# npm 全局安装权限问题 — 方案一

## 问题

执行：

```bash
npm install -g <package>
```

出现：

```text
EACCES: permission denied
```

通常是因为普通用户没有权限写入系统级 npm 全局目录，例如：

```text
/usr/local/lib/node_modules
```

---

## 解决方案：修改 npm 全局安装目录

将 npm 的全局安装目录改到当前用户自己的目录，从而不需要 `sudo`。

### 1. 创建用户级 npm 全局目录

```bash
mkdir -p ~/.npm-global
```

### 2. 修改 npm 的 global prefix

```bash
npm config set prefix '~/.npm-global'
```

检查：

```bash
npm config get prefix
```

应该类似：

```text
/home/ccs2/.npm-global
```

### 3. 将全局 npm 命令加入 PATH

编辑：

```bash
nano ~/.bashrc
```

在文件末尾添加：

```bash
export PATH="$HOME/.npm-global/bin:$PATH"
```

保存并退出：

```text
Ctrl + O
Enter
Ctrl + X
```

### 4. 立即加载配置

```bash
source ~/.bashrc
```

检查：

```bash
echo $PATH
```

应该包含：

```text
/home/ccs2/.npm-global/bin
```

### 5. 重新安装 npm 包

例如：

```bash
npm install -g @openai/codex
```

以后安装全局 npm 包时，都可以直接：

```bash
npm install -g <package>
```

不需要：

```bash
sudo npm install -g <package>
```

---

## 验证

查看 npm 全局安装目录：

```bash
npm prefix -g
```

查看全局 node_modules：

```bash
npm root -g
```

查看已经安装的全局包：

```bash
npm list -g --depth=0
```

查看 npm 全局命令：

```bash
ls -la ~/.npm-global/bin
```

---

## 一键配置

如果使用 Bash，可以直接执行：

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

然后：

```bash
npm install -g @openai/codex
```

---

## 注意

不要为了简单解决权限问题而长期使用：

```bash
sudo npm install -g <package>
```

推荐让 npm 的全局安装目录归当前用户管理：

```text
/usr/local/lib/node_modules
        ↓
~/.npm-global/lib/node_modules
```

这样可以避免 npm 全局包产生的权限问题。
