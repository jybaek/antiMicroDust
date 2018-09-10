# encoding=utf-8

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

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
msg = 'sample message' # XXX.

fb_client.sendMessage(msg, thread_id=friends.uid, thread_type=ThreadType.USER)
fb_client.logout()
