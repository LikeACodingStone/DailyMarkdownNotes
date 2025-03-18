- **std::bind 将成员函数绑定到类的实例上，并将其传递给 std::thread**
```
#include <iostream>
#include <thread>
#include <functional> // 需要包含 functional 头文件以使用 std::bind

class MyClass {
public:
    void startTask() {
        // 使用 std::bind 将成员函数 taskInfoHmiHotStart 绑定到当前对象（this）
        auto boundFunction = std::bind(&MyClass::taskInfoHmiHotStart, this);

        // 将绑定后的函数传递给 std::thread
        std::thread taskNotify(boundFunction);
        taskNotify.detach(); // 分离线程，使其在后台运行
    }

private:
    void taskInfoHmiHotStart() {
        // 访问类的私有成员
        privateFunction();
        std::cout << "Private variable: " << privateVariable << std::endl;
    }

    void privateFunction() {
        std::cout << "Private function called" << std::endl;
    }

    int privateVariable = 42; // 私有变量
};

int main() {
    MyClass obj;
    obj.startTask(); // 启动任务

    // 主线程等待一段时间，确保子线程有机会执行
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return 0;
}
```
