
- QVBoxLayout 无法除边框线
	- 在后面套一层QFrame, 然后再加QVBoxLayout , QFrame设置border为0，最好不跟其他控件重叠周边。
	