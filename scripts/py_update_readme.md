# Update README navigation

Run this block with Execute Code, just like `Python_test.md`.

If the Run indicator stays at `...`, Execute Code has queued this block behind an unfinished run. Open the command palette → **Execute Code: Open Code Runtime Management**, stop the runtime for this note, then run this block again. You can also disable and re-enable Execute Code to clear stuck runtimes.

```python
print("START: README updater code is running.", flush=True)

from pathlib import Path
import os
import subprocess
import sys

# Add "--check" to check without writing.
arguments = []
try:
    script = Path(@vault_path) / "scripts" / "py_update_readme.py"
    if not script.is_file():
        raise FileNotFoundError(f"Cannot find script: {script}")
    print("Running updater (maximum 30 seconds)...", flush=True)
    result = subprocess.run(
        [sys.executable, "-u", str(script), *arguments],
        cwd=script.parent.parent,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        timeout=30,
    )
    if result.stdout:
        print(result.stdout, end="", flush=True)
    if result.returncode == 0:
        print("SUCCESS: README navigation is up to date.", flush=True)
    else:
        print(f"FAILURE: updater exited with code {result.returncode}.", flush=True)
except subprocess.TimeoutExpired as error:
    if error.output:
        output = error.output
        if isinstance(output, bytes):
            output = output.decode("utf-8", errors="replace")
        print(output, flush=True)
    print("FAILURE: updater exceeded 30 seconds and was stopped.", flush=True)
except Exception as error:
    print(f"FAILURE: {type(error).__name__}: {error}", flush=True)
```

The first `START` message confirms that the plugin has begun executing Python. If only `...` appears and there is no `START`, the block is still waiting in the plugin runtime; its timeout has not started yet.
