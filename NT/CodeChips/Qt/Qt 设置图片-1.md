```
	m_lblPic = new QLabel();
   m_lblPic->setFixedSize(380, 320);
   QPixmap *pixmap = new QPixmap("../images/zarm.png");
   m_lblPic->setPixmap(*pixmap);
   m_lblPic->setScaledContents(true);
```