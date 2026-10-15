---
gists:
  - id: eb3eabde18ca7547736aa63fe48c54e4
    url: 'https://gist.github.com/LikeACodingStone/eb3eabde18ca7547736aa63fe48c54e4'
    createdAt: 2026-09-18T09:53:00.000Z
    updatedAt: '2026-10-15T09:02:21Z'
    filename: N_Version_Control_Containers_Cloud_Operations.md
    isPublic: true
    baseUrl: 'https://api.github.com'
---
### Git 
```bash
# for submodules
git pull --recurse-submodules
git checkout branch_name --recurse-submodules

# Create a local branch from a remote branch.
git branch local_branch --track remotes/origin/remote_branch
git checkout -b local_branch --track remotes/origin/remote_branch

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
```

## Repo
```bash
repo download -c . CHANGE_ID

### backup all local changes for repo
repo forall -c 'git stash push -u -m "backup-before-repo-sync"'
```
