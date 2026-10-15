### local.properties
```
sdk.dir=/home/taj4yh/Android/Sdk
aosp.dir=/home/taj4yh/aosp
```
****
##  Task Error info 
### 1. dev34_default_x86_64_Pixel_2
```
Gradle was not able to complete device setup for: dev34_default_x86_64_Pixel_2
The emulator failed to open the managed device to generate the snapshot.
This is because the emulator closed unexpectedly, try updating the emulator and
ensure a device can be run from Android Studio.
```
#### solution
1. Device Manager , delete exist virtual device
2. Open Android Studio → AVD Manager
3. Create a new virtual device, such as Pixel 2, with API level 34 (x86_64)
4. Running Pixel 2 to test function ability
5. /dev/kvm device: permission denied. Garant current user access to /dev/kvm
6. Termil run command `sudo chmod 755 -R /dev/kvm`  and `sudo chown user:user -R /dev/kvm`
7. start device again. succeed, then compile task again.

********
