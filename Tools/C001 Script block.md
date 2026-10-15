---
gists:
  - id: 53f1821e7f29c52360b604315579a211
    url: 'https://gist.github.com/LikeACodingStone/53f1821e7f29c52360b604315579a211'
    createdAt: '2026-09-24T09:45:14Z'
    updatedAt: '2026-09-24T09:45:15Z'
    filename: C001 Script block.md
    isPublic: true
    baseUrl: 'https://api.github.com'
---
# Ubuntu Swap
~~~bash
sudo swapoff -a
sudo rm /swapfile
sudo fallocate -l 32G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
free -h

sudo vi /etc/fstab
# Add: /swapfile none swap sw 0 0

cat /proc/sys/vm/swappiness
sudo sysctl vm.swappiness=10
sudo vi /etc/sysctl.conf
# Add: vm.swappiness=20
~~~
