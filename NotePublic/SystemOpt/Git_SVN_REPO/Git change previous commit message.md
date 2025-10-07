# 修改之前commit 的messsage

### 修改更早的提交信息

1. **使用 `git rebase -i`**：
   找到你想修改的提交的父提交 ID，执行：

   ```bash
   git rebase -i <commit-id>^
   ```

   这里 `<commit-id>` 是你想修改的提交的哈希值。`^` 表示选择该提交的父提交。

2. **选择要修改的提交**：
   在打开的编辑器中，找到你想修改的提交，将“pick”改为“reword”或“edit”。然后保存并关闭编辑器。

3. **修改提交信息**：
   如果选择了“reword”，Git 会暂停并允许你修改提交信息。编辑完成后保存并关闭编辑器。

   如果选择了“edit”，你需要手动运行以下命令来修改提交信息：

   ```bash
   git commit --amend
   ```

4. **继续 rebase**：
   修改完成后，继续 rebase 过程：

   ```bash
   git rebase --continue
   ```

5. 添加 submodule
```
git submodule add https://github.com/CodingKilling/ChipCode  CodeMemory/ChipCode/sub-repo
```

***
- **repo reset hard**
```
 repo forall -c 'git reset --hard HEAD && git clean -fd'
```


