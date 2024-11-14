
```
	void mousePressEvent(QMouseEvent *event);					// 同下
	void mouseMoveEvent(QMouseEvent *event)
	{
			if (event->buttons() == Qt::RightButton)		//判断是否鼠标右键
			{
			}
			else if (event->buttons() == Qt::LeftButton)		//判断是否鼠标左键
			{
			}
	}
	
	
```