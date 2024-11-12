- 查找当前界面weiget 并删除
```
 QLayoutItem *item = m_hblControlModel->itemAt(1);
    if (item != NULL)
    {
        QWidget *wgt = qobject_cast<QWidget*>(item->widget());
        if (wgt != NULL) {
            m_hblControlModel->removeWidget(wgt);
            delete wgt;
            wgt = NULL;
        }
    }
```