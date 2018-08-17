#!/usr/bin/python
#coding: utf-8

'''
install wxpy first:
  sudo pip install wxpy
'''
import sys
from wxpy import *

reload(sys)
sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding()

bot = Bot()
target_group = bot.groups().search('忽悠小分队'.encode('utf-8').decode('utf-8'))[0]

tuling = Tuling(api_key='')

@bot.register(target_group)
def print_msg(msg):
    print msg
    return tuling.do_reply(msg)

embed() 
