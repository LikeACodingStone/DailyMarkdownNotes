### 常见 .sh启动错误，可以通过添加log定位问题得原因。
**********
### smartgit，为例
- 添加log到/usr/share/smartgit/bin/smartgit.sh
```
echo "SmartGit is trying to execute: $_JAVA_EXEC"
```

```
SmartGit is trying to execute: /usr/share/smartgit/jre/bin/java
```
- 结果，可以发现smartgit使用了自己得jre，直接删除，改成系统得就可以解决这个问题
***
