
#### 修改所有子模块的用户名和邮箱：
```

git submodule foreach 'git config user.name "New Name"'
git submodule foreach 'git config user.email "newemail@example.com"'
```

####  修改所有子模块的远程仓库 URL：
```
git submodule foreach 'git remote set-url origin ssh://new_user@new_host/path/to/repo.git'
```
### 递归修改所有子模块的 `user.name` 和 `user.email`

- 可以使用 `git submodule foreach` 命令递归修改所有子模块的用户名和邮箱
```
git submodule foreach 'git config user.name "New Name"'
git submodule foreach 'git config user.email "newemail@example.com"'
```
- 修改所有子模块的远程仓库 URL
```
git submodule foreach 'git remote set-url origin ssh://new_user@new_host/path/to/repo.git'
```

# change remote user
```
git remote -v // check currently
git remote set-url origin $newurl
```