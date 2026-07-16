### bosch version info
```
~/baosp/baosp_sync/out/target$ cat product/aivi2_b/vendor/build.prop | grep version
```
### update current.txt
```
m com.neusoft.etcvicsmanager.stubs.source-update-current-api
```
### check bosch release version
```
adb shell "vendor.bosch.swupdate_scc.FHProxy -i version | grep AUTOSAR"
```
### etc effetive set
```
adb shell date "051510512022"
```
### debug command
```
adb shell "service call vendor.neusoft.service.etcvics 21 i32 0 s16 'InterruptTypeDebug 14'"
```


### Net Connect ADB
```
adb connect 192.168.7.1
```
*******************

## Flash Comand List
```
adb root
adb push .\7515752388-02.json /data/local/tmp/pd.json
adb push .\7515752388-02.json /data/local/tmp/pd.json
adb push .\7515752683-03.json /data/local/tmp/pd.json
adb push .\7515752683-05.json /data/local/tmp/pd.json

adb root & adb shell boschconfig --write /data/local/tmp/pd.json && adb logcat -s -d BoschConfig && adb reboot

adb root & adb shell cmd DiagAdb setBootMode NORMAL && adb shell sync && adb reboot

adb root & adb shell cmd DiagAdb Routine start 02A8
adb shell "setprop bosch.usb.adb true"

```
***
```
adb shell cmd DiagAdb Configuration set display_config/display/touch_and_screen_configuration:9  && adb shell cmd DiagAdb Configuration set multimedia_config/audio/output_information:1 && adb shell cmd DiagAdb Configuration set rvc_part2_config/rvc/nissancamerabuiltinpresent:0 && adb shell cmd DiagAdb Configuration set rvc_config/rvc_feature/rvcpresent:0 && adb shell cmd DiagAdb Configuration set hmi_config/adas/avm_d:0 && adb shell cmd DiagAdb Configuration set camera_nissan_config/rvc/avm_camsys_camcon:4 && adb shell cmd DiagAdb Configuration set camera_nissan_config/rvc/avm_avm_video_connection_type:1 && adb shell cmd DiagAdb Configuration set hmi_config/adas/apa:4 && adb shell cmd DiagAdb Configuration set camera_nissan_config/rvc/hmi_adas_fap:2 && adb shell cmd DiagAdb Configuration set camera_nissan_config/rvc/avm_setting_menu:3
```
