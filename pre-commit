#!/bin/sh

# 限制大小：50MB = 50 * 1024 * 1024 = 52428800 bytes
MAX_SIZE=52428800
MAX_SIZE_MB=50

# 标志位
TOO_LARGE=0

# 遍历所有准备 commit (staged) 的文件
git diff-index --cached --name-only HEAD | while read -r FILE; do
    # 忽略已被删除的文件
    if [ -f "$FILE" ]; then
        # 获取文件字节大小
        # 兼顾 macOS 和 Linux/Git Bash 的 stat 命令
        if stat -f "%z" "$FILE" >/dev/null 2>&1; then
            SIZE=$(stat -f "%z" "$FILE")
        else
            SIZE=$(stat -c "%s" "$FILE")
        fi

        # 判断是否超过 50M
        if [ "$SIZE" -gt "$MAX_SIZE" ]; then
            echo "warning: 文件 '$FILE' 大小为 $(($SIZE / 1048576))MB，超过了规定的 ${MAX_SIZE_MB}MB 限制！"
            TOO_LARGE=1
        fi
    fi

    if [ "$TOO_LARGE" -eq 1 ]; then
        exit 1
    fi
done

# 如果存在超大文件，阻止 commit 提交
if [ $? -ne 0 ]; then
    echo "错误: 请将大文件移除出暂存区，或改用 Git LFS 进行管理后再提交。"
    exit 1
fi