# Docker Install

- **Remove Previous Docker Installations**
```
    sudo apt-get remove docker docker-engine docker.io
```
- ****Install Docker****
  
```
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

- **Set Up the Repository**
- Update the apt package index:

```
sudo apt-get update
```

- Install packages to allow apt to use a repository over HTTPS:

```
sudo apt-get install \
   apt-transport-https \
   ca-certificates \
   curl \
   software-properties-common
```

- Add Docker’s official GPG key

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

- Verify that the key fingerprint is 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88

```
sudo apt-key fingerprint 0EBFCD88
```

- Use the following command to set up the stable repository

```
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
```

- **Set Up Insecure Registry and DNS Server**
    
- Ensure that your file `/etc/docker/daemon.json` contains this configuration:
- can be replaced directly

```
{"dns":["172.31.0.10","172.31.0.11"],"insecure-registries":["buildbot.nts.neusoft.local:5000","ntssy-lxbbma01.nts.neusoft.local:5000"]}
```

- **Add Own User to the Group Docker**

```
sudo usermod -G docker -a <username>
newgrp docker
```

- **Restart Docker**

```
sudo systemctl daemon-reload &&\
sudo service docker restart
```

- **Verify that Listing Docker Images Works**
- Run the command

```
docker images
```

* * *

# Docker Import & Export

- **export**

```
docker save -o <output_file>.tar <image_name>:<tag>

// multi export
docker save -o multiple_images.tar <image1>:<tag> <image2>:<tag>
```

- **import**

```
docker load -i <input_file>.tar
```

### Docker Error Debug
`
sudo dockerd -D
`
`
cat /var/log/docker.log
`
`
journalctl -u docker.service --no-pager -n 50
`