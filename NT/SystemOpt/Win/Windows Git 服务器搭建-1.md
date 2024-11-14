
Windows平台下搭建Git服务器的图文详解及教程
Git没有客户端服务器端的概念，但是要共享Git仓库，就需要用到SSH协议（FTP , HTTPS , SFTP等协议也能实现Git共享，此文档不讨论），但是SSH有客户端服务器端，所以在windows下的开发要把自己的Git仓库共享出去的话，就必 须做SSH服务器
Git服务现在独树一帜，相比与SVN有更多的灵活性，最流行的开源项目托管网站Github上面，如果托管开源项目，那么就是免费使用的，但是闭源的项目就会收取昂贵的费用，如果你不缺米，那么不在本文讨论的范围内，既然这样，我们可以自己搭建我们的Git服务器。
国内使用Windows Server平台的用户占大多数，那么本文就来讨论如何在Windows平台下搭建Git服务器。
第一步：下载Java，下载地址 http://www.java.com/zh_CN/
根据系统位数下载，32的下载32的，64的下载64的
![497de406d5ac332dbc43e0c34251a4c5.png](../../../_resources/497de406d5ac332dbc43e0c34251a4c5-1.png)

第二步：安装Java.安装步骤不再详述。
![e67055ff2c2cab121adb9e922b6d6c5c.png](../../../_resources/e67055ff2c2cab121adb9e922b6d6c5c-1.png)

第三步：配置Java环境变量
右键”计算机” => ”属性” => ”高级系统设置” => ”高级” => “环境变量” => “系统变量”。
1、新建：
变量名：JAVA_HOME
变量值：D:Program Files (x86)Javajdk1.6.0_21【具体要根据你自己的安装路径，我的是安装在D盘的】
![48404086d558f7824aaede48bec968f3.png](../../../_resources/48404086d558f7824aaede48bec968f3-1.png)
2. 新建：（切记，在跟别的变量值的时候必须加分号; 要不会报错的）
变量名：CLASSPATH
变量值：%JAVA_HOME%/lib/dt.jar;%JAVA_HOME%/lib/tools.jar
![1841d8d3c7d0c264bab3691ab67376e1.png](../../../_resources/1841d8d3c7d0c264bab3691ab67376e1-1.png)

3.　添加：找到PATH变量，选择编辑。把%JAVA_HOME%/bin;%JAVA_HOME%/jre/bin添加到”变量值”的结尾处。 图片描述
第四步：验证Java是否安装成功。
打开命令窗口=> 输入CMD => 确定。
![a7493317db2606f893abae6d227b47f8.png](../../../_resources/a7493317db2606f893abae6d227b47f8-1.png)

在命令窗口中，输入java命令：javac,回车，如果出现如下信息，说明安装成功。
![0ba97999dba51da8736b9c70fbd1e9e9.png](../../../_resources/0ba97999dba51da8736b9c70fbd1e9e9-1.png)

第五步：下载Gitblit.下载地址：http://www.gitblit.com/
![284db50251466a8e1e409486de0f8721.png](../../../_resources/284db50251466a8e1e409486de0f8721-1.png)

第六步：解压缩下载的压缩包即可，无需安装。
![6bb0210b87a0d2e7f97336d95ca4c599.png](../../../_resources/6bb0210b87a0d2e7f97336d95ca4c599-1.png)

第七步：创建用于存储资料的文件夹
![0244effc761984103069a7517c5978f6.png](../../../_resources/0244effc761984103069a7517c5978f6-1.png)

第八步：配置gitblit.properties 文件。
1、找到Git目录下的data文件下的defaults.properties文件，“记事本”打开。
![285c847821d45e391d8c278cd774b243.png](../../../_resources/285c847821d45e391d8c278cd774b243-1.png)

2、找到git.repositoriesFolder(资料库路径)，赋值为第七步创建好的文件目录。
![93c6056e5e07e13845a686a0a65007df.png](../../../_resources/93c6056e5e07e13845a686a0a65007df-1.png)

3.找到server.httpPort，设定http协议的端口号
![d65ecf3323a8fb6739f799fbd481a271.png](../../../_resources/d65ecf3323a8fb6739f799fbd481a271-1.png)

4.找到server.httpBindInterface，设定服务器的IP地址。这里就设定你的服务器IP或本地IP。
![7b7ca9ba4829e67c5c462ee056d3490e.png](../../../_resources/7b7ca9ba4829e67c5c462ee056d3490e-1.png)

5.找到server.httpsBindInterface，设定为localhost
![8787278cc4784f9398c3e54981a53270.png](../../../_resources/8787278cc4784f9398c3e54981a53270-1.png)

6.保存，关闭文件。
第九步：运行gitblit.cmd 批处理文件。
1、找到bitblit目录中的gitblit.cmd文件，双击。
![d0eb350a0c8f601a19d37b6aaf3397cd.png](../../../_resources/d0eb350a0c8f601a19d37b6aaf3397cd-1.png)

2.运行结果如下，运行成功。
![98fb6cbd9f7778632b31be6e56cdb9ed.png](../../../_resources/98fb6cbd9f7778632b31be6e56cdb9ed-1.png)
第十步：在浏览器中打开,现在就可以使用GitBlit了。
![d2a99a84b456fd88a01088aefaf93cec.png](../../../_resources/d2a99a84b456fd88a01088aefaf93cec-1.png)

第十一步：设置以WindowsService方式启动Gitblit.
1、在Gitblit目录下，找到installService.cmd文件
![63a613d14dfec3713cbfb0e73780df82.png](../../../_resources/63a613d14dfec3713cbfb0e73780df82-1.png)

2.用“记事本”打开。
![5a31f8cfa37dca92391a122a69674fad.png](../../../_resources/5a31f8cfa37dca92391a122a69674fad-1.png)

3.修改 ARCH
32位系统：SET ARCH=x86
64位系统：SET ARCH=amd64
![965839313d27f42b193f49307b02a741.png](../../../_resources/965839313d27f42b193f49307b02a741-1.png)

4.添加 CD 为程序目录
SET CD=D:GitGitblit-1.6.0(你的实际目录)
![6465c574c99e3b705be9c0a341af0964.png](../../../_resources/6465c574c99e3b705be9c0a341af0964-1.png)

5.修改StartParams里的启动参数，给空就可以了。 1gif
6.保存，关闭文件。
第十二步：以Windows Service方式启动Gitblit.
1.双击Gitblit目录下的installService.cmd文件(以管理员身份运行)。
![674f29bfdbe59fd42cb4c935cf9f5e5f.png](../../../_resources/674f29bfdbe59fd42cb4c935cf9f5e5f-1.png)

2.在服务器的服务管理下，就能看到已经存在的gitblit服务了。
![26b78dd07a6240d7344097132b9f863e.png](../../../_resources/26b78dd07a6240d7344097132b9f863e-1.png)