<div style="border: 3px solid #333; padding: 10px; border-radius: 8px;">

# <span style="color: red;">Aurix Checking</span>
## Checking If flash Aurix is necessary. Each version have relationship between Aurix and flashing binary files.
* * *

### For bosch built package. the relationship can be found on bosch Dashboards.

- [Bosch DailyBuild Page](https://ccs2-metrics.apac.bosch.com/d/UcrU38F4z/ccs2-nissan-sw-release-info-table?orgId=1)
    
- ### Example
    

![b33678f06ddc60f4462681d5dfcc4ced.png](b33678f06ddc60f4462681d5dfcc4ced.png)

- <span style="color: blue;">ccs2_qpr3_a12_int</span> is for Android12
    - ccs2_qpr3_a12_int_2025.49.4 &lt;=&gt; 25.0F2025.31
- <span style="color: blue;">ccs2_a14_vf_int</span> is for Android14
    - ccs2_a14_vf_int_2025.49.3 &lt;=&gt; 25.0F2025.41

* * *

### For engineering build package.

- need to confirm

* * *

### Checking current Aurix version and confirm if match or not

```
adb shell "vendor.bosch.swupdate_scc.FHProxy -i version | grep AUTOSAR"
```

</div><div style="border: 3px solid #333; padding: 10px; border-radius: 8px;">

## <span style="color: red;">Flash Aurix</span>

- [Bosch Aurix componets](https://rb-cmbinex-fe-p1.de.bosch.com/ui/repos/tree/General/basesoftware-repos/basesoftware/gen4/AURIX/pf_generic-autosar)
    
- ![5b2c9c073f1f2d3d15d6b34cf650cbc1.png](5b2c9c073f1f2d3d15d6b34cf650cbc1.png)
    
- ### For C1 target, we need to use cfg04
    
- ### For C2 target, we need to use cfg05
***    
### 1. Downloading FlashGui
    
### 2. Downloading FlashScripts_FlashGUI
    
### 3. Downloading .dnl file
- #### cfg04
	- ccs20_cfg04_board.dnl
	- ccs20_cfg04_board_DisableHsmOnly.dnl
	- ccs20_cfg04_board_withHSM.dnl
- #### cfg05
	- ccs20_cfg05_board.dnl
	- ccs20_cfg05_board_DisableHsmOnly.dnl
	- ccs20_cfg05_board_withHSM.dnl
### 4. Create floder tree, Copy files, Root folder can be anywhere
  - #### FlashGui, copy from downloading
  - #### FlashScripts_FlashGUI, copy from downloading
  - #### Output\vector\ccs20_cfg04_board\release\bin
	-  ccs20_cfg04_board.dnl
	-  ccs20_cfg04_board_DisableHsmOnly.dnl
	-  ccs20_cfg04_board_withHSM.dnl
![a7671f5fbb2ceb814ce8b74b13a41454.png](a7671f5fbb2ceb814ce8b74b13a41454.png)
### 5. Connect Board via USB
- ![fd79496fb03c4643ebdfa7b994980531.png](fd79496fb03c4643ebdfa7b994980531.png)
- ![3a59bdf048cc032dc2848e607572a7b1.png](3a59bdf048cc032dc2848e607572a7b1.png)
- ![a6834aac7bb865055b39357621e2d769.png](a6834aac7bb865055b39357621e2d769.png)

### 6. Open FlashGui/FlashGUI.exe
- #### Enter password "Halligalli"
- #### Settings->COM-Settings
	- Copy Port Content
		- "Quad-G3G-RS232-DebugAdapter C - FT7RGUOF"
	- Copy Baudrate
	  	- "1000000"
### 7. Enter FlashScripts_FlashGUI
- #### rename Example_User_Config.cmd -> User_Config.cmd
- #### Edit User_Config.cmd
	-  ccs20_cfg04_board(C1) or ccs20_cfg05_board(C2)
		- SET BOARD=ccs20_cfg04_board
		- **or**  SET BOARD=ccs20_cfg05_board
	- port copied from COM-Settings
		- SET COM_PORT_FTDI=Quad-G3G-RS232-DebugAdapter C - FT7RGUOF
	- Baudrate copied from COM-Settings
		- SET COM_PORT_BAUDRATE=1000000

	![d97c1615531e3cc9fadd428c154a4106.png](d97c1615531e3cc9fadd428c154a4106.png)
#### 8. Running bat via windows cmd inside FlashScripts_FlashGUI folder
  - `.\FlashGUI_VirginFlash.bat --cfg-path="./"`
  - #### waing for result
</div>


<div style="border: 3px solid #333; padding: 10px; border-radius: 8px;">

# <span style="color: red;">Flash SoC</span>
### <span style="color: red;"> Caution : switch debug board need to power off. </span>
### 1. Switch Debug Board Like this
- ![68b0ba761eca5e6f571a5d2d06b5f193.png](68b0ba761eca5e6f571a5d2d06b5f193.png)
### 2.Download xml  <span style="color: red;">Do not</span> select "ERASE ALL"  
##  <span style="color: red;"> use "rawprogram_ccs2.0_avi2-ccs20-C1.xml (for C1 target)  or rawprogram_ccs2.0_avi2-ccs20-C2.xml (for C2 target)" </span>
![7e76c9d795d318aced16aad8bd0d0b24.png](7e76c9d795d318aced16aad8bd0d0b24.png)

### 3. Change Debug board to ADB mode
- OPT2 ON only
- ![f41ab9ec881312457aa2a3b11e44e9e1.png](f41ab9ec881312457aa2a3b11e44e9e1.png)
### 4. PD configuration
- 7515752388 realted to the serial number
- Use the part number related to your devices,  for example 751575238802
	```
	adb root
	// 7515752388-02 rely on the device number
	adb push .\7515752388-02.json /data/local/tmp/pd.json
	adb shell boschconfig --write /data/local/tmp/pd.json 
	
	adb logcat -s -d BoschConfig 
	adb reboot
	```
### 5. Set serial number of device
- #### check number on the head unit, and add 0 prefix
	- 07515752388020000022 
![7601e9d4a62bccc21a3abd04e65211c0.png](7601e9d4a62bccc21a3abd04e65211c0.png)
- 
	```
	adb root
	adb shell
	cmd DiagAdb Configuration set ecu_serial_number_data_identifier/X/ecu_serial_number_data_identifier:"07515752388020000022"
	or
	cmd DiagAdb Configuration set ecu_serial_number_data_identifier/X/ecu_serial_number_data_identifier:"07515752388020000168"
	```
- #### <span style="color: red;"> Reboot Head Unit </span>
### 6. CD configuration
- #### For A14 use DRF version 4.0.4
	-  [EC_7515752850_01T_DR1_Nissan_CCS2_template_DRF4.0.4_V1.18_ALL_251105_Part Number Fixed.bat](EC_7515752850_01T_DR1_Nissan_CCS2_template_DRF4.0..bat)
- #### <span style="color: red;"> Reboot Head Unit </span>

### Static2 to Nomal
```
adb shell cmd DiagAdb setBootMode NORMAL 
adb shell sync 
adb reboot
```
</div>