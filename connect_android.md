### Python version: 3.10.x


## Steps to compile the source code to andorid
### Install WSL2 for windows 11/10
type in powershell
```wsl --install```

### Deploy kivyMd App Android
[Deploy kivy](https://kivy.org/doc/stable/guide/packaging-android.html)

### Install buldozer
[Install Buildozer and its dependencies](https://buildozer.readthedocs.io/en/latest/installation.html)

And then run 

```buildozer android debug deploy run```
or 
```buildozer android debug deploy run logcat```

### Connect Android phone Linux
first disable the firewall (optional)
- Create server connection(Windows powershell): ```adb -a -P 5000 nodaemon server```
- Create client connection(Linux ubuntu shell): ```adb -P 5000 -H  192.168.56.1 devices -l```
- This to set env variable: ```export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | awk '/nameserver/ {print $2}'):5000```

### Wireless connection
[Wirless connection](https://jaro.blog/blog/adb-in-wsl2.html)
- Get Android IP address: ```adb shell ip addr show wlan0``` and copy the IP address after the "inet" until the "/"
- Run on Linux shell: ```adb -P 5000 -H 192.168.56.1 tcpip 5555```
- ```adb -P 5000 -H 192.168.56.1 connect (android_ip):5555```
- then remove the cable

### Debug with adb logcat commands
- debug a service called Myservice: ```adb logcat "Myservice:D *:S"```
- Debug background services: ```adb logcat Myservice *:S python:D```
### Install on non-connected devices
If you have compiled a package, and want to share it easily with others devices, you might be interested with the serve command.<br> It will serve the bin/ directory over HTTP. Then you just have to access to the URL showed in the console from your mobile:<br>

```buildozer serve --address ip_address --port 8000```

you can get ip address on Linux as follows
```hostname -I```

```complete
buildozer android debug deploy run
buildozer android debug deploy run logcat
adb -a -P 5000 nodaemon server
export ADB_SERVER_SOCKET=tcp:$(cat /etc/resolv.conf | awk '/nameserver/ {print $2}'):5000
adb shell ip addr show wlan0
adb -P 5000 -H 192.168.56.1 tcpip 5555
adb -P 5000 -H 192.168.56.1 connect (android_ip):5555
adb logcat "Myservice:D *:S

```


### Usefull Links

- [ZMQ messaging](https://github.com/jeffbass/imagezmq#introduction)