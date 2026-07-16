#### App Center 
- install Android Studio
#### Set Aosp 
- ./app/bosch/ccs20/local.propertie
```
sdk.dir=/home/neu/Android/Sdk
aosp.dir=/home/neu/aosp
```
#### Install JDK 21 , command mandatory,  to trigger the gradle sync process
```
sudo apt update
sudo apt install openjdk-21-jdk
sudo apt install -f
```
#### SDK and tools
- ![e4d92b0f01c2a0659ba8982d4461ec8b.png](e4d92b0f01c2a0659ba8982d4461ec8b.png)
- ![85b61bed1f041ae410d52a896c60687a.png](85b61bed1f041ae410d52a896c60687a.png)
### Gradle and JDK settings
- ![5992e88b550b6c1f097e77cd73fdf125.png](5992e88b550b6c1f097e77cd73fdf125.png)

###  AGP 8.2.2
### Gradle-8.2

## Pass the first aosp compiling
- ![7d8a8fbd93de4fffd93d97dd31503eb9.png](7d8a8fbd93de4fffd93d97dd31503eb9.png)

### uninstall JDK 21
```
sudo apt purge openjdk-21-jdk
sudo apt autoremove
```
### Changing JDK to JDK-19
```
wget https://download.java.net/java/GA/jdk19/877d6127e982470ba2a7faa31cc93d04/36/GPL/openjdk-19_linux-x64_bin.tar.gz


tar -zxvf openjdk-19*.tar.gz
sudo mkdir -p /usr/lib/jvm
sudo mv jdk-19* /usr/lib/jvm/
```
#### changing  ~/.bashrc
```
export JAVA_HOME=/usr/lib/jvm/jdk-19
export PATH=$JAVA_HOME/bin:$PATH
```

### Create link
```
sudo ln -s $(which java) /usr/bin/java
```

### Issues, if the aosp gradle can not been sync
- check here if there are some warning messages for setting, then select the sync option
![de6707a39e03c0f7e4a09d255d493ecf.png](de6707a39e03c0f7e4a09d255d493ecf.png)
