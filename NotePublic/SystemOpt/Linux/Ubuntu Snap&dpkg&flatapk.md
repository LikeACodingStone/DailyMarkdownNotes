#### android-studio
```
sudo snap install android-studio --classic
```

### dpkg view path
```
dpkg -L smartgit
```

### flatapk install firefox
```
sudo apt update
sudo apt install flatpak -y
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
flatpak install flathub org.mozilla.firefox
sudo reboot
// start
flatpak run org.mozilla.firefox
```
