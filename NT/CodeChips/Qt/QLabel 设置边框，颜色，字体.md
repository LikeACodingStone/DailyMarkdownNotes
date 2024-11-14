
- QLabel 设置边框 。rgb背景颜色
```
lblStage->setStyleSheet("border:2px solid red;");
lblStage->setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}");
// lblStage->setStyleSheet("QLabel{border:1px solid gray;}"); //设置边框灰色
lblStage->setStyleSheet("background-color: rgb(203, 228, 169)");

QFont ftModel;
ftModel.setPointSize(12); //设置字体大小
QPalette paModel;
paModel.setColor(QPalette::WindowText, Qt::darkBlue); //设置颜色
lblStage->setFont(ftModel);
lblStage->setPalette(paModel);

lblStage->setStyleSheet("QLabel{border: 0px;}"); //去除QLabel 边框
```