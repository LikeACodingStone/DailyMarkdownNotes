

```
	//数值过大，fill初始化导致内存崩溃
	vector <vector<int>> VX(339205);
	vector<int> VY(88857);
	fill(VY.begin(), VY.end(), 1);
	fill(VX.begin(), VX.end(), VY);

	//for循环初始化，数值过大，程序不响应
	vector <vector<int>> VX;
	vector<int> VY;
	for (int i = 0; i < 339205; i++)
	{
		VY.clear();
		for (int j = 0; j < 88857; j++)
		{
			VY.push_back(1);
		}
		VX.push_back(yVec);
	}
	

	//用QVector 代替vector，然后用fill填充. 实现二维QVector初始化
	QVector <QVector<int>> VX(339205);
	QVector<int> VY(88857);
	fill(VY.begin(), VY.end(), 1);
	fill(VX.begin(), VX.end(), VY);
```