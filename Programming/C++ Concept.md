### Threads
- std::bind 将成员函数绑定到类的实例上，并将其传递给 std::thread
```
.startTask();   // 启动任务
.detach(); 	  // 分离线程
```
- windows 用CreateThread创建线程

### 指针类型转换
```
dynamic_cast
static_cast
reinterpret_cast
```

### 类内回调函数
`C++ 类内定义一个函数，如果要将这个函数作为回调函数，需要在声明的时候加上static 关键字`

### 字符串
```
str.find("abc") == std::string::npos
```

### 一般类函数概念
- std::setw(n) 设置下一个输出项占用的最小字符宽度为 n。如果数据长度不足，就会用空格填充。
-   std::ofstream 是C++写入文件的类
-   STL(Set/Map/Vector/Queue)
### 特殊记录
- vs2003 map会默认自动排序，可以通过std::multimap自定义实现不排序的map