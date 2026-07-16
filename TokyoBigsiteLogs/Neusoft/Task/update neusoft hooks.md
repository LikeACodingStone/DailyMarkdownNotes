### update neusoft hooks
```
mkdir -p `git rev-parse --git-dir`/hooks/ && curl -kLo `git rev-parse --git-dir`/hooks/commit-msg https://review.nts.neusoft.local/tools/hooks/commit-msg && chmod +x `git rev-parse --git-dir`/hooks/commit-msg
```

git clone --recurse-submodules "ssh://a1294.zhou_nsj@ntssy-lxcm01.nts.neusoft.local:29418/integration/bosch/ccs20"