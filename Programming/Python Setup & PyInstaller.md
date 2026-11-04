---
tags: [programming, python, pyqt5, pyinstaller, pycryptodome]
updated: 2026-11-04
---
# Python Setup & PyInstaller

> [!summary] Contents
> 1. Install PyQt5
> 2. Install a crypto library (and fix `No module named 'Crypto'`)
> 3. PyInstaller: build an exe

---

## 1. Install PyQt5

```bash
pip install PyQt5              # PyQt5
pip install PyQt5-tools        # tools, including Qt Designer
pip install pyqt5designer
```

Reference: https://blog.csdn.net/qq_23825121/article/details/125893796

---

## 2. Crypto Library

**Install only `pycryptodome`:**

```bash
pip install pycryptodome
```

> [!warning] Don't also install `crypto` and `pycrypto`
> The old note installed all three. `pycrypto` is abandoned and fails to build on Windows with modern Python:
> ```text
> Using legacy 'setup.py install' for pycrypto, since package 'wheel' is not installed.
> Running setup.py install for pycrypto ... error
> ERROR: Command errored out with exit status 1
> ```
> The lowercase `crypto` package then clashes with the real `Crypto` module.

> [!bug] `No module named 'Crypto'` after installing
> The folder was installed in lowercase. On Windows:
> 1. Open `...\Python\Lib\site-packages`
> 2. Find the folder **`crypto`** and rename it to **`Crypto`**
> 3. Run the program again: the error is gone

---

## 3. PyInstaller

```bash
pip3 install pyinstaller
```

**One exe, no console window, with an icon**

```bash
pyinstaller -F -w -i kent.ico SyncTwoDiskFiles.py
```

| Option | Meaning |
|---|---|
| `-F` | One single file (`--onefile`) |
| `-w` | Windowed: no console window |
| `-i kent.ico` | The program icon |
| `SyncTwoDiskFiles.py` | The main program (entry script) |

**Put the exe in the current folder and add config files**

```bat
pyinstaller --onefile --distpath . --add-data "config.ini;." --add-data "config_modules.ini;." MainForm.py
```

> [!warning] Three things to remember
> - **Everything must be on ONE line.** The old note split `MainForm.py` onto a second line, which breaks the command.
> - **The `--add-data` separator is `;` on Windows and `:` on Linux / macOS.**
> - In `--onefile` mode the added files are unpacked to a **temporary folder** when the program runs (`sys._MEIPASS`), not next to the exe.
