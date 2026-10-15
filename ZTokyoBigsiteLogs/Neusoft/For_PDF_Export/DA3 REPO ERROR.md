## error case 1
```
fatal: couldn't find remote ref refs/heads/rb_cbsw_lcm_int
 
components/cbsw/lcm/android/vhal_plugins:
fatal: couldn't find remote ref refs/heads/rb_cbsw_lcm_int
components/cbsw/lcm/android/vhal_plugins: sleeping 4.0 seconds before retrying
fatal: couldn't find remote ref refs/heads/rb_cbsw_lcm_int
fatal: couldn't find remote ref refs/heads/basesw_conf_int
 
platform/vendor/bosch/system/usb-hub-fw:
fatal: couldn't find remote ref refs/heads/basesw_conf_int
platform/vendor/bosch/system/usb-hub-fw: sleeping 4.0 seconds before retrying
fatal: couldn't find remote ref refs/heads/basesw_conf_int
fatal: couldn't find remote ref refs/heads/rb_cbsw_usb_int
 
components/cbsw/comm/usb_tools:
fatal: couldn't find remote ref refs/heads/rb_cbsw_usb_int
components/cbsw/comm/usb_tools: sleeping 4.0 seconds before retrying
fatal: couldn't find remote ref refs/heads/rb_cbsw_usb_int
````
### SOLUTION
#### original solution
```
mkdir -p /home/android14/tmp/szaosp_rsync/.repo/local_manifests

cp /home/android14/tmp/szaosp_rsync/.repo/manifests/submanifests/sp.xml /home/android14/tmp/szaosp_rsync/.repo/local_manifests/override_sp.xml
 
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
 
  <!-- VHAL LCM plugins -->
<remove-project name="components/cbsw/lcm/android/vhal_plugins" />
<project groups="boschoss,shareable" remote="origin" name="components/cbsw/lcm/android/vhal_plugins" path="vendor/bosch/hardware/vhal_plugins_lcm" revision="suzuki_da3_rb_cbsw_lcm_int_2025.26.2_stabi" />
 
  <!-- usbhub-->
<remove-project name="platform/vendor/bosch/system/usb-hub-fw" />
<project groups="boschoss,shareable" name="platform/vendor/bosch/system/usb-hub-fw" path="vendor/bosch/system/usb-hub-fw" revision="suzuki_da3_basesw_conf_int_2025.26.2_stabi" />
 
  <!-- usb-tools -->
<remove-project name="components/cbsw/comm/usb_tools" />
<project groups="boschoss,non-shareable" remote="origin" name="components/cbsw/comm/usb_tools" path="vendor/bosch/system/usb_tools" revision="suzuki_da3_rb_cbsw_usb_int_2025.26.2_stabi"/>
 
</manifest>
 
```
#### auto fix shell
```
#!/bin/bash

# 取得當前執行目錄
BASE_DIR="$(pwd)"

# 定義目標目錄
LOCAL_MANIFEST_DIR="$BASE_DIR/.repo/local_manifests"
MANIFEST_SRC="$BASE_DIR/.repo/manifests/submanifests/sp.xml"
MANIFEST_DST="$LOCAL_MANIFEST_DIR/override_sp.xml"

echo "Current path: $BASE_DIR"

# 建立目錄
mkdir -p "$LOCAL_MANIFEST_DIR"

# 複製原始 sp.xml（如果存在）
if [ -f "$MANIFEST_SRC" ]; then
    cp "$MANIFEST_SRC" "$MANIFEST_DST"
    echo "Copied base manifest"
else
    echo "Warning: $MANIFEST_SRC not found, will create new override file"
fi

# 覆蓋寫入 override_sp.xml
cat > "$MANIFEST_DST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<manifest>

    <!-- VHAL LCM plugins -->
    <remove-project name="components/cbsw/lcm/android/vhal_plugins" />
    <project groups="boschoss,shareable"
             remote="origin"
             name="components/cbsw/lcm/android/vhal_plugins"
             path="vendor/bosch/hardware/vhal_plugins_lcm"
             revision="suzuki_da3_rb_cbsw_lcm_int_2025.26.2_stabi" />

    <!-- usbhub -->
    <remove-project name="platform/vendor/bosch/system/usb-hub-fw" />
    <project groups="boschoss,shareable"
             name="platform/vendor/bosch/system/usb-hub-fw"
             path="vendor/bosch/system/usb-hub-fw"
             revision="suzuki_da3_basesw_conf_int_2025.26.2_stabi" />

    <!-- usb-tools -->
    <remove-project name="components/cbsw/comm/usb_tools" />
    <project groups="boschoss,non-shareable"
             remote="origin"
             name="components/cbsw/comm/usb_tools"
             path="vendor/bosch/system/usb_tools"
             revision="suzuki_da3_rb_cbsw_usb_int_2025.26.2_stabi"/>

</manifest>
EOF

echo "override_sp.xml generated at: $MANIFEST_DST"
```
****

## error case 2
#### init error
```
  repo init -u ssh://rbcm-gerrit-ext.de.bosch.com:29418/projects/suzuki-da3/manifests -b suzuki_da3_qpr1_a12_int
```
#### replace by the fellowing command
````
repo init -u ssh://shd5yh@rbcm-gerrit.de.bosch.com:29418/projects/suzuki-da3/manifests -b suzuki_da3_qpr1_a12_int
````