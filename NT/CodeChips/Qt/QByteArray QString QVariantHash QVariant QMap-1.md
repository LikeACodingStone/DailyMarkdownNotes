
# QByteArray  
- 相当于是QChar的一个vector<> ，占内存小，适用嵌入式，可以跟QString互相转换。
```
#include <QtCore/QByteArray>		
QByteArray byt("222");
QString str(byt);

```


# QVariantHash 
- 相比QMap，key是随机存储空间
```
#include <QtCore/QVariantHash>

QVariantHash hashSub;
hashSub[QLatin1String("one")] = 1;
hashSub[QLatin1String("three")] = 3;
hashSub[QLatin1String("seven")] = 7;

QVariantHash hashMain;
hashMain[QLatin1String("main")] = hashSub;
```