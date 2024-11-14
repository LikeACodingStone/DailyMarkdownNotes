1. 设置窗口模态显示，即始终悬浮在最上层
- 可以对QDialog类，调用exec()函数代替show()显示
 ```
 	theAWSDebugConsole->setModal(true);       
 ```
 - 或者在show 之前调用setModal函数
 - 参考 [setModal](d:/GitLab_Release/Mullis/source/SharedComponents/HgtTemplateWidget/HMessageBox.cpp/)
 -  第79行  `msgBx.setModal(true);`