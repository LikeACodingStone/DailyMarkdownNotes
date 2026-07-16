# Ubuntu Benchmark Guide (Short Version)

## 1. CPU Benchmark (7z)

### Install
```bash
sudo apt update
sudo apt install p7zip-full -y
```

### Run Benchmark
```bash
7z b
```

### Check Score
Look at the bottom:

```text
Tot: XXXXX MIPS
```

Higher score = better CPU performance.

Tips:
- Close browsers, Docker, IDEs, downloads
- Wait 1–2 minutes if CPU was hot
- Run 3 times and average for stable results

---

## 2. AMD GPU Benchmark (Works with Xshell / SSH)

### Install
```bash
sudo apt update
sudo apt install xvfb glmark2 -y
```

### Run Benchmark
```bash
xvfb-run -a glmark2 --off-screen
```

### Check Score
At the end:

```text
glmark2 Score: XXXX
```

Higher score = better GPU performance.

Notes:
- Works for AMD dedicated GPU and integrated graphics (iGPU)
- Fixes SSH/Xshell display errors
- No physical monitor required

---

## 3. Optional GPU Monitoring

Install:
```bash
sudo apt install radeontop -y
```

Run:
```bash
sudo radeontop
```

Used for checking GPU utilization in real time.
