# Speedtest Logger
A python script that can be run as a cronjob to test internet speed and post it to a web.py server.
## Installation
Download speedtest.py
```
curl -Lo speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
chmod +x speedtest-cli
```
Create a shell script for `pyspeedtest_task.py` and set as a cronjob.
Create a shell script for `pyspeedtest_webserver.py` and set to run on startup.
Speedtest results are hosted on an HTTP webserver:
```
http://[YOUR_MACHINE_IP_HERE]:8080/speedtest
```
