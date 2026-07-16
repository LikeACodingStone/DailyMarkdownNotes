#### WIKI
// build aosp
```
https://ntswiki.nts.neusoft.local/wiki/Bosch_CCS2_Building_Bosch_AOSP
```
// A14
```
https://ntswiki.nts.neusoft.local/wiki/Bosch_CCS2_-_Building_Bosch_AOSP_for_Android_14
https://ntswiki.nts.neusoft.local/wiki/Bosch_CCS2_-_Migration_to_Android_14
```

### A12
```
repo sync -d -c --force-sync --no-tags --no-clone-bundle -j1

rm -fr vendor/google/gas .repo/projects/vendor/google/gas.git/ ; repo sync -d -c --force-sync --no-tags --no-clone-bundle -j1 vendor/google/gas

vendor/bosch/hardware/vhal_plugins_lcm
vendor/bosch/system/usb-hub-fw
vendor/bosch/system/usb_tools

rm -fr vendor/neusoft/hardware/interfaces/etcvics .repo/projects/vendor/neusoft/hardware/interfaces/etcvics.git/ ; repo sync -d -c --force-sync --no-tags --no-clone-bundle -j1  vendor/neusoft/hardware/interfaces/etcvics 

rm -fr vendor/neusoft/services/etcvics .repo/projects/vendor/neusoft/services/etcvics.git/ ; repo sync -d -c --force-sync --no-tags --no-clone-bundle -j1  vendor/neusoft/services/etcvics

rm -fr vendor/qcom/proprietary .repo/projects/vendor/qcom/proprietary.git/ ; repo sync -d -c --force-sync --no-tags --no-clone-bundle -j1  vendor/qcom/proprietary

repo forall -c 'git reset --hard HEAD && git clean -fd'

repo sync platform/proprietary -j1 --fail-fast --force-sync

//update current.txt
m com.neusoft.etcvicsmanager.stubs.source-update-current-api
```

###A14
```
repo init -u ssh://rbcm-gerrit.de.bosch.com:29418/projects/ccs2/manifests -b ccs2_a14_vf_int

repo sync -d -c --force-sync --no-tags --no-clone-bundle -j4

repo sync -d -c --force-sync --no-clone-bundle --tags -j4 && ./repo-lfs

repo forall -c "git reset --hard && git clean -xdf"



# 1. 进入清单目录，回退版本定义
cd .repo/manifests
git reset --hard HEAD^

# 2. 回到根目录，强制同步（让所有子仓库跟随清单回退）
cd ../..
repo sync -d -c --force-sync -j$(nproc)

# 3. 终极清理：删除所有不在 Git 记录中的残留文件
# (这是解决“追踪不到”问题的关键，-x 会连同被忽略的垃圾文件一起删掉)
repo forall -c "git clean -dfx"

# 4. 物理删除输出目录，确保没有缓存干扰
rm -rf out/

```


### DA3 compiling
```
DA3编译命令：

cd /home/android14/tmp/szaosp_rsync  
docker run --rm -it -v $(pwd):/home/gls1yh buildbot.nts.neusoft.local:5000/suzuki-da3-builder:20240612  
./ci build-all TARGET_PRODUCT=da3_jpn
```

## Bosch VPN
- VPN German
```
sudo openconnect --protocol=anyconnect --useragent=AnyConnect -u zhs2yh  rasvpn-ext-emea.bosch.com/rbextssl
```
- VPN Japan
```
sudo openconnect --protocol=anyconnect --useragent=AnyConnect -u zhs2yh  rasvpn-apac-sgp-ext.bosch.com/rbextssl
```


firefox 代理
10.4.103.143 8080


A14 Kernel 6.1

