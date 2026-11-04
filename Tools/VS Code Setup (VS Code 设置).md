---
tags: [tools, vscode, clang, lldb, markdown]
updated: 2026-11-04
---
# VS Code Setup [VS Code 设置]

> [!summary] Summary [概要]
> 1. Paste images into `_resources/` when writing Markdown [写 Markdown 时把粘贴的图片存到 `_resources/`]
> 2. Build and debug C++ with Clang + CodeLLDB on Windows [在 Windows 用 Clang + CodeLLDB 编译调试 C++]

---

## 1. Markdown: Where Pasted Images Go [粘贴图片的保存位置]

> [!tip] Why [为什么]
> Pasted images then land in the same `_resources/` folder that Obsidian uses (`vscodeImages.png`, `vscodeImages-1.png`, ...).
> [这样粘贴的图片会进入 Obsidian 使用的同一个 `_resources/` 目录（`vscodeImages.png`、`vscodeImages-1.png` ……）。]

1. Press `Ctrl + Shift + P` → **Preferences: Open User Settings (JSON)** [打开 User Settings (JSON)]
2. Add [添加]:

```json
"markdown.copyFiles.destination": {
  "**/*": "_resources/vscodeImages"
}
```

---

## 2. C++ with Clang + CodeLLDB [Clang + CodeLLDB 编译调试]

**Needs [需要]:** Clang installed, and the **CodeLLDB** extension (a native debugger powered by LLDB: debug C++, Rust and other compiled languages).
[已安装 Clang，以及 **CodeLLDB** 扩展（基于 LLDB 的原生调试器，可调试 C++、Rust 等编译型语言）。]

### `tasks.json`: build [编译]

```jsonc
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build",
            "type": "shell",
            "command": "clang",
            "args": ["-o", "main.exe", "main.cpp"],
            "group": "build",
            "options": { "cwd": "${workspaceFolder}" },
            "problemMatcher": "$gcc"
        }
    ]
}
```

### `launch.json`: debug [调试]

```jsonc
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "(Windows) Launch",
      "type": "lldb",
      "request": "launch",
      "program": "${workspaceFolder}/main.exe",
      "args": [],
      "cwd": "${workspaceFolder}",
      "console": "integratedTerminal"
    }
  ]
}
```
