# qjson-0.8.1

- 添加qjson.lib
- 通常定义QString json
```
{
	"nodeId": "default",
	"acceleration": "default",
	"deceleration": "default",
	"subdivision": "default",
	"current": "default",
	"idleCurrent": "default",
	"maxStartAcce": "default",
	"momentStopAcce": "default",
	"s1": {
		"pyhsicalExists": "on",
		"changeNotice": "on",
		"edgeType": "default",
		"edgeAction": "default"
	},
	"s2": {
		"pyhsicalExists": "on",
		"changeNotice": "on",
		"edgeType": "dedfault",
		"edgeAction": "default"
	},
	"s3": {
		"pyhsicalExists": "off",
		"changeNotice": "on",
		"edgeType": "dedfault",
		"edgeAction": "default"
	}
}
```

- 解析如下
```
//读取
#include <string>
#include <QtCore/QByteArray>
#include <QtCore/QVariant>
#include <QtCore/QDebug>
#include <QtCore/QFile>
#include <QtCore/QList>
#include "qjson/parser.h"
using namespace std;
int main()
{

	QJson::Parser parser;
	bool ok;

	QFile file("../confige.json");
	file.open(QFile::ReadOnly); 
	QString str = file.readAll(); 
	QVariantMap result = parser.parse(str.toUtf8(), &ok).toMap();
	for (auto iter = result.begin(); iter != result.end(); iter++)
	{
		cout << "key *********	" <<iter.key().toStdString() << endl;
		if (iter.key().toStdString() == "s1")
		{
			QVariantMap varS1 = iter.value().toMap();
			cout << "s1		" << varS1["pyhsicalExists"].toString().toStdString() << endl;
		}
	}
}
```

- 读写
```
#include <iostream>
#include <string>
#include <signal.h>
#include <QtCore/QVariantHash>
#include "qjson/serializer.h"
#include "qjson/parser.h"
#include <QtCore/QByteArray>
#include <QtCore/QFile>
int main()
{
	Serializer serializer;
	bool ok;

	QVariantHash hashSub;
	hashSub[QLatin1String("one")] = 1;
	hashSub[QLatin1String("three")] = 3;
	hashSub[QLatin1String("seven")] = 7;
	
	QVariantHash hashMain;
	hashMain[QLatin1String("main")] = hashSub;
	hashMain[QLatin1String("mainInfo")] = "info";

	QByteArray byt("222");
	QByteArray json = serializer.serialize(hashMain, &ok);

	QString str(json);
	QFile file("../test.json");	
	file.open(QIODevice::WriteOnly);
	file.write(str.toStdString().c_str(), str.length());
	file.close();

	
	file.open(QFile::ReadOnly);
	QString strJson = file.readAll();
	QJson::Parser parser;
	bool parseOk;
	QVariantMap result = parser.parse(strJson.toUtf8(), &parseOk).toMap();
	for (auto itMotor = result.begin(); itMotor != result.end(); itMotor++)
	{
		if (itMotor.key() == "main")
		{
			QVariantMap resSub = itMotor.value().toMap();
			for (auto itSub = resSub.begin(); itSub != resSub.end(); itSub++)
			{
				cout << "itSub value " << itSub.value().toString().toStdString() << endl;
			}
		}
		else {
			cout << "itMotor value " << itMotor.value().toString().toStdString() << endl;
		}
	}
	while (1);
}
```




