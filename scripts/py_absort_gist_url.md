# 复制 Gist Markdown 链接

使用 Execute Code 点击 **Run** 后，程序会暂停等待输入。在代码块下方的输入框中输入文件名（例如 `repo_error_case_summary`），按 **Enter** 后自动生成链接并复制到剪贴板。文件名可以带或不带 `.md`，无需修改代码。等待输入时显示运行中是正常现象。

文件不存在或没有 Gist 地址时会提示并停止；复制成功时显示结果。不会上传文件或创建新的 Gist。

```python
print("START: Reading Gist URL...", flush=True)
from pathlib import Path
import runpy

try:
    script = Path(@vault_path) / "scripts" / "py_absort_gist_url.py"
    if not script.is_file():
        raise FileNotFoundError(f"Script not found: {script}")
    gist_tool = runpy.run_path(str(script))
    gist_tool["main"]([])
except Exception as error:
    print(f"FAILURE: {error}", flush=True)
```

示例结果：

```text
[repo_error_case_summary](https://gist.github.com/LikeACodingStone/daf4dcb15ea6b7ed6234e23baf06db76)
```

也可在终端运行：

```bash
python3 scripts/py_absort_gist_url.py
```

Windows 使用 PowerShell 写入剪贴板；macOS 使用 pbcopy；Linux 需要桌面会话以及 wl-copy、xclip 或 xsel。
