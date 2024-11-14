* **交叉编译指定编译器** 
	- ./configure --host=arm-linux CC=arm-linux-gcc
* **编译将执行文件改成so**
	- 添加 SHARE   := -fPIC -shared -o     
 	- $(CC) $(CXXFLAGS) -o $@ $(OBJS) $(LDFLAGS) $(LIBS)  改成
	- $(CC) $(CXXFLAGS) $(SHARE) $@ $(OBJS) $(LDFLAGS) $(LIBS)