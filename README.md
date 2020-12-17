# Speedtest Logger
A python script that can be run as a cronjob to test internet speed and post it to a web.py server.
## Installation
Clone this repository. Make sure to keep all the files in one folder.
All the dependencies are included in the folder except for web.py.
Install the web.py python library using pip or your operating system's package manager
```
python -m pip install web.py
```
or 
```
sudo apt-get install python-webpy
```
etc.

### Scheduling
Create a shell script for `pyspeedtest_task.py` and set as a cronjob.
Create a shell script for `pyspeedtest_webserver.py` and set to run on startup.

### Access Results
Speedtest results are hosted on an HTTP webserver:
```
http://[YOUR_MACHINE_IP_HERE]:8080/speedtest
```
## Attribution
speedtest.py is used in its unmodified form from the speedtest-cli project: https://github.com/sivel/speedtest-cli
speedtest-cli is released under an Apache-2.0 software license, which is provided in Apache-License.txt
