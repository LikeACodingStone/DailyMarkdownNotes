# QT中多线程之间无法发送信号的问题
- QT里面线程之间传递参数会有一定的特殊性。因此必须加入第五个参数指定，才能够成功的让新线程传递信号给GUI线程。
- 按要求加入第五个参数
```
	connect(this,SIGNAL(sigShowImg(std::string)),this,SLOT(onShowImage(std::string)),Qt::DirectConnection);
```

- 如果传输的参数为自定义的类或第三方类，还需添加元数据注册，如
```
		#include <QtCore/QMetaType>
		qRegisterMetaType<Mat>("Mat");
```
***
# QObject::connect: Cannot queue arguments of type 'string' (Make sure 'string' is registed using qRegisterMetaType().)
- 解决方案：
- 可以再main中加入：
- qRegisterMetaType<string>("string"); 注册该类型
