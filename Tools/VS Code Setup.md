---
tags: [tools, vscode, clang, lldb, markdown]
updated: 2026-11-04
---
# VS Code Setup

> [!summary] Summary
> 1. Paste images into `_resources/` when writing Markdown
> 2. Build and debug C++ with Clang + CodeLLDB on Windows

---

## 1. Markdown: Where Pasted Images Go

> [!tip] Why
> Pasted images then land in the same `_resources/` folder that Obsidian uses (`vscodeImages.png`, `vscodeImages-1.png`, ...).

1. Press `Ctrl + Shift + P` → **Preferences: Open User Settings (JSON)**
2. Add:

```json
"markdown.copyFiles.destination": {
  "**/*": "_resources/vscodeImages"
}
```

---

## 2. C++ with Clang + CodeLLDB

**Needs:** Clang installed, and the **CodeLLDB** extension (a native debugger powered by LLDB: debug C++, Rust and other compiled languages).

### `tasks.json`: build

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

### `launch.json`: debug

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
