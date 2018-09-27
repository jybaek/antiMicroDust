# encoding=utf-8

import configparser

config = configparser.RawConfigParser()
config.read('config.ini')

import dust_info

data = dust_info.get_data(config)

'''
print("dataTime: ", data['dataTime'])
print("pm10    : ", data['pm10Value'])
print("pm2.5   : ", data['pm25Value'])
'''

if not config['ACCOUNT']['USERID']:
    print('Error: USERID in config.ini')
    exit(255)
if not config['ACCOUNT']['PASSWD']:
    print('Error: USERID in config.ini')
    exit(255)

from fbchat import Client
from fbchat.models import *

fb_client = Client(config['ACCOUNT']['USERID'], config['ACCOUNT']['PASSWD'])

friends = fb_client.searchForUsers(config['TARGET']['USERNAME'])[0]
msg = "dataTime: %s\npm10    : %s\npm2.5   : %s" % ( data['dataTime'], data['pm10Value'], data['pm25Value'] )
print(msg)
exit(255)

fb_client.sendMessage(msg, thread_id=friends.uid, thread_type=ThreadType.USER)
fb_client.logout()
