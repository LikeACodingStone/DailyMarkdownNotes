![[Pasted image 20261027182104.png]]

- can not input password, hang here. 
#### solution
- ssh to this machine
```bash
## grep process
ps aux | grep -E "nm-applet|plasmashell|gnome-shell|network-manager"

### result
neu@neu:~$ ps aux | grep -E "nm-applet|plasmashell|gnome-shell|network-manager"
gdm         1623  0.0  0.6 3903692 222900 tty1   Sl+  Sep07  43:09 /usr/bin/gnome-shell
gdm         1740  0.0  0.0 2531676 26504 tty1    Sl+  Sep07   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.Shell.Notifications
gdm         1934  0.0  0.0 2662716 26884 tty1    Sl+  Sep07   0:00 /usr/bin/gjs -m /usr/share/gnome-shell/org.gnome.ScreenSaver
neu       273370  0.0  0.1 551212 51268 ?        Sl   Oct26   0:44 nm-applet --indicator
neu      3538305  0.0  0.0   9304  2676 pts/2    S+   18:23   0:00 grep --color=auto -E nm-applet|plasmashell|gnome-shell|network-manager


### kill process
kill -9 273370
# or 
pkill nm-applet
```