当发生一下情况时会产生绘制事件并调用paintEvent()函数:
1.在窗口部件第一次显示时，系统会自动产生一个绘图事件，从而强制绘制这个窗口部件。
2.当重新调整窗口部件的大小时，系统也会产生一个绘制事件。
3.当窗口部件被其他窗口部件遮挡，然后又再次显示出来的时候，就会对那些隐藏的区域产生一个绘制事件。
同时可以调用QWidget::update()或者QWidget::repaint()来强制产生一个绘制事件。二者的区别是:
repaint()函数会强制产生一个即时的重绘事件,而update()函数只是在Qt下一次处理事件时才调用一次绘制事件。
如果多次调用update(),Qt会把连续多次的绘制事件压缩成一个单一的绘制事件，这样可避免闪烁现象。
***
```
	painter.setBrush(Qt::black);			//设置画刷颜色
	painter.drawLine(start, end);			//画直线
	painter.drawRect(start.x(), start.y(), end.x() - start.x(), end.y() - start.y());		//画矩形
	
	
	painter.setBackground(Qt::gray);			//设置擦除后的背景颜色
	painter.eraseRect(start.x(), start.y(), end.x() - start.x(), end.y() - start.y());		//设置橡皮擦范围

```
***
# 自定义图形控件参考
- 代码地址 https://github.com/CodingKilling/GitLab_Jimi/tree/main/E015/E015DailyBasic/SharedComponents/src
- paintAroundcircle
- ![d604b00a868c56ea7cda5bee7a31b551.png](../../../../../_resources/d604b00a868c56ea7cda5bee7a31b551.png)
- https://github.com/CodingKilling/GitLab_Jimi/tree/main/E015/E015DailyBasic/SharedComponents/src/paintAroundcircle
***
- paintBattery
- ![f27d1f93576546ef769d0c17ef436e98.png](../../../../../_resources/f27d1f93576546ef769d0c17ef436e98.png)
***
- paintButtonBoard
- ![283459056cf4999396d593663faa6b6b.png](../../../../../_resources/283459056cf4999396d593663faa6b6b.png)
***
- paintChart
- ![d5648fe9b3815614eb70b2bf9de44196.png](../../../../../_resources/d5648fe9b3815614eb70b2bf9de44196.png)
***
- paintCoolBar
- ![4c52283a94896e5e2204863967533697.png](../../../../../_resources/4c52283a94896e5e2204863967533697.png)
***
- paintFlashList
- ![047ca8599c054f5364cd9a5647d293d8.png](../../../../../_resources/047ca8599c054f5364cd9a5647d293d8.png)
***
- paintGuage
- ![3ba0a1deaa378a4e6ddb9906748648bb.png](../../../../../_resources/3ba0a1deaa378a4e6ddb9906748648bb.png)
- ![fae5c13da2cba3b62e5f179f65fe4066.png](../../../../../_resources/fae5c13da2cba3b62e5f179f65fe4066.png)
- ![a7616c349bf2f8f629b62176fdda0729.png](../../../../../_resources/a7616c349bf2f8f629b62176fdda0729.png)
- ![7acdc088eaca0f3630c236012d569563.png](../../../../../_resources/7acdc088eaca0f3630c236012d569563.png)
- ![75edb757cc8e03dfc178fdd5706fe113.png](../../../../../_resources/75edb757cc8e03dfc178fdd5706fe113.png)
- ![8e8beb28734419619b6dcbf6b59766ce.png](../../../../../_resources/8e8beb28734419619b6dcbf6b59766ce.png)
- ![15b671fbc4d3192718a939c21bf929d6.png](../../../../../_resources/15b671fbc4d3192718a939c21bf929d6.png)
***
- paintInDicator
- ![a8195c9d34b7771e47577613eb2aa565.png](../../../../../_resources/a8195c9d34b7771e47577613eb2aa565.png)
***
- paintProcessBar
- ![676420a5880a7e68bfd54a90a6fa1bc9.png](../../../../../_resources/676420a5880a7e68bfd54a90a6fa1bc9.png)
***
- paintSliderButton
- ![c497fb9464f3f1c5a559008dd6bd90bc.png](../../../../../_resources/c497fb9464f3f1c5a559008dd6bd90bc.png)
***
- paintSwitchButton
- ![dd9a2bdca1513912f0a51949129e2089.png](../../../../../_resources/dd9a2bdca1513912f0a51949129e2089.png)
***
- paintVolume
- ![44654227f81a910ff6507d5f77cb5167.png](../../../../../_resources/44654227f81a910ff6507d5f77cb5167.png)
***
- paintWave
- ![54c622c4cc2bb82ccee2b7713707aa1c.png](../../../../../_resources/54c622c4cc2bb82ccee2b7713707aa1c.png)
- ![be7b495bc7fd0142c51392f6a064bf64.png](../../../../../_resources/be7b495bc7fd0142c51392f6a064bf64.png)
- ![8e1306ad88f0a18d511a7df2b53fa329.png](../../../../../_resources/8e1306ad88f0a18d511a7df2b53fa329.png)