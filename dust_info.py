# encoding=utf-8

import requests
import urllib.parse
import json

def get_data(config):
    url = config['DATA']['URL']
    service_key = config['DATA']['SERVICE_KEY']
    stationName = config['DATA']['STATION_NAME']

    decode_key = urllib.parse.unquote(service_key)
    params = {'ServiceKey': decode_key, 'stationName': stationName, 'dataTerm': 'daily', '_returnType': 'json', 'ver': '1.3', 'pageNo': 1}

    response = requests.get(url, params=params)
    response_body = json.loads(response.text)

    #print(response.url)
    if not response_body['list']:
        return None
    else:
        return response_body['list'][0]
