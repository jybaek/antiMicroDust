# encoding=utf-8

import configparser
import dust_info
import time
import datetime
from fbchat import Client
from fbchat.models import *

config = configparser.RawConfigParser()
config.read('config.ini')

if not config['ACCOUNT']['USERID']:
    print('Error: USERID in config.ini')
    exit(255)
if not config['ACCOUNT']['PASSWD']:
    print('Error: USERID in config.ini')
    exit(255)

fb_client = Client(config['ACCOUNT']['USERID'], config['ACCOUNT']['PASSWD'])
friends = fb_client.searchForUsers(config['TARGET']['USERNAME'])[0]

prev_data = []
while True:
    curr_data = dust_info.get_data(config)
    if curr_data is None:
        print('Error: get_data is None')
        exit(255)

    msg = "dataTime: %s\npm10    : %s\npm2.5   : %s" % ( curr_data['dataTime'], curr_data['pm10Value'], curr_data['pm25Value'] )
    print(msg)

    if not prev_data: 
        fb_client.sendMessage(msg, thread_id=friends.uid, thread_type=ThreadType.USER)
    elif prev_data['dataTime'] != curr_data['dataTime']:
        if prev_data['pm10Value'] != curr_data['pm10Value'] or prev_data['pm25Value'] != curr_data['pm25Value']:
            now = datetime.datetime.now()
            if now.hour in list(map(int, config['EXTEND']['MUTE_TIME'].split(','))):
                print(' # MUTE TIME: %s', now.hour)
            else:
                print(' # Update sendMessage: %s hour', now.hour)
                fb_client.sendMessage(msg, thread_id=friends.uid, thread_type=ThreadType.USER)
        else:
            print( ' # SKIP sendMessage: same status ' )
    else:
        print(' # SKIP sendMessage: same curr_dataTime [%s]' % curr_data['dataTime'])

    prev_data = curr_data

    time.sleep(10 * 60) # 10 min

fb_client.logout()
