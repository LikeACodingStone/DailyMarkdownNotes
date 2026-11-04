---
tags: [ubuntu, linux, find, grep, shell]
updated: 2026-11-04
---
# Ubuntu Quick Search

> [!summary] Summary
> Count files, and find which folders hold the most files.

---

## 1. Count files in the current folder

```bash
ls -la | grep "^-" | wc -l
```

`grep "^-"` keeps only lines starting with `-`, which are regular files (folders start with `d`). Not recursive.

## 2. Count everything under home

```bash
find ~ | wc -l
```

Counts files **and** folders, recursively.

## 3. Which folders hold the most files?

```bash
find ~ -xdev -type f | cut -d/ -f1-5 | sort | uniq -c | sort -nr | head -20
```

| Part | Meaning |
|---|---|
| `-xdev` | Stay on one filesystem (skip other mounts) |
| `-type f` | Files only |
| `cut -d/ -f1-5` | Keep the first 4 path levels, e.g. `/home/user/dir/subdir`, so files are grouped by folder |
| `sort \| uniq -c` | Count files per folder |
| `sort -nr \| head -20` | Top 20, largest first |

> [!tip] Group deeper or shallower
> Change `-f1-5` to `-f1-6` for one more level, or `-f1-4` for one less.
