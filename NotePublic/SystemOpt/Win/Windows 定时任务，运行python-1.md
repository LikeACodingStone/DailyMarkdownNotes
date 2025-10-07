
# 实现Windows下设置定时任务来运行python脚本
 
1. 自己用python写了一个签到脚本
经过测试已经可以成功打卡，于是研究了一下windows定时运行程序

2. 创建定时任务
2.1 打开“控制面板 ”C>“系统和安全”C>“管理工具”C>“计划任务”
![73e673c742d92987a435632687743f3a.png](../../../_resources/73e673c742d92987a435632687743f3a-1.png)

在这里插入图片描述

2.2 打开“计划任务”，如图，点击“创建基本任务”
![6fbb58fb771df8dbaa581cce7b130f97.png](../../../_resources/6fbb58fb771df8dbaa581cce7b130f97-1.png)

2.3 给定时任务命名，点击下一步
![b806e48f6bbe1ddaedc4b9ec66449c94.png](../../../_resources/b806e48f6bbe1ddaedc4b9ec66449c94-1.png)

2.4 选择脚本执行的时间，以每天执行为例，如图，点击下一步
![ac0ca713707cc409cfd154aa148f2c78.png](../../../_resources/ac0ca713707cc409cfd154aa148f2c78-1.png)

2.5 选择具体的每天执行时间
如从2021年8月24日起，后面每天早上8点执行定时任务，如图，点击下一步
![317f9b2331fe8f19b5843d07056bd793.png](../../../_resources/317f9b2331fe8f19b5843d07056bd793-1.png)

2.6 以执行程序为例，选择启动程序
点击下一步
![95d2ca0d09da7f9a049dc12c51e3be12.png](../../../_resources/95d2ca0d09da7f9a049dc12c51e3be12-1.png)

2.7 选择启动程序
填写参数如图：
![b44afeff8119fbb0bf3ce5797c538ba8.png](../../../_resources/b44afeff8119fbb0bf3ce5797c538ba8-1.png)

表示用位置：C:\ProgramData\Anaconda3\python.exe的解释器执行 E:\main.py脚本文件。

2.8 点击完成即可生成定时任务
![b209d1ba1cd8fd72b2de1afaccbb5c15.png](../../../_resources/b209d1ba1cd8fd72b2de1afaccbb5c15-1.png)

***

#  查看已经创建的任务
- 控制面板 - 系统和安全 - 任务计划程序库
