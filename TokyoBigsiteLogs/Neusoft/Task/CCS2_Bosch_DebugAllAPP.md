### APP debug
adb shell am broadcast -a jp.co.nissan.hmi.home.action.SHOW_ALL_APPS

### Start A14
adb shell cmd DiagAdb Configuration set multimedia_config/audio/output_information:2