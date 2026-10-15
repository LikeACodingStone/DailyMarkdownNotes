### Git 
```bash
# for submodules
git pull --recurse-submodules
git checkout branch_name --recurse-submodules

# Create a local branch from a remote branch.
git branch local_branch --track remotes/origin/remote_branch
git checkout -b local_branch --track remotes/origin/remote_branch
git checkout -b stabilization/2024/product_vics_DA3_Bosch --track origin/stabilization/2024/product_vics_DA3_Bosch   # 创建本地分支并映射远程分支

# push for review
git push origin HEAD:refs/for/ccs2_ccs2_android_a14_int

# add save directory
git config --global --add safe.directory /path/to/repository

# Inspect and replace the current repository remote.
git remote -v
git remote set-url origin NEW_REMOTE_URL

# Cache credentials for one hour.
git config --global credential.helper 'cache --timeout=3600'

# exclude files that don`t want to be tracked by the git for ignore purpose
git rm -r --cached "**/__pycache__"  
git rm -r --cached "**/*.pyc"

# revert code for specific commit file
git restore --source=bbe9a5^ -- java/vendor/neusoft/service/etcvics/BoschSystemHandler.java

# worktree using
git worktree add ../baosp_a14 ccs2_a14_int

# From windows sambe access linux samba. no access via IDE or smartgit 
git config --global --add safe.directory *

# test git connection
ssh -T git@github.com

## git tag
git tag <tagName> 
git push origin <tagName> 


# unable to access 'https://github.com/CodingKilling/GitLab_Jimi.git/': OpenSSL SSL_read: Connection was reset, errno 10054
git config --global http.sslVerify "false"			// 设置不需要SSL认证
git config http.postBuffer 5242880003					// 设置最大大小500M

git submodule update --init --recursiv


```

## Repo
```bash
repo download -c . CHANGE_ID

### backup all local changes for repo
repo forall -c 'git stash push -u -m "backup-before-repo-sync"'
```
