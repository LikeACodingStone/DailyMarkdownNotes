
```
SYSTEMTIME SystemTime;
GetLocalTime(&SystemTime);
int year = SystemTime.wYear;
int month = SystemTime.wMonth;
int day = SystemTime.wDay;
int hour = SystemTime.wHour;
int minute = SystemTime.wMinute;
int secs = SystemTime.wSecond;
int milSec = SystemTime.wMilliseconds;
```