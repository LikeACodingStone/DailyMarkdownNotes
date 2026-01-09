### Solution Example
- #### Error
```
error: Cannot checkout platform/proprietary
Checking out:  66% (948/1425), done in 4.310s
error: Unable to fully sync the tree
error: Checking out local projects failed.
```
- #### Solution
- #### grep error to get path
```
grep -r "platform/proprietary" .repo/manifests/
```
- #### the result show the platform/proprietary path is "proprietary"
```
fred@fred:~/baosp$ grep -r "platform/proprietary" .repo/manifests/
.repo/manifests/bosch.xml:  <remove-project name="platform/proprietary" />
.repo/manifests/bosch.xml:  <project name="platform/proprietary" path="proprietary" revision="ccs2_basesw_lbsp_la-3.4.2-r00012.3_a12_int" />
.repo/manifests/aosp.xml:<project name="platform/proprietary" path="proprietary" revision="ccs2_LA.AU.3.4.2_r00012.3" />
.repo/manifests/bosch_static.xml:  <remove-project name="platform/proprietary"/>
.repo/manifests/bosch_static.xml:  <project name="platform/proprietary" path="proprietary" revision="de7f0cac67c2f947621ddf6662d7c3348d34ff88" upstream="ccs2_basesw_lbsp_la-3.4.2-r00012.3_a12_int" dest-branch="ccs2_basesw_lbsp_la-3.4.2-r00012.3_a12_int"/>
.repo/manifests/aosp_static.xml:<project name="platform/proprietary" path="proprietary" revision="59edca68d1c495779bed3dc22efdbdf1c8c93feb" upstream="ccs2_LA.AU.3.4.2_r00012.3" dest-branch="ccs2_LA.AU.3.4.2_r00012.3"/>
fred@fred:~/baosp$ 
```
- #### 删除仓库重新下载
```
rm -rf proprietary
rm -rf .repo/projects/proprietary.git
rm -rf .repo/project-objects/platform/proprietary.git

# 重新同步该项目
repo sync proprietary -c --force-sync --no-tags --no-clone-bundle -j1
```

- #### repo在git子仓库下载代码
```
假如 1112877 是cherry-pick 的 id 号 
repo download -c . 1112877
``` 