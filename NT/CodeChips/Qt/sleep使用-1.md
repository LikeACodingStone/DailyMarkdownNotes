- boost sleep
```
#include <iostream>
#include <boost/thread/thread.hpp>
using namespace std;
int main()
{
    cout<<"sleep前"<<endl;
    
    boost::this_thread::sleep( boost::posix_time::seconds(3) );
    cout<<"3秒后"<<endl;
    boost::this_thread::sleep( boost::posix_time::milliseconds(3000) );
    cout<<"3秒后"<<endl;
    return 0;
}
```

- Qt sleep
```
#include <QtCore/QCoreApplication>

QCoreApplication::processEvents(QEventLoop::AllEvents, 1000000); 
```


- QTime
```
QTime timeSleep;
timeSleep.start();
while (timeSleep.elapsed() < 1000)
	QCoreApplication::processEvents();
```