### repo-lfs, git-lfs
- saving the credential for countinously input account
```bash
# 假如 1112877 是cherry-pick 的 id 号 
repo download -c . 1112877

### backup all local changes for repo
repo forall -c 'git stash push -u -m "backup-before-repo-sync"'
```
