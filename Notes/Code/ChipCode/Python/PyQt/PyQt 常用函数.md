- 
```
	#QtWidgets.QFileDialog 打开路径
 	g_fileNameA = QtWidgets.QFileDialog.getExistingDirectory()			//打开路径获取名称
	 keyPath = QtWidgets.QFileDialog.getOpenFileName(None, 
	 		"选择文件",  "../", "All Files (*);;Text Files (*.key)")[0]		//获取打开的文件名
 	ui.edtFileA.setAlignment(Qt.AlignCenter)							//设置对齐
```
- 

```
	#QMessageBox 用法
	msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText("ensure dir is correct")
    msgBox.setWindowTitle("sync both differ files")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Yes | QMessageBox.No)

    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
			pass
```
- 
```
	#QPlainTextEdit 
	
	ui.pdtInfo.document().setMaximumBlockCount(100)		//设置最大行数
	ui.pdtInfo.appendPlainText("back")					//末端加入
	ui.pdtInfo.insertPlainText("head")					//前端加入
```
- 
```
	# QTextBrowser 实时刷新的解决方法
	my_cursor = self.textBrowser.textCursor()
	self.textBrowser.moveCursor(my_cursor.End)
	# sleep(0.05)  # 0:00:01.156
	QtWidgets.QApplication.processEvents(QtCore.QEventLoop.AllEvents)

```