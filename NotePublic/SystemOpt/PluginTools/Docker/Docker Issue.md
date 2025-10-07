- **Docker Load Issue**
```
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/load?quiet=0": dial unix /var/run/docker.sock: connect: permission denied
```
```
sudo usermod -aG docker $USER

// reboot machine
// check docker status or start 
// sudo systemctl status docker

sudo systemctl start docker
```