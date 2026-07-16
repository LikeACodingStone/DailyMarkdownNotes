## d8.bash
```
#!/bin/bash

JAR_PATH="$1"
OUT_DIR=$(mktemp -d)

if [[ ! -f "$JAR_PATH" ]]; then
  echo "Error: File '$JAR_PATH' does not exist."
  exit 1
fi

# 运行 d8 编译
/home/neu/baosp/baosp_sync/out/soong/host/linux-x86/bin/d8 --output $OUT_DIR "$JAR_PATH"
if [[ $? -eq 0 ]]; then
  echo "d8 compilation succeeded."
else
  echo "d8 compilation failed."
fi

rm -rf "$OUT_DIR"

```
```
./d8.bash etcvics/service/java/na_vics.jar
```

***
### BoschPkg  NO BRANCH
```
repo status
/usr/bin/repo:681: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow()

... A new version of repo (2.54) is available.
... New version is available at: /home/neusoft/BaospA14/.repo/repo/repo
... The launcher is run from: /usr/bin/repo
!!! The launcher is not writable.  Please talk to your sysadmin or distro
!!! to get an update installed.

project vendor/bootable/bootloader/edk2/        (*** NO BRANCH ***)
 --     BoschPkg/



```


```

config_vehicleType

//ccs2_qssi_aasp_release_a14_v28.04.30.0_HMI missing



https://gemini.google.com/app/e26087347bb68ddd?hl=zh

### 某个路径报错太多 可以删掉整个文件夹
