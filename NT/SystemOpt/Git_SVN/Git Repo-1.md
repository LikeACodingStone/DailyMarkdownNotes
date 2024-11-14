# Push To Review
`
git push --porcelain --progress --recurse-submodules=check origin refs/heads/branch_name:refs/for/branch_name
`
***
# Recurse 
 - recurse pull
`
git pull --recurse-submodules 
`
 - recurse checkout
`
git checkout branch_name --recurse-submodules
`
***
# Create Local Branch For Remote Mirror
 - already exists remote
`
  remotes/origin/stabilization/2024/product_vics_CCS2_LGE
`

 - create only 
`
git branch stabilization/2024/product_vics_CCS2_LGE --track   remotes/origin/stabilization/2024/product_vics_CCS2_LGE
`

 - create and checkout
`
git checkout -b stabilization/2024/product_vics_CCS2_LGE --track   remotes/origin/stabilization/2024/product_vics_CCS2_LGE
`
***
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




