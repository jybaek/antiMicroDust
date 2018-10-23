[![Python 3.6](https://img.shields.io/badge/python-3.4%2C%203.5%2C%203.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# antiMicroDust
Imports micro-dust information from public data and sends it to specific users (friends) on Facebook.

## Install
Install the necessary modules.
```bash
$ pip install -r requirements.txt
```

## Usage
Now modify _config.ini.default_ to make it _config.ini_ and run the script.
```bash
$ python antiMicroDust.py
```

## config.ini example
```
[ACCOUNT]
USERID = foo@example.com
PASSWD = password

[TARGET]
USERNAME = user_name

[DATA]
URL = http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty
SERVICE_KEY = Enter the service key
STATION_NAME = 강남

[EXTEND]
MUTE_TIME = 0,1,2,3,4,5,6,7
```
No messages will be sent to `MUTE_TIME`.
