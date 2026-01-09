### repo在git子仓库下载代码
```
假如 1112877 是cherry-pick 的 id 号 
repo download -c . 1112877
``` 
### Got repo init address
```
cat .repo/manifests.git/config

// find url
[remote "origin"]
    url = https://android.googlesource.com/platform/manifest

repo init -u https://android.googlesource.com/platform/manifest
```
