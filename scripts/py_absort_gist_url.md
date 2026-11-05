# 更新 Gist 链接表

使用 Execute Code 点击 **Run** 后，程序会自动扫描 `gist_code` 文件夹里的所有笔记，读取每个笔记中的 Gist 地址，并重新生成 `scripts/gist-url-for-copy.md`。不需要输入文件名，也无需修改代码。

`gist-url-for-copy.md` 里是一个表格，每个笔记一行：左边是 `[name](link)` 链接，右边是 **Copy** 按钮。点击按钮即可把这一条 Markdown 链接复制到剪贴板。

**第一次使用前**：安装 **Dataview** 插件（设置 → 第三方插件 → 浏览 → 搜索 Dataview → 安装并启用），再在 Dataview 的设置里打开 **Enable JavaScript Queries**。按钮由 Dataview 渲染，没有这个插件，`gist-url-for-copy.md` 里只会显示一段代码。

还没有用 Share as Gist 分享过的笔记没有 Gist 地址，会被跳过并在输出里提示。每次运行都会覆盖整个 `gist-url-for-copy.md`，请不要手动编辑它。不会上传文件或创建新的 Gist。

```python
print("START: Scanning gist_code...", flush=True)
from pathlib import Path
import runpy

try:
    script = Path(@vault_path) / "scripts" / "py_absort_gist_url.py"
    if not script.is_file():
        raise FileNotFoundError(f"Script not found: {script}")
    gist_tool = runpy.run_path(str(script))
    gist_tool["main"]()
except Exception as error:
    print(f"FAILURE: {error}", flush=True)
```

点击某一行的 Copy 后，剪贴板里的内容形如：

```text
[repo-error-case-summary](https://gist.github.com/LikeACodingStone/daf4dcb15ea6b7ed6234e23baf06db76)
```

也可在终端运行：

```bash
python3 scripts/py_absort_gist_url.py
```
