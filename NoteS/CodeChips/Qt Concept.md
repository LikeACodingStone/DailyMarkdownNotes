Qt下载网址:
https://download.qt.io/new_archive/qt/
https://download.qt.io/

## Concept
#### 控件类型
```
QLabel
QPushbutton
QTextEdit		//并非实时刷新
QTextCodec		//适配字体
QButtonGroup
QByteArray		//相当于是QChar的一个vector<>,占内存小,适用嵌入式,可以跟QString互相转换
QVariantHash	//基于QHash,无序
QVariantMap		//基于QMap,有序
QIcon			//可直接使用的内部ICON,参照PasteFiles
QFileDialog		//打开文件
QJson			//JSON库，qjson.lib, qjson.dll
QPainter 		//Qt画图，自定义任意控件
QMetaType		//qRegisterMetaType注册Qt自定义的信号槽
QVBoxLayout
QGridLayout
QStackedWidget		//进行多页面切换
QTreeWidget
QCoreApplication
QApplication
QSettings
QTreeWidgetItem
QWSServer
QDir			//文件管理
QStringList	
QPlainTextEdit
```
```
	// 鼠标事件
	QEvent::MouseButtonPress	
	QEvent::MouseButtonRelease	
	QEvent::MouseButtonDblClick	
	QEvent::MouseMove
	QEvent::Wheel
```

#### 基础功能
```
1. 设置图片，形状，背景透明
2. setModal 设置模态，让窗口始终靠前
```

#### 使用细节和注意
```
1. delete 删除Qt控件，顺序应该先删除子控件，然后再释放主控件.
2. QVBoxLayout 无法除边框线, 在后面套一层QFrame,
   然后再加QVBoxLayout , QFrame设置border为0，
   最好不跟其他控件重叠周边。
3. QTimer *timer = new QTimer;         // QTimer inherits QObject
	timer->inherits("QTimer");          // returns true
	timer->inherits("QObject");         // returns true
4. widget->dynamicPropertyNames()列出所有弱属性名称
5. widget->property("name")取出对应的弱属性的值
6. 
```

***

### Sleep 三种方式
- boost sleep
- QCoreApplication
- QTime

### Qt Tools
- QtCreator bin目录下找到uic.exe, 将 .ui文件转换为.h/.cpp文件
- QSS 文件加载，通过读取.qss文件，自动设置Qt的ui

  