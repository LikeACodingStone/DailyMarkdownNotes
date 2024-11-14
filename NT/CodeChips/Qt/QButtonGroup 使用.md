- 头文件添加
```
#include <QtCore/QMap>

public solots:
 	void slot_OnButtonClicked(int id);

private:
	QMap<int, char*> m_mapBtnInfo;
	QMap<int, QPushButton *> m_mapBtnGrp;
	QButtonGroup *m_btnGroup;
	void initBtnGroups();
	void initBtnListInfo();
```
- 源文件添加
```
enum APS_DEBUG_GRP_BTN
{
    START,
    STOP,
    PAUSE,
    RESUME,
};


void initBtnListInfo()
{
    m_mapBtnInfo[START]         = "开始";
    m_mapBtnInfo[STOP]          = "停止";
    m_mapBtnInfo[PAUSE]         = "暂停";
    m_mapBtnInfo[RESUME]        = "恢复";
}

void initBtnGroups()
{
    this->initBtnListInfo();
    m_btnGroup = new QButtonGroup();
    for (auto iter : m_mapBtnInfo.toStdMap())
    {
        QPushButton *btnInit = new QPushButton(QObject::tr(iter.second));
        btnInit->setStyleSheet(BTN_BASE_QSS);
        btnInit->setFixedSize(BTN_WIDTH, BTN_HEIGHT);
        m_btnGroup->addButton(btnInit, iter.first);
        m_mapBtnGrp[iter.first] = btnInit;
    }
    connect(m_btnGroup, SIGNAL(buttonClicked(int)), SLOT(slot_OnButtonClicked(int)));
}
//使用方法
this->initBtnGroups();
m_layoutButton = new QGridLayout();
m_layoutButton->addWidget(m_mapBtnGrp[START], 1, 0);
m_layoutButton->addWidget(m_mapBtnGrp[STOP], 1, 1);
m_layoutButton->addWidget(m_mapBtnGrp[PAUSE], 1, 2);
m_layoutButton->addWidget(m_mapBtnGrp[RESUME], 1, 3);
```

***
# QButtonGroup 槽函数内获取它的QPushbutton方法
```
void HGTObsAutoSearchManage::slot_btnGrpWorkBenchClicked(int btnId)
{
	QPushButton *cutBtn = qobject_cast<QPushButton*>(m_btnGroupWorkBench->buttons().at(btnId));
}
```