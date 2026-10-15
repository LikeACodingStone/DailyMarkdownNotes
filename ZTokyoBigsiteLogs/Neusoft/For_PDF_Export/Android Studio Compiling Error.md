```
Execution failed for task ':nativelib:buildCMakeRelWithDebInfo[x86_64][etc20vicsstatic,na_vics]'.

> com.android.ide.common.process.ProcessException:
  ninja: Entering directory
  `/home/dpc/ccs2/ccs20/app/bosch/ccs20/nativelib/.cxx/RelWithDebInfo/4c1p6634/x86_64`

[1/104] Generating:
  ../include/com/neusoft/etcvics/types/CommonTypes.hpp
  src/com/neusoft/etcvics/types/CommonTypes.cpp
  ../include/com/neusoft/etcvics/types/ConfigurationInfos.hpp
  src/com/neusoft/etcvics/types/ConfigurationInfos.cpp
  ...
  ../include/com/neusoft/etcvics/types/WeatherInfos.hpp
  src/com/neusoft/etcvics/types/WeatherInfos.cpp

FAILED:
  app/na_vics/iface/mgr/include/com/neusoft/etcvics/types/CommonTypes.hpp
  app/na_vics/iface/mgr/fidl/src/com/neusoft/etcvics/types/CommonTypes.cpp
  ...
  app/na_vics/iface/mgr/include/com/neusoft/etcvics/types/WeatherInfos.hpp
  app/na_vics/iface/mgr/fidl/src/com/neusoft/etcvics/types/WeatherInfos.cpp

Command:
  cd /home/dpc/.../fidl && /usr/bin/java -Dfile.encoding=UTF-8 \
  -jar apifiddler-1.97.1.jar -q @ApiFiddler.iface_mgr_com_neusoft_etcvics.rsp

ERROR:
  /bin/sh: 1: /usr/bin/java: not found

--------------------------------------------------

[2/104]
cd /home/dpc/ccs2/ccs20/app/na_vics/src &&
cmake ... gitversion___9.cmake

-- Current Commit (HEAD): 5fd3007
-- Most recent tag: other/ccs20/bpoint/stabilization/...

[3/104]
cd .../etcvics/src/common &&
cmake ... gitversion___8.cmake

-- Current Commit: 5fd3007

[4/104]
cd .../na_common/src &&
cmake ... gitversion___7.cmake

-- Current Commit: b55ed89

...

ninja: build stopped: subcommand failed.

--------------------------------------------------

C++ build system [build] failed while executing:
  ninja -C
  /home/dpc/.../.cxx/RelWithDebInfo/.../x86_64
  etc20vicsstatic
  na_vics

* Try:
  Run with --stacktrace option
  Run with --info or --debug option
  Run with --scan
```

### Fix solution
- java already exist
```
sudo ln -s $(which java) /usr/bin/java
```