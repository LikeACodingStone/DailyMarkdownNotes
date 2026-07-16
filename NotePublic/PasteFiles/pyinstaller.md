- install pyinstaller
```
pip3 install pyinstaller
```
- compile with icon
```
pyinstaller -F -w -i kent.ico  SyncTwoDiskFiles.py			//kent.ico 是程序图片，SyncTwoDiskFiles.py是主程序入口

```

- specify current dir and add config
```
pyinstaller --onefile --distpath . --add-data "config.ini;."  --add-data "config_modules.ini;." 
 MainForm.py
```
