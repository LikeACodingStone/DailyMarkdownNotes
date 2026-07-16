-  模拟器连接本地地址
- 使用10.0.2.2 代替127.0.0.1 就可以
***
- 修改apk名字
```
在build.grandle (module文件)内添加如下

android.applicationVariants.all {
    variant ->
        variant.outputs.all {
            //这里修改apk文件名
            outputFileName = "HGTAxis.apk"
        }
}
```
- 修改app_name(app的抬头名称)
```
```
