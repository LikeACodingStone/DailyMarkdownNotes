```
#include <mutex>
std::mutex g_Mutex;
g_Mutex.try_lock();		
g_Mutex.unlock();
```
