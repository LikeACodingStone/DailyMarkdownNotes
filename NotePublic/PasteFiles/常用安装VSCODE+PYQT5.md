
- LINK
```
https://blog.csdn.net/qq_23825121/article/details/125893796
```


```
pip install PyQt5  # 安装pyqt5
pip install PyQt5-tools  # 安装pyqt5-tools
pip install pyqt5designer  # 安装pyqt5designer

```

***
- 	 安装 Crypto
```
pip install pycryptodome
pip install crypto
pip install pycrypto
```

```
使用pip install pycrypto命令时报错：
C:\Users\MI\AppData\Local\Programs\Python\Python37>Pip3.7 install pycrypto
Collecting pycrypto
  Using cached pycrypto-2.6.1.tar.gz (446 kB)
Using legacy 'setup.py install' for pycrypto, since package 'wheel' is not installed.
Installing collected packages: pycrypto
    Running setup.py install for pycrypto ... error
    ERROR: Command errored out with exit status 1:
     command: 'c:\users\mi\appdata\local\programs\python\python37\python37.exe' -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\MI\\AppData\\Local\\Temp\\pip-install-iwoi68sx\\pycrypto_11418f0350244305b0226b38fc392f84\\setup.py'"'"'; __file__='"'"'C:\\Users\\MI\\AppData\\Local\\Temp\\pip-install-iwoi68sx\\pycrypto_11418f0350244305b0226b38fc392f84\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record 'C:\Users\MI\AppData\Local\Temp\pip-record-8g35bcmi\install-record.txt' --single-version-externally-managed --compile --install-headers 'c:\users\mi\appdata\local\programs\python\python37\Include\pycrypto'
```

 - 打开\Python\Lib\site-packages这个路径，找到crypto这个文件夹。
- 将crypto这个文件夹重命名为Crypto。
- 重新运行程序即可发现No module named 'Crypto'报错消失。
***

