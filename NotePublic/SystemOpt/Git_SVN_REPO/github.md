# 一台电脑绑定两个git账号

- ` ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "liszhouyou@gmail.com"  一路回车 生成第一个证书`
    
- `ssh-keygen -t rsa -f ~/.ssh/id_rsa_2 -C  "othermail@xxx.com" 一路回车 生成第二个证书`
    
- 到github Setting网页，找到 SSH and GPG keys，在右上角，点击profiles settings
    
- 新建ssh key 把  .ssh文件夹目录下的id\_rsa.pub 或id\_rsa_2.pub内容复制粘贴到github网站
- 注意: .ssh文件夹只有运行 `ssh-keygen` 或者 `ssh` 远程命令的时候才能自动生成
    
- 新建config文件 示例 [config](../../../_resources/config)
    
- 代码拉去下来以后配置一下对应仓的邮箱
- `git config --global user.email "youmail@xxx.com"
`
* * *

# 测试连接情况

- ssh -T git@github.com
- 出现successfully authenticated 表示成功连接

***
# git tag 打包
```
创建本地 tag： git tag <tagName> 
推送到远程仓库： git push origin <tagName> 
```

# git 异常
```
unable to access 'https://github.com/CodingKilling/GitLab_Jimi.git/': OpenSSL SSL_read: Connection was reset, errno 10054

git config --global http.sslVerify "false"			// 设置不需要SSL认证
git config http.postBuffer 5242880003					// 设置最大大小500M

```
# git 日常指令
```
git submodule update --init --recursive   # 更新子模块一起
git checkout -b stabilization/2024/product_vics_DA3_Bosch --track origin/stabilization/2024/product_vics_DA3_Bosch   # 创建本地分支并映射远程分支

```

****


