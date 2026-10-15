source build/envsetup.sh
lunch 
lunch qssi_aivi2_b-userdebug
mmm vendor/neusoft/services/etcvics


/home/dpc/BaospA14K6/vendor/device/qcom/qssi_au
/home/dpc/BaospA14K6/vendor/device/qcom/msmnile_au_s_u
/home/dpc/BaospA14K6/vendor/device/qcom/msmnile_au

dpc@dpc:~/BaospA14K6/vendor/device/qcom/qssi_au$ git diff
diff --git a/BoardConfig.mk b/BoardConfig.mk
index f60ebe2..4e43668 100644
--- a/BoardConfig.mk
+++ b/BoardConfig.mk
@@ -158,7 +158,7 @@ BOARD_SUPER_PARTITION_SIZE := 5318967296
 endif
 BOARD_SUPER_PARTITION_GROUPS := qti_dynamic_partitions
 BOARD_QTI_DYNAMIC_PARTITIONS_PARTITION_LIST := system system_ext product
-BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 5314772992
+BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 6442450944
 BOARD_EXT4_SHARE_DUP_BLOCKS := true
 ifeq ($(ENABLE_AB), true)
 AB_OTA_PARTITIONS ?= system system_ext product


dpc@dpc:~/BaospA14K6/vendor/device/qcom/msmnile_au_s_u$ git diff
diff --git a/BoardConfig.mk b/BoardConfig.mk
index 5252858..5f0d45d 100644
--- a/BoardConfig.mk
+++ b/BoardConfig.mk
@@ -67,7 +67,7 @@ else
   BOARD_SUPER_PARTITION_SIZE := 5318967296
 endif
 BOARD_SUPER_PARTITION_GROUPS := qti_dynamic_partitions
-BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 5314772992
+BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 6438256640
 ifeq ($(TARGET_SINGLE_TREE), true)
   BOARD_QTI_DYNAMIC_PARTITIONS_PARTITION_LIST := vendor vendor_dlkm system_dlkm system system_ext product
 else
dpc@dpc:~/


dpc@dpc:~/BaospA14K6/vendor/device/qcom/msmnile_au$ git diff
diff --git a/BoardConfig.mk b/BoardConfig.mk
index 8e0c6a7..9193de5 100644
--- a/BoardConfig.mk
+++ b/BoardConfig.mk
@@ -50,7 +50,7 @@ else
   BOARD_SUPER_PARTITION_SIZE := 5318967296
 endif
 BOARD_SUPER_PARTITION_GROUPS := qti_dynamic_partitions
-BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 5314772992
+BOARD_QTI_DYNAMIC_PARTITIONS_SIZE := 6438256640
 ifeq ($(TARGET_SINGLE_TREE), true)
   BOARD_QTI_DYNAMIC_PARTITIONS_PARTITION_LIST := vendor vendor_dlkm system_dlkm system system_ext product
 else





super: 
super: 2026-07-17 07:36:50 - check_target_files_vintf.py - INFO    : stderr: 
super: 2026-07-17 07:36:50 - ota_from_target_files.py - WARNING : Builds doesn't support zucchini, or source/target don't have compatible zucchini versions. Disabling zucchini.
super: 2026-07-17 07:36:50 - ota_from_target_files.py - WARNING : Source build doesn't support lz4diff, or source/target don't have compatible lz4diff versions. Disabling lz4diff.
super: 2026-07-17 07:37:02 - common.py - INFO    :   Running: "/home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/delta_generator --out_file /home/dpc/BaospA14K6/vendor/tmp/payload-tq9lstqy.bin --partition_names boot:dtbo:odm:product:system:system_dlkm:system_ext:vbmeta:vbmeta_system:vendor:vendor_boot:vendor_dlkm --new_partitions /home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/boot.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/dtbo.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/odm.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/product.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/system.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/system_dlkm.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/system_ext.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vbmeta.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vbmeta_system.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vendor.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vendor_boot.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vendor_dlkm.img --new_mapfiles ::::::::::: --dynamic_partition_info_file /home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/META/dynamic_partitions_info.txt --major_version 2 --security_patch_level 2025-07-05 --enable_zucchini=false --enable_lz4diff=false --max_timestamp 1784266146 --partition_timestamps boot:1784257977,odm:1784257977,product:1784254173,system:1784266146,system_dlkm:1784273379,system_ext:1784254173,vendor:1784257977,vendor_dlkm:1784257977"
super: [0717/073702.671926:ERROR:payload_generation_config.cc(245)] Sum of sizes in qti_dynamic_partitions_partition_list is 5332328448, which is greater than qti_dynamic_partitions_size (5314772992)
super: [0717/073702.671977:FATAL:generate_delta_main.cc(706)] Check failed: payload_config.target.ValidateDynamicPartitionMetadata(). 
super: /home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/../lib64/libchrome.so(base::debug::StackTrace::StackTrace(unsigned long)+0x16) [0x780449eb3936]
super: /home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/../lib64/libchrome.so(logging::LogMessage::~LogMessage()+0x93) [0x780449e49ab3]
super: /home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/delta_generator(+0x10ae08) [0x650583571e08]
super: /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xf3) [0x78044991d083]
super: /home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/delta_generator(+0x108a29) [0x65058356fa29]
super: 
super: 2026-07-17 07:37:03 - common.py - INFO    : 
super: Traceback (most recent call last):
super:   File "internal/stdlib/runpy.py", line 196, in _run_module_as_main
super:   File "internal/stdlib/runpy.py", line 86, in _run_code
super:   File "/home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/ota_from_target_files/__main__.py", line 12, in <module>
super:   File "internal/stdlib/runpy.py", line 196, in _run_module_as_main
super:   File "internal/stdlib/runpy.py", line 86, in _run_code
super:   File "ota_from_target_files.py", line 1455, in <module>
super:   File "ota_from_target_files.py", line 1426, in main
super:   File "ota_from_target_files.py", line 1047, in GenerateAbOtaPackage
super:   File "ota_utils.py", line 865, in Generate
super:   File "ota_utils.py", line 802, in _Run
super:   File "common.py", line 316, in RunAndCheckOutput
super: common.ExternalError: Failed to run command '['delta_generator', '--out_file', '/home/dpc/BaospA14K6/vendor/tmp/payload-tq9lstqy.bin', '--partition_names', 'boot:dtbo:odm:product:system:system_dlkm:system_ext:vbmeta:vbmeta_system:vendor:vendor_boot:vendor_dlkm', '--new_partitions', '/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/boot.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/dtbo.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/odm.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/product.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/system.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/system_dlkm.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/system_ext.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vbmeta.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vbmeta_system.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vendor.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vendor_boot.img:/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/IMAGES/vendor_dlkm.img', '--new_mapfiles', ':::::::::::', '--dynamic_partition_info_file', '/home/dpc/BaospA14K6/vendor/tmp/target_filesl565ooty/META/dynamic_partitions_info.txt', '--major_version', '2', '--security_patch_level', '2025-07-05', '--enable_zucchini=false', '--enable_lz4diff=false', '--max_timestamp', '1784266146', '--partition_timestamps', 'boot:1784257977,odm:1784257977,product:1784254173,system:1784266146,system_dlkm:1784273379,system_ext:1784254173,vendor:1784257977,vendor_dlkm:1784257977']' (exit code -6):
super: 
super: 
super: real	0m15.881s
super: user	0m12.581s
super: sys	0m2.020s
super: ============================================
super: [build.sh]: FAILED: /home/dpc/BaospA14K6/vendor/tmp/tmp.CXfeYgF1z2/bin/ota_from_target_files                           --verbose --enable_vabc_xor=false out/dist/merged-qssi_au_aivi2_b-target_files.zip                           out/dist/merged-qssi_au_aivi2_b-ota.zip
super: ============================================
super: 2026-07-17 07:37:03 - build_image_standalone.py - ERROR   : FAILED:['bash', 'vendor/qcom/opensource/core-utils/build/build.sh', 'dist', '-j16', '--merge_only', '--rebuild_sepolicy_with_vendor_otatools=out/dist/vendor/otatools.zip']
super: file not found: /home/dpc/BaospA14K6/vendor/single_tree_support.txt
dpc@7dcddb9543b9:~/BaospA14K6$ 



https://rbcm-gerrit.de.bosch.com/c/projects/ccs2/vendor/neusoft/services/etcvics/+/1239011
https://rbcm-gerrit.de.bosch.com/c/projects/ccs2/vendor/neusoft/services/etcvics/+/1239016


The build failed during OTA payload generation because the combined size of the logical partitions (5,332,328,448 bytes) exceeded the maximum limit defined by `qti_dynamic_partitions_size` (5,314,772,992 bytes) by approximately 16.7 MB. This dynamic partition boundary acts as a safety threshold to prevent system images from encroaching on critical physical partitions like userdata. To resolve this, developers must either increase the partition group size limit in `BoardConfig.mk` (if physical space permits), clean up unnecessary prebuilts and assets from the system/vendor images, or enable automatic partition resizing to optimize partition storage utilization.

Recording to this function is not bellowing to neusoft side, the investigation is just some hits. Please feel free to fix it by any method you prefer.

Best Regards
Fred



```
Build file '/home/dpc/ccs2/ccs20/app/bosch/ccs20/buildSrc/build.gradle.kts' line: 3

Plugin [id: 'org.gradle.kotlin.kotlin-dsl', version: '4.0.14'] was not found in any of the following sources:

- Gradle Core Plugins (plugin is not in 'org.gradle' namespace)
- Plugin Repositories (could not resolve plugin artifact 'org.gradle.kotlin.kotlin-dsl:org.gradle.kotlin.kotlin-dsl.gradle.plugin:4.0.14')
  Searched in the following repositories:
    MavenLocal(file:/home/dpc/.m2/repository)
    maven(http://nexus.nts.neusoft.local/content/groups/public)

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.
> Get more help at https://help.gradle.org.
Fix with AI

```