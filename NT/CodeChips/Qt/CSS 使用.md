
- QSS 文件加载
```
void Widget::button_style()
{
QFile file(":/new/prefix1/button.qss"); //通过文件路径创建文件对象
file.open(QFile::ReadOnly); //文件打开方式
QString str = file.readAll(); //获取qss中全部字符
this->setStyleSheet(str); //设置样式表
}
```
- QSS 使用示例 涉及QPushbutton QLabel 
- https://github.com/CodingKilling/GitLab_Jimi/blob/main/E009/SharedComponents/source/HgtTemplateWidget/HFmTemplateJawsLoc.cpp
***
**QSS读取加载的模块封装示例**
- https://github.com/CodingKilling/GitLab_Jimi/blob/main/E015/E015DailyBasic/SharedComponents/src/QssFontFactory.h

