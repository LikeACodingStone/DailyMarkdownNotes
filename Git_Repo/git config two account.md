# 一台电脑绑定两个git账号

- ` ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "liszhouyou@gmail.com"  一路回车 生成第一个证书`
    
- `ssh-keygen -t rsa -f ~/.ssh/id_rsa_2 -C  "othermail@xxx.com" 一路回车 生成第二个证书`
    
- 到github Setting网页，找到 SSH and GPG keys，在右上角，点击profiles settings
    
- 新建ssh key 把  .ssh文件夹目录下的id\_rsa.pub 或id\_rsa_2.pub内容复制粘贴到github网站
- 注意: .ssh文件夹只有运行 `ssh-keygen` 或者 `ssh` 远程命令的时候才能自动生成
    
- 新建config文件 示例 [config](../assets/shared/config)
    
- 代码拉去下来以后配置一下对应仓的邮箱
- `git config --global user.email "youmail@xxx.com"
`


