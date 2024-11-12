```
1. 线程安全单例实现
2. 移动语义移动构造函数，移动赋值函数
3. 两个线程同步一前一后打印
4. 设计一个线程池, 池子四个线程，执行8个打印任务
5. lambda几种常用用法
	A. 函数对象
	B. STL结合
	C. 排序
	D. 标记为mutable
```
***
```
1.

class ClassInstance
{
public:
    static ClassInstance *GetInstance()
    {
        if(m_instance == nullptr)
        {
            lock_guard<mutex> lock(m_mutex);
            if(m_instance == nullptr)
            {
                m_instance = new ClassInstance();
            }
        }
        return m_instance;
    }
    


private:
    static ClassInstance *m_instance;
    static mutex m_mutex;
    ClassInstance(){}
    ClassInstance & operator=(const ClassInstance &) = delete;
    ClassInstance(const ClassInstance&) = delete;
};

ClassInstance *ClassInstance::m_instance = nullptr;
mutex ClassInstance::m_mutex;
```
***
```
2.
```