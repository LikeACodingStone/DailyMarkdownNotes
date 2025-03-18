# boost库
```
#include <boost/timer.hpp>
boost::timer m_tmHeartbeatMonitor;
```

# thread
```
// 分离线程执行
static void HFrameAxisMoving::mvPressForward();
void HFrameAxisMoving::mvPressForward()
{
}
std::thread thMoving(mvPressForward);
thMoving.detach();	



```

# srand,rand 随机和乱序
```
	// 对数组随机乱序
	int randInt[10] = { 0,1,2,3,4,5,6,7,8,9};
	QTime time;
	time = QTime::currentTime();
	qsrand(time.msec() + time.second() * 1000);
	random_shuffle(randInt, randInt + 10);
	
	// 生成0 - 100  随机数
	int randNum = rand() % 100;
	
```



# WINDOWS线程
```
DWORD WINAPI Thread_RecvLaser(LPVOID lpParam)
{
	SerialRDWR	*m_serial = (SerialRDWR*)lpParam;
	while (TRUE) {
		TRACE("This is thread1 running........");
		Sleep(100);
	}
	return 0;
}

bool TestThreadFunc()
{
	m_serial = new SerialRDWR();
	HANDLE thHdRecv = CreateThread(NULL, 0,	Thread_RecvLaser, m_serial, 0, NULL);
	if (m_serial == NULL)
	{
		CloseHandle(thHdRecv);
		return false;
	}
	return true;
}
```