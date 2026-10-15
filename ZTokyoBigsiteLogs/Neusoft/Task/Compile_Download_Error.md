

#### Android 12 compiling error
```
https://chatgpt.com/share/68b6a6f6-8cc0-800c-9df7-8d9e2079b54a
m clean
```
#### Android14 compiling error
```
rm -rf qssi/out/soong/.intermediates/external/boringssl/libcrypto
rm -rf qssi/out/soong/.intermediates/*header-abi*
export ANDROID_BUILD_TOP=/home/neusoft/Android14/baosp
cd qssi/

export TARGET_NO_ABI_CHECK=true
qssi/development/vndk/tools/header-checker/utils/create_reference_dumps.py -l libcrypto
export SKIP_ABI_CHECKS=true


cd vendor
source  build/envsetup.sh
lunch aivi2_b-userdebug
m clean
m android.hardware.power-V3-ndk_platform
Then continue to build
```

```
docker run --rm -it -v $(pwd):$(pwd) -w $(pwd) ccs2-builder:20

docker run --rm -it --privileged -v $(pwd):$(pwd) -w $(pwd) -e TARGET_VENDOR_PRODUCT=aivi2_b -e TARGET_QSSI_PRODUCT=qssi_aivi2_b  -e TARGET_BUILD_VARIANT=userdebug ccs2-builder:20_a14

docker run --rm -it -v $(pwd):$(pwd) -w $(pwd) ccs2-builder:20_a14

docker run --rm -it --privileged \
-v $(pwd):$(pwd) \
-w $(pwd) \
-e TARGET_VENDOR_PRODUCT=aivi2_b \
-e TARGET_QSSI_PRODUCT=qssi_aivi2_b  \
-e TARGET_BUILD_VARIANT=userdebug \
ccs2-builder:20_a14


```