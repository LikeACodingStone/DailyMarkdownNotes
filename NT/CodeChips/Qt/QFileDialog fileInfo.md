
- Qt 打开某个路径下文件
```
QFileDialog.getOpenFileName()    #获取一个打开文件的文件名
QFileDialog.getOpenFileNames()   #获取多个打开文件的文件名
QFileDialog.getOpenFileUrl()     #获取一个打开文件的统一资源定位符
QFileDialog.getOpenFileUrls()    #获取多个打开文件的统一资源定位符
QFileDialog.getSaveFileName()    #获取保存的文件名
QFileDialog.getSaveFileUrl()     #获取保存的url

dir_path=QFileDialog::getExistingDirectory(self,"choose directory","C:\Users\Administrator\Desktop") 	//选择路径

```

```
m_loadFile = QFileDialog::getOpenFileName(this, QObject::tr("open file"), "./",   QObject::tr("xml(*.xml);;Allfile(*.*)"));
QFileInfo fileInfo = QFileInfo(m_loadFile);		//打开文件信息
QString fileName = fileInfo.fileName(); 		//打开文件名字
QString fileSuffix = fileInfo.suffix();			//文件名后缀
QString filePath = fileInfo.absolutePath();		//文件绝对路径
QString completeBaseName = fileInfo.completeBaseName();		// 返回删除最短扩展名的文件名(file.tar.gz- > file.tar)
QString baseName = fileInfo.baseName();						//	返回删除了最长扩展名的文件名(file.tar.gz- > file)
```