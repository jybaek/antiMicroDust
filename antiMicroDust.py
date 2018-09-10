# encoding=utf-8

from fbchat import Client
from fbchat.models import *

fb_client = Client('email', 'password') # FIXME.

friends = fb_client.searchForUsers('friendName')[0] # XXX.
msg = 'sample message' # XXX.

fb_client.sendMessage(msg, thread_id=friends.uid, thread_type=ThreadType.USER)
fb_client.logout()
