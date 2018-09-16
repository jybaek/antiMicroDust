# encoding=utf-8

import requests
import urllib.parse
import json

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
service_key = '' # FIXME
stationName = '강남구' # FIXME

decode_key = urllib.parse.unquote(service_key)
params = {'ServiceKey': decode_key, 'stationName': stationName, 'dataTerm': 'daily', '_returnType': 'json', 'ver': '1.3', 'pageNo': 1}

response = requests.get(url, params=params)
response_body = json.loads(response.text)

print(response.url)
print("dataTime: ", response_body['list'][0]['dataTime'])
print("pm10    : ", response_body['list'][0]['pm10Value'])
print("pm2.5   : ", response_body['list'][0]['pm25Value'])
